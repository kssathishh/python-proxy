from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/proxy", methods=["GET"])
def proxy():
    target_url = request.args.get("url")

    if not target_url:
        return jsonify({"error": "Missing ?url= parameter"}), 400

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/118.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Referer": "https://thepiratebay.org/",
        "Cache-Control": "no-cache",
        "Pragma": "no-cache"
    }

    try:
        response = requests.get(target_url, headers=headers, timeout=20)

        # Return raw HTML
        return response.text, response.status_code

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/")
def home():
    return "Python proxy server is running ✔️"

