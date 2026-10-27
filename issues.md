# Static Code Analysis — Issue Report

## Issues Identified and Fixed

| Issue                            | Tool                   | Severity / Type    | Description                                                           | Fix Applied                                            |
| -------------------------------- | ---------------------- | ------------------ | --------------------------------------------------------------------- | ------------------------------------------------------ |
| Unsafe `eval()`                  | Bandit                 | Medium             | Executes a string as Python code.                                     | Replaced with direct GPA calculation.                  |
| Shell command execution          | Bandit                 | High               | `os.system()` can introduce command injection risks.                  | Removed shell execution and used Python operations.    |
| Weak MD5 hash                    | Bandit                 | High               | MD5 is unsuitable for security-sensitive hashing.                     | Replaced with SHA-256.                                 |
| Hard-coded token                 | Bandit                 | Low                | A token-like secret was embedded in the source.                       | Removed the hard-coded token.                          |
| Insecure PIN generation          | Bandit                 | Low                | `random.randint()` is not intended for security-sensitive randomness. | Used the `secrets` module.                             |
| Bare exception                   | Pylint, Bandit, Flake8 | Code quality / Low | Silently catches all exceptions.                                      | Added input validation and appropriate error handling. |
| Mutable default argument         | Pylint                 | Code quality       | A list default can be shared between function calls.                  | Changed the default to `None`.                         |
| Unused import and variables      | Pylint, Flake8         | Code quality       | Unused names reduce maintainability.                                  | Removed unused imports and variables.                  |
| Naming and formatting violations | Pylint, Flake8         | Style              | Non-standard naming and formatting reduce readability.                | Used `snake_case` and corrected formatting.            |

## Verification

- Before fixes, Pylint reported 5.51/10.
- After fixes, Pylint reported 10.00/10.
- Before fixes, Bandit reported six findings.
- After fixes, Bandit reported no issues.
- Before fixes, Flake8 reported eight violations.
- After fixes, Flake8 reported no violations.

The before-and-after reports are included as separate text files.
