from flask import Flask, jsonify, render_template
from database import get_latest_readings


app = Flask(__name__)

@app.route("/")
def home():
    return "Factory Monitor is running"

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/api/readings")
def readings():
    rows = get_latest_readings()
    data = []
    for row in rows:
        data.append({
            "topic": row[0],
            "value": row[1],
            "timestamp": row[2]
        })
    return jsonify(data)

@app.route("/api/latest")
def latest():
    rows = get_latest_readings()
    latest = {}
    for row in rows:
        topic = row[0].split("/")[-1]  # gets 'temperature', 'pressure', 'status'
        if topic not in latest:
            latest[topic] = {
                "value": row[1],
                "timestamp": row[2]
            }
    return jsonify(latest)

if __name__=="__main__":
    app.run(debug=True)