"""
Object oriented programming structure
OOPS
"""
class user:
    pass
class driver:
    pass

data=[]
print(type(data))
#object construction statement
u=user()
v=user()
d=driver()

print(type(u))
print(type(v))
print(type(d))
print(u)
print(v)
print(d)
#2.write data in object
u.name="John"
u.phone="+91....88938"
u.email="juuggsf@example.com"
u.address="ludhiana"
v.name="Fionna"
v.age=40
v.salry=40000

d.name="Geoge"
d.phone="+91....88924"
d.experience=5
d.license="PBXS316"
#Referrence copy
w=v
print(w)


#update operation
u.name="John watson"
v.age=46

#delete operation
del u.phone
del d.license

#read operation
print(u.__dict__)
print(v.__dict__)
print(d.__dict__)