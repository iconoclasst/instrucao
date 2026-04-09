# criar uma pilha funcional

class pilha:
    def __init__(self, n):
        self.n = n
        self.topo = 0
        self.items = []
    
    def vazio(self):
        if self.topo == 0:
            return True
        return False

    def push(self, x):
        if self.topo < self.n:
            self.items.append(x)
            self.topo+=1
    
    def pop(self):
        if not self.vazio():
            self.items.pop()
            self.topo-=1

    def show(self):
        print(self.items)

    def show_topo(self):
        print(f"Topo de indice {self.topo} e valor {self.items[self.topo - 1]}")

p = pilha(5)
p.show()
p.push(3)
p.push(1)
p.show()
p.show_topo()
p.pop()
p.show()
p.show_topo()