import sqlite3
lista_categoria=dict()
lista_categoria = {'salud':['medicamento', 'infraestructura salud','servicios','insumos'],'supermercado':['precios en supermercados'],'educacion':['infraestructura educacion','costo educacion'],'vivienda':['vivienda y salario','articulos para el hogar','gastos de vivienda'],'otros':['ropa y calazado','ocio y deportes','recreacion y cultura'],'transporte':['transporte y servicio','medios de transporte'],'restaurant y hoteles':['precio restaurant','precio hoteles']}
conn = sqlite3.connect('../db.sqlite3')
c = conn.cursor()


for categorias in lista_categoria:
    c.execute('''INSERT INTO  basedatos_categoria VALUES(?,?)''', (None, categorias))
    id= c.lastrowid
    subcategoria=lista_categoria[categorias]
    for sub in subcategoria:
        c.execute('''INSERT INTO  basedatos_subcategoria VALUES(?,?,?)''', (None,id ,sub))
        print(id)


conn.commit()
conn.close()
