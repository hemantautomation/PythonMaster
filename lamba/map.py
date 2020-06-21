lst1 = [10,20,20,34]
lst2 = [20,30,30,30]
var = map(lambda x,y: x+y , lst1 , lst2)
print(var)
for x in var:
    print(x)


var = map(lambda x: x+2 , lst1 )
print(var)
for x in var:
    print(x)