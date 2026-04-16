from authentication.register import RegisterManager
from src.artifacts.entities import student


if __name__ == "__main__":
    reg = RegisterManager()
    new_student = student(
        first_name="Alice",
        last_name="Smith",
        email="alice.smith@example.com",
        phone="1234567890",
        dob="2000-01-01",
        university_id=2,
        major="Computer Science",
        status="active",
        role="student"
    )
    try:
        student_id = reg.register_student(new_student)
        print(f"Student registered with ID: {student_id}")
    except Exception as e:
        print(f"Error registering student: {str(e)}")

