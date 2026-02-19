from flask import Blueprint,Flask, request, jsonify, render_template
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash
from db import get_conn, init_db

stamping_bp=Blueprint("stamping", __name__)

@stamping_bp.route("/clock_in", methods=["POST"])
@jwt_required()
def clock_in():    
    user = get_jwt_identity()
    return jsonify({"message": f"{user} さんの出勤を記録しました"})
