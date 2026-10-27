# Static Code Analysis — Reflection

### 1. What is static code analysis, and why is it useful?

Static code analysis examines source code without executing it. It helps developers identify potential bugs, security vulnerabilities, and style violations early, making code easier to maintain and safer to use.

### 2. What are the roles of Pylint, Bandit, and Flake8?

Pylint checks code quality, naming, unused variables, and potential programming mistakes. Bandit identifies potentially insecure coding patterns. Flake8 checks Python style and formatting according to common conventions.

### 3. What issues were found and how were they fixed?

The original program contained unsafe dynamic evaluation, shell execution, a hard-coded token, weak hashing, insecure random-number generation, a mutable default argument, a bare exception, unused imports, and style violations. These were addressed by replacing unsafe operations, improving input validation, removing unused code, and correcting naming and formatting.

### 4. What did you learn from this lab?

I learned that multiple static analysis tools complement each other. Pylint helps improve code quality, Bandit highlights security risks, and Flake8 identifies style issues. Running the tools before and after changes provides evidence that the code has improved.
