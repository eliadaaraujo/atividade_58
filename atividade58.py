# Leia uma frase e mostre:
# A palavra mais longa e a mais curta.
# A quantidade total de palavras digitadas.
# Dica: use split().

frase = input("Digite uma frase: ")

palavras = frase.split()
mais_longa = max(palavras, key=len)
mais_curta = min(palavras, key=len)
quantidade = len(palavras)

print("Palavra mais longa:", mais_longa)
print("Palavra mais curta:", mais_curta)
print("Quantidade de palavras:", quantidade)
