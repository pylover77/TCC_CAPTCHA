from captcha.image import ImageCaptcha
import random
import string
import os

# Função para gerar captchas fáceis com ajustes
def gerar_captchas(qtd=50, output_dir="imgs"):
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    width, height = 250, 100  # Aumentando a largura e altura para mais espaço
    font_size = 50  # Aumentando o tamanho da fonte

    # Usar uma fonte instalada no Windows
    font_path = r'C:\Windows\Fonts\Arial.ttf'  # Caminho correto para fontes no Windows
    image = ImageCaptcha(width=width, height=height, font_sizes=[font_size], fonts=[font_path])

    for i in range(qtd):
        
        # Gerar texto simples e fácil de ler
        captcha_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))

        # Gerar imagem com texto fácil de identificar
        captcha_image = image.generate_image(captcha_text)

        # Adicionar um fundo branco e sem interferências
        captcha_image = captcha_image.convert("RGB")
        
        # Salvar a imagem gerada
        captcha_image_path = os.path.join(output_dir, f"captcha_{i}_{captcha_text}.png")
        captcha_image.save(captcha_image_path)

        print(f"Captcha '{captcha_text}' gerado e salvo em '{captcha_image_path}'")


gerar_captchas(qtd=50)
