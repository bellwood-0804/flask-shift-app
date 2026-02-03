# C:\Users\USER\workspace
# docker compose up --build -d
#docker compose down

# request はpost getメソッドrequset.get_json()を使うときにやる jsonifyはpythonをjsonに変更　　API で { "message": "ok" } を返すときに使う
from flask import Flask, request, jsonify, render_template

# | 名前                    | 説明                                       | 使いどころ                                         |
# | --------------------- | ---------------------------------------- | --------------------------------------------- |
# | `JWTManager`          | Flask アプリに JWT（JSON Web Token）機能を登録するクラス | `jwt = JWTManager(app)` として初期化                |
# | `create_access_token` | JWT トークンを発行する関数                          | `/api/login` などで「ログイン成功時にトークンを作る」             |
# | `jwt_required`        | ルートに付けるデコレーター。トークンを持つユーザーだけがアクセス可能にする    | `/list` のようなログイン必須ページ                         |
# | `get_jwt_identity`    | 現在ログインしているユーザーの情報を取得する関数                 | `current_user = get_jwt_identity()` でユーザー名を取得 |


# 違うコードに書いているものもimportしてあげないといけない二重ガキだがそういうもの
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta
from ortools.sat.python import cp_model
# or-toolを使うためのインポート
from db import get_conn, init_db
# routesフォルダーのindex.pyからimportするという意味　index_bpは別のフォルダーでも書かれていてパッケージとして認識されていてこれをimportすると使える
# routesの中にあるindexやlistファイルからimportするという意味
from routes.index import index_bp
from routes.list import list_bp
from routes.register import register_bp
# from routes.stamping import stamping_bp

# create_access_toke ユーザー名などの情報を埋め込んだ JWT を生成する関数。
app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret-key"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

jwt = JWTManager(app)

# ログインするための処理
# 呼び出し　app.regiuster_buluprintは固定のかきかた　
app.register_blueprint(index_bp)

#ログイン後入るフォルダー
app.register_blueprint(list_bp)

# 人物を登録削除するためのルートに移動
app.register_blueprint(register_bp)

# 打刻時の時間をとうろくするもの
# app.stamping_blueprint(stamping_bp)

if __name__ == "__main__":
    init_db()
    # stamping_db()
    app.run(host="0.0.0.0",port=5000, debug=True)
