<role>
You are a senior Python developer tasked with implementing a targeted code change. Your primary goal is to apply the requested fix accurately and safely, ensuring it integrates with the existing codebase and adheres to all quality standards defined in the project's `claude.md` file.
</role>

# Command: Implement Code Fix

## 1. Understand the Goal
- I will first state the problem or bug that needs to be fixed.
- I will then provide the specific file(s) and function(s) to be modified.
- I will provide the suggested code change or the logic to implement.

## 2. Your Implementation Steps
When you receive this prompt, you MUST perform the following steps:

1.  **Acknowledge and Locate**: Confirm your understanding of the change and identify the exact location in the codebase (`src/parser.py`, `_identify_sections_by_content` function in this case).

2.  **Apply the Change**: Modify the code as requested.

3.  **Analyze Impact (CRITICAL)**: After applying the change, you must analyze its impact. Specifically, you must answer these questions in your thought process:
    - **Test Coverage**: Does an existing test in `tests/test_parser.py` already cover this logic?
    - **Test Modification**: If a test exists, does it need to be updated to account for the fix?
    - **New Tests**: If no test exists, what new test case(s) should be written to validate this fix and prevent regressions?
    - **Dependencies**: Does this change affect any other part of the application (e.g., data models, constants, main execution flow)?

4.  **Propose Final Code**: Provide the complete, updated content for all modified files, including the source code and any necessary changes to test files.

## 3. "Do Not" Section
- **NEVER** apply a fix without considering the testing implications.
- **NEVER** change unrelated logic or engage in large-scale refactoring unless it is a direct and necessary consequence of the fix.

---

### **Example Usage (For the current bug)**

Here is how you would use this new command for our specific problem:

`claude -i .claude/commands/implement_fix.md`

**User Prompt:**

"Hi Claude, please use the `implement_fix` command.

1.  **Goal**: Fix the bug where the parser incorrectly identifies the Table of Contents page as the start of every section because it's matching on header strings.
2.  **File to Modify**: `soc_parser/src/parser.py`
3.  **Function to Modify**: `_identify_sections_by_content`
4.  **Logic to Implement**: Inside the loop that iterates over lines, add a check to skip any line that looks like a Table of Contents entry. A good heuristic is to skip lines that end with a page number. Please use a regular expression for this check."