"""
Beecrowd 1002 - Área do Círculo

A fórmula para calcular a área de uma circunferência é: area = π . raio².
Considerando para este problema que π = 3.14159:

- Efetue o cálculo da área, elevando o valor de raio ao quadrado e
  multiplicando por π.

Entrada: O arquivo de entrada contém um valor de ponto flutuante (dupla precisão),
no caso, a variável raio.

Saída: Apresentar a mensagem "A=" seguido pelo valor da variável area, conforme
exemplo abaixo, com 4 casas após o ponto decimal. Utilize variáveis de dupla precisão
(double).
"""

# Link do problema: https://judge.beecrowd.com/pt/problems/view/1002

# Escreva sua solução abaixo

# Define o valor de pi conforme o enunciado
n = 3.14159

# Lê o valor do raio (convertendo para float para suportar decimais)
raio = float(input())

# Calcula a área: n multiplicado pelo raio ao quadrado
area = n * (raio ** 2)

# Imprime o resultado formatado com 4 casas decimais
# O :.4f garante o arredondamento e a exibição correta
print(f"A={area:.4f}")
