class Agenda:
  descricao = None
  data = None
  hora = None
  duracao = None

agenda = []

def imprimir(evento):
    print("\n---------------------------")
    print("Descrição: " + evento.descricao)
    print("Data: " + evento.data)
    print("Horário: " + evento.hora)
    print("Duração: " + evento.duracao + " horas")
    print("---------------------------")



def ler(evento = None):
  _evento = Agenda()
  if evento:
    _evento.data = evento.data
    _evento.hora = evento.hora
  else:
    _evento.data = input("Informe a data (dd/mm/yyyy): ")
    _evento.hora = input("Informe o horário (hh:mm): ")
  _evento.descricao = input("Informe a descrição do evento: ")
  _evento.duracao = input("Informe a duração em horas: ")
  return _evento



def filtrar(evento = None):
  if evento:
    data = evento.data
    hora = evento.hora
  else:
    data = input("Informe a data do evento: ")
    hora = input("Informe o horário do evento: ")
  for i in range(len(agenda)):
    if agenda[i].data == data and agenda[i].hora == hora:
      return agenda[i]



def incluir():
  evento = ler()
  if filtrar(evento):
    print("\nEvento não criado: Há outro evento no horário especificado.")
  else:
    agenda.append(evento)
    print("\nEvento criado.")      



def consultar():
  evento = filtrar()
  if evento:
    imprimir(evento)
  else:
    print("\nEvento não encontrado.")



def listar():
  for i in range(len(agenda)):
    imprimir(agenda[i])



def alterar():
  evento = filtrar()
  if evento:  
    novoEvento = ler(evento)
    for i in range(len(agenda)):
      if agenda[i] == evento:
        agenda[i] = novoEvento
        print("\nEvento alterado")
  else:
    print("\nEvento não encontrado")
  


def excluir():
  evento = filtrar();
  if evento:
    agenda.remove(evento)
    print("\nEvento excluído")
  else:
    print("\nEvento não encontrado")



while True:
  opcao = int(input(
      "\nSelecione uma operação: \n" +
      "1. Incluir evento na agenda; \n" +
      "2. Consultar evento na agenda; \n" +
      "3. Alterar evento da agenda; \n" +
      "4. Excluir evento da agenda; \n" +
      "5. Listar todos os eventos da agenda \n" +
      "6. Sair; \n" +
      "> "
  ))

  if opcao == 1:
    incluir()
  elif opcao == 2:
    consultar()
  elif opcao == 3:
    alterar()
  elif opcao == 4:
    excluir()
  elif opcao == 5:
    listar()
  else:
    break