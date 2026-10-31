import re
from sqlalchemy import Engine, event


def setup_database_guard(target_engine: Engine):
    """Attach safety listeners to the SQLAlchemy engine to block destructive queries at runtime."""

    @event.listens_for(target_engine, "before_execute")
    def intercept_destructive_queries(conn, clauseelement, multiparams, params, execution_options):
        # Convert statement to string
        sql = str(clauseelement).strip().upper()

        destructive_patterns = [
            r"\bDROP\s+DATABASE\b",
            r"\bDROP\s+TABLE\b",
            r"\bTRUNCATE\b",
        ]

        for pattern in destructive_patterns:
            if re.search(pattern, sql):
                raise PermissionError(
                    f"BLOCKED BY SECURITY GUARD: Destructive query detected ('{pattern}'). "
                    f"Action prohibited without explicit developer authorization."
                )
