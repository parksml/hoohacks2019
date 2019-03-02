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
    def __init__(self, annualFeeInt: int = None, aprFloat: float = None, balanceInt: int = None,
                 creditLimitInt: int = None) -> None:
        self.annualFeeInt = annualFeeInt
        self.aprFloat = aprFloat
        self.balanceInt = balanceInt
        self.creditLimitInt = creditLimitInt
