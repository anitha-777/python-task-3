# 1.	Access the value 200 from this nested tuple?
t = (10, 20, (30, 40, (100, 200)), 50)
print(t[2][2][1])


# 2.	Access the value 70 from the nested structure?
data = (10, (20, 30, (40, 50, (60, 70))), 80)
print(data[1][2][2][1])

# 3.	Convert   j=(10,20,30,40,50)  tuple data type to list data type?
j=(10,20,30,40,50)
l1=[]
for i in j:
    l1.append(i)
print(l1) 
print(type(l1))   


#4.	Find Common Elements Between Two Tuples
t1 = (1, 2, 3, 4)
t2 = (3, 4, 5, 6)
for i in t1:
    if i in t2:
       print(i)