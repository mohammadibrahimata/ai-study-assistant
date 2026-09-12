from flask import Flask, render_template, request, redirect, session
import sqlite3
import ollama
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "local-development-key"


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username=?",
            (username,)
        )

        user = cursor.fetchone()
        conn.close()

        if user and check_password_hash(user[2], password):
            session["username"] = username
            return redirect("/dashboard")
        else:
            return "Invalid username or password"

    return render_template("login.html")


@app.route("/users")
def users():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("SELECT username FROM users")
    data = cursor.fetchall()

    conn.close()

    return render_template("users.html", users=data)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        hashed_password = generate_password_hash(password)

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, hashed_password)
        )

        conn.commit()
        conn.close()

        return "Registered successfully!"

    return render_template("register.html")


@app.route("/dashboard")
def dashboard():
    if "username" not in session:
        return redirect("/login")

    return render_template("dashboard.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@app.route("/upload", methods=["GET", "POST"])
def upload():
    if "username" not in session:
        return redirect("/login")

    if request.method == "POST":
        notes = request.form["notes"]

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT
            )
        """)

        cursor.execute(
            "INSERT INTO notes (content) VALUES (?)",
            (notes,)
        )

        conn.commit()
        conn.close()

        return "Notes saved!"

    return render_template("upload.html")


@app.route("/notes")
def notes():
    if "username" not in session:
        return redirect("/login")

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM notes")
    all_notes = cursor.fetchall()

    conn.close()

    return render_template("notes.html", notes=all_notes)


@app.route("/ask", methods=["GET", "POST"])
def ask():
    if "username" not in session:
        return redirect("/login")

    answer = ""

    if request.method == "POST":
        question = request.form["question"]

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        cursor.execute("SELECT content FROM notes")
        notes = cursor.fetchall()

        conn.close()

        notes_text = "\n".join([note[0] for note in notes])

        response = ollama.chat(
            model="phi3",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful study assistant. Use the student's notes when answering."
                },
                {
                    "role": "user",
                    "content": f"""
Student Notes:
{notes_text}

Question:
{question}
"""
                }
            ]
        )

        answer = response["message"]["content"]

    return render_template("ask.html", answer=answer)


if __name__ == "__main__":
    app.run(debug=True)