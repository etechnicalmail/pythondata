l1 = ['abc','ba','c','daa']

for e in l1:
    print(e.count('a'))

for i in range(4):
    print(f'ans of {i+1} value')
    print(l1[i].count('a'))

for i,e in enumerate(l1):
    print(f'ans of {i+1} value')
    print(e.count('a'))
    
    
    

