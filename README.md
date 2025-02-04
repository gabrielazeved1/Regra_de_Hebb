# 🧠 Regra de Aprendizado Hebbiano em Funções Lógicas

Este repositório é dedicado à implementação da **Regra de Aprendizado Hebbiano**, um algoritmo clássico de aprendizado de máquinas, aplicado para resolver problemas lógicos com duas variáveis de entrada. O código foi criado para aprender e ajustar pesos em uma rede neural simples com base em diversas operações lógicas.

Ao longo do projeto, experimentei funções lógicas como **AND**, **OR**, **XOR**, **NAND**, e outras, com o objetivo de treinar um modelo que aprenda a partir dos dados usando a regra de Hebb. Além disso, a configuração foi feita de forma limpa e organizada, utilizando o **Poetry** para gerenciar as dependências de forma prática e eficiente.

## 🚀 Como Executar o Código

Para rodar o código e treinar as funções lógicas, siga as etapas abaixo:

### 1. Clone o repositório:

```bash
git clone https://seu-repositorio.git
cd seu-diretorio
2. Instale as dependências com Poetry:
Se você ainda não tem o Poetry instalado, siga as instruções no site oficial.

Após a instalação do Poetry, execute o comando abaixo para instalar todas as dependências do projeto:

bash
Copiar
poetry install
3. Execute o código:
Depois de instalar as dependências, execute o código com o seguinte comando:

bash
Copiar
poetry run python main.py
Isso iniciará o treinamento para todas as funções lógicas e você verá os pesos finais ajustados pela regra de Hebb.

🤖 O que o Código Faz?
Este código aplica a Regra de Hebb para ajustar os pesos de uma rede neural de forma simples, com base nas entradas e saídas de funções lógicas. O modelo aprende as relações entre as variáveis e ajusta os pesos durante várias iterações, até convergir para um resultado ideal.

Como a Regra de Hebb Funciona
A fórmula básica do aprendizado de Hebb é:

𝑤
(
𝑡
+
1
)
=
𝑤
(
𝑡
)
+
𝜂
⋅
𝑦
[
𝑖
]
⋅
𝑥
[
𝑖
]
w(t+1)=w(t)+η⋅y[i]⋅x[i]
Onde:

𝑤
(
𝑡
)
w(t) são os pesos anteriores.
𝑤
(
𝑡
+
1
)
w(t+1) são os novos pesos.
𝜂
η é a taxa de aprendizado (aqui definida como 1).
𝑦
[
𝑖
]
y[i] é a saída desejada para a entrada 
𝑖
i.
𝑥
[
𝑖
]
x[i] é a entrada 
𝑖
i.
O código utiliza essas fórmulas para aprender as 14 funções lógicas definidas abaixo.

🔥 Funções Lógicas Implementadas
O código treina a rede para aprender as seguintes funções lógicas com duas variáveis de entrada. Cada função é representada em forma bipolar (valores de -1 e 1):

F1 (Constante 0): Saída constante 0.
F2 (Constante 1): Saída constante 1.
F3 (x1): Saída igual ao valor de 
𝑥
1
x 
1
​
 .
F4 (x2): Saída igual ao valor de 
𝑥
2
x 
2
​
 .
F5 (não x1): Negação de 
𝑥
1
x 
1
​
 .
F6 (não x2): Negação de 
𝑥
2
x 
2
​
 .
F7 (x1 ou x2): Operação lógica OR (disjunção).
F8 (x1 e x2): Operação lógica AND (conjunção).
F9 (x1 e não x2): Operação AND com a negação de 
𝑥
2
x 
2
​
 .
F10 (não x1 e x2): Operação AND com a negação de 
𝑥
1
x 
1
​
 .
F11 (x1 ou exclusivo x2): Operação XOR (ou exclusivo).
F12 (x1 nand x2): Operação NAND (não AND).
F13 (não (x1 nand x2)): Negação de 
𝑥
1
x 
1
​
  NAND 
𝑥
2
x 
2
​
 .
F14 (não (x1 ou exclusivo x2)): Negação de 
𝑥
1
x 
1
​
  XOR 
𝑥
2
x 
2
​
 .
💡 Exemplo de Saída
Quando você rodar o código, ele irá realizar o treinamento para cada função lógica e imprimir os pesos finais após o processo de aprendizado. Aqui está um exemplo de como a saída será exibida no terminal:

java
Copiar
Treinamento para F1 (Constante 0):
Pesos finais: [4. 4.]

Treinamento para F2 (Constante 1):
Pesos finais: [0. 0.]

Treinamento para F3 (x1):
Pesos finais: [2. 2.]

Treinamento para F4 (x2):
Pesos finais: [4. 0.]

Treinamento para F5 (não x1):
Pesos finais: [-2. -2.]

...
🔧 Tecnologias Usadas
Python 3.10+: Linguagem de programação utilizada.
NumPy: Biblioteca para cálculos numéricos e manipulação de arrays.
Poetry: Gerenciador de dependências e ambientes virtuais para Python.
📝 Licença
Este projeto está licenciado sob a MIT License.

