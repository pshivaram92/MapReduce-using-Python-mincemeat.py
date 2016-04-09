# MapReduce-using-Python-mincemeat.py
Efficient calculation palindromic primes till 10 million integer, password hacking using brute force (md5 hashing)

This repository consists of two files.

1. primes.py - finds the palindrome primes between 2 and 10,000,000

2. passCrack.py - finds the password hased to a md5 hash (first five characters)

How to run:
1. primes.py (Use four workers) In the command line enter:  Master : primes.py 
                                                            Workers: mincemeat.py -p changeme

2. passCrack.py (##### - five character md5.hexdigest() hash) In the command line, enter: Master : passCrack.py ##### 
                                                                                          Workers: mincemeat.py -p changeme


Average times for execution:

1. primes.py = 18 s with four workers
2. passCrack.py = 4.2 s with one worker
