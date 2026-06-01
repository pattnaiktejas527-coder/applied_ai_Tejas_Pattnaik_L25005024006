#Add two no.
a= int(input("Enter first no."))
b= int(input("Enter second no."))
add= a+b
print(add)

#sum
sum=0
for i in range(1,11):
    sum=sum+1
print(sum)

#Eligible voter
p= int(input("Enter your age"))
if(p>=18):
    print("Your eligible")
else:
    print("YOur not eligible")