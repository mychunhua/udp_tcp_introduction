import re

strarr  = ["str", "_str", "str#123 ", "str_"]
for str in strarr:
  #result = re.match("[a-zA-Z_][a-zA-Z_]*", str)
  result = re.match("^[a-zA-Z_][a-zA-Z_]*$", str)
  if result:
    print("%s符合(%s)" % (str, result.group()))
  else:
    print("%s不符合" % str)
