## Funções de Exibição na Tela ##

def exibirMenu():
  print('''
        
  ================================ 
             
        Sistema de Cadastros

  --------------------------------
     
    1. Cadastrar Médico
    2. Cadastrar Paciente
    3. Cadastrar Exame
        
    4. Consultar Médicos
    5. Consultar Pacientes
    6. Consultar Exames do Paciente
  
    7. Sair
        
  ================================      
  ''')


def exibirHeaderMedico():
  print('''
  --------------------------------
          Cadastrar Médico
  --------------------------------
  ''')


def exibirHeaderPaciente():
  print('''
  --------------------------------
         Cadastrar Paciente
  --------------------------------
  ''')


def exibirHeaderExame():
  print('''
  --------------------------------
          Cadastrar Exame
  --------------------------------
  ''')

def exibirMsgExame():
  print('''
  ================================
        
    Atenção!
        
  ================================
        
    Para cadastrar o Exame, 
    são necessários:
        
    - Id do médico 
    - Id do paciente
          
  ================================
        
    O que você deseja fazer?
        
  ================================
        
    1. Consultar Cadastro Médico
        
    2. Consultar Cadastro Paciente
        
    3. Cadastrar Exame
        
    4. Sair    
    
  ================================
  ''')


def exibirHeaderConsultarMedico():
  print('''
  --------------------------------
          Consultar Médicos
  --------------------------------
  ''')


def exibirHeaderConsultarPaciente():
  print('''
  --------------------------------
         Consultar Pacientes
  --------------------------------
  ''')



def exibirHeaderConsultarExame():
  print('''
  --------------------------------
          Consultar Exames
  --------------------------------
  ''')


def exibirMsgFinal():
  print('''
  ================================
  
              Até Logo!!!
        
  ================================
  ''')
