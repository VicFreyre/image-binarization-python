import os
caminho = r"C:\Users\ruvic\Desktop\ml\orchid.jpg" #troque para o caminho da sua imagem

print("Existe?", os.path.exists(caminho))
print("Diretório existe?", os.path.isdir(r"C:\Users\ruvic\Desktop\ml"))
print("Arquivos na pasta:", os.listdir(r"C:\Users\ruvic\Desktop\ml"))
