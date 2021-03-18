x=[]
print('Enter 20 numbers:')
for i in range(20):
    a = int(input('number '+str(i)+" "))
    x.append(a)
    x[i]**= 2
print("List to the power of 2 : "+str(x))
x_min = x[0]
x_max = x[0]
for m in range(1,20):
    if x[m]>x_max:
        x_max=x[m]
    else:
        x_min=x[m]
print("The larger smallest number "+str(x_max), "     The smallest number "+str(x_min))
