# GCD function
gcd = lambda a, b: a if not b else gcd(b, a%b)

# LCM function
lcm = lambda a, b: abs(a*b) // gcd(a, b)

a = 25
b = 45

# Compute gcd
gcd_ab = gcd(a, b)
print("GCD of", a, "and", b, "is", gcd_ab)

# Compute lcm
lcm_ab = lcm(a, b)
print("LCM of", a, "and", b, "is", lcm_ab)

