idade = input('Qual a sua idade? ')
sexo = input('Qual o seu genero? F/M? ')

if sexo.upper() == 'F':
    # Codigo Feminino
    if int(idade) >= 60:
        print('Parabéns! Sua aposentadoria será concedida!')
    else:
        print(f'Sua vez ainda não chegou! Aguarde mais {60 - int(idade)} anos.')
        
elif sexo.upper() == 'M':
    # Codigo Masculino
    if int(idade) >= 65:
        print('Parabéns! Sua aposentadoria será concedida!')
    else:
        print(f'Sua vez ainda não chegou! Aguarde mais {65 - int(idade)} anos.')


else:
    print('Opção inválida! Tente novamente!')