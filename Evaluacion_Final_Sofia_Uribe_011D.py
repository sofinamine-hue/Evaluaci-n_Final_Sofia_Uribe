#Diccionario juegos
juegos = {
'G001': ['Eclipse Runner', 'PC', 'accion', 'T', True, 'NovaStudio'],
'G002': ['Puzzle Atlas', 'Switch', 'puzzle', 'E', False, 'BrightWorks'],
'G003': ['Sky Legends', 'PS5', 'aventura', 'T', True, 'OrionGames'],
'G004': ['Racing Pulse', 'PC', 'carreras', 'E', True, 'VelocityLab'],
'G005': ['Mystic Farm', 'Switch', 'simulacion', 'E', False, 'GreenSeed'],
'G006': ['Shadow Tactics', 'Xbox', 'estrategia', 'M', False, 'IronGate']
}

#Diccionario inventario
inventario = {
'G001': [9990, 7],
'G002': [19990, 0],
'G003': [42990, 3],
'G004': [14990, 5],
'G005': [17990, 9],
'G006': [39990, 2],
}

#La mayoria de las funciones no tienen como parametro los diccionarios ya que el ejercicio no pedia que los tuvieran

#Validaciones---------------------------------------------
def codigo_val(codigo):
    #En esta validacion solo valido si no se dejo en blanco, no valido si el codigo ya es parte de un diccionario, ya que el ejercicio pide que esa validacion
    #se haga adentro de la función agregar_juego
    if codigo.strip() != "":
        return True
    else:
        return False
    
def titulo_val(titulo):
    if titulo.strip() != "":
        return True
    else:
        return False
    
def plataforma_val(plataforma):
    if plataforma.strip() != "":
        return True
    else:
        return False
    
def genero_val(genero):
    if genero.strip() != "":
        return True
    else:
        return False
    
def clasificacion_val(clasificacion):
    if clasificacion == "E" or clasificacion == "T" or clasificacion == "M":
        return True
    else:
        return False
    
def multiplayer_val(multiplayer):

    if multiplayer == "s":
        return True
    else:
        return False
    
def editor_val(editor):
    if editor.strip() != "":
        return True
    else:
        return False
    
def precio_val(precio):
    if precio > 0:
        return True
    else:
        return False
    
def stock_val(stock):
    if stock >= 0:
        return True
    else:
        return False
#---------------------------------------------------------
def menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Stock por plataforma")
    print("2. Búsqueda de juegos por rango de precio")
    print("3. Actualizar precio de juego")
    print("4. Agregar juego")
    print("5. Eliminar juego")
    print("6. Salir")
    print("=====================================")

def elegir_opcion():
    opcion = input("Ingrese una opcion: ")
    if opcion in ["1","2","3","4","5","6"]:
        return opcion
    else:
        print("Debe seleccionar una opción válida")

def stock_plataforma(plataforma):
    cantidad_disponible = 0
    for id in juegos:
        if juegos[id][1].lower() == plataforma.lower():
            cantidad_disponible += inventario[id][1]

    if cantidad_disponible > 0:
        print(f"Cantidad disponibles de juegos en la platafora {plataforma}: {cantidad_disponible}")
    else:
        print("No hay juegos para esa plataforma")

def busqueda_precio(p_min,p_max):

    juegos_rango = []
    for id in inventario:
        if p_min <= inventario[id][0] <= p_max and inventario[id][1] >= 0:
            juegos_rango.append(
                f"{juegos[id][0]}--{id}"
            )

    if len(juegos_rango) > 0:
        juegos_rango_ordenado = sorted(juegos_rango)
        print(f"Juegos dentro del rango de precio: {juegos_rango_ordenado}")
    else:
        print("No hay juegos en ese rango de precios.")

def actualizar_precio(codigo,nuevo_precio):
    for id in inventario:
        if id == codigo:
            inventario[codigo][0] = nuevo_precio
            return True
        
    return False

def agregar_juego(codigo,titulo,plataforma,genero,clasificacion,m,editor,precio,stock,juegos,inventario):
    for id in juegos:
        if id == codigo:
            return False
        
    juegos[codigo] = [
        titulo,plataforma,genero,clasificacion,m,editor
    ]

    inventario[codigo] = [
        precio,stock
    ]
    return True

def eliminar_juego(codigo,juegos,inventario):
    for id in juegos:
        if id == codigo:
            del juegos[codigo]
            del inventario[codigo]
            return True
    return False
    
