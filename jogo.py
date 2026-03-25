print('=== JOGO DE ADIVINHAÇÃO ===')

numero_secreto = 7
tentativas = 0

while True:
    palpite = int(input('Tente adivinhar o número: '))
    tentativas += 1

    if palpite == numero_secreto:
        print('Acertou!')
        print('Tentativas:', tentativas)
        break
    elif palpite < numero_secreto:
        print('Muito baixo')
    else:
        print('Muito alto')

print('Fim de jogo!')
