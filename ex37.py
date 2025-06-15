#ex37
kl=[1,2,3,4,5,6,7,8,9]
del kl[2]
print(kl)
jk=[1,2,3,4,5,6,7,8,9]
del jk[1:2]
print(jk)
mk={'a':1, 'b': 2}
del mk['a']
print(mk)
keys=mk.keys()
print(keys)
print(mk.values())
print(mk.items())
print(mk.get('b'))
mk.update({'b': 5 ,'c': 9})
print(mk)
print(mk.pop('b'))
print(mk)
kl.append(50)
print(kl)
kl.remove(1)
print(kl)
kl.pop(-2)
print(kl)
kl.insert(4,80)
print(kl)
del jk
kl.clear()
print(kl)
hu={1,2,3,4,5}
hu.add(7)
print(hu)
hu.remove(3)
print(hu)
df={5,6,7,8,9}
print(hu.union(df))
print(hu.intersection(df))
metin='hello world'
print(metin.upper())
print(metin.lower())
print(metin.replace('hello', 'hi'))
print(metin.split())