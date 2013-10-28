#Blackjack project
import math
import random

def getcard(n):
    if n < 0 or n > 51:
        return 'error'
    
    suits = ['c', 'd', 'h', 's']
    rank = n % 13 + 1
    return str(rank) + ' ' + suits[(int(n) / 13)]    

def count_points(hand):
    points = 0
    ace_count = 0
    for i in range(0, len(hand)): 
        if (hand[i] == 1):
            ace_count += 1
            points += 10
        points += min(hand[i], 10)
    while (points > 21 and ace_count > 0): 
        points -= 10
        ace_count -= 1
    return points
        

def shuffle(cards):
    length = len(cards)
    for i in range(length, 0, 1): 
        j = (random.random() * length)
        swap(cards, i, j)
    return cards

def getstrategy(current_hand, n): 
    return (count_points(current_hand) < n)
    
def applystrategy(hand, n):
    strat = getstrategy(hand, n)
    if strat:
        return True
    else:
        return False


def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp
