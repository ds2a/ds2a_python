s = "this is ds2a first program"

print(s.upper())
print(s.title())
print(s.startswith("th"))
print(s.endswith("th"))
print(s[3:10])

vowels_lst = ['a','e','i','o','u']

for a in s:
    if a not in vowels_lst:
        print(a)


result = [ a for a in s  if a not in vowels_lst]
print(result)



