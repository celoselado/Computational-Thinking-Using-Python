# Aula 

linguagem = input('Linguagem: ')

match linguagem:
    case 'JavaScript':
        print('Desenvolvedor Web')
    case 'Python':
        print('Cientist de Dados')
    case 'PHP':
        print('Desenvolvedor Back-End')
    case 'Java':
        print('Desenvolvedor Back-End ou mobile')
    case 'Solidity':
        print('Desenvolvedor BlockChain')
    case _:
        print('Linguagem não encontrada!')

