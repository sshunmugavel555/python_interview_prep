
while True:
    n=input("Enter numerator / Q to quit ")
    if n=='Q':
        break
    d=input("Enter the denominator / Q to quit ")
    if d=='Q':
        break
    try:
        result=int(n) / int(d)
    except ZeroDivisionError:
        print(f"Division by zero")
    else:
        print(f"Result of the division {n} by {d} is {result} ")