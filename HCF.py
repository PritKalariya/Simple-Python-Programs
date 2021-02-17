# Find the HCF of 2 Numbers

def hcf(a, b):
    if(b == 0):
        return a
    else:
        return hcf(b, a % b)

print(hcf(60, 48))