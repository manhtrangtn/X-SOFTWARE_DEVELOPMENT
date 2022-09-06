def scp(n):
    for i in range(1,n//2+1):
        if i**2==n:
            return True
    return False
list = []
n=-1
while n!=100:
    n = int(input("Nhap so(0<n<200): "))
    list.append(n)
print("In day so:",end="")
for x in list:
    print("",x,end="")
print()
#Liet ke tan so cac phan tu
list2=[]
for x in list:
    if x not in list2:
        list2.append(x)
for x in list2:
    print("So lan xuat hien cua",x,"la:",list.count(x))
#Tim scp lon nhat trong day
max=0
for x in list:
    if x>max:
        max=x
print("SCP lon nhat trong day: ",max)