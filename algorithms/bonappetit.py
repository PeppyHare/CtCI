"""
Anna and Brian order n items at a restaurant, but Anna declines to eat any of the kth item (where 0 < k < n) due to an allergy. When the check comes, they decide to split the cost of all the items they shared; however, Brian may have forgotten that they didn't split the kth item and accidentally charged Anna for it.

You are given n, k, the cost of each of the n items, and the total amount of money that Brian charged Anna for her portion of the bill. If the bill is fairly split, print Bon Appetit; otherwise, print the amount of money that Brian must refund to Anna.
"""


def bonappetit(k, costs, b):
    correct_total = 0
    for idx, cost in enumerate(costs):
        if idx != k:
            correct_total += cost
    if b == (correct_total / 2):
        return "Bon Appetit"
    else:
        refund = b - (correct_total / 2)
        return refund
