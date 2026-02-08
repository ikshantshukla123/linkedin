# Date utility functions
from datetime import datetime, timedelta


def parse_relative_date(text: str) -> datetime | None:
    """Parse relative dates like '2 days ago', '1 week ago'"""
    # TODO: Implement date parsing logic
    pass


def format_datetime(dt: datetime) -> str:
    """Format datetime for display"""
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def get_date_range(days: int = 30) -> tuple[datetime, datetime]:
    """Get date range for the last N days"""
    end_date = datetime.utcnow()
    start_date = end_date - timedelta(days=days)
    return start_date, end_date
