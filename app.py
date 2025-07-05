from flask import Flask, request, render_template_string, redirect
import mysql.connector
import os

app = Flask(__name__)
DB_CFG = dict(
    host=os.getenv("DB_HOST", "localhost"),
    user=os.getenv("DB_USER", "root"),
    password=os.getenv("DB_PASS", "yourpassword"),
    database=os.getenv("DB_NAME", "login_db"),
)

HTML = """
<form method="post">
  <input name="username" placeholder="Username">
  <input name="password" placeholder="Password" type="password">
  <button>Login</button>
</form>
"""


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        conn = mysql.connector.connect(**DB_CFG)
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO users (username, password) VALUES (%s, %s)",
            (request.form["username"], request.form["password"]),
        )
        conn.commit()
        conn.close()
        return redirect("/success")
    return render_template_string(HTML)


@app.route("/success")
def success():
    return "User stored ✅", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
