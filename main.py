import json

# Carrega os dados do JSON
def carregar_dados():
    with open("racas_e_classes.json", "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

# Mostra as opções de raça ou classe
def exibir_opcoes(lista, tipo):
    print(f"\nEscolha sua {tipo}:")
    for i, item in enumerate(lista, 1):
        print(f"{i}. {item['nome']}")
        beneficios_ou_habilidades = "beneficios" if tipo == "raça" else "habilidades"
        for beneficio in item[beneficios_ou_habilidades]:
            print(f"   - {beneficio}")
    escolha = int(input(f"Digite o número da {tipo} desejada: ")) - 1
    return lista[escolha]

# Cria o personagem
def criar_personagem(dados):
    print("=== Bem-vindo ao Criador de Personagem ===")
    print("Primeiro, escolha sua raça:")
    raca = exibir_opcoes(dados["racas"], "raça")

    print("\nAgora, escolha sua classe:")
    classe = exibir_opcoes(dados["classes"], "classe")

    personagem = {
        "nome": input("\nDigite o nome do seu personagem: "),
        "raca": raca["nome"],
        "classe": classe["nome"],
        "beneficios": raca["beneficios"],
        "habilidades": classe["habilidades"]
    }

    print("\n=== Personagem Criado com Sucesso! ===")
    print(f"Nome: {personagem['nome']}")
    print(f"Raça: {personagem['raca']}")
    print(f"Classe: {personagem['classe']}")
    print("Benefícios:")
    for beneficio in personagem["beneficios"]:
        print(f"   - {beneficio}")
    print("Habilidades:")
    for habilidade in personagem["habilidades"]:
        print(f"   - {habilidade}")

    return personagem

# Função principal
def main():
    dados = carregar_dados()
    criar_personagem(dados)

if __name__ == "__main__":
    main()
