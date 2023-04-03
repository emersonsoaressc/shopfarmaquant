import pyrebase


firebaseConfig = {
    'apiKey': "AIzaSyD_-ZCVmTVY8v7aA327EK_N8lk-PR2oDDU",
    'authDomain': "shopfarma-quant.firebaseapp.com",
    'databaseURL': "https://shopfarma-quant-default-rtdb.firebaseio.com",
    'projectId': "shopfarma-quant",
    'storageBucket': "shopfarma-quant.appspot.com",
    'messagingSenderId': "584054373372",
    'appId': "1:584054373372:web:5f5503a9bafe559c9fd079",
    'measurementId': "G-5R8MWKL9NB"
    }

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

db = firebase.database()

product = {
    'name':'DORFLEX 36CP',
    'ean':'7891058017507',
    'shopfarma':{
        'codigo':'109136',
        'grupo':'3000',
        'preco':25.00,
        },
    'preco_popular':{
        'codigo':'729232',
        'preco':20.54,
        'link':'https://www.precopopular.com.br/dorflex-analgesico-e-relaxante-muscular-36-comprimidos/p'
        },
    'panvel':{
        'codigo':'468560',
        'preco':25.10,
        'link':'https://www.panvel.com/panvel/analgesico-dorflex-36-comprimidos/p-468560'
        },
    'raia':{
        'codigo':'6942',
        'preco':25.45,
        'link':'https://www.drogaraia.com.br/dorflex-analgesico-36-comprimidos.html'
        },
    'paguemenos':{
        'codigo':'47676',
        'preco':22.75,
        'link':'https://www.paguemenos.com.br/dorflex-analgesico-e-relaxante-muscular-36-comprimidos/p'
        },
    'saojoao':{
        'codigo':'47676',
        'preco':22.75,
        'link':'https://www.saojoaofarmacias.com.br/100016455/p'
        }
            }

db_products = db.child("products")
db_products.child(f"{product['ean']}").set(product)