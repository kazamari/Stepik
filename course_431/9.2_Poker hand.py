'''
A poker deck contains 52 cards. Each card has a suit of either clubs, diamonds, hearts, or spades (denoted C, D, H, S).
Each card also has a value of either 2 through 10, jack, queen, king, or ace (denoted 2, 3, 4, 5, 6, 7, 8, 9, 10, J,
Q, K, A). For scoring purposes card values are ordered as above, with 2 having the lowest and ace the highest value.
The suit has no impact on value.

A poker hand consists of five cards. Poker hands are ranked by the following partial order from lowest to highest.

High Card
Hands which do not fit any higher category are ranked by the value of their highest card.

Pair
Two of the five cards in the hand have the same value.

Two Pairs
The hand contains two different pairs.

Three of a Kind
Three of the cards in the hand have the same value.

Straight
Hand contains five cards with consecutive values.

Flush
Hand contains five cards of the same suit.

Full House
Three cards of the same value, with the remaining two cards forming a pair.

Four of a Kind
Four cards with the same value.

Straight Flush
Five cards of the same suit in numerical order.

Royal Flush
Consists of the ace, king, queen, jack and ten of a suit.

﻿Напишите программу, которая получает на вход пять карт и выводит старшую покерную комбинацию, которая образуется этими
картами.

Формат ввода:
Одна строка, на которой указаны пять карт в формате <value><suit>, записанные через пробел.

Формат вывода:
Название старшей комбинации, сформировавшейся на пришедшем наборе.

Sample Input:
    10C JC QC KC AC

Sample Output:
    Royal Flush
'''

import re

suits = ('C', 'D', 'H', 'S')
values = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
straight = [list(values[i:(i+5)]) for i in range(len(values)-4)]+[list(values[:4])+['A']]

def sort_by_values(inputStr):
    return values.index(inputStr)

def poker(s):
    value = [re.search(r'(.+)([CDHS])', x).group(1) for x in s]
    suit = [re.search(r'(.+)([CDHS])', x).group(2) for x in s]
    value.sort(key=sort_by_values)
    value1 = {x: value.count(x) for x in value}
    suit1 = {x: suit.count(x) for x in suits}
    res = ''
    if 5 in suit1.values():
        res = 'Flush'
        if value in straight:
            res = 'Royal Flush' if 'A' in value and '10' in value else 'Straight Flush'
    elif value in straight:
        res = 'Straight'
    elif 4 in value1.values():
        res = 'Four of a Kind'
    elif 3 in value1.values():
        res = 'Full House' if 2 in value1.values() else 'Three of a Kind'
    elif list(value1.values()).count(2) == 2:
        res = 'Two Pairs'
    elif list(value1.values()).count(2) == 1:
        res = 'Pair'
    else:
        res = 'High Card'
    return res

print(poker(input().split()))