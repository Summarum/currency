import sys
import json
import urllib3


apiURL = urllib3('http://api.fixer.io/latest?base='+sys.argv[1])
rawJSON = apiURL.read()
convertedJSON=json.loads(rawJSON)
value = float(convertedJSON['rates'][sys.argv[2]]) * float(sys.argv[3])


print (value)
