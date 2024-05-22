

prompt='Hello boss whats up '
prompt+='\nHow are you?'
print(prompt)

""" age=int(input(f"What is you age boss ? : "))
age=age+10
print(age) """


num=int(input(f"Enter a number. We will tell if even or odd : "))
if num%2 == 0:
    print(f"{num} is EVEN")
else:
    print(f"{num} is ODD")


num=int(input(f"Enter a number. We will tell if mul of 10 or NOT : "))
if num%10 == 0:
    print(f"{num} is mul of 10")
else:
    print(f"{num} is NOT a mul of 10")