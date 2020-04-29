import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request, make_response

@app.route('/', methods=['GET'])
def index():
    headers = {}
    return make_response(
        jsonify(
            {
                'msg': 'Build microservice(CRUD Operation) image in docker using Dockerfile with flask and mysql',
            }
        ), 200, headers
    )

@app.route('/add', methods=['POST'])
def add_user():
        try:
                _json = request.json
                _ID = _json['ID']
                _Name = _json['Name']
                _Age = _json['Age']
                _Department = _json['Department']
                _Subject = _json['Subject']
                if _ID and _Name and _Age and _Department and _Subject and request.method == 'POST':
                        sqlQuery = "INSERT INTO users(ID, Name, Age, Department, Subject) VALUES(%s, %s, %s, %s, %s)"
                        bindData = (_ID,_Name, _Age, _Department, _Subject)
                        conn = mysql.connect()
                        cursor = conn.cursor()
                        cursor.execute(sqlQuery, bindData)
                        respone = jsonify('user added successfully!')
                        respone.status_code = 200
                        conn.commit()
                        return respone
                else:
                        return not_found()
        except Exception as e:
                print(e)
        finally:
                cursor.close()
                conn.close()

@app.route('/users', methods=['GET'])
def users():
        try:
                conn = mysql.connect()
                cursor = conn.cursor(pymysql.cursors.DictCursor)
                cursor.execute("SELECT * FROM users")
                rows = cursor.fetchall()
                resp = jsonify(rows)
                resp.status_code = 200
                return resp
        except Exception as e:
                print(e)
        finally:
                cursor.close()
                conn.close()

@app.route('/user/<int:id>', methods=['GET'])
def user(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM users WHERE ID =%s", id)
		userRow = cursor.fetchone()
		respone = jsonify(userRow)
		respone.status_code = 200
		return respone
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()


@app.route('/update', methods=['PUT'])
def update_user():
        try:
                _json = request.json
                _ID = _json['ID']
                _Name = _json['Name']
                _Age = _json['Age']
                _Department = _json['Department']
                _Subject = _json['Subject']
                if _ID and _Name and _Age and _Department and _Subject and request.method == 'PUT':
                        sqlQuery = "UPDATE users SET ID=%s, Name=%s, Age=%s, Department=%s, Subject=%s WHERE ID=%s"
                        bindData = (_ID,_Name, _Age, _Department, _Subject,_ID)
                        conn = mysql.connect()
                        cursor = conn.cursor()
                        cursor.execute(sqlQuery, bindData)
                        conn.commit()
                        respone = jsonify('user updated successfully!')
                        respone.status_code = 200
                        return respone
                else:
                        return not_found()
        except Exception as e:
                print(e)
        finally:
                cursor.close()
                conn.close()

@app.route('/delete/<int:ID>', methods=['DELETE'])
def delete_user(ID):
        try:
                conn = mysql.connect()
                cursor = conn.cursor()
                cursor.execute("DELETE FROM users WHERE ID =%s", (ID))
                conn.commit()
                respone = jsonify('user deleted successfully!')
                respone.status_code = 200
                return respone
        except Exception as e:
                print(e)
        finally:
                cursor.close()
                conn.close()


if __name__ == "__main__":
    app.run(debug=True)
                                                                                                                                                                                                                                                                                                             
