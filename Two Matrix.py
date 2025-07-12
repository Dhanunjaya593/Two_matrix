#write a program  that read  two  numbers  M,N and  a MxN matrix representing the 
#jersey number of the volunteers and  prints  the  jersey numbers  of the co- ordinator

m,n = list(map(int,input().split()))
s_t = []
for i in range(m):
    numbers = list(map(int,input().split()))
    #print(numbers)

    for k in numbers:
        s_t.append(k)
New_list = sorted(s_t)
#print(New_list)
length = len(New_list)-1
d= round(length/2 )
print(New_list[d])