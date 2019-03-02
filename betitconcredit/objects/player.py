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
    return uniform(1000, 9000)


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
        self.creditCardList = List[CreditCard]
        self.devilsDealBool = False
        self.incomeInt = get_random_account_income_int()
        self.billTotalFloat = self.incomeInt * get_random_bill_percent_float()
        self.jobBool = True
        self.nameStr = nameStr
