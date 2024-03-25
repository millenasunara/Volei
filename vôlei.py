jogadores = {}
time = []


def exibir_detalhes_jogador(indice):
    if indice < 1 or indice > len(jogadores):
        print("Índice inválido.")
        return

    nome_jogador, info = list(jogadores.items())[indice - 1]
    print(f"Detalhes do jogador(a) {nome_jogador}:")
    print(f"Total de Pontos: {info['total_pontos']}")
    if info['pontos']:
        print(f"Pontos por partida: {info['pontos']}")
    print(f"Time: {time[indice - 1]}")

print("-=-=-=-=-=-=-=-=VÔLEI-=-=-=-=-=-=-=-=")
while True:
    nome_jogador = input("Insira o nome do jogador(a): ")
    jogou_partida = input(f"O jogador(a) {nome_jogador} jogou alguma partida? (SIM/NÃO): ").strip().lower()

    if jogou_partida == "sim":
        num_partidas = int(input(f"Quantas partidas {nome_jogador} jogou? "))
        pontos_jogador = []
        for i in range(1, num_partidas + 1):
            pontos_partida = int(input(f"Insira os pontos do jogador {nome_jogador} na partida {i}: "))
            pontos_jogador.append(pontos_partida)

        total_pontos = sum(pontos_jogador)

        jogadores[nome_jogador] = {
            'pontos': pontos_jogador,
            'total_pontos': total_pontos,
        }

        time_jogador = input(f"Insira o time do jogador(a) {nome_jogador}: ")
        time.append(time_jogador)

    else:
        jogadores[nome_jogador] = {
            'pontos': [],
            'total_pontos': 0,
        }

        time.append(None)

    continuar = input("Deseja adicionar mais um jogador(a)? (SIM/NÃO): ").strip().lower()

    if continuar != "sim":
        break

print("\n-=-=-=-=-=-=-=-=Jogadores cadastrados: -=-=-=-=-=-=-=-=")
for indice, (nome, info) in enumerate(jogadores.items(), start=1):
    print(
        f"Time:  {indice} || {time[indice - 1]} || Nome: {nome} || Total de Pontos: {info['total_pontos']} ||  Pontos por partida: {info['pontos']}")
print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=")

while True:
    try:
        indice_jogador = int(input("Insira o índice do jogador(a) para exibir detalhes (0 para sair): "))
        if indice_jogador == 0:
            break
        exibir_detalhes_jogador(indice_jogador)
    except ValueError:
        print("\nÍndice inválido. Insira um número válido.")


def finalizar_programa():
    print("-=-=-=-=-=-=-=-=Programa finalizado.-=-=-=-=-=-=-=-=")
    exit()

finalizar_programa()




