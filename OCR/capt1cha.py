import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def preprocess_image(img):
    img = img.convert("L")
    threshold = 140
    img = img.point(lambda p: p > threshold and 255)
    img = img.filter(ImageFilter.MedianFilter(size=3))
    img = ImageEnhance.Contrast(img).enhance(2)
    return img

def quebrar_captchas(input_dir="imgs"):
    if not os.path.exists(input_dir):
        print(f"A pasta {input_dir} não existe!")
        return

    total_acertos = 0
    total_erros = 0

    for filename in os.listdir(input_dir):
        if filename.endswith(".png"):
            img_path = os.path.join(input_dir, filename)
            img = Image.open(img_path)

            img = preprocess_image(img)

            captcha_text = pytesseract.image_to_string(img, config='--psm 7 -c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ').strip()

            correct_text = filename.split('_')[2].replace('.png', '')

            if captcha_text == correct_text:
                resultado = "acertou"
                total_acertos += 1
            else:
                resultado = "errado"
                total_erros += 1

            print(f"Arquivo: {filename}, Texto OCR: '{captcha_text}', Resultado: {resultado}")

    print(f"\nTotal de acertos: {total_acertos}")
    print(f"Total de erros: {total_erros}")

quebrar_captchas()
