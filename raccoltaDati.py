from datetime import datetime, timezone
import openpyxl
import os


def datiGabor(N, dizionario):
    with open('values.txt', 'r') as f:
        lines = f.readlines()
    cognome = lines[0].split(':')[-1].strip()


    data = datetime.today().strftime('%d-%m-%Y')
    filename = cognome + str(data)+'.xlsx'
    orario = str(datetime.today().strftime('%H-%M-%S'))

    if os.path.isfile(filename):
        wb = openpyxl.load_workbook(filename)
    else:
        wb = openpyxl.Workbook()
        # Rimuovi il foglio predefinito "sheet"
        default_sheet = wb['Sheet']
        wb.remove(default_sheet)


    wb.create_sheet(orario)
    sh1 = wb[orario]
    start_char = "A"
    num_chars = N*2

    for i in range(num_chars):
        casella = start_char + str(i+2)
        sh1[casella].value = 'Quadrante N ' + str((i+1))
    sh1['B1'].value = "Giusti"
    sh1['C1'].value = "Sbagliati"
    for i in range(N*2):
        sh1['B'+ str(i+2)].value = dizionario['Q'+str(i+1)]['Giusti']
        sh1['C' + str(i + 2)].value = dizionario['Q' + str(i + 1)]['Sbagliati']

    try:
        sh1.column_dimensions['A'].auto_size = True
        sh1.column_dimensions['A'].width += 1
        wb.save(filename)
    except PermissionError:
        print('File might be opened, please close it before writing')



def creazioneDizionario(n):
    n=n*2
    dizionario = {}
    for i in range(n):
        dizionario['Q'+str(i+1)] = {'Giusti':0,'Sbagliati':0,'Non visti':0}
    return dizionario

dizionario =  creazioneDizionario(2)
datiGabor(2,dizionario)