import modos


url = 'https://readthedocs.org/projects/python-guide/downloads/pdf/latest/'
try:
    modos.modo1(url, 'pdf/python-guide0.pdf')    #não cria diretório
except FileNotFoundError as e:
    print(f'{e}')

modos.modo2(url, 'pdf/python-guide1.pdf')

modos.modo3(url, 'downloads/python-guide.pdf')

modos.modo3('https://pastebin.com/raw/nuXMp5tm', 'downloads/clientesbanco.csv')

modos.modo3('https://pastebin.com/raw/nuXMp5tmx', 'downloads/clientesbanco.csv')