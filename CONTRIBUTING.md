# Contributing to Financial Dashboard

Thank you for your interest in contributing to the Financial Dashboard project! This document provides guidelines and instructions for contributing.

## Quick Start

### Prerequisites
- Python 3.11+
- Node.js 18+
- PostgreSQL 15+
- Git

### Setup Development Environment
1. Clone the repository
2. Set up backend: cd backend && python -m venv venv && source venv/bin/activate && pip install -r requirements.txt
3. Set up database: docker-compose up -d postgres
4. Run migrations: cd backend && alembic upgrade head
5. Start backend: uvicorn app.main:app --reload

## Development Workflow

### Branch Strategy (GitFlow)
- main - Production-ready code
- develop - Integration branch for features
- feature/feature-name - New features
- hotfix/fix-name - Critical fixes
- release/version - Release preparation

### Step-by-Step Process
1. Start from develop branch
   git checkout develop
   git pull origin develop

2. Create feature branch
   git checkout -b feature/your-feature-name

3. Make your changes
   - Write code
   - Add tests
   - Update documentation

4. Commit with proper messages (see format below)
   git add .
   git commit -m "feat(auth): add JWT token authentication"

5. Push branch and create Pull Request
   git push origin feature/your-feature-name

6. Create Pull Request on GitHub
   - Base: develop
   - Compare: feature/your-feature-name
   - Fill out PR template

## Commit Message Format

Follow this format for all commits:

type(scope): description

Optional longer description explaining the change in detail.

Closes #issue-number

### Commit Types
- feat: New feature
- fix: Bug fix
- docs: Documentation changes
- style: Code style changes (formatting, semicolons, etc.)
- refactor: Code refactoring without feature changes
- test: Adding or updating tests
- chore: Maintenance tasks, dependencies

### Examples
feat(auth): implement JWT authentication system
fix(parser): handle malformed CSV files gracefully
docs(api): add endpoint documentation for transactions
test(auth): add unit tests for login functionality

## Code Style Guidelines

### Backend (Python)
- Follow PEP 8 style guide
- Use Black formatter: black .
- Use type hints for all functions
- Maximum line length: 88 characters
- Use docstrings for all public functions

Example:
def process_transaction(amount: float, description: str) -> Transaction:
    """
    Process a financial transaction.
    
    Args:
        amount: Transaction amount
        description: Transaction description
        
    Returns:
        Processed Transaction object
    """
    pass

### Frontend (React/TypeScript)
- Use Prettier formatter
- Use TypeScript for all components
- Use functional components with hooks
- Use Tailwind CSS for styling
- Component names in PascalCase

Example:
interface TransactionProps {
  amount: number;
  description: string;
}

const Transaction: React.FC<TransactionProps> = ({ amount, description }) => {
  return (
    <div className="bg-white p-4 rounded-lg shadow">
      <p className="font-bold">${amount}</p>
      <p className="text-gray-600">{description}</p>
    </div>
  );
};

## Testing Guidelines

### Backend Testing
- Use pytest for all tests
- Aim for 80%+ test coverage
- Test files in tests/ directory
- Name test files: test_*.py

Example:
def test_create_transaction():
    """Test transaction creation."""
    transaction = create_transaction(100.50, "Grocery store")
    assert transaction.amount == 100.50
    assert transaction.description == "Grocery store"

### Frontend Testing
- Use Vitest and React Testing Library
- Test user interactions, not implementation
- Test files: *.test.tsx

## Pull Request Guidelines

### PR Checklist
- [ ] Branch is up to date with develop
- [ ] All tests pass
- [ ] Code follows style guidelines
- [ ] Documentation updated if needed
- [ ] Commit messages follow format
- [ ] No merge conflicts

### PR Description Template
## What changes were made?
Brief description of the changes.

## Why were these changes necessary?
Explain the problem this PR solves.

## How to test?
Steps to test the changes locally.

## Screenshots (if applicable)
Add screenshots for UI changes.

Closes #issue-number

## Bug Reports

### Before Reporting
1. Check existing issues
2. Try to reproduce the bug
3. Check if it's fixed in develop branch

### Bug Report Template
- Bug Description: What happened?
- Expected Behavior: What should happen?
- Steps to Reproduce: Detailed steps
- Environment: OS, browser, versions
- Screenshots: If applicable

## Feature Requests

### Feature Request Template
- Feature Description: What feature do you want?
- Use Case: Why is this feature needed?
- Proposed Solution: How should it work?
- Alternative Solutions: Other ways to solve this

## Security Issues

Do not create public issues for security vulnerabilities.

Instead, email: [your-email@example.com]

## Resources

### Documentation
- FastAPI Documentation: https://fastapi.tiangolo.com/
- React Documentation: https://react.dev/
- TypeScript Documentation: https://www.typescriptlang.org/docs/
- Tailwind CSS Documentation: https://tailwindcss.com/docs

### Learning Resources
- Python Testing with pytest: https://docs.pytest.org/
- React Testing Library: https://testing-library.com/docs/react-testing-library/intro/
- Git Workflow Tutorial: https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow

## Community Guidelines

### Be Respectful
- Use inclusive language
- Be constructive in feedback
- Help newcomers learn

### Communication
- Ask questions in issues or discussions
- Be patient with response times
- Provide clear, detailed information

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to the Financial Dashboard project!