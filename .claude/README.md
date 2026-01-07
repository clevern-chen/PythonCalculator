# Claude Code Settings Directory

This directory contains configuration and templates for Claude Code that can be reused across projects.

## Files in This Directory

### `settings.json`
Project-specific Claude Code settings including:
- Code quality rules
- Git workflow preferences
- Python-specific configurations
- Commit message templates

### `PORTABLE_SETTINGS.json` ⭐ **COPY THIS TO NEW PROJECTS**
A clean, language-agnostic settings template you can copy to new projects. Simply:
1. Create a `.claude` folder in your new project
2. Copy this file to `.claude/settings.json`
3. Customize as needed for your specific project

### `PROJECT_TEMPLATE.md`
Comprehensive guide including:
- Best practices and workflows
- Commit message templates
- Project startup checklists
- Language-specific configurations
- Quick reference commands

## How to Use These Settings in New Projects

### Quick Start
```bash
# In your new project directory
mkdir .claude
cp /path/to/PythonCalculator/.claude/PORTABLE_SETTINGS.json .claude/settings.json
```

### Customize for Your Project
Edit `.claude/settings.json` to:
- Add language-specific rules
- Adjust coding standards
- Set project-specific preferences

## What These Settings Do

These settings help Claude Code:
- ✅ Follow consistent coding practices
- ✅ Write better commit messages
- ✅ Test code before committing
- ✅ Link commits to GitHub issues
- ✅ Maintain high code quality
- ✅ Keep documentation up to date

## Tips for Effective Settings

1. **Start Simple**: Begin with PORTABLE_SETTINGS.json and add rules as needed
2. **Be Specific**: Clear rules lead to better results
3. **Include Examples**: Show the format you want for commits, code style, etc.
4. **Update Regularly**: Add new rules as you discover patterns that work
5. **Share Across Projects**: Reuse settings that work well

## Example: Language-Specific Customization

### For Python Projects
Add to rules:
```json
"Verify syntax with 'python -m py_compile' before committing",
"Follow PEP 8 style guidelines",
"Use type hints for function parameters and return values"
```

### For JavaScript Projects
Add to rules:
```json
"Run 'npm test' before committing",
"Follow ESLint configuration",
"Use JSDoc comments for functions"
```

### For Any GUI Project
Add to rules:
```json
"Test both mouse and keyboard input methods",
"Ensure good color contrast for accessibility",
"Test on actual display before committing changes"
```

## Learn More

- [Claude Code Documentation](https://claude.com/claude-code)
- See `PROJECT_TEMPLATE.md` for detailed workflows and best practices

---

**Remember**: Settings are guidelines to help maintain consistency and quality. Adjust them to fit your specific project needs!
