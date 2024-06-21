from flask import Blueprint, request, jsonify
from flask_restful import Resource, Api
from .models import Note, db

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

class NoteResource(Resource):
    def get(self, note_id=None):
        if note_id:
            note = Note.query.get(note_id)
            if note:
                return jsonify(note.to_dict())
            else:
                return {'error': 'Note not found'}, 404
        else:
            notes = Note.query.all()
            return jsonify([note.to_dict() for note in notes])
    
    def post(self):
        data = request.get_json()
        new_note = Note(
            title=data.get('title'),
            content=data.get('content')
        )
        db.session.add(new_note)
        db.session.commit()
        return jsonify(new_note.to_dict()), 201
    
    def put(self, note_id):
        note = Note.query.get(note_id)
        if note:
            data = request.get_json()
            note.title = data.get('title', note.title)
            note.content = data.get('content', note.content)
            db.session.commit()
            return jsonify(note.to_dict())
        else:
            return {'error': 'Note not found'}, 404
    
    def delete(self, note_id):
        note = Note.query.get(note_id)
        if note:
            db.session.delete(note)
            db.session.commit()
            return '', 204
        else:
            return {'error': 'Note not found'}, 404

api.add_resource(NoteResource, '/notes', '/notes/<int:note_id>')
