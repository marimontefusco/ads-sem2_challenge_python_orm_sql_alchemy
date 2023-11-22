# AC05 -> INTEGRAÇÃO COM BANCO DE DADOS
from funcoesExibicao import *;
from funcoesExibicao import *
from funcoes import *
from classes import *

## CLASSE MAIN
try:

  while True:

    exibirMenu()
    opcao = int(input('''    Digite a opção desejada: '''))
    print('\n')

    match opcao:
      case 1:
        exibirHeaderMedico()
        cadastrarMedico()

      case 2:
        exibirHeaderPaciente()
        cadastrarPaciente()

      case 3: 
        exibirMsgExame()
        op = int(input('''    Digite a opção desejada: '''
        ))
        
        if op == 1:
          exibirHeaderConsultarMedico()
          consultarMedicos()       
        elif op == 2:
          exibirHeaderConsultarPaciente()
          consultarPacientes()
        elif op == 3:
          exibirHeaderExame()
          cadastrarExame()
        elif op == 4:
          exibirMsgFinal()
          break

        else:
          print('Opção inválida, tente novamente')
          break

      case 4:
        exibirHeaderConsultarMedico()
        consultarMedicos()
      
      case 5:
        exibirHeaderConsultarPaciente()
        consultarPacientes()

      case 6:
        exibirHeaderConsultarExame()
        consultarExames()

      case 7:
        exibirMsgFinal()
        break

      case _:
        print('Opção inválida, tente novamente')
        break

except Exception as erro:
  print(f'Erro: {erro}')

finally:
  connection.close() # Fechando Conexão com BD