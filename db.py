# databaseを直接操作するファイル

import mysql.connector
import time
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
    # 変更を保存
    conn.commit()
    # カーソルを閉じる
    cur.close()
    # データベース接続を閉じる
    conn.close()

