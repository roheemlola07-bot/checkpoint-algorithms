def dot_product(v1, v2, n, ps):
    ps[0] = 0                          
    for i in range(n):                  
    ps[0] = ps[0] + v1[i] * v2[i]   

print("--- Procedure version ---")
pairs = int(input("How many pairs of vectors? "))
size = int(input("How many components in each vector? "))

for p in range(pairs):
    v1 = []
    v2 = []
    print("Pair", p + 1)

    for i in range(size):
        v1.append(int(input("v1 component " + str(i + 1) + ": ")))
        v2.append(int(input("v2 component " + str(i + 1) + ": ")))

    ps = [0]                            
    dot_product(v1, v2, size, ps)       

    if ps[0] == 0:
        print("Orthogonal")
    else:
        print("Not orthogonal, dot product =", ps[0])

def dot_product_fn(v1, v2, n):
    total = 0
    for i in range(n):
        total = total + v1[i] * v2[i]
    return total


print("--- Function version ---")
pairs = int(input("How many pairs of vectors? "))
size = int(input("How many components in each vector? "))

for p in range(pairs):
    v1 = []
    v2 = []
    print("Pair", p + 1)

    for i in range(size):
        v1.append(int(input("v1 component " + str(i + 1) + ": ")))
        v2.append(int(input("v2 component " + str(i + 1) + ": ")))

    ps = dot_product_fn(v1, v2, size)   

    if ps == 0:
        print("Orthogonal")
    else:
        print("Not orthogonal, dot product =", ps)