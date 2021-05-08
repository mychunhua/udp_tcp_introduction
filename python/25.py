import re

strarr  = ["str1", "_str2", "3_str", "_str4_"]
for str in strarr:
  result = re.match("[a-zA-Z_]+[\w]*", str)
  if result:
    print("%s符合" % str)
  else:
    print("%s不符合" % str)



