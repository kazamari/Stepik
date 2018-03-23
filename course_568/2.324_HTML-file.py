'''
Your program gets a link to an HTML-file as input.
You need to download this file, and then find all links in a form <a ... href="..." ... > inside it, and output a list
of websites to which there is a link.

In this problem a website – is a domain name with all subdomains. I.e., this is a sequence of symbols, which follows
right after the protocol symbols, if any, up to the symbols of port or path, if any, excluding the cases with relative
links in the form
<a href="../some_path/index.html">.

Please output websites in the alphabetical order.

Example of an HTML file:
    <a href="http://stepic.org/courses">
    <a href='https://stepic.org'>
    <a href='http://neerc.ifmo.ru:1345'>
    <a href="ftp://mail.ru/distib" >
    <a href="ya.ru">
    <a href="www.ya.ru">
    <a href="../skip_relative_links">

Solution example:
    mail.ru
    neerc.ifmo.ru
    stepic.org
    www.ya.ru
    ya.ru
'''

# Posted from PyCharm Edu
import requests, re

url = input().strip()

doc = requests.get(url).text
hrefs = set(re.findall(r'<a.*href= *[\'\"]?(?:(?:[\w-]+\:)?//)?(\w[\w\.-]*\.[\w]*)', doc))

print('\n'.join(sorted(hrefs)))
