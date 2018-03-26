'''
Input data
The first line contains the only integer number N that is the number of Spanish words in the dictionary. Then N
descriptions follow: each of the descriptions is located in a separate line, where first goes a Spanish word, next goes
the space separated dash (symbol number 45), and then go the translations of this Spanish word into Latin, separated by
spaces and commas. Translations are sorted in the lexicographic order. The order of the Spanish words in the dictionary
is also lexicographic.

All words consist of only the lowercase Latin letters; length of each word does not exceed 15 characters. The total
number of words at the input is not greater than 100000.

Output data
Output the Latin-Spanish dictionary, corresponding to the given one, strictly observing the format of the input data.
In particular, the first should be the translation of a lexicographically minimal Latin word, further - the second in
this order, etc. Spanish words inside the translation must also be sorted in a lexicographic order.

Sample Input:
    3
    apple - malum, pomum, popula
    fruit - baca, bacca, popum
    punishment - malum, multa

Sample Output:
    7
    baca - fruit
    bacca - fruit
    malum - apple, punishment
    multa - punishment
    pomum - apple
    popula - apple
    popum - fruit
'''
from sys import stdin

dict = {}

for i, line in enumerate(stdin):
    if i > 0:
        spanish, latin = line.strip().split(' - ')
        dict.update({word:dict.get(word, []) + [spanish] for word in latin.split(', ')})

print(len(dict))
[print('{} - {}'.format(x, ', '.join(dict[x]))) for x in sorted(dict)]
