from flask import Blueprint, render_template, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity,get_jwt
from werkzeug.security import check_password_hash
from db import get_conn, init_db


# Blueprint を作成  indexの部分は何でも構わない
index_bp = Blueprint("index", __name__)

# ルートでHTMLを返す
@index_bp.route("/", methods=["GET"])
def index():
    return render_template("index.html")

# ログインAPI
@index_bp.route("/api/login", methods=["POST"])
def login():
    print("LOGIN API HIT")

    # indexでjson形式に変更したがこっちではまずdataにrequestの中身(submitされたものの情報)をpython形式で取り込んでいる
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

#     if username in users and users[username] == password:
#         # 後で誰がログインしているかわかるようになる　jwtによって下のような形式で誰がログインしているか確認
#         # トークンの中身　は以下のようになっている。
# #         {
# #   "identity": "taro",
# #   "exp": 1670000000   # 有効期限
# # }
# # 中身はpython形式

#         access_token = create_access_token(identity=username)
#         # json形式に変更　retrunは一つ目はbody 二つ目はステータスコードを指定できる
#         return jsonify(access_token=access_token), 200
#     else:
#         return jsonify({"msg": "Invalid username or password"}), 401



    conn = get_conn()
    # dictionaryを付けることで、配列を数字ではなくて、実際のデータべ＾－スの名前でできる
    cur = conn.cursor(dictionary=True)

    # ユーザー取得
    cur.execute("""
        SELECT id, name, password
        FROM adminuser
        WHERE name = %s
    """, (username,))

    user = cur.fetchone()

    cur.close()
    conn.close()

    # ユーザーが存在しない or パスワード不一致
    # check_password_hashは１行目がハッシュ化されたもの、二行目は入力されたパスワード
    if user is None or not check_password_hash(user["password"], password):
        return jsonify({"msg": "Invalid username or password"}), 401

    # JWT発行（idを入れるのがベター）
    # additionalは追加で入れたい情報　ほかにもroleなど権限を指定できる　subは誰か特定　expは有効期限
#     access_token = create_access_token(
#     identity=user["id"],
#     additional_claims={
#         "name": user["name"]
#     }
# )
    access_token = create_access_token(
     identity=username,
     additional_claims={"name": username}
)


# access token : access token　と同義　access tokenの値を返している
    return jsonify(access_token=access_token), 200








