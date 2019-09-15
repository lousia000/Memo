from urllib import request
from urllib import error


def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64;rv:23.0)Gecko/20100101Firefox/23.0'}
    req = request.Request(url=url, headers=headers)
    page = request.urlopen(req)
    print(page.read())


url = r'https://v4.bootcss.com/docs/4.0/examples/sign-in'
get_html(url)
