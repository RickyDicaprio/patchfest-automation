## Patchfest DSA Repo

## 1. Overview
A collection of curated Data Structures &amp; Algorithms problems, starter templates, and challenge tasks for PatchFest. Solve issues, optimize solutions, and contribute new approaches to climb the leaderboard.



Contributions focus on:
- Correctness
- Readability / style
- Efficiency (where applicable)
- Tests and documentation

## 2. Folder Structure
/arrays/ → problems relating to arrays and basic manipulations
/strings/ → string problems and parsing tasks
/linked-list/ → linked list problems and helpers
/recursion/ → recursive solutions and backtracking
/backtracking/ → combinatorics and search problems
/dp/ → dynamic programming problems
/trees/ → binary tree / BST / tree algorithms
/graphs/ → graph algorithms (BFS, DFS, shortest path, etc.)
/templates/ → starter templates for C++, Python, Java
/tests/ → sample test harnesses and unit tests
/.github/ISSUE_TEMPLATE/ → issue templates for easy/medium/hard


## 3. How to Contribute
1. Fork the repository.
2. Create a branch: `git checkout -b feat/<short-description>`
3. Claim an issue by commenting “I want to work on this” on GitHub and wait for maintainer assignment.
4. Implement the solution in `/<<appropriate-folder>>/`.
5. Add/modify tests in `/tests/` (if issue requires tests).
6. Commit with a clear message: `feat: add solution for <issue-id> - <brief>`
7. Push and open a Pull Request to `IEEE-PatchFest/patchfest-dsa` with the issue number in the PR title: e.g. `Fixes #12 — Add LIS solution (C++)`.
8. Link any sample inputs/outputs and explain complexity in the PR description.

## 4. Supported Languages / Templates
- C++ (preferred for performance): use `templates/template.cpp`
- Python (for quick prototyping): use `templates/template.py`
- Java (optional): add `templates/template.java` if desired

## 5. Difficulty & Scoring
- **easy** = 5 points  
- **medium** = 10 points  
- **hard** = 20 points

Maintainers reserve the right to award partial points for partially correct or suboptimal solutions with tests.

## 6. Code Style
- C++: prefer modern C++ (C++17), meaningful variable names, avoid magic numbers, add comments.
- Python: follow PEP8, keep functions small and testable.

## 7. Communication
- Use the issue comment for coordination.
- Add short explanation of approach in PR.
- For large changes, break into multiple PRs where possible.

