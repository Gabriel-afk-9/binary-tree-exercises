class Arvore:
    def __init__(self,valor,esquerda,direita):
        self.valor = valor
        self.esquerda = esquerda
        self.direita = direita
        
    def percorrer(self,no):
        if no == None:
            return 0
        else:
            return 1 + self.percorrer(no.esquerda) + self.percorrer(no.direita)

    def maior(self,no):
        if no == None:
            return float('-inf')
        valor_atual = no.valor
        valor_esquerda = self.maior(no.esquerda)
        valor_direita = self.maior(no.direita)
        return max(valor_atual,valor_esquerda,valor_direita)
    
    def menor(self,no):
        if no == None:
            return float('inf')
        valor_atual = no.valor
        valor_esquerda = self.menor(no.esquerda)
        valor_direita = self.menor(no.direita)
        return min(valor_atual,valor_esquerda,valor_direita)

    def soma(self,no):
        if no == None:
            return 0
        valor_a = no.valor
        valor_e = self.soma(no.esquerda)
        valor_d = self.soma(no.direita)
        return valor_a + valor_e + valor_d
    
    def altura (self,no):
        if no == None:
            return 0
        altura_esquerda = self.altura(no.esquerda)
        altura_direita =self.altura(no.direita)
        return 1 + max(altura_esquerda,altura_direita)

if __name__ == '__main__':

    no3 = Arvore(3,None,None)
    no7 = Arvore(7,None,None)
    no5 = Arvore(5,no3,no7)
    no20 = Arvore(20,None,None)
    raiz = Arvore(10,no5,no20)
    print('Numero de elementos:',raiz.percorrer(raiz))
    print('Maior elemento:',raiz.maior(raiz))
    print('Menor elemento:',raiz.menor(raiz))
    print('A soma da árvore é:',raiz.soma(raiz))
    print('A altura da árvore é:',raiz.altura(raiz))