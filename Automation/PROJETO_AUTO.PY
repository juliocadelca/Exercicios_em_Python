# 1. Apertar tecla windows


import pyautogui
import time
pyautogui.PAUSE = 2
pyautogui.press("win")

# 2. Digitar bloco de notas

pyautogui.write("Bloco de notas")

# 3. Dar enter para abrir

pyautogui.press("enter")

# 4. Escrever dado do outro bloco de notas (Dados)
# 4.1 Abrir o bloc de notas
# 4.2 Copiar dados
# 4.3 Fechar a base dados

pyautogui.click(x=1597, y=880)
pyautogui.doubleClick(x=29, y=522)
pyautogui.hotkey("ctrl", "a", "ctrl", "c")
pyautogui.hotkey("alt", "tab")
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("alt", "tab")
pyautogui.hotkey("alt", "F4")

# 5. Salvar como

pyautogui.hotkey("ctrl", "shift", "s")

# 6. Nomear como "Combo açaí"

pyautogui.write("Combo Acai perfeito")
pyautogui.press("enter")

# 7. Fechar tudo

pyautogui.hotkey("alt", "F4")
