from functools import reduce 
print("reduce with additions")
var = reduce(lambda x,y: x+y , [22,55,66,77,]) 
print(var)

f = lambda a,b: a if a> b else b: