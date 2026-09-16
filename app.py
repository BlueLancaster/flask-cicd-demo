from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "Flask CI/CD Demo"


@app.route("/health")
def health():
    return jsonify({
        "status": "ok"
    })


@app.route("/api/users")
def get_users():
    return jsonify([
        {
            "id": 1,
            "name": "Alice"
        },
        {
            "id": 2,
            "name": "Bob"
        }
    ])


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )