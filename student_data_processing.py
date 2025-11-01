import json
from logfactory import get_logger
from constants import STUDENT_QUEUE
from kafka_producer import send_message
from student_repository import StudentRepository

logger = get_logger()
repo = StudentRepository()

with open('customers/asdf1234/students.jsonl', 'r') as students_file:
    for line in students_file:
        student_data = json.loads(line)
        
        # Save to database
        student = repo.create_student(student_data)
        
        if student:
            logger.info(f"{student.first_name} saved to database and sent to queue")
            # Send to Kafka queue
            send_message(STUDENT_QUEUE, student.to_dict())
        else:
            logger.error(f"Failed to save student: {student_data.get('first_name')}")
