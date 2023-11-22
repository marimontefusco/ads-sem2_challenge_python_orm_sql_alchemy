from classes import Medico, Paciente, Exame, session

# ---------------------------------------------------

def cadastrarMedico():
  nome = input('  Nome: ')
  crm =  input('  CRM: ')
  especializacao = input('  Especialidade: ')

  # Cria obj medico
  medico = Medico(nome, crm, especializacao) 

  # Insere obj medico no BD
  session.add(medico)
  session.commit()

  # Feedback obj cadastrado
  print('\n--------------------------------')
  print('\n Médico cadastrado com sucesso')
  print('\n--------------------------------')

# ---------------------------------------------------

def cadastrarPaciente():   
  nome = input('  Nome: ')
  cpf = input('  CPF: ')
  idade = int(input('  Idade: '))

  # Cria obj paciente
  paciente = Paciente(nome, cpf, idade)

  # Insere obj paciente no BD 
  session.add(paciente)
  session.commit()  

  # Feedback obj cadastrado   
  print('\n--------------------------------')
  print('\nPaciente cadastrado com sucesso')
  print('\n--------------------------------')

# ---------------------------------------------------

def consultarMedicos():
  tb_medico = session.query(Medico).order_by(Medico.id)
  
  for obj in tb_medico:
    print(f'''
    --------------------------------
          
      Id: {obj.id}
      Nome: {obj.nome}
      CRM: {obj.crm}
      Especialidade: {obj.especializacao}

    --------------------------------
    ''')

# ---------------------------------------------------

def consultarPacientes():
  tb_paciente = session.query(Paciente).order_by(Paciente.id)

  for obj in tb_paciente:
    print(f'''
    --------------------------------
          
      Id: {obj.id}
      Nome: {obj.nome}
      CPF: {obj.cpf}
      Idade: {obj.idade}

    --------------------------------
    ''')

# ---------------------------------------------------

def cadastrarExame():
  
  tb_id_medico = session.query(Medico).filter(Medico.id)
  tb_id_paciente = session.query(Paciente).filter(Paciente.id)

  # Consultando id Médico
  input_id_medico = int(input('    Insira o Id do Médico: '))

  if input_id_medico not in tb_id_medico:
    print('    Médico não cadastrado')
  else:
    print('    Médico cadastrado')
    return input_id_medico

  # Consultando id Paciente
  input_id_paciente = int(input('Insira o Id do Paciente: '))

  if input_id_paciente not in tb_id_paciente:
    print('    Paciente não cadastrado')
  else:
    print('    Paciente cadastrado: ')
    id_paciente = session.query(Paciente).get(Paciente.id)
    return id_paciente

  descricao = input('    Descrição do Exame: ')
  resultado = input('    Resultado do Exame: ')

  # Cria obj exame
  exame = Exame (
    id_medico = input_id_medico,
    id_paciente = input_id_paciente,
    descricao = descricao,
    resultado = resultado
    )

  # lista_exames = []
  # Inserindo medico no BD
  session.add(exame)
  session.commit()

  # Feedback obj cadastrado
  print('\n--------------------------------')
  print('\n Exame cadastrado com sucesso')
  print('\n--------------------------------')
    

def consultarExames():
  tb_exame = session.query(Exame).order_by(Exame.id_paciente)

  resultado = session.query(Paciente, Exame).filter(Paciente.id == Exame.id_paciente) 

  for obj in resultado:
    print(f'''
    --------------------------------
          
      Id: {obj.id}
      Id_medico: {obj.id_medico}
      Id_paciente: {obj.id_paciente}
      Descricao: {obj.descricao}
      Resultado: {obj.resultado}

    --------------------------------
    ''')
    
