



x = input(f"What is the power level of the first number? ")
y = input(f"What is the power level of the seocnd number? ")
if x > y:
    print(f"{x} wins!")
elif y > x:
    print(f"{y} wins!")
elif x == y:
    print(f"it's a tie!")