from app import app , db
import jwt
from Utily.UserModel import Userapi
from flask import Blueprint , request , make_response , jsonify
import datetime

utilty = Blueprint ( "utilty" , __name__ )


@utilty.route ( "/login" , methods = [ "GET" , "POST" ] )
def auth_encoding ( ) :
    try :
        if request.method == "POST" :
            person_id = request.args.get ( "person_id" )
            if person_id :
                payload = {
                    "exp" : datetime.datetime.utcnow ( ) + datetime.timedelta ( days = 1 ) ,
                    "iat" : datetime.datetime.utcnow ( ) ,
                    "sub" : person_id
                }

                token: bytes = jwt.encode ( payload , app.config [ "SECRET_KEY" ] )

                return jsonify ( token.decode ( "UTF-8" ) )

            return make_response ( { "Message" : " Error on authenticate" } )

        return make_response ( { "Messagge" : "Method not Allowed " } , 405 )

    except Exception as e :
        return e


@utilty.route ( "/create" , methods = [ "GET" , "POST" ] )
def create_employee ( ) :
    try :
        if request.method == "POST" :
            em_data = Userapi ( name = request.json [ "name" ] ,
                                registerd = datetime.datetime.utcnow ( ) ,
                                password = request.json [ "password" ]
                                )
            if em_data :
                db.session.add ( em_data )
                db.session.commit ( )
            else :
                return jsonify ( "data is missing" )
        else :
            return jsonify ( { "Message" : "Only POST method Allowed" } )
    except Exception as e :
        return e

    return make_response ( str ( "200" ) )
