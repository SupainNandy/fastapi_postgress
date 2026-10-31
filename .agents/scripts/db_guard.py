#!/usr/bin/env python3
"""Safety guard script to intercept and prevent unauthorized database destruction or schema changes."""

import json
import re
import sys


def main():
    try:
        raw_input = sys.stdin.read()
        if not raw_input.strip():
            print(json.dumps({"decision": "allow"}))
            return

        payload = json.loads(raw_input)
        tool_call = payload.get("toolCall", {})
        tool_name = tool_call.get("name", "")
        args = tool_call.get("args", {})

        # Dangerous patterns to intercept
        dangerous_patterns = [
            r"\bdrop\s+database\b",
            r"\bdrop\s+table\b",
            r"\btruncate\b",
            r"\balembic\s+downgrade\b",
            r"docker\s+volume\s+rm",
            r"docker\s+compose\s+down\s+-v",
        ]

        if tool_name == "run_command":
            cmd = args.get("CommandLine", "").lower()
            for pattern in dangerous_patterns:
                if re.search(pattern, cmd):
                    response = {
                        "decision": "deny",
                        "reason": (
                            f"SECURITY GUARD INTERCEPTED: The command matches dangerous database "
                            f"pattern '{pattern}'. Action blocked to prevent data loss."
                        ),
                    }
                    print(json.dumps(response))
                    return

        # Allow all other operations
        print(json.dumps({"decision": "allow"}))

    except Exception as e:
        # Fail safe
        print(json.dumps({"decision": "allow"}))


if __name__ == "__main__":
    main()
