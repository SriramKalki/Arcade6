from flask import Blueprint, render_template, request, redirect, url_for

main = Blueprint('main', __name__)

notes = []

@main.route('/')
def index():
    return render_template('index.html', notes=notes)

@main.route('/add', methods=['GET', 'POST'])
def add_note():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        notes.append({'title': title, 'content': content})
        return redirect(url_for('main.index'))
    return render_template('add_note.html')
