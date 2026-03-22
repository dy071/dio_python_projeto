# Variáveis e Constantes 
nome = 'Diana'
idade = 26 

nome = 'João'

print(nome, idade)

limite_saque_diario = 1000

BRAZILIAN_STATES = ['SP', 'RJ', 'SC']

print(BRAZILIAN_STATES)

nome, idade = ('Guilherme', 30)
print(nome, idade)

# Convertendo Tipos 
print(int(1.9))
print(int("10"))
print(type(str(10.10)))

print(100 / 2)
print(100 // 2)

# Funções de entrada e saída 
nome = input("Informe o seu nome: ")
print(f"Bem-vindo, {nome}")

dia = input("Informe um número: ")
mes = 5
ano = 2000
print(dia, mes, ano, sep="/")