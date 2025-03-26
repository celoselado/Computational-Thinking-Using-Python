# rodizio

print('--------------------------')
print('Exemplo com If-Elif-else')
print('--------------------------')
final_placa = int(input('Digite o ultimo número da placa do seu carro: '))

if final_placa == 1 or final_placa == 2:
    print('Segunda-Feira você pode rodar')
elif final_placa == 3 or final_placa == 4:
    print('Terça-Feira você pode rodar')
elif final_placa == 5 or final_placa == 6:
    print('Quarta-Feira você pode rodar')
elif final_placa == 7 or final_placa == 8:
    print('Quinta-Feira você pode rodar')
elif final_placa == 9 or final_placa == 0:
    print('Sexta você pode rodar')
else:
    print('Número inválido')

print('-----------------------------')
print('Exemplo feito com Match-Case')
print('-----------------------------')

final_placa = int(input('Digite o ultimo número da placa do seu carro: '))

match final_placa:
    case 1 | 2:
        print('Segunda-Feira')
    case 3 | 4:
        print('Terça-Feira')
    case 5 | 6:
        print('Quarta-Feira')
    case 7 | 8:
        print('Quinta-Feira')
    case 9 | 0:
        print('Sexta-Feira')
    case _:
        print('Número inválido!') 