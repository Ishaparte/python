
# List
myList=["banana","cherry","apple"]
print(myList)

myList2=list()
print(myList2)  #Creats an empty list

myList3=[5,True,"apple"]
print(myList3)

item=myList3[0]
print(item)

for i in myList3:
    print(i)

if "banana" in myList:
    print("YES")
else:
    print("NO")  

print(len(myList))

myList.append("lemmon")
print(myList)

myList.insert(1,"blueberry")
print(myList)

item1=myList.pop()
print(item1)

item2=myList.remove("cherry")
print(item2)

item3=myList.reverse()
print(myList)

item4=myList.sort()
print(myList)

myList4=[0]*5
print(myList4)

new_list=myList+myList2
print(new_list)

myList5=[1,2,3,4,5,6]
a=myList5[1:5]
b=myList5[::2]
print(a)
print(b)


# if condition 
x=2
if x==2:
    print("YES")
elif x>2:
    print("NO") 

# try/except 
astr="hello"
try:
    istr=int(astr)
except:
    istr=-1
print('First',istr)

astr=123
try:
    istr=int(astr)
except:
    istr=-1
print('second',istr)