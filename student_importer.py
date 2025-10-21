import json
from logfactory import get_logger

from constants import STUDENT_QUEUE
from kafka_producer import send_message

logger = get_logger()
with open('customers/asdf1234/students.jsonl', 'r') as students_file:
    for line in students_file:
        student = json.loads(line)
        logger.info(student['first_name'] + ' sent to the queue')
        send_message(STUDENT_QUEUE, student)
