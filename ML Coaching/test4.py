import re
testString="this is a test string containing 1234 and @?"
email="ahdva ahdgb had ad h 19191 abhsihek@gmail.com"
# print(re.findall("\d",testString))
print(re.search("\w+@+\S+.\S",email))