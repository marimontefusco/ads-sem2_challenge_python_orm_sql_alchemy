# AC05 -> INTEGRAÇÃO COM BANCO DE DADOS
from classes import *
from funcoes import *
from funcoesExibicao import *

## CLASSE MAIN
try:

  while True:

    exibirMenu()
    opcao = int(input('Digite a opção desejada: '))

    match opcao:
      case 1:
        exibirHeaderMedico()
        cadastrarMedico()

      case 2:
        exibirHeaderPaciente()
        cadastrarPaciente()

      case 3: 
        exibirHeaderExame()
        cadastrarExame()

      case 4:
        exibirHeaderConsultar()
        #consultar()
      
      case 5:
        exibirFinal()
        break

      case _:
        print('Opção inválida, tente novamente')
        break

except Exception as erro:
  print(f'Erro: {erro}')

finally:
  connection.close() # Fechando Conexão com BD