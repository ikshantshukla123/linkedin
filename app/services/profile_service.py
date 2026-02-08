# Profile business logic
from sqlalchemy.orm import Session
from app.models.profile import Profile
from app.schemas.profile import ProfileCreate


class ProfileService:
    @staticmethod
    def create_profile(db: Session, profile: ProfileCreate) -> Profile:
        """Create a new profile"""
        db_profile = Profile(**profile.model_dump())
        db.add(db_profile)
        db.commit()
        db.refresh(db_profile)
        return db_profile
    
    @staticmethod
    def get_profile(db: Session, profile_id: int) -> Profile | None:
        """Get profile by ID"""
        return db.query(Profile).filter(Profile.id == profile_id).first()
    
    @staticmethod
    def get_profiles(db: Session, skip: int = 0, limit: int = 100) -> list[Profile]:
        """Get all profiles with pagination"""
        return db.query(Profile).offset(skip).limit(limit).all()
