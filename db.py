# databaseを直接操作するファイル

import mysql.connector
import time
from werkzeug.security import generate_password_hash

# # MySQL接続（dbはdocker-composeのservice名）
# 初回でも通常接続でも必ず実行される関数
def get_conn():
    
    # _は変数不要のため　tryは接続をする関数、接続したらretrunを実行
    for _ in range(10): 
        try:
            return mysql.connector.connect(
                # 左側は変えてはいけない　右側は任意
                host="db",
                user="user",
                password="pass",
                database="shift_db"
            )
        except mysql.connector.Error:
            time.sleep(2)
    raise Exception("MySQL に接続できませんでした")


# 初回起動時にテーブル作成　名前登録削除データベース
def init_db():
    time.sleep(5)  # MySQL起動待ち
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS staff (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50) unique,
            password VARCHAR(255) NOT NULL,
            hourly_wage INT NOT NULL
        )
    """)
     
# 初回起動時にテーブル作成 勤怠情報確認
    cur.execute("""
        CREATE TABLE IF NOT EXISTS stamping (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50),
            dates DATE,
            start_stamping TIME,
            end_stamping TIME,
            overtime TIME,
            rest TIME,
            total TIME,
            log TIMESTAMP    
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS adminuser (
            id INT AUTO_INCREMENT PRIMARY KEY,
            staff_id int NOT NULL,
            name VARCHAR(50) unique,
            password VARCHAR(255) NOT NULL,
            FOREIGN KEY (staff_id) REFERENCES staff(id) ON DELETE CASCADE
        )
    """)

#     cur.execute("""
#     SELECT id FROM adminuser WHERE name = %s
# """, ("admin",))
# # fetchoneはselectされた値から一つ取り出すもの　何もなかったらnone
#     if cur.fetchone() is None:
#       password = generate_password_hash("1234")
#       cur.execute("""
#         INSERT INTO staff (name, password, hourly_wage)
#         VALUES (%s, %s, %s)
#     """, ("admin", password, 3000))

#     staff_id = cur.lastrowid  # ← staff.id を取得 直前に取得したプライマリー気を取得t

#     # ② adminuser を作る
#     cur.execute("""
#         INSERT INTO adminuser (staff_id, name, password)
#         VALUES (%s, %s, %s)
#     """, (staff_id, "admin", password))


    # 変更を保存
    conn.commit()
    # カーソルを閉じる
    cur.close()
    # データベース接続を閉じる
    conn.close()


