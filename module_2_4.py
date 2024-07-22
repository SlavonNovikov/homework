numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for num in numbers:  # num - число в списке numbers
    if num > 1:
        is_prime = True
        for divider in range(2, num):  # divider -делитель
            if num % divider == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        else:
            not_primes.append(num)

print(f'Primes:', primes)
print(f'Not Primes:', not_primes)
