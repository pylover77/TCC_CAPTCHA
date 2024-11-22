import os
import random
import string
from captcha.image import ImageCaptcha

# Função para gerar um captcha de 4 letras
def gerar_texto_captcha():
    return ''.join(random.choices(string.ascii_uppercase, k=4))  


image = ImageCaptcha()

img_directory = 'img'
os.makedirs(img_directory, exist_ok=True)  # Cria a pasta 'img' se ela não existir

# Gerar e salvar 20 captchas
for i in range(20):
    captcha_text = gerar_texto_captcha() 
    file_path = os.path.join(img_directory, f'{captcha_text}.png') 
    image.write(captcha_text, file_path)  
    print(f"Captcha {captcha_text} gerado e salvo como '{file_path}'.")

print("Todos os captchas foram gerados e salvos na pasta 'img'.")
