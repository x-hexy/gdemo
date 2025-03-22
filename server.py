from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3
import json

app = Flask(__name__)
CORS(app)  # 允许所有来源访问

# 连接 SQLite 数据库
def get_db_connection():
    conn = sqlite3.connect('power_network.db')
    conn.row_factory = sqlite3.Row  # 让查询结果以字典形式返回
    return conn

# API 端点：获取所有数据（转换为 GeoJSON 格式）
@app.route('/network', methods=['GET'])
def get_network():
    conn = get_db_connection()
    cursor = conn.cursor()

    # 获取变电站
    cursor.execute("SELECT * FROM Substations")
    substations = cursor.fetchall()

    # 获取线路
    cursor.execute("SELECT * FROM Lines")
    lines = cursor.fetchall()

    # 转换为 GeoJSON 格式
    features = []

    # 处理变电站
    for substation in substations:
        features.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [substation['longitude'], substation['latitude']]
            },
            "properties": {
                "name": substation['name'],
                "type": "Substation"
            }
        })

    # 处理线路
    for line in lines:
        coordinates = json.loads(line['coordinates'])
        features.append({
            "type": "Feature",
            "geometry": {
                "type": "LineString",
                "coordinates": coordinates
            },
            "properties": {
                "name": line['name'],
                "voltage": line['voltage']
            }
        })

    geojson = {
        "type": "FeatureCollection",
        "features": features
    }

    conn.close()
    return jsonify(geojson)

# 启动 Flask 服务
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)