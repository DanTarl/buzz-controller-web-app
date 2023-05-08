#!flask/bin/python
from flask import Flask
from flask import render_template
from flask import send_file
from flask import make_response
import json
import os
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.DEBUG)
app = Flask(__name__)

try:
  import pydirectinput as keyboard
  pydirectinput.PAUSE = 0.05
except:
  from pynput.keyboard import Controller
  keyboard = Controller()

@app.route('/buzz/')
def main():
  response = make_response(render_template("index.html"))
  response.headers.set('Access-Control-Allow-Origin', os.environ.get("WEB_SERVER_URL"))
  return response

@app.route('/buzz/static/<string:file>')
def file_send(file):
  return send_file("static/" + file)

@app.route('/buzz/buttons/<int:player>')
def buttons(player):
  with open('button_mappings/player_' + str(player) + '.json') as f:
    player_mappings = json.load(f)
  response = make_response(render_template("buttons.html", player=player, player_mappings=player_mappings, server_url=os.environ.get("WEB_SERVER_URL")))
  response.headers.set('Access-Control-Allow-Origin', os.environ.get("WEB_SERVER_URL"))
  return response

@app.route('/buzz/trigger/<string:key>')
def trigger(key):
  keyboard.press(key)
  keyboard.release(key)
  response = make_response("<html></html>")
  response.headers.set('Access-Control-Allow-Origin', os.environ.get("WEB_SERVER_URL"))
  return response

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
