'''
Given a string Text, its k-mer Compositionk(Text) is the collection of all k-mer substrings of Text (including repeated
k-mers). For example,

Composition3(TATGGGGTGC) = {ATG, GGG, GGG, GGT, GTG, TAT, TGC, TGG}

CODE CHALLENGE: Solve the String Composition Problem.
     Input: An integer k and a string Text.
     Output: Compositionk(Text) (the k-mers can be provided in any order).

Sample Input:
     5
     CAATCCAAC

Sample Output:
     CAATC
     AATCC
     ATCCA
     TCCAA
     CCAAC
'''