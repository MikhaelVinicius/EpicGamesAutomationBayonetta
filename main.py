import time

import pyautogui

pyautogui.alert("""Automoção preste a ser executada"""
                """Não toque em nada!"""
                """Clique somente em Enter no teclado!""")


pyautogui.PAUSE = 1
pyautogui.press('winleft')
pyautogui.PAUSE = 1
pyautogui.write('g')
pyautogui.PAUSE = 2
pyautogui.press('enter')
pyautogui.click(1083, 641)
pyautogui.PAUSE = 2
pyautogui.click(342, 18)
pyautogui.write('https://store.epicgames.com/pt-BR/free-games')
pyautogui.press('enter')
pyautogui.PAUSE = 3
pyautogui.hotkey('winleft','left')

pyautogui.click(943, 412)


