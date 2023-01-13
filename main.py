import time

import pyautogui

pyautogui.alert("""Automoção preste a ser executada"""
                """Não toque em nada!"""
                """Clique somente em Enter no teclado!""")
#Clicar no jogo(
#Mover o mouse para obter
#Clicar enter
#Mover o mouse para fazer pedido
#Clicar enter

pyautogui.PAUSE = 1
pyautogui.press('winleft')
pyautogui.PAUSE = 1
pyautogui.write('E')
pyautogui.PAUSE = 0.8
pyautogui.press('enter')
time.sleep(15)
##pyautogui.moveTo(1679, 194)
##pyautogui.mouseDown()#Pressiona o mouse
pyautogui.moveTo(1681, 364)
pyautogui.click()
pyautogui.PAUSE=2.0
pyautogui.click()
pyautogui.PAUSE=2.0

pyautogui.click()
pyautogui.PAUSE=8.0#Pausa na pagina do jogo gratis v
pyautogui.click(793, 340)
pyautogui.PAUSE=10.0
pyautogui.click(1440, 820)
pyautogui.PAUSE=8.0
pyautogui.click(1493, 791)


#Entrar na áreas de trabalho
#Abrir a barra de pesquisa do windowns
#Digitar "Epic Games Laucher"
#Clicar em enter
#Descer com mouse