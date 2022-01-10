dict={"Abin":7,"Kiran":21,"Ajay":2,"Aswin":8,"Sudev":12,"Rahul":1,"Amal":18,"Nideesh":17,"Niranjan":5}
l1=list(dict.items())
l1.sort()
print("Dictionary in ascending order : ",l1)

l2=list(dict.items())
l2.sort(reverse=True)
print("Dictionary in descending order : ",l2)
