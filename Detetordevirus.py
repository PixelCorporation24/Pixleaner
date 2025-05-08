virus_hashes = {
    "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855": "EICAR Test File",

}

import hashlib

def calcular_hash(arquivo):
    #Calcula o hash de um arquivo
    hasher = hashlib.md5()
    with open(arquivo, "rb") as f:
        while chunk := f.read(4096):
            hasher.update(chunk)
    return hasher.hexdigest()
