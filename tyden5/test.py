import urllib3

def get_html(url):
    f = urllib3.connection_from_url(url)
    content = f.read()
    f.close()
    return content

print(get_html('https://google.com'))
