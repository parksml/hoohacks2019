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
from random import randrange, uniform
from typing import List
# End standard library imports.

# Start third party imports.
# End third party imports.

# Start project imports.
from betitconcredit.objects.creditcard import CreditCard


# End project imports.


def get_random_account_balance_float() -> float:
    """
    """
    return round(uniform(1000, 9000), 2)


def get_random_account_income_int() -> int:
    """
    """
    return randrange(15000, 40000)


def get_random_bill_percent_float() -> float:
    """
    """
    return uniform(.3, .5)


class Player:
    def __init__(self, avatarUrlStr: str, nameStr: str) -> None:
        self.accountBalanceFloat = get_random_account_balance_float()
        self.avatarUrlStr = avatarUrlStr
        self.creditScoreInt = 600
        self.creditCardObjList = list()
        self.devilsDealBool = False
        self.incomeInt = get_random_account_income_int()
        self.monthlyExpensesFloat = round(self.incomeInt * get_random_bill_percent_float(), 2)
        self.jobBool = True
        self.nameStr = nameStr

    def get_average_credit_card_total_float(self):
        """
        """
        totalBalanceFloat = 0
        numberOfCardsInt = 0
        for nowCreditCardObj in self.creditCardObjList:
            if nowCreditCardObj.revolvingBool is True:
                numberOfCardsInt += 1
                totalBalanceFloat += nowCreditCardObj.balanceFloat
        return totalBalanceFloat / numberOfCardsInt

    def get_credit_utilization_percent_float(self):
        """
        """
        totalAvalaibleInt = 0
        totalUsedInt = 0
        for nowCreditCardObj in self.creditCardObjList:
            if nowCreditCardObj.revolvingBool is True:
                totalAvalaibleInt += nowCreditCardObj.creditLimitInt
                totalUsedInt += nowCreditCardObj.balanceFloat
        return totalUsedInt / totalAvalaibleInt * 100
