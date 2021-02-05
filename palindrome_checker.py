def check(s:str):
  return s == s[::-1]

print(check("racecar"))
print(check("not work"))
