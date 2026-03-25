a = int(input("Enter start: "))
b = int(input("Enter end: "))

even_sum = 0
odd_sum = 0
even_count = 0
odd_count = 0

for n in range(a, b+1):
    f = 0
    for i in range(2, n):
        if n % i == 0:
            f = 1
            break

    if n <= 1 or f == 1:   # non-prime
        print(n, end=" ")
        if n % 2 == 0:
            even_count += 1
            even_sum += n
        else:
            odd_count += 1
            odd_sum += n

print("\nEven non-prime count:", even_count)
print("Odd non-prime count:", odd_count)
print("Even non-prime sum:", even_sum)
print("Odd non-prime sum:", odd_sum)