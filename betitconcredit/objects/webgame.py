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
INFO_PAGE_JSON_FILE_PATH_STR = '../jsonfiles/infopage.json'
SCENARIO_JSON_FILE_PATH_STR = '../jsonfiles/scenarios.json'


class WebGame:
    def __init__(self, creditCardJsonFilePathStr: str = CREDIT_CARD_JSON_FILE_PATH_STR,
                 infoPageJsonFilePathStr: str = INFO_PAGE_JSON_FILE_PATH_STR,
                 scenarioJsonFilePathStr: str = SCENARIO_JSON_FILE_PATH_STR) -> None:
        self.creditCardJsonFilePathStr = creditCardJsonFilePathStr
        self.monthsSinceStartInt = 0
        self.monthsSinceMissingPaymentInt = -1
        self.infoPageJsonFilePathStr = infoPageJsonFilePathStr
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

    # def scenario_over(self, accountBalanceFloat: float, creditCardDictList: dict, choiceIdStr: str) -> dict:
    #     """
    #     """
    #     self.playerObj.balanceFloat = accountBalanceFloat
    #     self.monthsSinceCreditEstablishedInt += 6
    #     for nowCreditCardDict in creditCardDictList:
    #         annualFeeFloat = nowCreditCardDict['fee']
    #         aprFloat = nowCreditCardDict['apr']
    #         balanceFloat = nowCreditCardDict['balance']
    #         cashbackFloat = nowCreditCardDict['cashback']
    #         creditLimitInt = nowCreditCardDict['limit']
    #         revolvingBool = nowCreditCardDict['revolving']
    #         paymentFloat = nowCreditCardDict['paymentmade']
    #         putOnCardFloat = nowCreditCardDict['newexpenses']
    #         foundBool = False
    #         for nowCreditCard in self.playerObj.creditCardObjList:
    #             if nowCreditCard.nameStr == nowCreditCardDict:
    #                 foundBool = True
    #                 nowCreditCard.annualFeeFloat = annualFeeFloat
    #                 nowCreditCard.aprFloat = aprFloat
    #                 nowCreditCard.balanceFloat = balanceFloat
    #                 nowCreditCard.cashbackFloat = cashbackFloat
    #                 nowCreditCard.creditLimit = creditLimitInt
    #                 nowCreditCard.revolvingBool = revolvingBool
    #                 break
    #         if paymentFloat < nowCreditCard.get_minimum_payment_float():
    #             nowCreditCard.missedPaymentBool = True
    #         nowCreditCard.make_payment(paymentFloat=paymentFloat)
    #         cashbackFloat = nowCreditCard.put_on_card(putOnCardFloat=putOnCardFloat)
    #         self.playerObj.balanceFloat += cashbackFloat
    #     if self.monthsSinceMissingPaymentInt >= 0:
    #         self.monthsSinceMissingPaymentInt += 6
    #     for nowCreditCard in self.playerObj.creditCardObjList:
    #         if nowCreditCard.get_missed_payment_bool() is True:
    #             self.monthsSinceMissingPaymentInt = 0
    #             break
    #     # Do choice ID stuff.
    #     for nowCreditCard in self.playerObj.creditCardObjList:
    #         nowCreditCard.make_payment(paymentFloat=)
    #     with open(self.infoPageJsonFilePathStr) as inFile:
    #         infoPageDict = load(inFile)
    #     returnInfoPageDict = infoPageDict[choiceIdStr]
    #     if returnInfoPageDict['InfoPage'] == 'RANDOM':
    #         if self.randomTipStrList is None:
    #             self.randomTipStrList = list()
    #             for nowKeyStr in infoPageDict.keys():
    #                 if 'random' in nowKeyStr.lower():
    #                     self.randomTipStrList.append(infoPageDict[nowKeyStr])
    #         randomTipIndexInt = randrange(len(self.randomTipStrList))
    #         randomTipStr = self.randomTipStrList[randomTipIndexInt]
    #         del self.randomTipStrList[randomTipIndexInt]
    #         returnInfoPageDict['InfoPage'] = randomTipStr
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
    #     self.inquiresInPathSixMonthsInt = 0
    #     return returnInfoPageDict

    def update_balance_by_choice_id(self, choiceIdStr) -> None:
        """
        """
        for nowScenarioDict in self.json_to_scenario_dict_gen():
            for nowScenarioChoiceDict in nowScenarioDict['Choices']:
                if nowScenarioChoiceDict['choiceID'] == choiceIdStr:
                    self.playerObj.accountBalanceFloat += nowScenarioChoiceDict['BalanceDiff']
                    if len(nowScenarioChoiceDict['account']) > 0:
                        self.inquiresInPathSixMonthsInt += 1
                        choiceDict = nowScenarioChoiceDict['account']
                        nameStr = choiceDict['nameStr']
                        annualFeeFloat = choiceDict['fee']
                        aprFloat = choiceDict['apr']
                        balanceFloat = choiceDict['balance']
                        cashbackFloat = choiceDict['cashback']
                        creditLimitInt = choiceDict['limit']
                        revolvingBool = choiceDict['revolving']
                        nowCreditCard = CreditCard(annualFeeFloat=annualFeeFloat, aprFloat=aprFloat,
                                                   balanceFloat=balanceFloat,
                                                   cashbackFloat=cashbackFloat, creditLimitInt=creditLimitInt,
                                                   nameStr=nameStr, revolvingBool=revolvingBool)
                        self.playerObj.creditCardObjList.append(nowCreditCard)
                    return

    def json_to_scenario_dict_gen(self):
        """
        """
        with open(self.scenarioJsonFilePathStr) as inFile:
            scenarioDict = load(inFile)
        for nowScenarioPhaseStr in scenarioDict.keys():
            scenarioDictList = scenarioDict[nowScenarioPhaseStr]
            randIndexInt = randrange(len(scenarioDictList))
            yield scenarioDictList[randIndexInt]
            del scenarioDictList[randIndexInt]
