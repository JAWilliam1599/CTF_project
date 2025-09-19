from flask import Flask, request, jsonify, send_from_directory
from utils.email_assistant import EmailAssistant

app = Flask(__name__, static_url_path="", static_folder="static")


@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")


email_assistant = EmailAssistant()


@app.route("/send_mail", methods=["POST"])
def send_mail():
    try:
        body = request.json.get("body")
        subject = request.json.get("subject", "")
        if not body:
            return jsonify({"error": "No body provided"}), 400
        result = email_assistant.process_email(body, subject)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=25003)
