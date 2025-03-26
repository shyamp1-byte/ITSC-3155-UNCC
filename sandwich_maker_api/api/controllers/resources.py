from sqlalchemy.orm import Session
from ..models import models, schemas

def create_resource(db: Session, resource: schemas.ResourceCreate):
    db_resource = models.Resource(**resource.dict())
    db.add(db_resource)
    db.commit()
    db.refresh(db_resource)
    return db_resource

def get_resources(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Resource).offset(skip).limit(limit).all()

def get_resource(db: Session, resource_id: int):
    return db.query(models.Resource).filter(models.Resource.id == resource_id).first()

def update_resource(db: Session, resource: schemas.ResourceUpdate, resource_id: int):
    db_resource = db.query(models.Resource).filter(models.Resource.id == resource_id).first()
    if db_resource:
        for key, value in resource.dict(exclude_unset=True).items():
            setattr(db_resource, key, value)
        db.commit()
        db.refresh(db_resource)
        return db_resource
    return None

def delete_resource(db: Session, resource_id: int):
    db_resource = db.query(models.Resource).filter(models.Resource.id == resource_id).first()
    if db_resource:
        db.delete(db_resource)
        db.commit()
        return db_resource
    return None
