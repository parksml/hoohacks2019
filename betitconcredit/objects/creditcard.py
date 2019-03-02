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
# End third party imports.

# Start project imports.
# End project imports.


class CreditCard:
    def __init__(self, annualFeeFloat: float, aprFloat: float, cashbackPercentFloat: float,
                 creditLimitInt: int, balanceFloat: float = 0, missedPaymentBool: bool = False) -> None:
        self.annualFeeFloat = annualFeeFloat
        self.aprFloat = aprFloat
        self.balanceFloat = balanceFloat
        self.cashbackPercentFloat = cashbackPercentFloat
        self.creditLimitInt = creditLimitInt
        self.missedPaymentBool = missedPaymentBool

    def get_missed_payment_bool(self) -> bool:
        """
        """
        missedPaymentBool = self.missedPaymentBool
        self.missedPaymentBool = False
        return missedPaymentBool

    def get_minimum_payment_float(self) -> float:
        """
        Assuming 6 months is your phase.
        """
        return self.balanceFloat * (self.aprFloat / 2 + .05)

    def make_payment(self, paymentFloat: float) -> None:
        """
        Call this first.
        """
        self.balanceFloat -= paymentFloat
        if self.balanceFloat > 0:
            self.balanceFloat += self.balanceFloat * self.aprFloat / 2

    def put_on_card(self, putOnCardFloat: float) -> None:
        """
        Call this last.
        """
        putOnCardFloat = putOnCardFloat - (putOnCardFloat * self.cashbackPercentFloat)
        self.balanceFloat += putOnCardFloat
