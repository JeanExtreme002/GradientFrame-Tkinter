
from tkinter import Canvas

class GradientFrame(Canvas):
    """
    Classe para criar um frame com cores em degradê
    """

    __tag = "GradientFrame"

    hex_format = "#%04x%04x%04x"
    top2bottom = 1
    left2right = 2


    def __init__(self,parent,geometry,colors=("red","black"),direction=left2right,**kw):
        
        #Invoca o método construtor do Canvas
        Canvas.__init__(self,parent,width=geometry[0],height=geometry[1],**kw)

        #Instância os parâmetros
        self.__geometry = geometry
        self.__colors = colors
        self.__direction = direction

        #Desenha um degradê no canvas
        self.__drawGradient()

        
    def __drawGradient(self):
        
        """
        Método para pintar o canvas com cores em degradê
        """

        #Deleta o degradê do canvas, caso exista
        self.delete(self.__tag)

        #Recebe o limite de largura
        limit = self.__geometry[0] if self.__direction == self.left2right else self.__geometry[1]
       
        #Recebe os valores RGB das cores
        red1,green1,blue1 = self.winfo_rgb(self.__colors[0])
        red2,green2,blue2 = self.winfo_rgb(self.__colors[1])

        #Calcula os valores RGB de acréscimo de cores (Ex: while red1 != red2: red1 += r_ratio ) 
        #dividindo o mesmo pelo limite de largura.
        r_ratio = float(red2 - red1) / limit
        g_ratio = float(green2 - green1) / limit
        b_ratio = float(blue2 - blue1) / limit

        for pixel in range(limit):
            
            #Calcula a cor em formato RGB
            red = int( red1 + ( r_ratio * pixel ) )
            green = int( green1 + ( g_ratio * pixel ) )
            blue = int( blue1 + ( b_ratio * pixel ) )

            #Transforma a cor de RGB em Hex
            color = self.hex_format % (red,green,blue)

            #Define a posição (x1,y1,x2,y2) no objeto
            x1 = pixel if self.__direction == self.left2right else 0
            y1 = 0 if self.__direction == self.left2right else pixel
            x2 = pixel if self.__direction == self.left2right else self.__geometry[0]
            y2 = self.__geometry[1] if self.__direction == self.left2right else pixel

            #Cria o retângulo no canvas
            self.create_line(x1,y1,x2,y2 , tag=self.__tag , fill=color)


    def setColors(self,colors):
        """
        Método para definir as cores que serão usadas no degradê
        """

        self.__colors = colors
        self.__drawGradient()


    def setDirection(self,direction):
        """
        Método para definir a direção do degradê
        """

        if direction in (self.left2right,self.top2bottom):
            self.__direction = direction
            self.__drawGradient()
        else:
            raise ValueError('The "direction" parameter must be self.left2right or self.top2bottom')
        

    def setGeometry(self,geometry):
        """
        Método para definir as dimensões do frame
        """

        self.config(width=geometry[0],height=geometry[1])
        self.__geometry = geometry
        self.__drawGradient()
 

