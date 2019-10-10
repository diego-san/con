import random

class algoritmo:

    def inicio(data, monto, numero_produc):

        algoritmo.lista_random(data, numero_produc)



        pass

    def lista_random(data, n):
        cantidad = len(data)
        if cantidad > 0:
            list_elegido= []
            elegidos= []
            if cantidad != 1:
                for x in range(0, n):
                    numero_random = random.randint(0, cantidad-1)
                    try:
                        o = elegidos.index(numero_random)
                    except:
                        elegidos.append(numero_random)


            else:
                list_elegido.append({'producto': {'idbs': data[0]['idbs'],
                                                    'nombrebs': data[0]['nombrebs'],
                                                    'precio': data[0]['precio'],
                                                    'fuente': data[0]['fuente'],
                                                    'fechas': data[0]['fechas'],
                                                    'fechapub': data[0]['fechapub'],
                                                    'img':data[0]['img']}})

        return list_elegido

    #funcion que elije la cantidad de productos a mostrar
    def monto_dividir(monto):
        if int(monto) <= 1000:
            cantidad_produc = 1
        elif int(monto) > 1000 and int(monto) <= 10000:
            cantidad_produc = random.randint(1, 2)
        elif int(monto) > 10000 and int(monto) <= 100000:
            cantidad_produc = random.randint(1, 3)
        elif int(monto) > 100000 and int(monto) <= 1000000:
            cantidad_produc = random.randint(1, 4)
        else:
            cantidad_produc = random.randint(1, 5)

        return cantidad_produc