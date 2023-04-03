import pandas as pd
from tqdm import tqdm
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import shutil
options = webdriver.ChromeOptions()
options.add_argument("--headless")

from password import passwordTrier
login_trier = passwordTrier()[0]
password_trier = passwordTrier()[1]




# Função para extrair ean codigo shopfarma:
def extractEanCodShopfarma(nome_relatorio, tipo_relatorio, cod_grupo=None, categoria=None, laboratorio=None, excluir_categoria=False, excluir_laboratorio=False):
    if tipo_relatorio == 'cadastro':
        driver = webdriver.Chrome()
        driver.implicitly_wait(30)
        driver.get("http://189.27.220.204:4647/sgfpod1/Rel_0087.pod?cacheId=1676047264063")
        sleep(1)
        driver.find_element(By.NAME, 'id_cod_usuario').send_keys(login_trier)
        sleep(1)
        driver.find_element(By.NAME, 'nom_senha').send_keys(password_trier)
        sleep(1)
        driver.find_element(By.NAME, 'login').click()
        sleep(1)
        if cod_grupo != None:
            driver.find_element(By.NAME, 'cod_grupoEntrada').send_keys(cod_grupo)
            driver.find_element(By.NAME, 'cod_grupoEntrada').send_keys(Keys.RETURN)
            sleep(1)
        if categoria != None:
            driver.find_element(By.NAME, 'cod_categoriaEntrada').send_keys(categoria)
            driver.find_element(By.NAME, 'cod_categoriaEntrada').send_keys(Keys.RETURN)
            sleep(1)
        if laboratorio != None:
            driver.find_element(By.NAME, 'cod_laboratEntrada').send_keys(laboratorio)
            driver.find_element(By.NAME, 'cod_laboratEntrada').send_keys(Keys.RETURN)
            sleep(1) 
        if excluir_categoria == True:
            driver.find_element(By.ID, 'consid_categ_1').click()  
            sleep(1)
        if excluir_laboratorio == True:
            driver.find_element(By.ID, 'consid_labor_1').click()   
            sleep(1)         
        driver.find_element(By.LINK_TEXT, 'Dados III').click()
        sleep(1)
        driver.find_element(By.ID, 'tipo_rel_0').click()
        sleep(1)
        driver.find_element(By.ID, 'saida_4').click()
        sleep(1)
        driver.find_element(By.NAME, 'runReport').click()
        sleep(15)
        caminho = 'C:/Users/Samsung/Downloads'
        lista_datas = []
        for file in os.listdir(caminho):
            if file.endswith(".xls"):
                data = os.path.getmtime(f"{caminho}/{file}")
                lista_datas.append((data, file))
        lista_datas.sort(reverse=True)
        ultimo_arquivo = lista_datas[0][1]
        shutil.move(f'{caminho}/{ultimo_arquivo}', f'{nome_relatorio}_dados_cadastro.xls')
        driver.close()
    if tipo_relatorio == 'valores':
        driver = webdriver.Chrome()
        driver.implicitly_wait(15)
        driver.get("http://189.27.220.204:4647/sgfpod1/Rel_0087.pod?cacheId=1676047264063")
        sleep(1)
        driver.find_element(By.NAME, 'id_cod_usuario').send_keys(login_trier)
        sleep(1)
        driver.find_element(By.NAME, 'nom_senha').send_keys(password_trier)
        sleep(1)
        driver.find_element(By.NAME, 'login').click()
        sleep(1)
        if cod_grupo != None:
            driver.find_element(By.NAME, 'cod_grupoEntrada').send_keys(cod_grupo)
            driver.find_element(By.NAME, 'cod_grupoEntrada').send_keys(Keys.RETURN)
            sleep(1)
        if categoria != None:
            driver.find_element(By.NAME, 'cod_categoriaEntrada').send_keys(categoria)
            driver.find_element(By.NAME, 'cod_categoriaEntrada').send_keys(Keys.RETURN)
            sleep(1)
        if laboratorio != None:
            driver.find_element(By.NAME, 'cod_laboratEntrada').send_keys(laboratorio)
            driver.find_element(By.NAME, 'cod_laboratEntrada').send_keys(Keys.RETURN)
            sleep(1)
        if excluir_categoria == True:
            driver.find_element(By.ID, 'consid_categ_1').click()  
            sleep(1)
        if excluir_laboratorio == True:
            driver.find_element(By.ID, 'consid_labor_1').click()   
            sleep(1)   
        driver.find_element(By.LINK_TEXT, 'Dados III').click()
        sleep(1)
        driver.find_element(By.ID, 'tipo_rel_1').click()
        sleep(1)
        driver.find_element(By.ID, 'saida_4').click()
        sleep(1)
        driver.find_element(By.NAME, 'runReport').click()
        sleep(15)
        caminho = 'C:/Users/Samsung/Downloads'
        lista_datas = []
        for file in os.listdir(caminho):
            if file.endswith(".xls"):
                data = os.path.getmtime(f"{caminho}/{file}")
                lista_datas.append((data, file))
        lista_datas.sort(reverse=True)
        ultimo_arquivo = lista_datas[0][1]
        shutil.move(f'{caminho}/{ultimo_arquivo}', f'{nome_relatorio}_dados_valores.xls')
        driver.close()
        

