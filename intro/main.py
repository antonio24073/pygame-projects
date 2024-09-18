# comentário => #

# variáveis
nome = "Hero"
vida = 10
gravidade = 9.8
vivo = False

# inputs
nome = input("Digite o seu nome:") or "Antonio"
vida = input("Digite um número:") or 20
print("Nome: ", nome)
print("Vida: ", vida)

# condições
if nome == "Hero":
    print("O nome é Hero.")
elif nome != "Hero":
    print("O nome não é Hero.")

if nome == "Hero":
    print("O nome é Hero.")
else:
    print("O nome não é Hero.")

# operadores aritméticos
print("Vida: ", vida + 5)
print("Vida: ", vida - 5)
print("Vida: ", vida * 5)
print("Vida: ", vida / 5)

# funções
def pulo():
    print("pular")
def defesa():
    print("defender")
pulo()
defesa()

# parâmetro
def ataque(x):
    print("dano:", x)
ataque(15)

# repetição
x = range(3, 9, 2)
for n in x:
  print(n)

ns = ["soldado", "princesa", "ogro", "rei"]

for n in ns:
    print(n)
    if n == "ogro":
        defesa()
    elif n == "rei":
        ataque()

while True:
    print("infinito")

from biblioteca import pulo
pulo()

import pygame