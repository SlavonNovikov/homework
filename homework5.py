immutable_var=1,2,"world","jetta",5,6,True
print(immutable_var)
# immutable_var[0]=2
# переменую immutable_var нельзя изменить, потому что она принадлежит к типу данных кортеж

mutable_list=[5.6,True ,"Hard Rock","Cafe",7,8]
mutable_list[1:3]=False,"Happy"

print(mutable_list)