from google.colab import files
import cv2
from matplotlib import pyplot as plt

uploaded = files.upload()

image_name = list(uploaded.keys())[0]
print("Arquivo carregado:", image_name)

img_colorida = cv2.imread(image_name)

if img_colorida is None:
    print("Erro: imagem não foi carregada. Verifique o nome do arquivo.")
else:
    img_cinza = cv2.cvtColor(img_colorida, cv2.COLOR_BGR2GRAY)

    _, img_binaria = cv2.threshold(img_cinza, 127, 255, cv2.THRESH_BINARY)

    plt.figure(figsize=(15,5))

    plt.subplot(1,3,1)
    plt.title("Imagem Original")
    plt.imshow(cv2.cvtColor(img_colorida, cv2.COLOR_BGR2RGB))
    plt.axis("off")

    plt.subplot(1,3,2)
    plt.title("Imagem em Cinza")
    plt.imshow(img_cinza, cmap="gray")
    plt.axis("off")

    plt.subplot(1,3,3)
    plt.title("Imagem Binária")
    plt.imshow(img_binaria, cmap="gray")
    plt.axis("off")

    plt.show()
