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


CREDIT_CARD_JSON_FILE_PATH_STR = '../jsonfiles/creditcards.json'
SCENARIO_JSON_FILE_PATH_STR = '../jsonfiles/scenarios.json'


class WebGame:
    def __init__(self, creditCardJsonFilePathStr: str = CREDIT_CARD_JSON_FILE_PATH_STR,
                 scenarioJsonFilePathStr: str = SCENARIO_JSON_FILE_PATH_STR) -> None:
        self.creditCardJsonFilePathStr = creditCardJsonFilePathStr
        self.monthsSinceStartInt = 0
        self.monthsSinceMissingPaymentInt = -1
        self.inquiresInPathSixMonthsInt = 0
        self.monthsSinceCreditEstablishedInt = 24
        self.nextScenarioDictGen = None
        # self.playerObj = Player()
        self.playerObj = None
        self.scenarioJsonFilePathStr = scenarioJsonFilePathStr

    def get_next_scenario_dict(self):
        """
        """
        if self.nextScenarioDictGen is None:
            self.nextScenarioDictGen = self.json_to_scenario_dict_gen()
        try:
            return next(self.nextScenarioDictGen)
        except StopIteration:
            return dict()

    def make_player_obj(self, avatarUrlStr: str, nameStr: str):
        """
        """
        bogusCreditCardObj = self.make_bogus_credit_card()
        studentLoadObj = self.make_student_loan_obj()
        self.playerObj = Player(avatarUrlStr=avatarUrlStr, nameStr=nameStr)
        self.playerObj.creditCardObjList.append(bogusCreditCardObj)
        self.playerObj.creditCardObjList.append(studentLoadObj)

    def make_bogus_credit_card(self):
        """
        """
        annualFeeFloat = randrange(500, 1000)
        aprFloat = uniform(.2, .3)
        cashbackFloat = 0.0
        return CreditCard(annualFeeFloat=annualFeeFloat, aprFloat=aprFloat, balanceFloat=uniform(900, 1200),
                          cashbackFloat=cashbackFloat, creditLimitInt=2000, nameStr='Discover Card')

    def make_student_loan_obj(self):
        """
        """
        annualFeeFloat = 'N/A'
        aprFloat = uniform(.05, .15)
        cashbackFloat = 'N/A'
        return CreditCard(annualFeeFloat=annualFeeFloat, aprFloat=aprFloat, balanceFloat=uniform(20000, 80000),
                          cashbackFloat=cashbackFloat, creditLimitInt='N/A', nameStr='College Loans')

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

    # def next_scenario(self):
    #     """
    #     """
    #     # Miller time.
    #     monthsSinceMissedPayment = self.monthsSinceMissingPaymentInt
    #     avgBalance = self.playerObj.get_average_credit_card_total_float()
    #     numberMonths = self.monthsSinceCreditEstablishedInt
    #     numberInquiresLastSixMonths = self.inquiresInPathSixMonthsInt
    #     numberTradeLines = len(self.playerObj.creditCardObjList)
    #     utilization = self.playerObj.get_credit_utilization_percent_float()
    #     creditScoreInt = calc_credit_score(monthsSinceMissedPayment=monthsSinceMissedPayment, avgBalance=avgBalance,
    #                                        numberMonths=numberMonths,
    #                                        numberInquiriesLastSixMonths=numberInquiresLastSixMonths,
    #                                        numberTradeLines=numberTradeLines, utilization=utilization)
    #     self.playerObj.creditScoreInt = creditScoreInt
    #     # End Miller time.
    #     self.monthsSinceCreditEstablishedInt += 6
    #     self.inquiresInPathSixMonthsInt = 0
    #     if self.monthsSinceMissingPaymentInt >= 0:
    #         self.monthsSinceMissingPaymentInt += 6
    #     for nowCreditCard in self.playerObj.creditCardObjList:
    #         if nowCreditCard.get_missed_payment_bool() is True:
    #             self.monthsSinceMissingPaymentInt = 0
    #             break
    #     for nowCreditCard in self.playerObj.creditCardObjList:
    #         nowCreditCard.make_payment(paymentFloat=)

    def json_to_scenario_dict_gen(self):
        """
        """
        with open(self.scenarioJsonFilePathStr) as inFile:
            scenarioDict = load(inFile)
        for nowScenarioDictList in scenarioDict.keys():
            for nowScenarioDict in nowScenarioDictList:
                randIndexInt = randrange(len(nowScenarioDictList))
                yield nowScenarioDictList[randIndexInt]
                del nowScenarioDictList[randIndexInt]
