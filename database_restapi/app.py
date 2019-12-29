from flask import Flask , request,jsonify
import sqlite3

app= Flask(__name__)

@app.route('/adduser',methods=['POST'])
def add_user():
    data = request.get_json()
    id = data['userid']
    password=data['pass']

    connection =sqlite3.connect('data.db')
    cursor=connection.cursor()
    insert_query ='INSERT INTO users VALUES (?,?)'
    cursor.execute(insert_query,(id,password))
    connection.commit()
    connection.close()

    return jsonify({"message":"User Added"})


@app.route('/getuser')
def get_user():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    select_query = 'select * from users'
    result=cursor.execute(select_query)
    result=list(result)
    connection.commit()
    connection.close()
    return jsonify({"all users":result})


@app.route('/displayuser')
def get_users():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    select_query = 'select * from users'
    result=cursor.execute(select_query)
    user=[]
    for i in result:
        user.append({'user':i[0],'pass':i[1]})
    return jsonify({'all users':user})
    connection.commit()
    connection.close()

app.run(port=5000)

