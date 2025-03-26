# ExercicioConceitoMedia

print('\n------------------------------------------')
print('Aplicação para calcular média e conceito')
print('------------------------------------------')

NomeAluno = input("\nDigite o nome do aluno: ")

nota1 = float(input("\nDigite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))
nota3 = float(input("Digite a nota da terceira prova: "))

media = (nota1 + nota2 + nota3) / 3

if(media >= 9 and media <= 10):
    conceito = 'A'
    situacao = "Aprovado"
elif(media >= 8 and media < 9):
    conceito = "B"
    situacao = "Aprovado"
elif(media >= 7 and media < 8):
    conceito = "C"
    situacao = "Aprovado"
elif(media >= 6 and media < 7):
    conceito = "D"
    situacao = "Aprovado"
else:
    conceito = "E"
    situacao = "Reprovado"

match conceito:
    case 'A':
        print(f"\nO conceito de conhecimento do aluno {NomeAluno} é de nivel {conceito} sua média foi {media:.1f} e portanto está {situacao}") #Essa é a forma de fazer um print FORMATADO
    case 'B':
       print(f"\nO conceito de conhecimento do aluno {NomeAluno} é de nivel {conceito} sua média foi {media:.1f} e portanto está {situacao}")
    case 'C':
        print(f"\nO conceito de conhecimento do aluno {NomeAluno} é de nivel {conceito} sua média foi {media:.1f} e portanto está {situacao}")
    case 'D':
        print(f"\nO conceito de conhecimento do aluno {NomeAluno} é de nivel {conceito} sua média foi {media:.1f} e portanto está {situacao}")
    case 'E':
        print(f"\nO conceito de conhecimento do aluno {NomeAluno} é de nivel {conceito} sua média foi {media:.1f} e portanto está {situacao}")
    case _:
        print("\nAlgo deu errado durante a aplicação! Por favor reinicie o programa e tente novamente.") 

    

        