# Função para encontrar código do produto na Preço Popular
def incluirPreco_PP(dataframe, desconto_medio=0.23):
    lst_preco = []
    lst_error = []
    lst_no_pmc = []
    for index, row in tqdm(dataframe.iterrows()):
        try:
            ean = int(row["ean"])
            driver = webdriver.Chrome(options=options)
            driver.get(f"https://www.precopopular.com.br/{ean}")
            sleep(1)
            preco_pp = driver.find_element(By.CLASS_NAME, 'product-item__best-price')
            preco_pp = preco_pp.text
            preco_pp = float(preco_pp.split('R$ ')[1].replace(',', '.'))
            product = ean, preco_pp
            lst_preco.append(product)
            dif_pp_shopfarma = round((row["preco_venda"]/preco_pp-1)*100, 2)
            print(f'Produto {row["produto"]} {ean} encontrado com sucesso! O preço na preço popular é R$ {preco_pp} e na Shopfarma é R$ {row["preco_venda"]}, uma diferença percentual de {dif_pp_shopfarma}%')
        except:
            ean = int(row["ean"])
            driver = webdriver.Chrome()
            driver.get(f"http://179.187.94.169:4647/sgfpod1/Cad_0020.pod?cacheId=1676047264063")
            sleep(1)
            driver.find_element(By.NAME, 'id_cod_usuario').send_keys(login_trier)
            sleep(1)
            driver.find_element(By.NAME, 'nom_senha').send_keys(password_trier)
            sleep(1)
            driver.find_element(By.NAME, 'login').click()
            sleep(1)
            driver.find_element(By.NAME, 'cod_redbarraEntrada').clear()
            driver.find_element(By.NAME, 'cod_redbarraEntrada').send_keys(ean)
            driver.find_element(By.NAME, 'cod_redbarraEntrada').send_keys(Keys.RETURN)
            sleep(1)
            driver.find_element(By.LINK_TEXT, 'Preço').click()
            sleep(1)
            try:
                valor_pmc = driver.find_element(By.NAME, 'vlr_pmc').get_attribute('value')
                valor_pmc = float(valor_pmc.replace(',','.'))
                preco_erro = valor_pmc - (int(row["preco_venda"]) * desconto_medio)
                product = ean, preco_erro
                lst_preco.append(product)
            except:
                no_pmc = ean
                lst_no_pmc.append(no_pmc)
                print(f'O código {ean} não possui pmc cadastrado no sistema!')
            #print(f'O código {ean} está com problemas! O preço foi alterado para {preco_erro}')
            lst_error.append(ean)
        driver.close()
    return lst_preco, lst_error, lst_no_pmc

# Funçao para importar o arquivo XLS
def GeraDataframe(arquivoXLS, tipo_relatorio):
    if tipo_relatorio == 'cadastro':
        data = pd.read_excel(arquivoXLS, header=13, usecols='C,D,F,K')
        df = data.rename({'Reduz. ':'codshopfarma', 'Unnamed: 3': 'produto', 'Unnamed: 5': 'laboratorio' ,'Unnamed: 10':'ean'}, axis=1)
        df.dropna(inplace=True)
        return df
    if tipo_relatorio == 'valores':
        data = pd.read_excel(arquivoXLS, header=13, usecols='C,D,P,Y')
        df = data.rename({'Reduz.  ':'codshopfarma',' Descrição Produto':'produto','Venda ':'preco_venda','Unnamed: 24':'preco_compra'}, axis=1)
        df.dropna(inplace=True)
        return df

# Funçao para importar o arquivo XLS
def importaxlsOBS(arquivoXLS):
    lista_pbm = pd.read_excel(arquivoXLS)
    lista_pbm = lista_pbm
    lista_pbm['DESC. PACIENTE'] = lista_pbm['DESC. PACIENTE'].replace('%','')*100
    lista_pbm = lista_pbm.fillna('')
    return lista_pbm

# Função para incluir observações de pbm na venda dos produtos
def incluirObsPBM(lista_cod, observacao=0):
    driver = webdriver.Chrome()
    driver.get("http://179.187.94.169:4647/sgfpod1/Cad_0020.pod?cacheId=1652232659788")
    sleep(1)
    driver.find_element_by_name('id_cod_usuario').send_keys(login_trier)
    sleep(1)
    driver.find_element_by_name('nom_senha').send_keys(passwordTrier())
    sleep(1)
    driver.find_element_by_name('login').click()
    sleep(3)
    for index, row in lista_cod.iterrows():
        try:
            codigo = row['EAN']
            pbm = row['PLATAFORMA']
            descpaciente = row['DESC. PACIENTE']
            programa = row['PROGRAMA']
            outrasobs = row['OBSERVAÇÃO DE DESCONTO ']
            obs1 = f'Este produto possui desconto do laboratório pelo programa {programa}. Favor efetuar a venda através da plataforma {pbm}! Desconto do paciente: {descpaciente}%. Outras observações: {outrasobs}'
            driver.find_element_by_name('cod_redbarraEntrada').send_keys(f'{codigo}')
            driver.find_element_by_name('cod_redbarraEntrada').send_keys(Keys.RETURN)
            sleep(1)
            driver.find_element_by_id('tabTabdhtmlgoodies_tabView1_1').click()
            sleep(1)
            driver.find_element_by_id('nom_obsvenda').clear()
            sleep(1)
            driver.find_element_by_id('nom_obsvenda').send_keys(f'{obs1}')
            sleep(1)
            driver.find_element_by_name('salvar').click()
            sleep(1)
            driver.refresh()
            print(f'O código {codigo} foi salvo com sucesso!')
            sleep(1)
        except:
            driver.get("http://http://179.187.94.169:4647/sgfpod1/Cad_0020.pod?cacheId=1652232659788")
            print(f'O código {codigo} está com problemas!')