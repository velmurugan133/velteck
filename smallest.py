l=list(map(str,input()))
list1=[]
for i in range(len(l)):
    a=l[:i+1:]
    list1.append(a)
#print(list1)
l2=[]
for i in list1:
    s=tuple(i)
    s=list(s)
    s=set(s)
    s=list(s)
    l2.append(s)
l3=[]
for i in range(len(l2)):
    if len(l2[i])==len(list1[i]):
        l3.append(len(l2[i]))
    elif len(l2[i])<len(list1[i]):
        l3.append(len(l2[i]))
    elif len(list1[i])<len(l2[i]):
        l3.append(len(list1[i]))
        
        
#print(l2)
max_small_no_of_sub_strings=max(l3)
print("max_small_no_of_sub_strings:",max_small_no_of_sub_strings)
    
