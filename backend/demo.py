# from authentication.register import RegisterManager
# from src.artifacts.entities import student
# from authentication.hashing import hash_password


# if __name__ == "__main__":
#     reg = RegisterManager()
#     email="alice.smith@example.com"
#     password="securepassword123"
#     hashed_password = hash_password(password)
#     new_student = student(
#         first_name="Alice",
#         last_name="Smith",
#         phone="1234567890",
#         dob="2000-01-01",
#         university_id=2,
#         major="Computer Science",
#         year_of_student=2,
#         status="UG",
#         role="student"
#     )
#     try:
#         student_id = reg.register(email, hashed_password, new_student)
#         print(f"Student registered with ID: {student_id}")
#     except Exception as e:
#         print(f"Error registering student: {str(e)}")

# from authentication.login import LoginManager

# if __name__ == "__main__":
#     login_manager = LoginManager()
#     email = "aspirantdebtanu07@gmail.com"
#     password ="Debtanu@7861"
#     try:
#         login_response = login_manager.login(email, password)
#         print("Login successful!")
#         print("Access Token:", login_response["access_token"])
#         print("User ID:", login_response["user_id"])
#         print("Email:", login_response["email"])
#         print("Role:", login_response["role"])
#     except Exception as e:
#         print("Login failed:", str(e))

from src.data_connection.connection import connect_db, disconnect_db
from src.logger import logging
from src.exception import MyException
import sys

if __name__ == "__main__":
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        print(users)
    except Exception as e:
        logging.error("Error occurred while connecting to the database")
        raise MyException("Error occurred while connecting to the database")
    finally:
        disconnect_db()
