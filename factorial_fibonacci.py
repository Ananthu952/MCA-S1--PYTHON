num=2
fact=1
for i in range(1, num+1):
    fact*=i
print(f"factorial of {num} is {fact}")

num=3
a,b=0,1
print("Fibonacci Series:")
for _ in range(num):
    print(a,end=" ")
    a,b=b,a+b

list1=[2,4,6,8,10]
sum = sum(list1)
print("\nSum=",sum)
