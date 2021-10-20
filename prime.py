def isPrime(n) :
if (n &lt;= 1) :
return False
if (n &lt;= 3) :
return True
if (n % 2 == 0 or n % 3 == 0) :
return False
i = 5
while(i * i &lt;= n) :
if (n % i == 0 or n % (i + 2) == 0) :
return False
i = i + 6
return True
if (isPrime(11)) :
print(" true")
else :
print(" false")
if(isPrime(15)) :
print(" true")
else :
print(" false")
