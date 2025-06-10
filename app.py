import psycopg2
import os

# Lấy DATABASE_URL từ biến môi trường Render
DATABASE_URL = os.environ.get("DATABASE_URL")

def run_sql_dump():
    with open("dump.sql", "r", encoding="utf-8") as f:
        sql = f.read()

    try:
        conn = psycopg2.connect(DATABASE_URL)
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute(sql)
        print("✅ Dữ liệu đã được import thành công.")
        cur.close()
        conn.close()
    except Exception as e:
        print("❌ Có lỗi khi import dữ liệu:", e)

if __name__ == "__main__":
    run_sql_dump()
