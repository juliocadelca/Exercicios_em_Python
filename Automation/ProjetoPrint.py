# 0 Criar um bot que manda de hora a hora.
# 1 Clicar em minizar tela do VS.

import pyautogui as py
import time
while True:
    py.PAUSE = 1
    py.click(x=1477, y=15)
    # 2 Tirar print com Ctrl win S ou outra opção do pyautogui

    py.hotkey("Shift", "win", "s")
    time.sleep(1)
    py.moveTo(x=801, y=248)
    py.dragTo(x=1447, y=654, button="left", duration=1)

    # 3 Abrir o chrome e selecionar o perfil

    py.press("win")
    py.write("Chrome")
    py.press("enter")
    py.click(x=611, y=519)
    py.click(x=1287, y=113)

    # 4 Abrir whatsapp e selecionar contato e mensagem para enviar.

    py.click(x=58, y=96)
    time.sleep(13)
    py.click(x=185, y=223)
    py.write("Anotacoes")
    py.press("enter")
    py.hotkey("Ctrl", "v")
    py.write(str("Vista atual"))
    py.press("enter")
    # colocar esrito em cima "Visão atual"
    time.sleep(5)
