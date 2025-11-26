dict1 = {'StdNo':'532','StuName': 'Naveen', 'StuAge': 21, 'StuCity': 'Hyderabad'}
print("\n Dictionary is :",dict1)
print("\n Student Name is :",dict1['StuName'])
print("\n All Keys in Dictionary ")
for x in dict1:
    print(x)
dict1["Phno"]=85457854
print("\n Uadated Dictionary is :",dict1)
dict1["StuName"]="Madhu"
print("\n Uadated Dictionary is :",dict1)
dict1.pop("StuAge");
print("\n Uadated Dictionary is :",dict1)
print("Length of Dictionary is :",len(dict1))
dict2=dict1.copy()
print("\n New Dictionary is :",dict2)
dict1.clear()
print("\n Uadated Dictionary is :",dict1)