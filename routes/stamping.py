from flask import Blueprint,Flask, request, jsonify, render_template
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash
from datetime import datetime
import zoneinfo
from db import get_conn, init_db

stamping_bp=Blueprint("stamping", __name__)
# 出勤処理
@stamping_bp.route("/clock_in", methods=["POST"])
@jwt_required()
def clock_in():    
    user = get_jwt_identity()
    now = datetime.now(zoneinfo.ZoneInfo("Asia/Tokyo")).replace(second=0, microsecond=0)
    # 出勤時刻をデータベースに登録
    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO stamping (name,start_stamping) VALUES (%s,%s)", (user,now))
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(e)
        return jsonify({"message": str(e)}), 500
    finally:
        cur.close()
        conn.close()
    

    return jsonify({"message": f"{user} さんが{now}に出勤を記録しました"})

# 退勤処理
@stamping_bp.route("/clock_out", methods=["POST"])
@jwt_required()
def clock_out():
    user = get_jwt_identity()
    now = datetime.now(zoneinfo.ZoneInfo("Asia/Tokyo")).replace(second=0, microsecond=0)
    # 出勤時刻をデータベースに登録
    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO stamping (name,end_stamping) VALUES (%s,%s)", (user,now))
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(e)
        return jsonify({"message": str(e)}), 500
    finally:
        cur.close()
        conn.close()
    return jsonify({"message": f"{user} さんが{now}に退勤を記録しました"})
