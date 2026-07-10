from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import config

# Create engine
engine = create_engine(config.DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)
    file_name = Column(String, index=True)
    instruction = Column(Text)
    status = Column(String, default="pending")  # pending, processing, preview, done, failed
    input_file_path = Column(String)
    output_file_path = Column(String, nullable=True)
    error_message = Column(Text, nullable=True)
    preview_text = Column(Text, nullable=True)
    user_confirmed = Column(Integer, default=0)  # 0=pending, 1=confirmed, -1=cancelled


# Create tables
Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_job(file_name: str, instruction: str, input_file_path: str) -> Job:
    db = SessionLocal()
    job = Job(file_name=file_name, instruction=instruction, input_file_path=input_file_path)
    db.add(job)
    db.commit()
    db.refresh(job)
    db.close()
    return job


def update_job_status(job_id: int, status: str, output_file_path: str = None, 
                     error_message: str = None, preview_text: str = None):
    db = SessionLocal()
    job = db.query(Job).filter(Job.id == job_id).first()
    if job:
        job.status = status
        if output_file_path:
            job.output_file_path = output_file_path
        if error_message:
            job.error_message = error_message
        if preview_text:
            job.preview_text = preview_text
        db.commit()
    db.close()


def get_job(job_id: int) -> Job:
    db = SessionLocal()
    job = db.query(Job).filter(Job.id == job_id).first()
    db.close()
    return job


def get_recent_jobs(limit: int = 10):
    db = SessionLocal()
    jobs = db.query(Job).order_by(Job.timestamp.desc()).limit(limit).all()
    db.close()
    return jobs


def confirm_job(job_id: int, confirmed: bool = True):
    db = SessionLocal()
    job = db.query(Job).filter(Job.id == job_id).first()
    if job:
        job.user_confirmed = 1 if confirmed else -1
        db.commit()
    db.close()
