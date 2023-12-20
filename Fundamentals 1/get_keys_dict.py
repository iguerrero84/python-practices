security_found = None

mydict = {'securityKey_1': 'securityValue_1',
          'securityKey_2': 'securityValue_2'}

security = mydict.get('securityKey_2')

if security is None:
    mydict.setdefault('securityKey_3', 'securityValue_3')
else:
    security_found = type(mydict.get('securityKey_2'))


key = list(mydict.keys())[0]
value = list(mydict.values())[0]
print('len(mydict)', len(mydict))
print(security)
print(security_found)
