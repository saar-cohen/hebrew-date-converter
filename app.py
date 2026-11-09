from datetime import date

import requests
from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__)
HEBCAL_URL = "https://www.hebcal.com/converter"


@app.route("/")
def index():
    return send_from_directory("static", "index.html")


@app.route("/api/convert")
def convert():
    # 1. Validate the input date (expected format: YYYY-MM-DD)
    try:
        gregorian = date.fromisoformat(request.args.get("date", ""))
    except ValueError:
        return jsonify(error="Invalid date. Please use YYYY-MM-DD."), 400

    # 2. Call the Hebcal converter API
    params = {"cfg": "json", "g2h": 1, "strict": 1, "date": gregorian.isoformat()}
    try:
        response = requests.get(HEBCAL_URL, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException:
        return jsonify(error="Hebcal service is unavailable. Please try again."), 502

    # 3. Return only what the frontend needs
    return jsonify(
        gregorian=gregorian.isoformat(),
        hebrew=data["hebrew"],
        hebrew_english=f"{data['hd']} {data['hm']} {data['hy']}",
    )


if __name__ == "__main__":
    app.run(debug=True)
