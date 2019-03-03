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
from betitoncredit.objects.webgame import WebGame
# End project imports.


FLASK_OBJ = Flask(__name__, template_folder='../templates')
FLASK_OBJ.add_url_rule('/images/<path:filename>', endpoint='images', view_func=FLASK_OBJ.send_static_file)
WEBGAME_OBJ = WebGame()


@FLASK_OBJ.route('/')
def home():
    """
    Display the home page.
    """
    return render_template('home.html')


@FLASK_OBJ.route('/set', methods=['POST', 'GET'])
def set_name_str_and_avatar_url_str():
    if request.method == 'GET':
        return render_template('Avatar.html')
    nameStr = request.form['name']
    avatarUrlStr = request.form['avatar']
    WEBGAME_OBJ.make_player_obj(avatarUrlStr=avatarUrlStr, nameStr=nameStr)
    return render_template('playerdetails.html', player=WEBGAME_OBJ.playerObj)


@FLASK_OBJ.route('/scenario', methods=['POST', 'GET'])
def scenario():
    """
    """
    if request.method == 'GET':
        WEBGAME_OBJ.tempbutt = WEBGAME_OBJ.get_next_scenario_dict()
        return render_template('scenario.html', player=WEBGAME_OBJ.playerObj,
                               scenarioDict=WEBGAME_OBJ.tempbutt, action='scenario')
    creditCardFormDict = request.form
    infoDict = WEBGAME_OBJ.scenario_over(creditCardFormDict)
    return render_template('playerdetails.html', player=WEBGAME_OBJ.playerObj, info=infoDict, action='info')


@FLASK_OBJ.route('/info', methods=['GET'])
def info():
    """
    """
    WEBGAME_OBJ.tempbutt = WEBGAME_OBJ.get_next_scenario_dict()
    return render_template('scenario.html', player=WEBGAME_OBJ.playerObj, action='scenario',
                           scenarioDict=WEBGAME_OBJ.tempbutt)


@FLASK_OBJ.route('/scenario/select', methods=['POST'])
def select():
    """
    """
    choiceIdStr = request.form['choice']
    try:
        nameStr = request.form['cardName']
    except Exception:
        nameStr = str()
    WEBGAME_OBJ.update_balance_by_choice_id(choiceIdStr=choiceIdStr, nameStr=nameStr)
    return render_template('scenario.html', scenarioDict=WEBGAME_OBJ.tempbutt,
                           player=WEBGAME_OBJ.playerObj, action='month')


if __name__ == '__main__':
    FLASK_OBJ.debug = True
    FLASK_OBJ.run()
