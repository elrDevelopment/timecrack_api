from flask import Flask, request, current_app, jsonify
from flask_restful import Resource, Api, reqparse
from Model import Notes as mod_obj, TasksSchema as schema


this_repo = {}

multiple = schema(many=True, strict=True)
single= ()

parser = reqparse.RequestParser()

class Notes(Resource):
    def get(self, id):
        this_repo = mod_obj.get_one(id)

        return response


class NotesList(Resource):
    def get(self):
        obj_repo = mod_obj.get_all()
      
        response = multiple.dump(obj_repo).data
        return response
