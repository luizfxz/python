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
              

def janela_login():
        layout = [

                sg.theme('Tema')
                [sg.Text('Login: ', font='Arial 11'), sg.Input(key='login', font='Arial 11', size=(20, 1))],

                [sg.Text('Senha:',justification='center', font='Arial 11'), sg.Input(key='senha', password_char=' ', size=(45, 1))],

                [sg.Button('Entrar')]
        ]

        return sg.Window('Login', Layout=layout)