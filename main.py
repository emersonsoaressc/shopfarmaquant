import pandas as pd
from bs4 import BeautifulSoup
import requests
from tqdm import tqdm
from time import sleep

def extrai_dados_preco_popular(ean):
    url_cliquefarma = f'https://www.cliquefarma.com.br/preco/site/farmacia-preco-popular/{ean}'
    headers = {'user-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
    site = requests.get(url_cliquefarma, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    link_interno_cliquefarma = soup.find('a', class_='link-oferta')['href']
    site_interno_cliquefarma = requests.get(link_interno_cliquefarma, headers=headers)
    soup_interno_cliquefarma = BeautifulSoup(site_interno_cliquefarma.content, 'html.parser')
    link = soup_interno_cliquefarma.find('a', class_='inline-block')['href']
    link_final_preco_popular = link.split('?idsku')[0]
    site_precopopular = requests.get(link_final_preco_popular, headers=headers)
    soup_site_precopopular = BeautifulSoup(site_precopopular.content, 'html.parser')
    name_pp = soup_site_precopopular.find('h1', class_='product-main__name').get_text()
    cod_preco_popular = soup_site_precopopular.find('div', class_='productReference').get_text()
    preco_preco_popular = soup_site_precopopular.find('strong', class_='skuBestPrice').get_text()
    preco_preco_popular = float(preco_preco_popular.split('R$')[1].replace(',', '.'))
    lst_preco_popular = [name_pp, link_final_preco_popular, cod_preco_popular, preco_preco_popular]
    return lst_preco_popular

def extrai_dados_saojoao(ean):
    url_principal = f'https://www.saojoaofarmacias.com.br/{ean}'
    headers = {'user-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
    site = requests.get(url_principal, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    link_interno_saojoao = "https://www.saojoaofarmacias.com.br" + f"{soup.find('a', class_='vtex-product-summary-2-x-clearLink vtex-product-summary-2-x-clearLink--vitrine h-100 flex flex-column')['href']}"
    site_saojoao = requests.get(link_interno_saojoao, headers=headers)
    soup_site_saojoao = BeautifulSoup(site_saojoao.content, 'html.parser')
    cod_saojoao = ''
    preco_saojoao = soup_site_saojoao.find('span', class_='sjdigital-custom-apps-0-x-currencyContainer').get_text()
    preco_saojoao = float(preco_saojoao.replace('R$','').replace('.','').replace(',','.'))
    lst_saojoao = [link_interno_saojoao, cod_saojoao, preco_saojoao]
    return lst_saojoao

def extrai_dados_raia(ean):
    url_cliquefarma = f'https://www.cliquefarma.com.br/preco/site/drogaraia/{ean}'
    headers = {'user-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
    site = requests.get(url_cliquefarma, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    link_interno_cliquefarma = soup.find('a', class_='link-oferta')['href']
    site_interno_cliquefarma = requests.get(link_interno_cliquefarma, headers=headers)
    soup_interno_cliquefarma = BeautifulSoup(site_interno_cliquefarma.content, 'html.parser')
    link = soup_interno_cliquefarma.find('a', class_='inline-block')['href']
    link_final_raia = f"{'https://drogaraia.com.br/' + link.split('.br%2F')[1].split('%3')[0]}"
    site_raia = requests.get(link_final_raia, headers=headers)
    soup_site_raia = BeautifulSoup(site_raia.content, 'html.parser')
    cod_raia = soup_site_raia.find('span', class_='RaiaProductDescriptionstyles__Data-sc-1ijezxr-8').get_text()
    preco_raia = soup_site_raia.find('span', class_='ProductPricestyles__Price-i0kwh2-4').get_text()
    preco_raia = float(preco_raia.split('R$ ')[1].replace(',', '.'))
    lst_raia = [link_final_raia, cod_raia, preco_raia]
    return lst_raia

def extrai_dados_paguemenos(ean):
    url_principal = f'https://www.paguemenos.com.br/{ean}'
    headers = {'user-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
    site = requests.get(url_principal, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    link_interno_paguemenos = "https://www.paguemenos.com.br" + f"{soup.find('a', class_='vtex-product-summary-2-x-clearLink')['href']}"
    site_paguemenos = requests.get(link_interno_paguemenos, headers=headers)
    soup_site_paguemenos = BeautifulSoup(site_paguemenos.content, 'html.parser')
    cod_paguemenos = soup_site_paguemenos.find('div', class_='pr0')
    cod_paguemenos = cod_paguemenos.find('p').get_text()
    cod_paguemenos = cod_paguemenos.split(' ')[1]
    preco_paguemenos = soup_site_paguemenos.find('span', class_='vtex-store-components-3-x-sellingPrice vtex-store-components-3-x-sellingPriceValue t-heading-2-s dib ph2 vtex-store-components-3-x-price_sellingPrice').get_text()
    preco_paguemenos = float(preco_paguemenos.replace('R$','').replace('.','').replace(',','.'))
    lst_paguemenos = [link_interno_paguemenos, cod_paguemenos, preco_paguemenos]
    return lst_paguemenos