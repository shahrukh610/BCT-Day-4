s={1,2,3,8,9}
s.add(7)
print(s)
s.discard(3)
print(s)
s0={8,5,3,9,21}
s.update(s0)
print(s)

s1={1,4,7,5,9,15}
s2={2,3,7,6,14}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.isdisjoint(s2))
print(s1.issuperset(s2))