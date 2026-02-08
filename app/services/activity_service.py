# Activity business logic
from sqlalchemy.orm import Session
from app.models.activity import Activity
from app.schemas.activity import ActivityCreate


class ActivityService:
    @staticmethod
    def create_activity(db: Session, activity: ActivityCreate) -> Activity:
        """Create a new activity"""
        db_activity = Activity(**activity.model_dump())
        db.add(db_activity)
        db.commit()
        db.refresh(db_activity)
        return db_activity
    
    @staticmethod
    def get_activities_by_profile(db: Session, profile_id: int) -> list[Activity]:
        """Get all activities for a profile"""
        return db.query(Activity).filter(Activity.profile_id == profile_id).all()
