from socket import *
from constCS import *

operacao = 0;

while operacao < 5:

    operacao = int(input("Escolha a operação a ser executada:\n" +
                     "1 - Soma\n" +
                     "2 - Subtração\n" +
                     "3 - Divisão\n" +
                     "4 - Multiplicação\n" +
                     "5 - Sair\n"))

    if operacao >= 5:
        continue

    numero1 = input("Qual o primeiro número?\n")
    numero2 = input("Qual o segundo número?\n")

    mensagem = str(operacao) + ";" + numero1 + ";" + numero2;

    s = socket(AF_INET, SOCK_STREAM)
    s.connect((HOST, PORT))
    s.send(str.encode(mensagem))
    data = s.recv(1024)
    print ("Resultado: " + bytes.decode(data))
    s.close()