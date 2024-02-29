def computador_escolhe_jogada(n, m):
    if n <= m:
        return n
    else:
        if n % (m + 1) > 0:
            return n % (m + 1)
        return m

def usuario_escolhe_jogada(n, m):
  pecas = int(input("Quantas peças você vai tirar? "))
  while pecas > m or pecas > n or pecas <= 0:
    print("Oops! Jogada inválida! Tente de novo.")
    pecas = int(input("Quantas peças você vai tirar? "))
  return pecas

def partida():
    n = int(input("Digite o número de peças do jogo: "))
    m = int(input("Digite o número máximo de peças que é possível retirar em uma rodada: "))

    if m > n:
        print("A quantidade de peças por jogadas devem ser menor ou igual as peças totais")
        partida()

    valor = 0
    jogada = 0
    if (n % (m + 1) == 0):
        print("Você começa!")
        jogada = 1
        while n > 0:
            if jogada == 1:
                valor = usuario_escolhe_jogada(n, m)
                print("Você tirou", valor, "peça(s).")
                n = n - valor
                print("Agora restam", n, "peças no tabuleiro.")
                jogada = 2
            else:
                valor = computador_escolhe_jogada(n, m)
                print("O computador tirou", valor, "peça(s)")
                n = n - valor
                print("Agora restam", n, "peças no tabuleiro.")
                jogada = 1
        if jogada == 1:
            print("Fim do jogo! O computador ganhou!")
            return 2
        else:
            print("Fim do jogo! O você ganhou!")
            return 1

    else:
        print("Computador começa!")
        jogada = 2
        while n > 0:
            if jogada == 1:
                valor = usuario_escolhe_jogada(n, m)
                print("Você tirou", valor, "peça(s).")
                n = n - valor
                print("Agora restam", n, "peças no tabuleiro.")
                jogada = 2
            else:
                valor = computador_escolhe_jogada(n, m)
                print("O computador tirou", valor, "peça(s)")
                n = n - valor
                print("Agora restam", n, "peças no tabuleiro.")
                jogada = 1
        if jogada == 1:
            print("Fim do jogo! O computador ganhou!")
            return 2
        else:
            print("Fim do jogo! O você ganhou!")
            return 1

def campeonato():
    partida_num = 1
    placar_jogador = 0
    placar_comp = 0

    while partida_num < 4:
        print("**** Rodada", partida_num ,"****\n")
        if partida() == 1:
            placar_jogador = placar_jogador + 1
        else:
            placar_comp = placar_comp + 1
        partida_num = partida_num + 1 
    print("**** Final do campeonato! ****\n")
    print("Placar: Você", placar_jogador, "X", placar_comp, "Computador")

def main():
	print ("Bem-vindo ao jogo do NIM! Escolha:")
	print ("1 - para jogar uma partida isolada")
	print ("2 - para jogar um campeonato")

	number = int(input("Digite o número: "))
	if number == 1:
		print ("Voce escolheu uma partida isolada!")
		partida()
	elif number == 2:
		print ("Voce escolheu um campeonato!")
		campeonato()
	else:
		print ("Esse valor nao é valido")
		main()

main()
