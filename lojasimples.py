# INTRODUÇÃO
print('=== BEM VINDO! ====')
print('FAÇA SEU CADASTRO!')

# ORGANIZAÇÃO

nome = (input('Digite o seu nome: '))
idade = int(input('Digite sua idade: '))
if idade >= 18:
    print('Você atende aos requisitos de idade. ')
else:
    print('Você não atende aos requisitos de idade.')
cpf = input('Digite seu CPF: ')

# PRECO, PRODUTOS

preco1 = 450.99
preco2 = 1200.00    
preco3 = 677.67
preco4 = 749.99
preco5 =  819.90


print('')

print ('1 - Mouse gamer sem fio Attack Shark R5 Ultra R5 Ultra! por apenas - R$:', preco1)
print ('2 - Mouse Gamer Sem Fio Logitech G PRO X SUPERLIGHT. - R$:', preco2)
print ('3 - Teclado Gamer Sem Fio Logitech G PRO X!  por apenas - R$:', preco3)
print ('4 - Teclado Mecânico Gamer Logitech G PRO! por apenas - R$:', preco4)
print ('5 - Microfone Condensador USB HyperX QuadCast 2. - por apenas R$:', preco5)


print('')


produtos = input('Escolha os produtos desejados abaixo: ')

print('')

quantidade = str(input('Quantidade: '))

print('')

# RESUMO

print('=== RESUMO ===')

print('Cliente:', nome)
print('Atende aos requisitos:', idade)
print('CPF:', cpf )
print('Produto:', produtos)
print('Quantidade:', quantidade)

print('Obrigado pela compra')
exit = input('Aperte enter para finalizar...')