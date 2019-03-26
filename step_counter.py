import matplotlib.pyplot as plt

a = []
b = []
with open("/root/Documents/answers.txt", "r") as m:
    for index,line in enumerate(m):
        a.append(index)
        b.append(line)


b = list(map(lambda s: s.strip(), b))
map(float, b)
b = [float(i) for i in b]
b = [i*100000 for i in b]
b = [int(float(i)) for i in b]
plt.plot(a,b, 'ro')
plt.ylabel('some numbers')
plt.show()
