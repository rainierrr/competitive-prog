import sys
from typing import List


def list_primes(limit: int) -> List[int]:
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0] = False
    is_prime[1] = False

    for p in range(0, limit + 1):
        if not is_prime[p]:
            continue
        primes.append(p)  # 素数発見
        for i in range(p * p, limit + 1, p):
            is_prime[i] = False

    return primes


def main(n: int) -> int:
    limit = 1000
    while True:
        primes = list_primes(limit)
        if len(primes) > n:
            return primes[n - 1]
        limit *= 2


if __name__ == '__main__':
    ans = main(int(sys.argv[1]))
    print(ans)
