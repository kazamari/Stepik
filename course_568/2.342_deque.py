'''
Implement the deque with dynamic looped buffer.

Commands are given as input in order to test the deque.

The first line contains the number of commands. Then each line contains one command.

Each command is specified as 2 integer numbers: a b.

    a = 1 - push front,
    a = 2 - pop front,
    a = 3 - push back,
    a = 4 - pop back.

If given command is pop, then the number b is expected value. If the pop command is called for an empty deque,
then “-1” is expected.

You should output YES if all the expected values matched. Otherwise, if at least one expectation was not met, then
output NO.асбтрас

Sample Input:
    5
    1 44
    3 50
    2 44
    2 50
    2 -1

Sample Output:
    YES
'''
import collections

de = collections.deque([])
commands = {1: lambda x: de.appendleft(x),
            2: lambda x: de.popleft() if de else -1,
            3: lambda x: de.append(x),
            4: lambda x: de.pop() if de else -1 }

n = int(input())
for _ in range(n):
    c, value = map(int, input().split())
    exp = commands[c](value)
    if exp and exp != value:
        print('NO')
        break
else:
    print('YES')
