start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

print("Prime numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
    if num > 1:
        i = 2
        is_prime = True

        while i < num:
            if num % i == 0:
                is_prime = False
                break
            i += 1

        if is_prime:
            print(num)