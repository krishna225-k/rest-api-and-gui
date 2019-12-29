from flask import Flask, request,jsonify
import json

rawinfo= json.load(open('data.json'))
app=Flask(__name__)

@app.route('/meaning',methods=['POST'])
def find_meaning():
    data = request.get_json()
    word=data['word given']
    if word.lower() in rawinfo:
        return jsonify({'meaning':rawinfo[word]})
    else:
        return jsonify({'message':'word not found'})

app.run(port=5000)