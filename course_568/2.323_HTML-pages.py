'''
There are two HTML-pages – A and B.
From A we can go to B in one step, if inside A there is a link to B, i.e. inside A there is a tag <a href="B">, possibly
with additional parameters inside the tag.
From A we can go to B in two steps, if there is such document C, that from A to C we can go in one step, and from C to B
we can go in one step.

On input your program gets two lines, containing the URLs to the two documents A and B.
Output Yes, if you can go from A to B for two steps, otherwise output No.

Please note that not all links inside the HTML pages can lead to an existing HTML pages.

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

# Posted from PyCharm Edu
import urllib.request
import re

def get_links(url):
    try:
        doc = urllib.request.urlopen(url)
        return re.findall(r'href=[\'\"]([^"]*)[\'\"]', str(doc.read()))
    except:
        return []

url1, url2 = input(), input()

for x in get_links(url1):
    if url2 in get_links(x):
        print('Yes')
        break
else:
    print('No')
