""" 
Program intended to check for primality.

Each test incorporates a more sophisticated stategy to check for primes.
test_D is a Fermat test.
Our goal is efficiency with large numbers.

Also included is a Sieve of Eratosthenes to generate a list of prime numbers, 
and a large_prime generator to generate primes that you can put through the
tests.

Created by Dexter.
Python 3.6
"""

import math
import secrets

def user_errors(single_test_num, range_max):
	""" Function for raising exceptions.

	"""
	if single_test_num != 0 and range_max != 0 or\
	   single_test_num == 0 and range_max == 0:
		raise ValueError("range_max and single_test_num cannot both be zero or"
						 " nonzero")

	if single_test_num == 1:
		raise ValueError("One is neither a prime nor composite number.")

def call_test(test_N, range_max=0, single_test_num=0, num_executions=1, k=1):
	""" Simple calling function that makes it easier to call the primality
	testing functions and displays some statistics.

	Input: test_N - the function name of the test you would like to perform
		   range_max - tests prime test_N with n's from [2, n)
		   single_test_num - used if you only want to test a single number for
		   					 primality, set to 0 if you're testing a range.
		   num_executions - the number of times to execute the whole function
		   k - number of random numbers to test (see test_D)
	"""
	user_errors(single_test_num, range_max)

	for i in range(num_executions):
		max_steps = 0
		total_steps = 0
		num_primes = 0 # Will only be 100% accurate with test_A,B, and C

		if single_test_num == 0:
			for i in range(2, range_max):
				if test_N != test_D:
					prime, steps = test_N(i)

				elif test_N == test_D:
					prime, steps, k = test_N(i, k)

				total_steps += steps

				if steps > max_steps:
					max_steps = steps

				if prime == True:
					num_primes += 1

			### Statistics for range testing. ###
			if test_N == test_D:
				print("Probability of mistakenly outputting a prime: ",
		 			 (1 / 2 ** k) * 100, "%", sep="")
			print("The number of primes counted below", range_max,
				  "is:", num_primes)
			print("The maximum amount of steps for", test_N.__name__,
				  "was:", max_steps)
			print("The total amount of steps for", test_N.__name__,
				  "is:", total_steps)

		elif single_test_num != 0:
			if test_N != test_D:
				prime, steps = test_N(single_test_num)

			elif test_N == test_D:
				prime, steps, k = test_N(single_test_num, k)

			### Stastistics for single test. ###
			if test_N == test_D:
				print("Probability of mistakenly outputting a prime: ",
		 			 (1 / 2 ** k) * 100, "%", sep="")
			if prime == True:
				print("The number", single_test_num, "is prime. Steps:", steps)
			if prime == False:
				print("The number", single_test_num, "is composite. "
					  "Steps:", steps)

def sieve(n):
	""" Sieve of Eratosthenes algorithm that generates a list of prime numbers.
	This is not an optimized algorithm.

	Input: n - the number that is the upper bound on the possible list values
	"""

	# Ignore input that is less than 2
	if n < 2:
		return None

	# A list to store our primes
	primes = []

	# List to store all integers. The list is full of Boolean values.
	# A value of 1 indicates the integer with the value of the observed index is
	# marked... 0 means the integer has not been checked.
	# The entire list is initialized with 0's, and is of length n.
	# The numbers zero and one are marked by default.
	integers = [1, 1]
	for i in range(n - 2):
		integers.append(0)

	# Check range [2, sqrt(n)]
	for i in range(2, math.floor(math.sqrt(n)) + 1):

		# Values that have not been searched are assumed prime, then marked.
		if integers[i] == 0:
			primes.append(i)
			integers[i] = 1
			
			# Once we find a prime number, we mark all of its multiples as
			# composite starting at i squared.
			for j in range(i * i, n, i):
				integers[j] = 1

	# Temporary value to search less of the list in the next step
	# (At the end of the for loop, all numbers will have been marked up to
	# i, so there's no reason to iterate through the loop later at index 0.)
	start = i

	# Any remaining zeroes in the integers list must be prime
	for i in range(start, len(integers)):
		if integers[i] == 0:
			primes.append(i)

	return primes

