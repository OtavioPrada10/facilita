import PySimpleGUI as sg
import webbrowser

"""
Site de consulta cpf https://solucoes.receita.fazenda.gov.br/servicos/cnpjreva/cnpjreva_solicitacao.asp
"""

sg.theme('DarkBlue')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Facilitador de pesquisa de Contas', size = 10)],
            [sg.Text('dominio',         size = 10), sg.InputText()],
            [sg.Text('nome da empresa', size = 10), sg.InputText()],
            [sg.Text('CNPJ' ,           size = 10), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

window = sg.Window('Facilitador', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if(event == 'Ok'):
        sDominio = values[0]
        if(sDominio):
            if ('.br' in sDominio or '.BR' in sDominio):
                link = "https://registro.br/tecnologia/ferramentas/whois?search="+ sDominio
            else:
                sDominio = sDominio + ".br"
                link = "https://registro.br/tecnologia/ferramentas/whois?search="+ sDominio
            webbrowser.open(link)
        webbrowser.Chrome('teste pesquisa')
        # chromeNav.open('teste do nome da empresa')
        sNomeEmpesa = values[1]
        

window.close()