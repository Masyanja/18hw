from flask_restx import Resource, Namespace
from marshmallow import Schema
from implemented import genre_service
from dao.model.schema import GenreSchema
from service.genre import GenreService


genre_ns = Namespace('genres')
genre_schema = GenreSchema(many=True)

@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        return genre_schema.dump(genre_service.get_genres()), 200



@genre_ns.route('/<int:genre_id>')
class GenresView(Resource):
    def get(self, genre_id: int):
        return genre_schema.dump([genre_service.get_genre_by_id(genre_id)]), 200
