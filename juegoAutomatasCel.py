import turtle

def dibujarTriangulo(puntos, color, miTortuga):
    """
    Dibuja un triángulo con los puntos dados y lo rellena con el color especificado.
    
    :param puntos: Lista de tres puntos (x, y) que definen el triángulo.
    :param color: Color de relleno del triángulo.
    :param miTortuga: Objeto turtle que dibuja el triángulo.
    """
    miTortuga.fillcolor(color)
    miTortuga.up()
    miTortuga.goto(puntos[0])    
    miTortuga.down()
    miTortuga.begin_fill()
    '''
    ESTRUCTURA ORIGINAL
    miTortuga.goto(puntos[1][0], puntos[1][1])
    miTortuga.goto(puntos[2][0], puntos[2][1])
    miTortuga.goto(puntos[0][0], puntos[0][1])
    miTortuga.end_fill()
    '''
    #ESTRUCTURA SIMPLICADA
    for punto in puntos[1:]:
        miTortuga.goto(punto)
    miTortuga.goto(puntos[0])
    miTortuga.end_fill()

def obtenerMitad(p1, p2):
    """
    Calcula el punto medio entre dos puntos.
    
    :param p1: Primer punto (x, y).
    :param p2: Segundo punto (x, y).
    :return: Punto medio (x, y).
    """
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(puntos, grado, miTortuga):
    """
    Dibuja el triángulo de Sierpinski de un grado específico.
    
    :param puntos: Lista de tres puntos (x, y) que definen el triángulo inicial.
    :param grado: Grado de recursión para el triángulo de Sierpinski.
    :param miTortuga: Objeto turtle que dibuja los triángulos.
    """
    # Cambio de colores
    colormap = ['#7700FF', '#CC00FF', '#E68AFF', '#FFFFFF']
    dibujarTriangulo(puntos, colormap[grado], miTortuga)
    if grado > 0:
        '''
        METODO ORIGINAL
        sierpinski([puntos[0],
                    obtenerMitad(puntos[0], puntos[1]),
                    obtenerMitad(puntos[0], puntos[2])],
                   grado - 1, miTortuga)
        sierpinski([puntos[1],
                    obtenerMitad(puntos[0], puntos[1]),
                    obtenerMitad(puntos[1], puntos[2])],
                   grado - 1, miTortuga)
        sierpinski([puntos[2],
                    obtenerMitad(puntos[2], puntos[1]),
                    obtenerMitad(puntos[0], puntos[2])],
                   grado - 1, miTortuga)
        ''' 
        #METODO MODIFICADO
        sub_puntos = [
            [puntos[0], obtenerMitad(puntos[0], puntos[1]), obtenerMitad(puntos[0], puntos[2])],
            [puntos[1], obtenerMitad(puntos[0], puntos[1]), obtenerMitad(puntos[1], puntos[2])],
            [puntos[2], obtenerMitad(puntos[2], puntos[1]), obtenerMitad(puntos[0], puntos[2])]
        ]
        
        for sub_punto in sub_puntos:
            sierpinski(sub_punto, grado - 1, miTortuga)
def main():
    """
    Función principal que inicializa la ventana y la tortuga, y dibuja el triángulo de Sierpinski.
    """
    miTortuga = turtle.Turtle()
    miVentana = turtle.Screen()
    misPuntos = [[-200, -100], [0, 200], [200, -100]]  # Incrementar dimensiones
    sierpinski(misPuntos, 3, miTortuga)
    miVentana.exitonclick()

main()
