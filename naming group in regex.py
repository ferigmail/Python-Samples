import re
a=r"New York, New York 11235"
m=re.search("([A-Za-z\s]+)\,? (\w+ \w+) (\d+)",a)#all condition should have the same space or
                #comma or anything like the string
print(m.group())
print(m.group(1,2,3))
p=re.compile("(?P<state>[A-Za-z\s]+), (?P<city>\w+ \w+) (?P<postalcode>\d+)") #have same space,comma....
t=re.search(p,a)
print((t.group('postalcode'),t.group('city')),t.group('state'))
print(t.groupdict()) #incase u forget the name of group u can have them in a dict




