from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Note, db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    notes = Note.query.all()
    return render_template('index.html', notes=notes)

@main.route('/add', methods=['GET', 'POST'])
def add_note():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        new_note = Note(title=title, content=content)
        db.session.add(new_note)
        db.session.commit()
        flash('Note added successfully!', 'success')
        return redirect(url_for('main.index'))
    return render_template('add_note.html')
