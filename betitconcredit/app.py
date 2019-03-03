#!/usr/bin/env python
"""
[WHEN TO USE THIS FILE]
[INSTRUCTIONS FOR USING THIS FILE]

Project name: [MISSING]
Author: Micah Parks

This lives on the web at: [MISSING URL]
Target environment: python 3.7
"""

# Start standard library imports.
# End standard library imports.

# Start third party imports.
from flask import Flask, render_template, request
# End third party imports.

# Start project imports.
from betitconcredit.objects.webgame import WebGame
# End project imports.


FLASK_OBJ = Flask(__name__, template_folder='../templates')
WEBGAME_OBJ = WebGame()


@FLASK_OBJ.route('/')
def home():
    """
    Display the home page.
    """
    return render_template('home.html')

@FLASK_OBJ.route('/set', methods=['POST','GET'])
def set_name_str_and_avatar_url_str():
    if request.method == 'GET':
        return render_template('Avatar.html')

    nameStr = request.form['name']
    avatarUrlStr = request.form['avatar']
    WEBGAME_OBJ.make_player_obj(avatarUrlStr=avatarUrlStr, nameStr=nameStr)
    return render_template('playerdetails.html', player=WEBGAME_OBJ.playerObj)


if __name__ == '__main__':
    FLASK_OBJ.debug = True
    FLASK_OBJ.run()
