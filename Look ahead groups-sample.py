import re
a='grapes 100 red\ncherries 200\norange 300'
# we want to pull out just the those fruits which had the number and color

p=re.compile(r'([a-z]+) (\d+) (?=\w+)') # but it pulls out the number as well, so not this
print(re.findall(p,a))
p=re.compile(r'([a-z\s])+(?=\d+)(?=\s+)(?=\w+)' )
print(re.findall(p,a))  #empty braket, because it consumes graoes to space before number, then
# it checks look ahead by \d+ and it satisfies but the cursor gets back to space and then check
# the \s+ which is not satisifed because look ahead does not consume characters, so to have the
# three condition ahead as the same time we need to use a look ahead goups, also bear in mind
# having these look ahead like seperate group meand all should be satisfied but the order is not
#important, so it can be used for password checks not just a group
p=re.compile(r'([a-z]+)\s*(?=\d+\s*[a-z]+)',re.M)# order for look ahead is consered here
print(re.findall(p,a))
