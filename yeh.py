# ==============================================================================
# PROVA PRÁTICA AV2 - 3º BIMESTRE
# ARQUIVO: av2_sistema_modular.py
# Nome do Aluno: Ana Valenttina
# Data:
# Link do Repositório:
# ==============================================================================

dados_brutos = [
    " carlos eduardo silva;desenvolvedor;11988887777 ",
    " ana paula mendes;analista de rh;21977776666 ",
    " roberto carlos oliveira;gerente de projetos;31966665555 "
]


def formatar_texto(texto):
    return texto.strip().upper()


def pegar_ddd(telefone):
    telefone = telefone.strip()
    return telefone[:2]


def processar_cadastros(cadastros):
    total_registros = 0

    for cadastro in cadastros:
        dados = cadastro.split(";")

        nome = formatar_texto(dados[0])
        cargo = formatar_texto(dados[1])
        ddd = pegar_ddd(dados[2])

        print(f"Nome: {nome}")
        print(f"Cargo: {cargo}")
        print(f"DDD: {ddd}")
        print("-" * 42)

        total_registros += 1

    print(f"Total de registros processados: {total_registros}")


print("=" * 50)
print("     SISTEMA DE GESTÃO MODULARIZADO - AV2")
print("=" * 50)

print("\nIniciando o processamento dos dados...\n")

processar_cadastros(dados_brutos)

print("\nPROCESSAMENTO CONCLUÍDO")