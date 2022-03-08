from flask import Blueprint, render_template, flash, request, jsonify
from flask_login import login_required, current_user
from website.models import Note
from . import db
import json

views = Blueprint('views', __name__)
# need not be same as file name (i.e. views, auth) but good practice


# this line is referred to as the decorator
@views.route('/', methods=['GET', 'POST'])
@login_required
# '/' is the URL
# when route is accessed, the function home() will run
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
    return render_template("home.html", user=current_user)


@views.route('delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})
