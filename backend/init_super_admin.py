import bcrypt
from src.data_connection.connection import connect_db

def initialize_super_admin():
    db_connection = connect_db()
    db_cursor = db_connection.cursor()
    
    admin_email = "master@folio.edu"
    raw_password = "supersecret123"
    
    # Hash password
    password_bytes = raw_password.encode('utf-8')
    hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt()).decode('utf-8')
    
    try:
        # 🔥 IMPORTANT: Use RETURNING to get user_id
        insert_user_query = """
            INSERT INTO users (email, password, role) 
            VALUES (%s, %s, 'super_admin')
            RETURNING user_id;
        """
        db_cursor.execute(insert_user_query, (admin_email, hashed_password))
        
        # ✅ Now this works
        super_admin_id = db_cursor.fetchone()[0]
        
        # Insert into employees
        insert_employee_query = """
            INSERT INTO employees 
            (emp_id, first_name, last_name, gender, salary, aadhaar, phone) 
            VALUES (%s, 'Master', 'Control', 'Other', 150000, '000011112222', '9998887776')
        """
        db_cursor.execute(insert_employee_query, (super_admin_id,))
        
        db_connection.commit()
        
        print("✅ SUCCESS! Master account provisioned securely.")
        print(f"Email: {admin_email}")
        print(f"User ID: {super_admin_id}")
        
    except Exception as e:
        db_connection.rollback()
        print(f"❌ DATABASE ERROR: {e}")
        
    finally:
        db_cursor.close()
        db_connection.close()


if __name__ == "__main__":
    print("Initializing Super Admin setup...")
    initialize_super_admin()