# Project Development Governance & AI Agent Rules

## 1. Project Objective
I want to learn and implement PostgreSQL integration using FastAPI in this project.
This project must be developed as a professional, production-oriented backend application while following industry-standard software engineering practices, security principles, clean architecture, and maintainable coding standards.
The primary goal is not just to complete the project but also to understand every implementation step, especially PostgreSQL integration, database design, SQLAlchemy, migrations, authentication, authorization, and API development.

## 2. Communication Rules
- The user communicates with AI agents in Hinglish (Hindi + English).
- Every AI agent must understand and interpret Hinglish instructions correctly.
- Agent chat responses and technical explanations must be provided in conversational, clear Hinglish as requested by the user.
- All source code, variable names, function names, class names, comments, API documentation, error messages, database identifiers, and configuration examples must be written strictly in professional English.
- Never generate Hindi or Hinglish inside the codebase or documentation files.
- Follow consistent naming conventions and professional programming standards.

## 3. Strict Security Governance
Security is the highest priority. Every implementation must follow secure development practices:
- Never expose passwords, API keys, JWT secrets, database credentials, or sensitive information.
- Never hardcode secrets in source code.
- Use environment variables and maintain a properly structured `.env.example`.
- Never commit `.env` files or credentials.
- Validate and sanitize all incoming user inputs.
- Implement proper authentication and authorization.
- Follow secure password hashing practices (e.g., Argon2 or Bcrypt).
- Prevent SQL injection using parameterized queries and ORM operations.
- Implement proper exception handling without exposing internal system traces.
- Apply least-privilege principles to database users and application permissions.
- Never disable security mechanisms to make an implementation work.
- Never introduce insecure dependencies or configurations.

## 4. Strict Permission & Approval Policy
**NO ACTION WITHOUT EXPLICIT PERMISSION.**
AI agents must operate in a permission-controlled mode.
The following actions require explicit approval before execution:
1. Creating, deleting, renaming, or restructuring files and directories.
2. Modifying existing source code or configuration files.
3. Installing, removing, or upgrading dependencies.
4. Modifying `requirements.txt`, lock files, or package configurations.
5. Changing database schemas or executing migrations.
6. Creating, deleting, truncating, or modifying database records.
7. Executing destructive SQL commands.
8. Changing authentication, authorization, or security configurations.
9. Modifying Docker, Docker Compose, Nginx, or deployment configurations.
10. Running shell commands that modify the system or project.
11. Modifying Git configuration, branches, commits, or repository history.
12. Accessing external services or transmitting project data.

Before performing any sensitive action:
- Explain what needs to be changed.
- Explain why the change is required.
- Identify exact files, dependencies, database objects, or commands affected.
- Explain possible risks and consequences.
- Present the proposed implementation.
- Wait for explicit user approval.
- Do not interpret silence or previous approvals as permission for a new action.

## 5. Multi-Agent Compatibility
Maintain a single source of truth for:
- Project architecture (`docs/ARCHITECTURE.md`)
- Database design & migrations (`docs/DATABASE.md`)
- Project context & tech stack (`docs/PROJECT_CONTEXT.md`)
- Task tracker & milestones (`docs/TASK_TRACKER.md`)
- Universal agent guide (`AGENTS.md`)
All agent-specific configuration files (`CLAUDE.md`, `.cursorrules`) must reference this central governance policy.

## 6. Mandatory Workflow for Every Task
1. **Understand**: Interpret requirements and review existing documentation/code.
2. **Analyze**: Identify affected components, architecture fit, and security risks.
3. **Propose**: Present implementation plan and list all affected files/commands.
4. **Wait for Approval**: Do not modify files or run mutating commands without permission.
5. **Implement**: Apply only approved changes following conventions.
6. **Validate**: Run tests and automated verification to confirm correctness.
7. **Documentation**: Keep documentation synchronized with codebase changes.
8. **Report**: Summarize changes, technical concepts, tests, and remaining tasks in Hinglish.
