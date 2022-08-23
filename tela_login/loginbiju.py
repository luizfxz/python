from distutils.cmd import Command
from email.errors import MessageError
from tkinter import CENTER
from tkinter import font
from tkinter.font import BOLD
from tkinter.ttk import Style
from typing import Sized
import PySimpleGUI as sg

sg.LOOK_AND_FEEL_TABLE['Tema'] = {'BACKGROUND': '#FFAFCA',
                                      'TEXT': '#000000', 
                                        'INPUT': '#FFFFFF', 
                                        'TEXT_INPUT': '#000000', 
                                        'SCROLL': '#99CC99', 
                                        'BUTTON': ('#000000', '#FFFFFF'), 
                                        'PROGRESS': ('#D1826B', '#CC8019'), 
                                        'BORDER': 1, 'SLIDER_DEPTH': 0,  
                                        'PROGRESS_DEPTH': 0, } 

                
sg.theme('Tema')
layout_column = [
    
        [sg.Image('D:\Aulas\projeto_lf\python\imgs\logo3.png')],

        [sg.Text('Email:', justification='center', font='Ivy 12')],

        [sg.Input(size=(40, 40))],

        [sg.Text('Senha:',justification='center', font='Ivy 12', border_width=10)],
        
        [sg.Input(password_char='*', size=(40, 40))],

        [sg.Button('Entrar'), sg.Button('Esqueceu a senha?')]
]


layout = [[sg.Column(layout_column, element_justification='center'),]]

window = sg.Window('Login', layout, grab_anywhere=True, size=(460,500))

while True:

    event, values = window.read()

    print(event, values)

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

def login_Senha():

    if event == 'Admin' and values == '1234':
        MessageError('Logado!')

    else:
        MessageError('Errado!')

       

    


window.close()
