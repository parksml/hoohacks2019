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



# monthsSinceMissedPayment : number of months since the last missed payment
def get_payment_history_points(monthsSinceMissedPayment: int) -> int:
    if monthsSinceMissedPayment == -1 :
        return 75
    elif monthsSinceMissedPayment < 6 :
        return 10
    elif monthsSinceMissedPayment < 12 :
        return 15
    elif monthsSinceMissedPayment < 24 :
        return 25
    else :
        return 55

# avgBalance : average balance of all credit cards the player has
def get_outstanding_debt_points(avgBalance: int) -> int:
    return 0

# numberMonths : total number of months on the player's credit history,
# equivalent to the age in months of their oldest account.
def get_credit_history_points(numberMonths: int) -> int:
    return 0

# numberInquiriesLastSixMonths : number of inquiries into the player's
# credit in the last 6 months. Would be dictated by the scenario.
def get_inquiries_points(numberInquiriesLastSixMonths: int) -> int:
    return 0

# numberTradeLines : number of credit accounts assosciated with the player. 
# This includes both credit cards and loans.
def get_credit_mix_points(numberTradeLines: int) -> int:
    return 0
"""
Arg : meaning

monthsSinceMissedPayment : number of months since the last missed payment
        note : -1 indicates no missed payments

avgBalance : average balance of all credit cards the player has
        note : -1 indicates no credit cards (we won't see this in our usage, 
        but just for reference.)

numberMonths : total number of months on the player's credit history,
  equivalent to the age in months of their oldest account.

numberInquiriesLastSixMonths : number of inquiries into the player's
  credit in the last 6 months. Would be dictated by the scenario.

numberTradeLines : number of credit accounts assosciated with the player. 
  This includes both credit cards and loans.
"""
def calc_credit_score(monthsSinceMissedPayment: int, avgBalance: int, numberMonths: int,
    numberInquiriesLastSixMonths: int, numberTradeLines: int) -> int:
    score = 505
    score += get_credit_history_points(numberMonths)
    score += get_credit_mix_points(numberTradeLines)
    score += get_inquiries_points(numberInquiriesLastSixMonths)
    score += get_outstanding_debt_points(avgBalance)
    score += get_payment_history_points(monthsSinceMissedPayment)
    return score