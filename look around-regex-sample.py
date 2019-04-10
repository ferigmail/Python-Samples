mport regex
a='1111    ABC   45678   active'
p=regex.compile(r'(?<=[A-Z]+)\s+(\S+)(?=\s+active)')
print(regex.findall(p,a))