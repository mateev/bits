import urllib.request
import re
from random import shuffle

response = urllib.request.urlopen("http://www.aaaugh.com/jokes/monty_python.html")
lines = map(lambda line: line.decode('utf-8'), response.readlines())
quotes = map(lambda line: line[:-6], filter(lambda line: line.endswith('<BR>\r\n'), lines))

quotes = list(quotes)[:-1]
