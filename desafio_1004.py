"""
Beecrowd 1004 - Produto Simples

Leia dois valores inteiros. A seguir, calcule o produto entre estes dois valores
e atribua esta operação à variável PROD. A seguir mostre a variável PROD com
mensagem correspondente.

Entrada: O arquivo de entrada contém 2 valores inteiros.

Saída: Imprima a mensagem "PROD" conforme exemplo abaixo, com um espaço em branco
antes e depois da igualdade. Não esqueça de imprimir o fim de linha após o produto,
caso contrário seu programa apresentará a mensagem: "Presentation Error".
"""

# Link do problema: https://judge.beecrowd.com/pt/problems/view/1004

# Escreva sua solução abaixo

# Lê os dois valores inteiros de entrada
valor1 = int(input())
valor2 = int(input())

# Realiza a multiplicação (produto)
PROD = valor1 * valor2

# Exibe o resultado com a formatação exigida pelo Beecrowd
# Importante: "PROD" em maiúsculas e espaços ao redor do "="
print(f"PROD = {PROD}")
