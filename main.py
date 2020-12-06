#!flask/bin/python
from flask import Flask
from flask import render_template
import pyautogui
import pydirectinput
import json
import os
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
app = Flask(__name__)

@app.route('/buzz/')
def main():
  return render_template("index.html")

@app.route('/buzz/buttons/<int:player>')
def buttons(player):
  with open('button_mappings/player_' + str(player) + '.json') as f:
    player_mappings = json.load(f)
  return render_template("buttons.html", player_mappings=player_mappings, server_url=os.environ.get("WEB_SERVER_URL"))

@app.route('/buzz/trigger/<string:key>')
def trigger(key):
  pydirectinput.press(key)
  return ""

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000, ssl_context=('../cert.pem', '../key.pem'))
