#!/usr/bin/env python
"""
[WHEN TO USE THIS FILE]
[INSTRUCTIONS FOR USING THIS FILE]

Project name: [MISSING]
Author: Justin Miller

This lives on the web at: [MISSING URL]
Target environment: python 3.7
"""

# Start standard library imports.
import math
# End standard library imports.

# Start third party imports.
# End third party imports.

# Start project imports.
# End project imports.



# monthsSinceMissedPayment is the number of months since the last missed payment
def get_payment_history_points(monthsSinceMissedPayment: int) -> int:
    return 0

# avgBalance is the average balance of all credit cards the player has
def get_outstanding_debt_points(avgBalance: int) -> int:
    return 0

# numberMonths is the total number of months on the player's credit history,
# equivalent to the age in months of their oldest account.
def get_credit_history_points(numberMonths: int) -> int:
    return 0

# numberInquiriesLastSixMonths is the number of inquiries into the player's
# credit in the last 6 months. Would be dictated by the scenario.
def get_inquiries_points(numberInquiriesLastSixMonths: int) -> int:
    return 0

# numberTradeLines is the number of credit accounts assosciated with the player. 
# This includes both credit cards and loans.
def get_credit_mix_points(numberTradeLines: int) -> int:
    return 0

def calc_credit_score(monthsSinceMissedPayment: int, avgBalance: int, numberMonths: int,
    numberInquiriesLastSixMonths: int, numberTradeLines: int) -> int:
        