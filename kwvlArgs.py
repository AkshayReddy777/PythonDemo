

def person(name, **data):
    print(name)
    for i,j in  data.items():
        print(i,j)
        

person("nain", age=28, city='Mum', phno='5566998866')

