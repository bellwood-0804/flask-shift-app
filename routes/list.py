from flask import Blueprint, Flask, request, jsonify, render_template
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

list_bp = Blueprint("list", __name__)

# 名前を登録削除するページ肉貯めのもの
@list_bp.route("/list",methods=["GET"])
# jwt認証後じゃないと入れないようにするため
def list():
    return render_template("list.html")

# 打刻ページへ
@list_bp.route("/stamping",methods=["GET"])
def ortools():
    return render_template("stamping.html")

