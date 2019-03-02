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
from json import load
from random import randrange, uniform
from typing import List
# End standard library imports.

# Start third party imports.
from flask import Flask, render_template, request
# End third party imports.

# Start project imports.
from betitconcredit.objects.creditcard import CreditCard
# End project imports.


CREDIT_CARD_JSON_FILE_PATH_STR = './jsonfiles/creditcards.json'

FLASK_OBJ = Flask(__name__, template_folder='./templates')


@FLASK_OBJ.route('/home')
def home():
    """
    Display the home page.
    """
    return render_template('home.html')


@FLASK_OBJ.route('/set', methods=['POST'])
def set_name_str_and_avatar_url_str():
    """
    """
    nameStr = request.form['name']
    avatarUrlStr = request.form['avatar']


class WebGame:
    def __init__(self) -> None:
        self.player = None

    def make_player_obj(self):
        """
        """
        pass

    def make_bogus_credit_card(self):
        """
        """
        annualFeeFloat = randrange(500, 1000)
        aprFloat = uniform(.2, .3)
        cashbackFloat = 0.0

    def json_to_credit_card_obj_list(self, jsonFilePathStr: str = CREDIT_CARD_JSON_FILE_PATH_STR) -> List[CreditCard]:
        """
        """
        creditCardObjList = list()
        with open(jsonFilePathStr) as inFile:
            creditCardDictList = load(inFile)
        for nowCreditCardDict in creditCardDictList:
            annualFeeFloat = nowCreditCardDict['annualFeeFloat']
            aprFloat = nowCreditCardDict['aprFloat']
            cashbackFloat = nowCreditCardDict['cashbackFloat']
            creditLimitInt = nowCreditCardDict['creditLimitInt']
            nameStr = nowCreditCardDict['nameStr']
            creditCardObj = CreditCard(annualFeeFloat=annualFeeFloat, aprFloat=aprFloat, cashbackFloat=cashbackFloat,
                                       creditLimitInt=creditLimitInt, nameStr=nameStr)
            creditCardObjList.append(creditCardObj)
        return creditCardObjList


if __name__ == '__main__':
    FLASK_OBJ.debug = True
    FLASK_OBJ.run()
