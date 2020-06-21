ItemIncart  = 0

if ItemIncart != 2:
#   raise Exception("Product cart not matching")
    pass


assert(ItemIncart == 0)

try:
    with open("file.txt",'r') as reader:
        reader.read()
except Exception as e:
    print(e)

finally:
    print("clean the resources")