from pathlib import Path

categorias = {
    ".png": "Imagens",
    ".jpg": "Imagens",
    ".gif": "Imagens",
    ".pdf": "Documentos",
    ".docx": "Documentos",
    ".txt": "Documentos",
    ".mp3": "Audios",
    ".jpeg": "Imagens"
}


def organiza_pasta(item, pasta_raiz):
    extensao = item.suffix.lower()
    nome_da_pasta = categorias.get(extensao, "Outros")
    destino = pasta_raiz / nome_da_pasta
    destino.mkdir(exist_ok=True)

    arquivo_final = destino / item.name
    contador = 1

    # Evita erro se já existir um arquivo com o mesmo nome no destino
    while arquivo_final.exists():
        novo_nome = f"{item.stem}_{contador}{item.suffix}"
        arquivo_final = destino / novo_nome
        contador += 1

    item.rename(arquivo_final)


verificacao = False

while not verificacao:
    nome_pasta = input("Qual pasta deseja organizar? ").strip()
    pasta = Path(nome_pasta)

    if nome_pasta != "" and pasta.is_dir():
        verificacao = True
        for item in pasta.iterdir():
            if item.is_file():
                organiza_pasta(item, pasta)
            elif item.is_dir() and item.name not in categorias.values():
                for subitem in item.iterdir():
                    if subitem.is_file():
                        organiza_pasta(subitem, pasta)
        print("Organização concluída com sucesso!")
    else:
        print("Digite uma pasta válida no computador!")