import sys
import json
from urllib2 import urlopen

kittens = urlopen('http://api.fixer.io/latest?base='+sys.argv[1])
d = kittens.read()
response=json.loads(d)
value = float(response['rates'][sys.argv[2]]) * float(sys.argv[3])


print value
