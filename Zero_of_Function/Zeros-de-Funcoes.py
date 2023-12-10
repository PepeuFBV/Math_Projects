# Código para descobrir a aproximação de uma raíz de uma função por meio do metódo da Bissecção

import string


a = 1
b = 3
c = 2
# f(x) = x^2 + 3x + 2

# intervalos para achar a raíz
x = -8     # x para a funcão f(x)
y = -1.5   # y para a funcão f(y)


inserirValores = input("Deseja inserir valores para a, b e c? (S/N)")
if (inserirValores == "S" or inserirValores == "s"):
   a = float(input("Insira o valor de a: "))
   b = float(input("Insira o valor de b: "))
   c = float(input("Insira o valor de c: "))
   x = float(input("Insira o valor do 1º x do intervalo: "))
   y = float(input("Insira o valor do 2º x do intervalo: "))
   print("A função é: f(x) = ", a, "x^2 + ", b, "x + ", c)
   print("O intervalo é: [", x, ", ", y, "]")
   

def f(valor): # Gerar a função
   return (valor*a)**2 + b*valor + c


max_iteracoes = 10
for _ in range(max_iteracoes): # Loop para achar a aproximação da raíz
   pontoMedio = (x + y) / 2
   if f(pontoMedio) == 0:
      break  # Achou uma raíz aproximada
   elif f(pontoMedio) * f(x) < 0:
      y = pontoMedio
   else:
      x = pontoMedio
   if (f(x) * f(y)) >= 0:
      break

print("The root is approximately at:", round(pontoMedio, 2))