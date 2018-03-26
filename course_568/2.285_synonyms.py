'''
You are given the dictionary, consisting of pairs of words. Each word is a synonym to its pair-word. All the words in
the dictionary are different. Determine the synonym to a one given word.

Input data
On input, the program receives the number of synonym pairs – an integer N. Next go the N lines; each line contains
exactly two words-synonyms. After this goes one word.

Output data
The program should output the synonym to this word.

Sample Input:
    3
    Hello Hi
    Bye Goodbye
    List Array
    Goodbye

Sample Output:
    Bye
'''
synonyms = [input() for _ in range(int(input()))]
word = input()

for pair in synonyms:
    if word in pair:
        print(pair.replace(word, '').strip())
        break
