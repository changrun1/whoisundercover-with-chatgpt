
import flask
import chat.chat as chat
import random
 
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

gameNumber = 0
words = []
badpeople = 0
connected_users = 0

@app.route('/getWord', methods=['POST'])
def getTwoWords():
    global words, connected_users

    if(words == []):
        return "遊戲未開始"
    
    connected_users += 1
    if connected_users % 4 == badpeople:
        return words["詞9"]
    else:
        return words["詞10"]


@app.route('/getNumber', methods=['GET'])
def getNumber():
    global gameNumber
    print(gameNumber)
    return  str(gameNumber)


@app.route('/newGame', methods=['POST'])
def newGame():
    global words, gameNumber, connected_users
    gameNumber += 1
    connected_users = 0
    badpeople = random.randint(1, 2)

    words = eval(chat.getTwoWords())
    return  "詞已刷新"


@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('static', path)


if __name__ == '__main__':
    app.run(host='192.168.0.10', port=80)


