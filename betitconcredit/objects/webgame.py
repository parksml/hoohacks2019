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
# End third party imports.

# Start project imports.
from betitconcredit.fico import calc_credit_score
from betitconcredit.objects.creditcard import CreditCard
from betitconcredit.objects.player import Player
# End project imports.


CREDIT_CARD_JSON_FILE_PATH_STR = './jsonfiles/creditcards.json'


class WebGame:
    def __init__(self, creditCardJsonFilePathStr: str = CREDIT_CARD_JSON_FILE_PATH_STR) -> None:
        self.creditCardJsonFilePathStr = creditCardJsonFilePathStr
        self.monthsSinceStartInt = 0
        self.monthsSinceMissingPaymentInt = -1
        self.inquiresInPathSixMonthsInt = 0
        self.monthsSinceCreditEstablishedInt = 24
        self.playerObj = Player

    def get_average_credit_card_total_float(self):
        """
        """
        totalBalanceFloat = 0
        numberOfCardsInt = 0
        for nowCreditCardObj in self.playerObj.creditCardList:
            numberOfCardsInt += 1
            totalBalanceFloat += nowCreditCardObj.balanceFloat
        return totalBalanceFloat / numberOfCardsInt

    def make_player_obj(self, avatarUrlStr: str, nameStr: str):
        """
        """
        bogusCreditCardObj = self.make_bogus_credit_card()
        self.playerObj = Player(avatarUrlStr=avatarUrlStr, nameStr=nameStr)
        self.playerObj.creditCardObjList.append(bogusCreditCardObj)

    def make_bogus_credit_card(self):
        """
        """
        annualFeeFloat = randrange(500, 1000)
        aprFloat = uniform(.2, .3)
        cashbackFloat = 0.0
        return CreditCard(annualFeeFloat=annualFeeFloat, aprFloat=aprFloat, cashbackFloat=cashbackFloat,
                          creditLimitInt=2000, nameStr='College Credit Card')

    def json_to_credit_card_obj_list(self) -> List[CreditCard]:
        """
        """
        creditCardObjList = list()
        with open(self.creditCardJsonFilePathStr) as inFile:
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

    def next_scenario(self):
        """
        """
        monthsSinceMissedPayment = self.monthsSinceMissingPaymentInt
        avgBalance = self.get_average_credit_card_total_float()
        numberMonths = self.monthsSinceCreditEstablishedInt
        numberInquiresLastSixMonths = self.inquiresInPathSixMonthsInt
        numberTradeLines = None
        utilization = None
        ficoInt = calc_credit_score()
        self.monthsSinceCreditEstablishedInt += 6
        self.inquiresInPathSixMonthsInt = 0
