from flask import Flask, request, jsonify, render_template, redirect
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Initialize the database
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_first_name TEXT,
            user_second_name TEXT,
            user_surname TEXT,
            user_id_number TEXT,
            user_email TEXT UNIQUE,
            user_tel TEXT,
            user_password TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Render sign-up page
@app.route('/')
def home():
    return render_template('sign_in.html')

# Render login page
@app.route('/log_in')
def log_in_page():
    return render_template('log_in.html')

# Render tutorial/dashboard page
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Handle sign-up
@app.route('/sign_in', methods=['POST'])
def sign_in():
    try:
        data = request.get_json()
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('''
            INSERT INTO users (
                user_first_name, user_second_name, user_surname,
                user_id_number, user_email, user_tel, user_password
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            data['user_first_name'],
            data['user_second_name'],
            data['user_surname'],
            data['user_id_number'],
            data['user_email'],
            data['user_tel'],
            data['user_password']
        ))
        conn.commit()
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})
    finally:
        conn.close()

# Handle login
@app.route('/log_in', methods=['POST'])
def log_in():
    data = request.get_json()
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''
        SELECT * FROM users WHERE user_email = ? AND user_password = ?
    ''', (data['user_email'], data['user_password']))
    user = c.fetchone()
    conn.close()

    if user:
        return jsonify({"success": True})
    else:
        return jsonify({"success": False, "message": "Invalid email or password."})

# Start the app
if __name__ == '__main__':
    app.run(debug=True)

    