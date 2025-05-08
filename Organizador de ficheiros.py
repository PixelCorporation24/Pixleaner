import os
import shutil
from pathlib import Path

CATEGORIES = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif"],
    "Documentos": [".txt", ".docx", ".pdf", ".xlsx"],
    "Vídeos": [".mp4", ".avi", ".mov"],
    "Áudios": [".mp3", ".wav", ".aac"],
    "Executáveis": [".exe", ".py", ".ja"],
    "Compactos": [".zip", ".rar"],
}

def organizar_ficheiros(diretorio: str):
    path = Path(diretorio)
    if not path.exists():
        print("Diretório não encontrado!")
        return

for file in path.interdir():
    if file.is_file():
        for categoria, extensoes in CATEGORIES.items():
            pasta_destino = path / categoria
            pasta_destino.mkdir(exist_ok=True)
            shutil.move(str(file), str(pasta_destino / file.name))
            print(f"Movido: {file.name} -> (pasta_destino)")
            break
        
if __name__ == "__main__":
    diretorio_utilizador = input("Digita o diretorio a ser organizado: ")
    organizar_ficheiros(diretorio_usuario)