from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/proxy", methods=["GET"])
def proxy():
    target_url = request.args.get("url")

    if not target_url:
        return jsonify({"error": "Missing ?url= parameter"}), 400

    try:
        response = requests.get(target_url, headers={
            "User-Agent": "Python-Proxy-Server"
        }, timeout=15)

        return response.text, response.status_code

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/")
def home():
    return "Python proxy server is running2 ✔️"

