#README File

# Financial Dashboard

A full-stack financial dashboard that processes bank statements and provides insights into income and expenses.

## Features (Planned)
- Bank statement parsing (CSV/PDF)
- Expense categorization and visualization
- Monthly/weekly financial summaries
- Offline-capable Progressive Web App

## Tech Stack
- **Backend**: FastAPI, PostgreSQL, SQLAlchemy
- **Frontend**: React, TypeScript, Tailwind CSS
- **Deployment**: Railway (backend), Vercel (frontend)
- **CI/CD**: GitHub Actions

## Development Setup

### Prerequisites
- Python 3.11+
- Node.js 18+
- PostgreSQL 15+
- Docker (optional)

###

### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```
### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```