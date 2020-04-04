import requests, zipfile, io, pathlib, re
import pandas as pd

to_dir = './lotofacil/'
arquivo = 'd_lotfac.htm'

class Extrai():
    
    def unzipa():
        link = requests.get("http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_lotfac.zip")
        #to_dir = './lotofacil/'
        current_dir = str(pathlib.Path().absolute()) + re.sub(r"[^lotofacil]+", "\\\\", to_dir)
        zip = zipfile.ZipFile(io.BytesIO(link.content))
        print('Extraindo arquivos agora...')
        zip.extractall(to_dir)
        print('Arquivos extraidos em: ', current_dir )
        
    def cria_df():
        fullpath = to_dir + arquivo
        dframe = pd.read_html(fullpath)[0]
        colunas = ['Concurso', 'Data Sorteio', 'Bola1', 'Bola2', 'Bola3', 'Bola4', 'Bola5',
       'Bola6', 'Bola7', 'Bola8', 'Bola9', 'Bola10', 'Bola11', 'Bola12',
       'Bola13', 'Bola14', 'Bola15']

        dframe=dframe.filter(colunas)
        dframe = dframe.drop_duplicates()
        dframe.reset_index(drop=True, inplace=True)
        return dframe

if __name__ == "__main__":
    Extrai.unzipa()
    df = Extrai.cria_df()
    df.head()