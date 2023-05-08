import math
import heapq


hy = -(3/8 * math.log2(3/8) + 5/8 * math.log2(5/8))

print("hy", hy)

p11 = 3/8
p10 = 5/8

p111 = 2/3
p011 = 1/3
p110 = 3/5
p010 = 2/5

hy11 = - (p111 * math.log2(p111) + p011 * math.log2(p011))
hy10 = - (p110 * math.log2(p110) + p010 * math.log2(p010))
print("hy11: ", hy11)
print("hy10: ", hy10)
hy1 = p11 * hy11 + p10 * hy10
print("hy1", hy1)

ig1 = hy - hy1
print("ig1", ig1)


p41 = 4/8
p40 = 4/8

p141 = 3/4
p041 = 1/4
p140 = 2/4
p040 = 2/4

hy41 = - (p141 * math.log2(p141) + p041 * math.log2(p041))
hy40 = - (p140 * math.log2(p140) + p040 * math.log2(p040))
print("hy41: ", hy41)
print("hy40: ", hy40)
hy4 = p41 * hy41 + p40 * hy40

print("hy4", hy4)

ig4 = hy - hy4
print("ig4", ig4)

n = 1
cumulative_sum = 0

while True:
    term = ((2 / 3) ** n) * 5*n
    cumulative_sum += term

    if term < 1e-12:
        break

    n += 1

print("cumulative_sum: ", cumulative_sum)



print((5/7290) * (30/343))


# heapq.



