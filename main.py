import json

# Dados do arquivo JSON
data = {
    "racas": [
        {
            "nome": "Humano",
            "beneficios": ["+1 em todas as habilidades", "+5% de experiência adicional"]
        },
        {
            "nome": "Elfo",
            "beneficios": ["+2 Destreza", "Visão no Escuro", "Imunidade a sono mágico"]
        },
        {
            "nome": "Anão",
            "beneficios": ["+2 Constituição", "Resistência a venenos", "+1 contra gigantes"]
        }
    ],
    "classes": [
        {
            "nome": "Guerreiro",
            "habilidades": ["Ataque Poderoso", "Defesa Robusta", "Grito de Guerra"]
        },
        {
            "nome": "Mago",
            "habilidades": ["Bola de Fogo", "Escudo Arcano", "Teletransporte"]
        },
        {
            "nome": "Ladino",
            "habilidades": ["Ataque Furtivo", "Esconder-se nas Sombras", "Abrir Fechaduras"]
        }
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
    exibir_opcoes(data["racas"], "raça")
    raca = selecionar_opcao(data["racas"], "raça")
    print(f"\nVocê escolheu a raça: {raca['nome']}")
    print("Benefícios:")
    for beneficio in raca["beneficios"]:
        print(f"- {beneficio}")

    # Escolha da classe
    exibir_opcoes(data["classes"], "classe")
    classe = selecionar_opcao(data["classes"], "classe")
    print(f"\nVocê escolheu a classe: {classe['nome']}")
    print("Habilidades:")
    for habilidade in classe["habilidades"]:
        print(f"- {habilidade}")

    # Exibir resumo do personagem
    print("\nSeu personagem foi criado com sucesso!")
    print(f"Raça: {raca['nome']}")
    print(f"Classe: {classe['nome']}")
    print("Benefícios:")
    for beneficio in raca["beneficios"]:
        print(f"- {beneficio}")
    print("Habilidades:")
    for habilidade in classe["habilidades"]:
        print(f"- {habilidade}")

# Executar o jogo
if __name__ == "__main__":
    criar_personagem()
