from flask_restx import Resource, Namespace
from flask import request
from marshmallow import Schema
from implemented import movie_service
from dao.model.schema import MovieSchema


movie_ns = Namespace('movies')
movie_schema = MovieSchema(many=True)
movie_schema_one = MovieSchema()

@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        if len(request.args) > 0:
            return movie_schema.dump(movie_service.get_movie_by(
                **request.args)
            )

        else:
            return movie_schema.dump(movie_service.get_movies()), 200

        # if director_id := request.args.get("director_id"):
        #     return movie_schema.dump(movie_service.get_movie_by(director_id=director_id)), 200
        # elif genre_id := request.args.get("genre_id"):
        #     return movie_schema.dump(movie_service.get_movie_by(genre_id=genre_id)), 200
        # elif year := request.args.get("year"):
        #     return movie_schema.dump(movie_service.get_movie_by(year=year)), 200

    def post(self):

        movie_service.add_file(request.json)
        return "", 201


@movie_ns.route('/<int:movie_id>')
class MoviesView(Resource):
    def get(self, movie_id):
        return movie_schema.dump([movie_service.get_one(movie_id)]), 200

    def put(self, movie_id: int):
        movie_service.update_film(request.json)
        return "", 201


    def delete(self, movie_id: int):
        movie_service.delete_film_by_id(movie_id)
        return "", 201