import os
import twocaptcha

solver = twocaptcha.TwoCaptcha(apiKey='172928fb2b0c8d3cb96317dbc81e3c63')

img_directory = 'img'

def resolver_captchas():
    acertos = 0
    erros = 0
    for file_name in os.listdir(img_directory):
        if file_name.endswith('.png'):
            captcha_path = os.path.join(img_directory, file_name)
            captcha_text = file_name.replace('.png', '').lower()
            
            try:
                result = solver.normal(captcha_path)
                solved_text = result['code'].lower()
                
                print(f"Esperado: {captcha_text}, Resolvido: {solved_text}")
                
                if solved_text == captcha_text:
                    print(f"Captcha correto! Texto: {solved_text.upper()} = Nome do arquivo: {captcha_text.upper()}")
                    acertos += 1
                else:
                    print(f"Captcha incorreto! Texto resolvido: {solved_text.upper()}, Nome do arquivo: {captcha_text.upper()}")
                    erros += 1
            
            except Exception as e:
                print(f"Erro ao resolver o captcha {captcha_path}: {e}")
                erros += 1

    print(f"\nTotal de acertos: {acertos}")
    print(f"Total de erros: {erros}")

resolver_captchas()
