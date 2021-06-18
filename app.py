from random import randint


print('-=-' * 20)
print('SEJA BEM VINDO AO GAME PEDRA, PAPEL E TESOURA')
print('-=-' * 20)

#base para condicionais
pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

lista_valores = ['pedra', 'papel', 'tesoura']

escolha_usuario = input('Qual sua jogada?\n \n[0] para Pedra \n[1] para Papel\n[2] para Tesoura: ')


if escolha_usuario == '0':
    print('\n\033[1;93mVocê:\n\033[m')
    print(pedra)

if escolha_usuario == '1':
    print('\n\033[1;93mVocê:\n\033[m')
    print(papel)

if escolha_usuario == '2':
    print('\n\033[1;93mVocê:\n\033[m')
    print(tesoura)


escolha_computador = lista_valores[randint(0, 2)]


if escolha_computador == 'pedra':
    print('\n\033[1;94mComputador:\n\033[m')
    print(pedra)

if escolha_computador == 'papel':
    print('\n\033[1;94mComputador:\n\033[m')
    print(papel)

if escolha_computador == 'tesoura':
    print('\n\033[1;94mComputador:\n\033[m')
    print(tesoura)


#condições empate

if escolha_usuario == '0' and escolha_computador == 'pedra':
    print('\033[;7mEMPATE!\033[m')

elif escolha_usuario == '1' and escolha_computador == 'papel':
    print('\033[;7mEMPATE!\033[m')

elif escolha_usuario == '2' and escolha_computador == 'tesoura':
    print('\033[;7mEMPATE!\033[m')

#vitorias usuáiro
elif escolha_usuario == '0' and escolha_computador == 'tesoura':
    print('\033[1;92mVOCÊ VENCEU\033[m')

elif escolha_usuario == '1' and escolha_computador == 'pedra':
    print('\033[1;92mVOCÊ VENCEU!\033[m')

elif escolha_usuario == '2' and escolha_computador == 'papel':
    print('\033[1;92mVOCÊ VENCEU!\033[m')

else:
    print('\033[1;91mVOCÊ PERDEU!\033[m')




