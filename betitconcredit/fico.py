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
# End standard library imports.

# Start third party imports.
# End third party imports.

# Start project imports.
# End project imports.



# monthsSinceMissedPayment : number of months since the last missed payment
def get_payment_history_points(monthsSinceMissedPayment: int) -> int:
    if monthsSinceMissedPayment == -1:
        return 75
    elif monthsSinceMissedPayment < 6:
        return 10
    elif monthsSinceMissedPayment < 12:
        return 15
    elif monthsSinceMissedPayment < 24:
        return 25
    else:
        return 55

# avgBalance : average balance of all credit cards the player has
def get_outstanding_debt_points(avgBalance: int) -> int:
    if avgBalance == -1:
        return 30
    elif avgBalance < 1: 
        return 55
    elif avgBalance < 100:
        return 65
    elif avgBalance < 500:
        return 50
    elif avgBalance < 750:
        return 40
    elif avgBalance < 1000:
        return 25
    else:
        return 15

# numberMonths : total number of months on the player's credit history,
# equivalent to the age in months of their oldest account.
def get_credit_history_points(numberMonths: int) -> int:
    if numberMonths < 12:
        return 12
    elif numberMonths < 24:
        return 35
    elif numberMonths < 48:
        return 60
    else:
        return 70

# numberInquiriesLastSixMonths : number of inquiries into the player's
# credit in the last 6 months. Would be dictated by the scenario.
def get_inquiries_points(numberInquiriesLastSixMonths: int) -> int:
    if numberInquiriesLastSixMonths == 0:
        return 70
    elif numberInquiriesLastSixMonths == 1:
        return 60
    elif numberInquiriesLastSixMonths == 2:
        return 45
    elif numberInquiriesLastSixMonths == 3:
        return 25
    else:
        return 20

# numberTradeLines : number of credit accounts assosciated with the player. 
# This includes both credit cards and loans.
def get_credit_mix_points(numberTradeLines: int) -> int:
    if numberTradeLines == 0:
        return 15
    elif numberTradeLines == 1:
        return 25
    elif numberTradeLines == 2:
        return 50
    elif numberTradeLines == 3:
        return 60
    else:
        return 50

# utilization : the percent utilization of the overall lines of credit. 
# It should be total balance divided by total limit.
def get_utilization_points(utilization: float) -> int:
    if utilization > 0 and utilization < 0.15:
        return 165
    elif utilization < 0.3:
        return 145
    elif utilization < 0.45:
        return 90
    elif utilization < 0.6:
        return 75
    elif utilization < 0.75:
        return 50
    elif utilization < 1:
        return 10
    else:
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

utilization : the percent utilization of the overall lines of credit. 
    It should be total balance divided by total limit.
"""
def calc_credit_score(monthsSinceMissedPayment: int, avgBalance: int, numberMonths: int,
    numberInquiriesLastSixMonths: int, numberTradeLines: int, utilization: float) -> int:
    score = 340
    score += get_credit_history_points(numberMonths)
    score += get_credit_mix_points(numberTradeLines)
    score += get_inquiries_points(numberInquiriesLastSixMonths)
    score += get_outstanding_debt_points(avgBalance)
    score += get_payment_history_points(monthsSinceMissedPayment)
    score += get_utilization_points(utilization)
    return score