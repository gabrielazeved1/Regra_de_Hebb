# 🧠 Regra de Aprendizado Hebbiano e Suas Aplicações em Machine Learning

A **Regra de Aprendizado Hebbiano** é um princípio fundamental no campo do **Machine Learning** e redes neurais. Baseada no trabalho do neurocientista Donald Hebb, a regra de aprendizado estabelece que **as conexões entre os neurônios são ajustadas com base na sua atividade conjunta**, ou seja, **"neurônios que disparam juntos, se conectam".** Esse conceito foi inicialmente desenvolvido para entender como os neurônios do cérebro podem se ajustar e aprender com o tempo, mas se mostrou extremamente útil para a construção de modelos de aprendizado de máquina.

Neste repositório, implementamos a **Regra de Hebb** para treinar um modelo simples de rede neural que aprende a partir das entradas e saídas de funções lógicas. Utilizando duas variáveis de entrada e um conjunto de funções lógicas, o modelo ajusta os pesos da rede neural de acordo com os princípios da Regra de Hebb.

## 📚 O que é a Regra de Hebb?

A Regra de Hebb é uma regra de aprendizado **não supervisionado** em redes neurais, ou seja, o modelo ajusta os pesos das conexões entre os neurônios com base nas entradas e saídas observadas, mas sem precisar de rótulos explícitos.

A fórmula básica da Regra de Hebb é:

$$
w(t+1) = w(t) + \eta \cdot y[i] \cdot x[i]
$$

Onde:
- \( w(t) \) é o peso atual,
- \( w(t+1) \) é o peso ajustado,
- \( \eta \) é a taxa de aprendizado (normalmente um valor pequeno),
- \( y[i] \) é a saída desejada para a entrada \( i \),
- \( x[i] \) é o valor da entrada \( i \).
A cada iteração, os pesos são ajustados de acordo com a entrada e a saída, permitindo que a rede aprenda e ajuste as conexões de forma incremental.

## ⚙️ A Importância da Regra de Hebb no Machine Learning

A Regra de Hebb é uma das primeiras tentativas de simular o comportamento de aprendizado do cérebro humano. Embora simples, ela possui uma grande relevância para o desenvolvimento de redes neurais e modelos de **aprendizado não supervisionado**. Ela está na base de muitos algoritmos de redes neurais e ajuda a entender o comportamento de como os neurônios ajustam suas conexões.

### Vantagens da Regra de Hebb:
- **Aprendizado Local:** A regra é baseada na interação local entre os neurônios, o que permite que os sistemas de aprendizado operem sem a necessidade de supervisão externa.
- **Simplicidade:** Sua implementação é simples e eficiente, sendo adequada para a construção de redes neurais iniciais e para o aprendizado de funções simples.
- **Fundamentação Biológica:** Como mencionado, a Regra de Hebb se inspira diretamente em como os neurônios do cérebro humano aprendem e se conectam.

## 🔢 As Funções Lógicas e Suas Limitações

Ao aplicar a Regra de Hebb a funções lógicas, é importante entender o conceito de **funções lógicas com duas variáveis de entrada**. Existem 16 possíveis combinações para as entradas binárias (0 e 1) para duas variáveis. No entanto, **nem todas essas 16 funções podem ser representadas com a Regra de Hebb**.

### Por que apenas 14 das 16 funções são representáveis?

A razão para isso está nas **propriedades matemáticas** da Regra de Hebb e como ela ajusta os pesos. A Regra de Hebb é baseada na ideia de **fortalecer as conexões entre os neurônios que são ativados ao mesmo tempo**. No entanto, para que a rede aprenda corretamente todas as 16 funções lógicas possíveis, é necessário que as entradas e saídas apresentem uma relação coerente para que a rede possa ajustar seus pesos de forma eficaz. 

**Das 16 funções lógicas possíveis com duas variáveis de entrada**, algumas não podem ser representadas pela Regra de Hebb devido a **incompatibilidades matemáticas**. As funções que não podem ser representadas são aquelas que não seguem uma relação linear entre as entradas e as saídas, como:

- **Função XOR (exclusive OR)**: Esta função não pode ser representada de forma simples porque a relação entre as entradas e a saída não é linear.
- **Função XNOR**: Semelhante à XOR, não segue a mesma lógica de aprendizado, tornando-a impossível de aprender com a Regra de Hebb.

Por isso, apenas **14 das 16 funções lógicas** podem ser representadas de forma eficaz. Essas funções são aquelas que possuem uma relação linear ou que podem ser aprendidas sem a necessidade de interação mais complexa entre as entradas.

## 🔍 Funções Lógicas Implementadas

No código, o modelo treina para aprender as seguintes **14 funções lógicas** com duas variáveis de entrada:

1. **F1 (Constante 0):** Saída constante 0.
2. **F2 (Constante 1):** Saída constante 1.
3. **F3 (x1):** Saída igual ao valor de x1.
4. **F4 (x2):** Saída igual ao valor de x2.
5. **F5 (¬x1):** Negação de x1.
6. **F6 (¬x2):** Negação de x2.
7. **F7 (x1 ∨ x2):** Operação lógica OR.
8. **F8 (x1 ∧ x2):** Operação lógica AND.
9. **F9 (x1 ∧ ¬x2):** Operação AND com a negação de x2.
10. **F10 (¬x1 ∧ x2):** Operação AND com a negação de x1.
11. **F11 (x1 ⊕ x2):** Operação XOR (ou exclusivo).
12. **F12 (x1 ⊙ x2):** Operação NAND.
13. **F13 (¬(x1 ⊙ x2)):** Negação de x1 NAND x2.
14. **F14 (¬(x1 ⊕ x2)):** Negação de x1 XOR x2.

Essas funções são usadas para demonstrar como a Regra de Hebb ajusta os pesos de forma incremental durante o treinamento, permitindo que a rede aprenda a partir de exemplos e generalize a partir deles.

## 📝 Conclusão

A Regra de Hebb é uma base importante no desenvolvimento de redes neurais, especialmente para aprendizado não supervisionado. A aplicação dessa regra em funções lógicas simples é uma excelente maneira de entender como os neurônios ajustam suas conexões e como a aprendizagem pode ocorrer de maneira simples e eficiente. A limitação de representabilidade de algumas funções lógicas é um aspecto interessante que nos ajuda a compreender melhor as condições necessárias para o aprendizado com a Regra de Hebb.

Ao aprender essas funções lógicas, o modelo pode ser estendido para problemas mais complexos de aprendizado de máquina e redes neurais, pavimentando o caminho para sistemas mais avançados.