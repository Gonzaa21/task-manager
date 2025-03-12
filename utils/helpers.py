# Validation
import re

def validate_date(date: str) -> bool:
    pattern = r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$"
    return bool(re.match(pattern, date))

# Replace ANSI code color
def remove_ansi_codes(text):
    return re.sub(r'\033\[[0-9;]*m', '', text)

# ID Generator
import uuid

def generate_task_id(): return str(uuid.uuid4())[:8]