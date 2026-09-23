import os

from flask import Flask, jsonify, request
from psycopg.rows import dict_row
from psycopg_pool import ConnectionPool

app = Flask(__name__)


database_url = os.environ.get("DATABASE_URL")
if not database_url:
    raise RuntimeError("DATABASE_URL environment variable is required")

pool = ConnectionPool(
    conninfo=database_url,
    min_size=1,
    max_size=5,
    kwargs={"row_factory": dict_row},
)



@app.route("/")
def home():
    return "Flask CI/CD Demo - GCP"


@app.route("/health")
def health():
    return jsonify({
        "status": "ok"
    })


@app.route("/api/users")
def get_users():
    with pool.connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT id, name FROM users ORDER BY id"
            )
            users = cur.fetchall()

    return jsonify(users)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )