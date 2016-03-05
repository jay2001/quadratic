# Test Code

print("Enter values from the equation in the format y = ax2 + bx + c.")

a = float(input("Input the value of a: "))
b = float(input("Input the value of b: "))
c = float(input("Input the value of c: "))

root1 = (-b + (b**2 - 4 * a * c)) / 2 * a
root2 = (-b - (b**2 - 4 * a * c)) / 2 * a

print(root1)
print(root2)
