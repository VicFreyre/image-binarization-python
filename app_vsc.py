import cv2

caminho = r"C:\Users\ruvic\Desktop\ml\orchid.jpg" #troque o caminho para a imagem que desejar usar

img_colorida = cv2.imread(caminho)

img_cinza = cv2.cvtColor(img_colorida, cv2.COLOR_BGR2GRAY)

_, img_binaria = cv2.threshold(img_cinza, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("Imagem Original", img_colorida)
cv2.imshow("Imagem em Cinza", img_cinza)
cv2.imshow("Imagem Binaria", img_binaria)

cv2.waitKey(0)
cv2.destroyAllWindows()
