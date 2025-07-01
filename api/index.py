from flask import Flask, render_template
import sys
import traceback

# Для вывода ошибок в логах Vercel

def print_exception(exc_type, exc_value, exc_traceback):
    traceback.print_exception(exc_type, exc_value, exc_traceback, file=sys.stderr)

sys.excepthook = print_exception

app = Flask(__name__, template_folder="../templates", static_folder="../static")
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    return render_template('index.html')

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
