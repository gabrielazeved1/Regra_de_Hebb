import numpy as np

def aprendizado_hebbiano(X, y, iteracoes=1):
#inciar com peso zero
    pesos = np.zeros(X.shape[1])
    taxa_aprendizado = 1
    
# funcao dos pesos
    for iteracao in range(iteracoes):
        for i in range(len(X)):
            pesos = pesos + taxa_aprendizado * y[i] * X[i]
    
    return pesos

# dicionario com entradas
funcoes = {
    "F1 (Constante 0)": np.array([[-1, -1], [-1, 1], [1, -1], [1, 1]]),  
    "F2 (Constante 1)": np.array([1, 1, 1, 1]),  
    "F3 (x1)": np.array([-1, 1, 1, 1]),  
    "F4 (x2)": np.array([-1, -1, 1, 1]),  
    "F5 (not x1)": np.array([1, -1, -1, -1]),  
    "F6 (not x2)": np.array([1, -1, 1, -1]),  
    "F7 (x1 ou x2)": np.array([-1, 1, 1, 1]),  
    "F8 (x1 e x2)": np.array([-1, -1, -1, 1]),  
    "F9 (x1 e not x2)": np.array([-1, -1, 1, -1]),  
    "F10 (not x1 e x2)": np.array([-1, 1, -1, -1]),  
    "F11 (x1 ou exclusivo x2)": np.array([1, -1, -1, 1]),  
    "F12 (x1 nand x2)": np.array([1, 1, 1, -1]),  
    "F13 (not (x1 nand x2))": np.array([1, 1, 1, 1]),  
    "F14 (not (x1 ou exclusivo x2))": np.array([-1, 1, 1, -1]),  
}


for nome, y in funcoes.items():
#  4entradas possiveis
    X = np.array([[-1, -1], [-1, 1], [1, -1], [1, 1]])
    
    print(f"Treinamento para {nome}:")
    pesos_finais = aprendizado_hebbiano(X, y, iteracoes=1)
    print(f"Pesos finais: {pesos_finais}\n")
