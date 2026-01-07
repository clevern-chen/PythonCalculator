# Claude Code Project Template

This file contains reusable settings and best practices from this project that you can apply to future projects.

## General Rules for Claude Code

Copy these rules to your `.claude/settings.json` in new projects:

### Code Quality Rules
- Always test code before committing (syntax check, linting, running tests)
- Prefer editing existing files over creating new ones
- Keep changes focused - avoid scope creep and unnecessary refactoring
- Use meaningful names for variables, functions, and files
- Add comments only where logic isn't self-evident
- Handle errors gracefully with user-friendly messages

### Git Workflow Rules
- Check for open GitHub issues before starting work
- Review all changes with `git status` and `git diff` before committing
- Use clear, descriptive commit messages (explain "why" not just "what")
- Reference issue numbers in commits (e.g., "Fixes #1")
- Test thoroughly before pushing to remote

### Documentation Rules
- Always include README.md with project description, installation, and usage
- Update documentation when adding features
- Include code examples in documentation
- Keep .gitignore updated for your language/framework

## Commit Message Template

```
Brief summary of changes (50 chars max)

Detailed explanation:
- What was changed
- Why it was changed
- Any important notes or breaking changes

[Optional: Fixes #issue-number]

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
```

## Project Startup Checklist

When starting a new project with Claude Code:

1. **Initialize Project Structure**
   - [ ] Create main source files
   - [ ] Create README.md
   - [ ] Create .gitignore
   - [ ] Create requirements.txt (Python) or package.json (Node.js)

2. **Setup Git**
   - [ ] Initialize git repository: `git init`
   - [ ] Make initial commit
   - [ ] Create GitHub repository: `gh repo create`

3. **Configure Claude**
   - [ ] Copy .claude/settings.json from template
   - [ ] Customize rules for specific project needs

4. **Development Workflow**
   - [ ] Check for issues: `gh issue list`
   - [ ] Make changes
   - [ ] Test changes
   - [ ] Commit with descriptive message
   - [ ] Push to GitHub

## Language-Specific Settings

### Python Projects
```json
{
  "preCommitChecks": [
    "python -m py_compile *.py",
    "python -m pytest (if tests exist)"
  ],
  "standardFiles": [
    "requirements.txt",
    "README.md",
    ".gitignore",
    "setup.py (for packages)"
  ],
  "styleGuide": "PEP 8"
}
```

### JavaScript/Node.js Projects
```json
{
  "preCommitChecks": [
    "npm run lint (if configured)",
    "npm test (if tests exist)"
  ],
  "standardFiles": [
    "package.json",
    "README.md",
    ".gitignore",
    ".eslintrc (optional)"
  ]
}
```

## Best Practices from This Project

### GUI Development
- Ensure good color contrast for readability
- Support both mouse and keyboard input
- Test on actual display before committing
- Use consistent layout and spacing
- Provide visual feedback for user actions

### Error Handling
- Use try-except blocks for operations that might fail
- Display user-friendly error messages
- Don't let the app crash - handle edge cases
- Validate input before processing

### Testing Strategy
- Test syntax before committing
- Run the application and verify functionality
- Test edge cases (empty input, invalid operations, etc.)
- Test all input methods (mouse, keyboard)

### Version Control
- Commit frequently with focused changes
- Each commit should be a logical unit of work
- Write commit messages for humans, not computers
- Link commits to issues when applicable

## Reusable .gitignore Templates

### Python
```
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
dist/
*.egg-info/
.env
venv/
.vscode/
.idea/
```

### Node.js
```
node_modules/
dist/
build/
*.log
.env
.DS_Store
.vscode/
.idea/
```

## Quick Reference Commands

### Git with GitHub CLI
```bash
# Check authentication
gh auth status

# Create repo and push
gh repo create ProjectName --public --source=. --remote=origin --push

# List issues
gh issue list

# View specific issue
gh issue view 1

# Close issue from commit
git commit -m "Fix bug in feature X

Fixes #1"
```

### Python Development
```bash
# Syntax check
python -m py_compile file.py

# Run application
python file.py

# Install dependencies
pip install -r requirements.txt

# Freeze dependencies
pip freeze > requirements.txt
```

---

**Note**: Customize these templates based on your specific project needs. These are starting points based on successful patterns from the Python Calculator project.