#-----------------------MAIN-----------------------
while True:

    menu()
    opcion = elegir_opcion()

    match opcion:
        case "1": #Stock por plataforma
            plataforma = input("Ingrese nombre de alguna plataforma: ")
            stock_plataforma(plataforma)

        case "2": #Busqueda de juegos por rango de precio
            while True:
                try:

                    p_min = int(input("Ingrese precio mínimo: "))
                    if p_min >= 0:
                        p_max = int(input("Ingrese precio máximo: "))
                        if p_max >= p_min:
                            busqueda_precio(p_min,p_max)
                            break

                #ERRORES------------------------------------------------
                        else:
                            print("Debe ingresar un número positivo")
                    else:
                        print("Debe ingresar un número positivo")
                except ValueError:
                    print("Debe ingresar valores enteros")
                #-------------------------------------------------------

        case "3": #Actualizar precio de juego
            desicion = "s"
            while desicion == "s":

                codigo = input("Ingrese código del producto que desea cambiar el precio: ").upper()

                try:
                    nuevo_precio = int(input("Ingrese nuevo precio: "))

                    if nuevo_precio >= 1:
                        print("Debe ingresar un valor mayor a 0")

                        proceso = actualizar_precio(codigo,nuevo_precio)
                        if proceso:
                            print("Precio actualizado")
                        else:
                            print("El código no existe")

                    else:
                        print("Debe ingresar un valor mayor a 0")
                except ValueError:
                    print("Debe ingresar un valor entero")

                

                desicion = input("¿Desea actualizar otro precio (s/n)?: ").lower()

        case "4": #Agregar juego
            #En toda esta opcion hice que se verificara altiro si era true o false la validación para que asi tirara error altiro y no te dejara ingresar mas datos cuando en una de esas ya habias escrito
            #algo mal en el inicio
            codigo = input("ingrese codigo: ").upper()
            c = codigo_val(codigo)
            if c:

                titulo = input("ingrese titulo: ")
                t = titulo_val(titulo)
                if t:
                    plataforma = input("ingrese plataforma: ")
                    p = plataforma_val(plataforma)
                    if p:

                        genero = input("ingrese género: ")
                        g = genero_val(genero)
                        if g:

                            clasificacion = input("ingrese clasificación (E/T/M): ").upper()
                            cl = clasificacion_val(clasificacion)
                            if cl:

                                multiplayer = input("ingrese si es multiplayer (s/n): ").lower()
                                m = multiplayer_val(multiplayer)
                                #Aqui se valida como multiplayer es igual a "s" o "n" ya que si pusiera que valida si "m" es true o false, lo va tomar como false en el caso de "n".
                                if multiplayer == "s" or multiplayer == "n":

                                    editor = input("ingrese editor: ")
                                    e = editor_val(editor)
                                    if e:

                                        try:
                                            precio = int(input("ingrese precio: "))
                                            pr = precio_val(precio)
                                            if pr:

                                                stock = int(input("ingrese stock: "))
                                                s = stock_val(stock)
                                                if s:
                                                    #Tuve que agregar como parametros el diccionario juegos y inventario, ya que se van a modificar
                                                    proceso = agregar_juego(codigo,titulo,plataforma,genero,clasificacion,m,editor,precio,stock,juegos,inventario)
                                                    if proceso:
                                                        print("Juego agregado")

            #ERRORES------------------------------------------------------------------------------------
                                                    else:
                                                        print("El código ya existe")
                                                else:
                                                    print("El stock debe ser mayor o igual a 0")
                                            else:
                                                print("El precio debe ser mayor a 0")
                                        except ValueError:
                                            print("Debe ingresar valores enteros")
                                    else:
                                        print("El campo quedo vacío")
                                else:
                                    print("Debe ingresar 's' o 'n'")
                            else:
                                print("Debe ingresar 'E' o 'T' o 'M'")
                        else:
                            print("El campo quedo vacío")
                    else:
                        print("El campo quedo vacío")
                else:
                    print("El campo quedo vacío")
            else:
                print("El campo quedo vacío")
            #--------------------------------------------------------------------------------------------
        
        case "5": #Eliminar juego
            codigo = input("Ingrese código que desea eliminar: ").upper()

            #Le agrege como parametro juegos e invetario ya que los va a modificar
            proceso = eliminar_juego(codigo,juegos,inventario)
            if proceso:
                print("Juego eliminado")
            else:
                print("El código no existe")

        case "6": #Salir
            print("Programa finalizado")
            break
