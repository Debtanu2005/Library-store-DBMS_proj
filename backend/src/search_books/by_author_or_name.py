from src.data_connection.connection import connect_db, disconnect_db


class BookSearch:
    def __init__(self):
        self.conn = connect_db()
        self.cursor = self.conn.cursor()

    def search(self, query=None) -> dict:
        try:
            if not query or query.strip() == '':
                # Return all books
                self.cursor.execute("""
                    SELECT 
                        b.book_id, b.title, b.publisher, b.price,
                        b.quantity, b.type, b.purchase_option, b.format,
                        COALESCE(AVG(r.rating), 0) as rating
                    FROM books b
                    LEFT JOIN reviews r ON b.book_id = r.book_id
                    GROUP BY 
                        b.book_id, b.title, b.publisher, b.price,
                        b.quantity, b.type, b.purchase_option, b.format
                """)
            else:
                self.cursor.execute("""
                    SELECT 
                        b.book_id, b.title, b.publisher, b.price,
                        b.quantity, b.type, b.purchase_option, b.format,
                        COALESCE(AVG(r.rating), 0) as rating
                    FROM books b
                    LEFT JOIN reviews r ON b.book_id = r.book_id
                    WHERE b.title ILIKE %s OR b.publisher ILIKE %s
                    GROUP BY 
                        b.book_id, b.title, b.publisher, b.price,
                        b.quantity, b.type, b.purchase_option, b.format
                """, (f'%{query}%', f'%{query}%'))

            results = self.cursor.fetchall()

            books = []
            for row in results:
                books.append({
                    "book_id"         : row[0],
                    "title"           : row[1],
                    "author"          : row[2],
                    "price"           : float(row[3]) if row[3] else 0,
                    "quantity"        : row[4],
                    "type"            : row[5],
                    "purchase_option" : row[6],
                    "format"          : row[7],
                    "rating"          : round(float(row[8]), 1)
                })

            return {"results": books}

        except Exception as e:
            raise Exception(str(e))

    def __del__(self):
        disconnect_db()