num = 12  # change this value

print("Factors of", num, "are:")

for i in range(1, num + 1):
    if num % i == 0:
        print(i)
