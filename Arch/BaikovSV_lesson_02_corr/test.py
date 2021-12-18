import html.parser as hlmtparser
a = '&#1085;&#1077;&#1090;'
parser = hlmtparser.HTMLParser()
a = parser.unescape(a)
print(a)