from socket import *
from constCS import *

s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print('Servidor iniciado!')

while True:
  (conn, addr) = s.accept()
  print("Cliente conectado!")

  data = conn.recv(1024)

  if not data:
    conn.close()
    break

  comando = bytes.decode(data)
  print("Dados recebidos: " + comando)

  comandos = comando.split(";")

  operacao = int(comandos[0])
  numero1 = float(comandos[1])
  numero2 = float(comandos[2])

  resultado = 0.0;

  if operacao == 1:
    resultado = numero1 + numero2
  elif operacao == 2:
    resultado = numero1 - numero2
  elif operacao == 3:
    resultado = numero1 / numero2
  elif operacao == 4:
    resultado = numero1 * numero2

  print("Dados enviados: " + str(resultado))

  conn.send(str.encode(str(resultado)))
  conn.close()