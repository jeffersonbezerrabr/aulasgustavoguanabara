import pygame
import time

# Inicialização correta
pygame.mixer.init()  # Inicializa especificamente o mixer

try:
    pygame.mixer.music.load("exe021.mp3")  # Confira o nome/caminho do arquivo
    pygame.mixer.music.play()
    
    # Espera ativa enquanto a música está tocando
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)  # Não sobrecarrega a CPU
        
except Exception as e:
    print(f"Erro: {e}")
finally:
    pygame.quit()
