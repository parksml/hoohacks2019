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
from typing import List
# End standard library imports.

# Start third party imports.
from flask import Flask, render_template
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
        pass

    def json_to_credit_card_obj_list(self, jsonFilePathStr: str = CREDIT_CARD_JSON_FILE_PATH_STR) -> List[CreditCard]:
        """
        """
        with open(jsonFilePathStr) as inFile:
            creditCardDictList = load(inFile)
        for nowCreditCardDict in creditCardDictList:
            aprFloat = nowCreditCardDict['aprFloat']
            annualFeeFloat = None
            creditCardObj = CreditCard(aprFloat=None)


if __name__ == '__main__':
    FLASK_OBJ.run()
