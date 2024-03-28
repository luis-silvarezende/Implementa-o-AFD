class AFD:
    def __init__(self, estados, alfabeto, transicoes, estado_inicial, estados_final):
        self.estados = estados
        self.alfabeto = alfabeto
        self.transicoes = transicoes
        self.estado_inicial = estado_inicial
        self.estados_final = estados_final

    def processar_palavra(self, palavra):

        estado_atual = self.estado_inicial

        for simbolo in palavra:
            if simbolo not in self.alfabeto: # Verifica se pertece ao alfabeto
                return "palavra rejeitada - símbolo inválido"
            estado_atual = self.transicoes.get((estado_atual, simbolo)) # Recebe uma tupla com o estado atual e o simbolo do alfabeto e vai para o proximo estado
            if estado_atual is None: # Verifica se existe um estado valido após ler o estado atual e o simbolo, se não rejeita
                return "palavra rejeitada"
            
        if estado_atual in self.estados_final: # Se estado atual estiver no conjunto de estados finais a w é aceita
            return "palavra aceita"
        else:
            return "palavra rejeitada"

# Descricao do AFD
estados = {'q0', 'q1', 'q2', 'q3'}
alfabeto = {'a', 'b'}
transicoes = {('q0', 'a'): 'q1', ('q1', 'a'): 'q1', ('q1', 'b'): 'q2', ('q2', 'b'): 'q2', ('q2', 'a'): 'q3', ('q3', 'a'): 'q3', ('q3', 'b'): 'q2'}
estado_inicial = 'q0'
estados_final = {'q3'}

afd = AFD(estados, alfabeto, transicoes, estado_inicial, estados_final)

print(afd.processar_palavra('aba'))  # Saída: palavra aceita
print(afd.processar_palavra('aaaaa')) # Saída: palavra rejeitada