def fast_modulo(n, power, modulus):
	""" The fast modulo function performs modulo exponentiation much faster than
	the normal mod operation. This is necessary for large numbers.

	Given A**B mod C
	Inputs: n = A, the base number for modulation
			power = B, the exponent
			modulus = C, our modulus 
	"""
	remainder = 1

	while power > 0:
		if power % 2 == 1:
			remainder = (n * remainder) % modulus
			power -= 1
		power /= 2
		n = (n * n) % modulus

	return remainder

def large_prime(bit_size=50, attempts=10000):
	""" This function generates a very large random number, and uses test_D to 
	check for primality. It is not optimized and there exist much better
	algorithms for very large bit sizes.

	Input: bit_size - the number of bits you would like the large prime to have
		   attempts - the number of random numbers to check for primality (may
		   			  need to be a higher number to find a prime)
	"""
	large_rand = 0

	for i in range(attempts):
		while large_rand % 2 == 0:
			large_rand = secrets.randbits(bit_size)

		prime, steps, k = test_D(large_rand, k=400)

		if prime == True:
			print("Found prime:", large_rand)
			print("Probability of error = ", (1 / 2 ** k) * 100, "%", sep="")
			return large_rand

	print("Error: Couldn't find a prime in", attempts, "attempts. "
		  "You may want to try a higher number.")

def test_A(n):
	""" This is the most basic test, and can also be used as a prime counter.
	It checks all numbers up to n - 1 and sees if they are a factor of n.

	Worst case: n - 2 steps (happens every time)
	"""
	steps = 0
	prime = True

	# Check range [2, n)
	for i in range(2, n):
		steps += 1
		if n % i == 0:
			prime = False

	return prime, steps

def test_B(n):
	""" This basic test is smart enough to check only up to the square root of n
	and it also exits the loop as soon as a number is found to be composite.
	
	Worst case: sqrt(n) steps
	"""
	steps = 0

	# Check range [2, sqrt(n)]
	for i in range(2, math.floor(math.sqrt(n)) + 1):
		steps += 1
		if n % i == 0:
			return False, steps

	return True, steps

def test_C(n):
	""" This test is improved from test_A because if a number is not even, we
	only test odd integers from then on.

	Worst case: sqrt(n)/2 steps
	"""
	steps = 0

	if n == 2:
		steps += 1
		return True, steps

	# Checking if number is divisble by 2, return if it is
	if n % 2 == 0:
		steps += 1
		return False, steps

	# Check range [3, sqrt(n)], and skip even numbers
	for i in range(3, math.floor(math.sqrt(n)) + 1, 2):
		steps += 1
		if n % i == 0:
			return False, steps

	return True, steps

def test_D(n, k=10):
	""" A far more efficient algorithm is the Fermat primality test.

	It works by using random number generation in order to test for primality
	to a certain degree of confidence. The more iterations you do, the more
	confident you can be that the number is correctly labeled as prime.
	The weakness of this is that it can fail due to the existence of Carmichael
	numbers. 
	The error of this function is 1 / 2 ** k.

	Worst case: k * 3 steps, a composite number is incorrectly labeled as prime

	Inputs: n - the number to do prime testing on
			k - the amount of random numbers to test
	"""
	steps = 0
	random_num = 0

	if n == 2:
		steps += 1
		return True, steps, k

	for i in range(k):
		while random_num < 2:
			random_num = secrets.randbelow(n)

		steps += 3 # For each of the below operations

		# if the gcd is > 1, the number is composite
		if math.gcd(random_num, n) != 1:
			return False, steps, k

		# This is the Fermat test. If the value != 1 it must be composite.
		# Fermat test: A^(P-1) = 1 mod P
		if (fast_modulo(random_num, n - 1, n) != 1):
			return False, steps, k

	return True, steps, k


# Uncomment to call any test
#call_test(test_D, range_max=0, single_test_num=13, num_executions=1, k=50)

# Uncomment for list a primes
#print(sieve(65000))

# Uncomment for a large prime number
#large_prime = large_prime(50, 100000)



