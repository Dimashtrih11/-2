from flask import Flask, render_template, redirect, url_for, request, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'
DATABASE = 'site.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    if not os.path.exists(DATABASE):
        conn = get_db()
        conn.execute('''CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )''')
        conn.commit()
        conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db()
        try:
            conn.execute('INSERT INTO users (username, password) VALUES (?, ?)',
                         (username, generate_password_hash(password)))
            conn.commit()
            flash('Регистрация успешна! Войдите в аккаунт.', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Пользователь с таким именем уже существует.', 'danger')
        finally:
            conn.close()
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db()
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        conn.close()
        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            session['username'] = user['username']
            flash('Вы вошли в аккаунт!', 'success')
            return redirect(url_for('profile'))
        else:
            flash('Неверное имя пользователя или пароль.', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('Вы вышли из аккаунта.', 'info')
    return redirect(url_for('index'))

@app.route('/profile')
def profile():
    if 'user_id' not in session:
        flash('Сначала войдите в аккаунт.', 'warning')
        return redirect(url_for('login'))
    return render_template('profile.html', username=session['username'])

# Заготовки для разделов
@app.route('/cs2')
def cs2():
    return render_template('cs2.html')

@app.route('/dota2')
def dota2():
    return render_template('dota2.html')

@app.route('/standoff')
def standoff():
    return render_template('standoff.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/guides')
def guides():
    return render_template('guides.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/videos')
def videos():
    return render_template('videos.html')

@app.route('/tournaments')
def tournaments():
    return render_template('tournaments.html')

@app.route('/rating')
def rating():
    return render_template('rating.html')

@app.route('/forum')
def forum():
    return render_template('forum.html')

if __name__ == '__main__':
    init_db()
    # app.run(debug=True)
else:
    init_db()
