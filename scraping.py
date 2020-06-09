class Culc:
    value = 0

    def square(self):
        s = self.value * self.value
        return s


culcs = [Culc(), Culc(), Culc(), Culc()]

culcs[0].value = 3
culcs[1].value = 6
culcs[2].value = 8
culcs[3].value = 9

print(culcs[0].square())
print(culcs[1].square())
print(culcs[2].square())

for i in culcs:
    print(i.square())
