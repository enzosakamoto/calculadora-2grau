from PySimpleGUI import PySimpleGUI as sg
import numpy as np
    
# Layout
sg.theme('Reds')
layout = [
    [sg.Push(), sg.Text('Formato de equação: Ax^2 + Bx + C'), sg.Push()],
    [sg.Text('Digite o valor de A:'), sg.Input(key='a', size = (4,1))],
    [sg.Text('Digite o valor de B:'), sg.Input(key='b', size = (4,1))],
    [sg.Text('Digite o valor de C:'), sg.Input(key='c', size = (4,1))],
    [sg.Push(), sg.Button('Calcular!'), sg.Button('Limpar!'), sg.Button('Limpar tudo!'), sg.Button('Sair'), sg.Push()],
    [sg.Push(), sg.Text('Equação e Raízes:'), sg.Push()],
    [sg.Push(), sg.Output(key='resultado', size = (70,4)), sg.Push()],
    ]

# Janela
janela = sg.Window('Calculadora de equação de segunda grau', layout, size=(500, 300))

# Eventos
while True:
    eventos, valores = janela.read()
    if eventos in (sg.WIN_CLOSED, 'Sair'):
        break
    
    if eventos == 'Limpar!':
        janela['resultado'].update('')
        
    if eventos == 'Limpar tudo!':
        janela['a'].update('')
        janela['b'].update('')
        janela['c'].update('')
        janela['resultado'].update('')
        
    if eventos == 'Calcular!':
        janela['resultado'].update('')
        values = [valores['a'], valores['b'], valores['c']]
        coefs = []
        for numero in values:
            if numero in ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ;:?/~+!@#$'):
                sg.popup('Digite números e não letras!')
                break
            else:
                for e in numero:
                    if e not in ['0','1','2','3','4','5','6','7','8','9','.','-']:
                        sg.popup('Digite números e não letras!')
                        break
                    # equa = np.poly1d(coefs)
                    # raizes = np.roots(coefs)
                    # print(equa)
                    # print(raizes)
                    
            coefs.append(float(numero))
        
        if len(coefs) == 3:
            equa = np.poly1d(coefs)
            raizes = np.roots(coefs)
            print(equa)
            print('X1 = %s e X2 = %s' %(raizes[0], raizes[1]))
            # print(coefs)
            
            
janela.close()