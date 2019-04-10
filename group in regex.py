import re
A=r"Farzad is 37 years,I assume Farid is 35 years and finally Nazi is 40 years"
print(re.findall('([A-Za-z]+) \w+ (\d+)',A))
m=re.search('([A-Za-z]+) \w+ (\d+)',A)
print(m.group())
print(m.group())
print(m.group(1,2))
print(m.group(1))
print(m.group(2))
print(m.span(1))
print(m.span(2))
print(m.start(2))
print(m.end(2))

