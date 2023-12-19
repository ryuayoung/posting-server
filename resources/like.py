from flask import request
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource
from config import Config
from mysql_connection import get_connection
from mysql.connector import Error

class LikeResource(Resource) :

    @jwt_required()
    def post(self, posting_id) :
        user_id = get_jwt_identity()
    
        try :
            connection = get_connection()
            query = '''insert into 'like'
                    (userId, postingId)
                    values
                    (%s,%s);'''
            record = (user_id, posting_id)
            cursor = connection.cursor()
            cursor.execute(query,)
        except Error as e :
            pass

    @jwt_required()
    def delete 












