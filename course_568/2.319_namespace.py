'''
Implement a program that will simulate the work with namespaces. It is necessary to implement the support for the
creation of namespaces and adding variables into them.

In this problem, each of the namespaces has its unique text identifier - its name.

On input, your program is served the following requests:
    create <namespace> <parent> –  create the new namespace with the name <namespace> inside the space <parent>
    add <namespace> <var> – add the <var> variable to the namespace <namespace>
    get <namespace> <var> – get the name of the namespace, from which the <var> will be taken during the request from
    the <namespace>, or None, if such namespace does not exist

Let us review the set of requests
    add global a
    create foo global
    add foo b
    create bar foo
    add bar a

Structure of the namespaces, described by these requests, will be equivalent to the structure of the namespaces that
were created when performing the following code:
    a = 0
    def foo():
      b = 1
      def bar():
        a = 2

In the main body of the program we declare the a variable, thus adding it to the namespace global. Further, we declare the foo function, which leads to creation of its local namespace inside the global namespace. In our case this is described by the command create foo global. Next, inside the foo function we declare the bar function, thus creating the bar namespace inside the foo namespace, and add a variable into bar.

Let’s add the following get requests to our previous requests:
    get foo a
    get foo c
    get bar a
    get bar b

Imagine how this could look like in a code:
    a = 0
    def foo():
      b = 1
      get(a)
      get(c)
      def bar():
        a = 2
        get(a)
        get(b)

The result of the get query is the name of the namespace, from which the desired variable will be taken.

For example, the result of the get foo a query is global, because in the foo namespace the a variable is not declared,
but it is declared in the global namespace, inside which foo is located. Similarly, the result of get bar b request is
foo, and the result of get bar a operation is bar.

The result of get foo c will be None, because the c variable was not declared neither in the namespace foo, nor in its
outer space global.

More formally, the result of operation of get <namespace> <var> is:
    <namespace>, if inside this <namespace> was declared the variable <var>
    get <parent> <var> – the result of query to the space, inside which the <namespace> was created, if the variable was
    not declared
    None, if <parent> does not exist, i.e. if <namespace> is global

Input data format
    Given the number n (1 ≤ n ≤ 100) in the first line – the number of requests.
    Each of the following n lines contain one request each.
    The requests are executed in the order in which they are provided in the input data.
    The names of the namespaces and the names of the variables are strings having the length of not more than 10,
    consisting of lowercase Latin letters.

Output data format
    For each of the get requests, output its results on a separate line.

Sample Input:
    9
    add global a
    create foo global
    add foo b
    get foo a
    get foo c
    create bar foo
    add bar a
    get bar a
    get bar b

Sample Output:
    global
    None
    bar
    foo
'''

ns = {'global': {'parent':'', 'vars': []}}

def func(*args):
    def create(namespace, parent):
        if not namespace in ns.keys():
            ns.update({namespace: {'parent': parent}})

    def add(namespace, var):
        if namespace in ns.keys():
            if not 'vars' in ns[namespace].keys():
                ns[namespace].update({'vars':[var]})
            else:
                ns[namespace]['vars'].append(var)

    def get(namespace, var):
        if namespace == '':
            return None
        elif 'vars' in ns[namespace].keys() and var in ns[namespace]['vars']:
            return namespace
        else:
            return get(ns[namespace]['parent'], var)

    ff = {'create': create, 'add': add, 'get': get}
    ff[args[0]](args[1], args[2]) if args[0] != 'get' else print(ff[args[0]](args[1], args[2]))

[func(*input().split()) for i in range(int(input()))]
