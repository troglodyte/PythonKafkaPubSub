# student_repository.py
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from database import SessionLocal
from models import Student
from typing import List, Optional


class StudentRepository:
    """Repository for Student CRUD operations"""
    
    @staticmethod
    def create_student(student_data: dict) -> Optional[Student]:
        """Create a new student"""
        db = SessionLocal()
        try:
            student = Student(**student_data)
            db.add(student)
            db.commit()
            db.refresh(student)
            print(f"Created student: {student}")
            return student
        except SQLAlchemyError as e:
            db.rollback()
            print(f"Error creating student: {e}")
            return None
        finally:
            db.close()
    
    @staticmethod
    def get_student_by_id(student_id: int) -> Optional[Student]:
        """Get a student by ID"""
        db = SessionLocal()
        try:
            return db.query(Student).filter(Student.id == student_id).first()
        finally:
            db.close()
    
    @staticmethod
    def get_student_by_email(email: str) -> Optional[Student]:
        """Get a student by email"""
        db = SessionLocal()
        try:
            return db.query(Student).filter(Student.email == email).first()
        finally:
            db.close()
    
    @staticmethod
    def get_all_students(skip: int = 0, limit: int = 100) -> List[Student]:
        """Get all students with pagination"""
        db = SessionLocal()
        try:
            return db.query(Student).offset(skip).limit(limit).all()
        finally:
            db.close()
    
    @staticmethod
    def update_student(student_id: int, update_data: dict) -> Optional[Student]:
        """Update a student"""
        db = SessionLocal()
        try:
            student = db.query(Student).filter(Student.id == student_id).first()
            if student:
                for key, value in update_data.items():
                    if hasattr(student, key):
                        setattr(student, key, value)
                db.commit()
                db.refresh(student)
                print(f"Updated student: {student}")
                return student
            return None
        except SQLAlchemyError as e:
            db.rollback()
            print(f"Error updating student: {e}")
            return None
        finally:
            db.close()
    
    @staticmethod
    def delete_student(student_id: int) -> bool:
        """Delete a student"""
        db = SessionLocal()
        try:
            student = db.query(Student).filter(Student.id == student_id).first()
            if student:
                db.delete(student)
                db.commit()
                print(f"Deleted student ID: {student_id}")
                return True
            return False
        except SQLAlchemyError as e:
            db.rollback()
            print(f"Error deleting student: {e}")
            return False
        finally:
            db.close()
    
    @staticmethod
    def bulk_create_students(students_data: List[dict]) -> bool:
        """Bulk create students"""
        db = SessionLocal()
        try:
            students = [Student(**data) for data in students_data]
            db.bulk_save_objects(students)
            db.commit()
            print(f"Bulk created {len(students)} students")
            return True
        except SQLAlchemyError as e:
            db.rollback()
            print(f"Error bulk creating students: {e}")
            return False
        finally:
            db.close()


# Example usage
if __name__ == "__main__":
    repo = StudentRepository()
    
    # Create a student
    student_data = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "age": 20,
        "grade": 3.8,
        "phone": "+1234567890"
    }
    
    student = repo.create_student(student_data)
    
    if student:
        print(f"Created student with ID: {student.id}")
        
        # Get the student
        retrieved = repo.get_student_by_id(student.id)
        print(f"Retrieved: {retrieved}")
        
        # Update the student
        updated = repo.update_student(student.id, {"grade": 3.9})
        print(f"Updated: {updated}")
        
        # Get all students
        all_students = repo.get_all_students()
        print(f"Total students: {len(all_students)}")