import re
a1=r'1sdfYH67!SSmm.'
a2=r'1sdfYH67SSmm'
p=re.compile(r'(?=.*[A-Z]+)(?=.*[a-z]+)(?=.*\d+)(?=.*[!?#])\S+')
print(re.findall(p,a1))
#this is for pass checking, so all condition should be satisfied hence inside the condition
#you have .* before waht u want meand any charactor before your condition and in orderso
#means any uppercase character follow after bunch of anything(.*), if all condition satisfied
# then \S+ consume the string
print(re.findall(p,a1)) # no result, as one condition is not satisfied
