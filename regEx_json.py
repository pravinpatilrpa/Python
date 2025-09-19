import json
x = {"name": "John","age": 30,"city": "New York"}
# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y)

import re
txt = "hello planet 1"
x = re.findall("^hello", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")

x = re.findall("\d", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")