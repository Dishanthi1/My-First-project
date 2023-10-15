def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False

    for current in range(2, int(limit**0.5) + 1):
        if sieve[current]:
            for multiple in range(current * current, limit + 1, current):
                sieve[multiple] = False

    primes = [num for num, is_prime in enumerate(sieve) if is_prime]
    return primes

# Example usage
limit = 100
prime_numbers = sieve_of_eratosthenes(limit)
print("Prime numbers up to", limit, "are:", prime_numbers)
