q = str(input("Digite uma frase: ")).upper()
print("Analisando...")
print("A  letra A aparece {} vezes na frase.".format(q.count('A')))
print("A primeira letra A aparece na posição: {}".format(q.find('A')+1))
print("A ultima letra A aparece na posição: {} ".format(q.rfind('A')+1))