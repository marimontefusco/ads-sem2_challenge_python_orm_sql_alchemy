from sqlalchemy import create_engine, text, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, Session

# Conectando com o banco SQLite:
engine = create_engine('sqlite:///db_hospital.db')

# Criando as Tabelas no BD
with engine.connect() as connection:
  result = connection.execute(text('''
    CREATE TABLE IF NOT EXISTS PACIENTE (
      ID INTEGER PRIMARY KEY,
      NOME VARCHAR(255),
      CPF VARCHAR(255),
      IDADE INTEGER
    )'''
  ))

with engine.connect() as connection:
  result = connection.execute(text('''
    CREATE TABLE IF NOT EXISTS MEDICO (
      ID INTEGER PRIMARY KEY,
      NOME VARCHAR(255),
      CRM VARCHAR(255),
      ESPECIALIZACAO VARCHAR(255)                              
    )'''
  ))

with engine.connect() as connection:
  result = connection.execute(text('''
    CREATE TABLE IF NOT EXISTS EXAME (
      ID INTEGER PRIMARY KEY,
      ID_MEDICO INTEGER,
      ID_PACIENTE INTEGER,
      DESCRICAO VARCHAR(255),
      RESULTADO VARCHAR(255)                            
    )'''
  ))

# Iniciando Sessão com BD
session = Session(engine)

# Classe Base do SQLAlchemy
class Base(DeclarativeBase):
  pass


## ## Definição das Classes e MAPEAMENTO das Tabelas ## ##

# classe Paciente
class Paciente(Base):
  __tablename__ = 'PACIENTE'
  id = Column('ID', Integer, autoincrement = True, primary_key=True)
  nome = Column('NOME', String(255))
  cpf = Column('CPF', String(255))
  idade = Column('IDADE', Integer)

  def __init__(self, nome, cpf, idade):
    self.nome = nome
    self.cpf = cpf
    self.idade = idade

# classe Medico
class Medico(Base):
  __tablename__ = 'MEDICO'
  id = Column('ID', Integer, autoincrement = True, primary_key=True)
  nome = Column('NOME', String(255))
  crm = Column('CRM', String(255))
  especializacao = Column('ESPECIALIZACAO', String(255))

  def __init__(self, nome, crm, especializacao):
    self.nome = nome
    self.crm = crm
    self.especializacao = especializacao

# classe Exame
class Exame(Base):
  __tablename__ = 'EXAME'
  id = Column('ID', Integer, autoincrement = True, primary_key=True)
  id_medico = Column('ID_MEDICO', Integer)
  id_paciente = Column('ID_PACIENTE', Integer)
  descricao = Column('DESCRICAO', String(255))
  resultado = Column('RESULTADO', String(255))

  def __init__(self, id_medico, id_paciente, descricao, resultado):
    self.id_medico = id_medico
    self.id_paciente = id_paciente
    self.descricao = descricao
    self.resultado = resultado