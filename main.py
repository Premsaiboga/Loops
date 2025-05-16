# ===== PRACTICE LOOPS IN PYTHON =====

print("1. For loop: Print numbers 1 to 5")
for i in range(1, 6):
    print(i, end=" ")
print("\n-------------------\n")

print("2. While loop: Print numbers 5 to 1")
count = 5
while count > 0:
    print(count, end=" ")
    count -= 1
print("\n-------------------\n")

print("3. For loop with list: Print each fruit")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
print("-------------------\n")

print("4. Nested loops: Print a 3x3 star pattern")
for row in range(3):
    for col in range(3):
        print("*", end=" ")
    print()
print("-------------------\n")

print("5. While loop with break: Stop when number is 4")
num = 1
while True:
    print(num)
    if num == 4:
        break
    num += 1
print("-------------------\n")

print("6. For loop with continue: Print odd numbers from 1 to 7")
for num in range(1, 8):
    if num % 2 == 0:
        continue
    print(num, end=" ")
print("\n=== END OF LOOP PRACTICE ===")
