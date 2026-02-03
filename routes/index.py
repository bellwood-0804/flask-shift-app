from flask import Blueprint, render_template, request, jsonify
from flask_jwt_extended import create_access_token

# Blueprint を作成  indexの部分は何でも構わない
index_bp = Blueprint("index", __name__)

# ユーザー認証用（簡易例）
users = {
    "admin": "3318higashi"
}

# ルートでHTMLを返す
@index_bp.route("/", methods=["GET"])
def index():
    return render_template("index.html")

# ログインAPI
@index_bp.route("/api/login", methods=["POST"])
def login():
    # indexでjson形式に変更したがこっちではまずdataにrequestの中身(submitされたものの情報)をpython形式で取り込んでいる
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username in users and users[username] == password:
        # 後で誰がログインしているかわかるようになる　jwtによって下のような形式で誰がログインしているか確認
        # トークンの中身　は以下のようになっている。
#         {
#   "identity": "taro",
#   "exp": 1670000000   # 有効期限
# }
# 中身はpython形式

        access_token = create_access_token(identity=username)
        # json形式に変更　retrunは一つ目はbody 二つ目はステータスコードを指定できる
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"msg": "Invalid username or password"}), 401
