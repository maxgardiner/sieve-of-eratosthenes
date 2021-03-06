import sys
import numpy as np

#Print User Usage info
if len(sys.argv) < 2:
    print "Usage: python sieve.py <upper limit>"
    sys.exit(1)

#set upper bounds and create array
upper = int(sys.argv[1])
sMap = np.zeros(upper + 1, dtype=int)
prime = 2 #let p equal 2, the smallest prime number.

for i in xrange(len(sMap)):
    sMap[i] = i
    
#Enumerate the multiples of p
while(prime < upper):
    for i in xrange(prime, upper + 1):
        if (i % prime == 0) and (i != prime):
            sMap[i] = 0
            
    i = prime + 1

    #Find the first number greater than p in the list that is not marked
    try:
        prime = sMap[i]
        i += 1
        while (prime == 0) and (prime <= upper):
            prime = sMap[i]
            i += 1

    #If there was no such number then stop
    except:
        break
        
    if prime <= upper and i < upper:
        print prime,
        print "",