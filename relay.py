from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace with your Pi's webhook URL
PI_WEBHOOK = "http://islandboy@pi-bot.bumblebee-monitor.ts.net:7777/run"

@app.route("/gpt-relay", methods=["POST"])
def relay_command():
    data = request.get_json()
    if not data or "command" not in data:
        return jsonify({"error": "Missing command"}), 400

    try:
        response = requests.post(PI_WEBHOOK, json={"command": data["command"]})
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888)
