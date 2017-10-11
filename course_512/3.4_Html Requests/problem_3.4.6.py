'''
Рассмотрим два HTML-документа A и B.
Из A можно перейти в B за один переход, если в A есть ссылка на B, т. е. внутри A есть тег <a href="B">,
возможно с дополнительными параметрами внутри тега.
Из A можно перейти в B за два перехода если существует такой документ C, что из A в C можно перейти за один переход
и из C в B можно перейти за один переход.

Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.

Обратите внимание на то, что не все ссылки внутри HTML документа могут вести на существующие HTML документы.

Sample Input 1:
    https://stepic.org/media/attachments/lesson/24472/sample0.html
    https://stepic.org/media/attachments/lesson/24472/sample2.html

Sample Output 1:
    Yes

Sample Input 2:
    https://stepic.org/media/attachments/lesson/24472/sample0.html
    https://stepic.org/media/attachments/lesson/24472/sample1.html

Sample Output 2:
    No

Sample Input 3:
    https://stepic.org/media/attachments/lesson/24472/sample1.html
    https://stepic.org/media/attachments/lesson/24472/sample2.html

Sample Output 3:
    Yes
'''

import requests, re

def get_links(url):
    try:
        doc = requests.get(url).text
        return re.findall(r'href=[\'\"]([^"]*)[\'\"]', doc)
    except:
        return []

url1, url2 = input(), input()

for x in get_links(url1):
    if url2 in get_links(x):
        print('Yes')
        break
else:
    print('No')