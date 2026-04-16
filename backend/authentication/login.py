from authentication.jwt import create_access_token
from authentication.hashing import verify_password
from src.data_connection.connection import connect_db, disconnect_db
from src.logger import logging
from src.exception import MyException
import sys


class LoginManager:
    def __init__(self):
        self.conn = connect_db()
        self.cursor = self.conn.cursor()

    def login(self, email: str, password: str) -> dict:
        try:
            self.cursor.execute("""
                SELECT user_id, email, password, role
                FROM users
                WHERE email = %s
            """, (email,))

            user_data = self.cursor.fetchone()

            if not user_data:
                raise Exception("Invalid email or password")

            user_id, email, hashed_password, role = user_data

            if not verify_password(password, hashed_password):
                raise MyException("Invalid email or password")

            token_data = {
                "user_id": str(user_id),   # ← cast to str (fixes previous bug)
                "email":   str(email),
                "role":    str(role)
            }

            access_token = create_access_token(token_data)

            self.conn.commit()             # ← commit on success

            return {
                "access_token": access_token,
                "user_id": user_id,
                "email": email,
                "role": role
            }

        except Exception as e:
            self.conn.rollback()           # ← THIS is the critical fix
            logging.error(f"Login error: {str(e)}")
            raise e
        
    def __del__(self):
        try:
            disconnect_db()
        except Exception as e:
            logging.error(f"Error during database disconnection: {str(e)}", sys)