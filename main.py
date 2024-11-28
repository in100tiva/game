import json
import random

# Dados dos monstros
monstros = {
    "monstros": [
        {
            "nome": "Goblin",
            "nivel": 1,
            "xp": 50,
            "vida": 7,
            "ataque": 5,
            "defesa": 12,
            "recompensas": ["Pequena bolsa de ouro", "Flechas quebradas"]
        },
        {
            "nome": "Kobold",
            "nivel": 1,
            "xp": 25,
            "vida": 5,
            "ataque": 4,
            "defesa": 10,
            "recompensas": ["Daga enferrujada", "2 moedas de prata"]
        },
        # Outros monstros omitidos para simplicidade
    ]
}

def exibir_opcoes(lista, tipo):
    print(f"\nEscolha uma {tipo}:")
    for i, item in enumerate(lista, start=1):
        print(f"{i}. {item['nome']}")

def selecionar_opcao(lista, tipo):
    while True:
        try:
            escolha = int(input(f"Digite o número da sua {tipo}: ")) - 1
            if 0 <= escolha < len(lista):
                return lista[escolha]
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

def criar_personagem():
    print("Bem-vindo ao criador de personagens!")
    
    # Escolha da raça
    racas = [
        {"nome": "Humano", "beneficios": ["+1 em todas as habilidades", "+5% de experiência adicional"]},
        {"nome": "Elfo", "beneficios": ["+2 Destreza", "Visão no Escuro", "Imunidade a sono mágico"]},
        {"nome": "Anão", "beneficios": ["+2 Constituição", "Resistência a venenos", "+1 contra gigantes"]}
    ]
    exibir_opcoes(racas, "raça")
    raca = selecionar_opcao(racas, "raça")

    # Escolha da classe
    classes = [
        {"nome": "Guerreiro", "habilidades": ["Ataque Poderoso", "Defesa Robusta", "Grito de Guerra"]},
        {"nome": "Mago", "habilidades": ["Bola de Fogo", "Escudo Arcano", "Teletransporte"]},
        {"nome": "Ladino", "habilidades": ["Ataque Furtivo", "Esconder-se nas Sombras", "Abrir Fechaduras"]}
    ]
    exibir_opcoes(classes, "classe")
    classe = selecionar_opcao(classes, "classe")

    personagem = {
        "nome": input("\nDigite o nome do seu personagem: "),
        "raca": raca["nome"],
        "classe": classe["nome"],
        "beneficios": raca["beneficios"],
        "habilidades": classe["habilidades"],
        "vida": 10,  # Vida inicial
        "ataque": 5,  # Ataque inicial
        "defesa": 10,  # Defesa inicial
    }

    # Salvar personagem em JSON
    with open("personagem.json", "w") as arquivo:
        json.dump(personagem, arquivo, indent=4)
    print("\nPersonagem salvo com sucesso!")
    
    return personagem

def batalha(personagem):
    print("\nIniciando uma batalha contra um monstro!")
    
    # Escolher um monstro de nível 1 aleatório
    monstros_nivel_1 = [m for m in monstros["monstros"] if m["nivel"] == 1]
    monstro = random.choice(monstros_nivel_1)
    
    print(f"\nVocê encontrou um {monstro['nome']}!")
    print(f"Vida: {monstro['vida']}, Ataque: {monstro['ataque']}, Defesa: {monstro['defesa']}")

    while personagem["vida"] > 0 and monstro["vida"] > 0:
        # Turno do jogador
        print("\nSeu turno!")
        dano = max(personagem["ataque"] - monstro["defesa"], 1)
        monstro["vida"] -= dano
        print(f"Você atacou o {monstro['nome']} causando {dano} de dano!")
        
        if monstro["vida"] <= 0:
            print(f"Você derrotou o {monstro['nome']}!")
            print(f"Recompensas: {', '.join(monstro['recompensas'])}")
            break

        # Turno do monstro
        print("\nTurno do monstro!")
        dano = max(monstro["ataque"] - personagem["defesa"], 1)
        personagem["vida"] -= dano
        print(f"O {monstro['nome']} atacou você causando {dano} de dano!")

        if personagem["vida"] <= 0:
            print("Você foi derrotado! Fim do jogo.")
            break

def main():
    personagem = criar_personagem()
    batalha(personagem)

if __name__ == "__main__":
    main()
