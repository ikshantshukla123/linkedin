# LinkedIn Heatmap Backend

Backend service for LinkedIn activity heatmap visualization.

## Project Structure

```
linkedin-heatmap-backend/
├── app/                     # All backend code
│   ├── main.py             # FastAPI entry point
│   ├── api/                # API routes (controllers)
│   ├── core/               # App configuration
│   ├── models/             # Database tables (SQLAlchemy)
│   ├── schemas/            # Request/response shapes (Pydantic)
│   ├── services/           # Business logic
│   ├── workers/            # Background workers
│   ├── scraper/            # LinkedIn scraping logic
│   └── utils/              # Helper functions
├── tests/                  # Tests
├── alembic/                # Database migrations
└── requirements.txt        # Python dependencies
```

## Setup

1. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
uvicorn app.main:app --reload
```

## API Endpoints

- `GET /health` - Health check
- More endpoints coming soon...

## Development

- Python 3.11+
- FastAPI
- SQLAlchemy
- Playwright (for scraping)

## License

MIT
