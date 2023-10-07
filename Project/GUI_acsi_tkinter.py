# Codigo App diabetica

from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import threading
import _thread
import datetime
import time
import os

class DiabeApp(Tk):
    def __init__(self):

        super().__init__()
        
        # Parámetros iniciales
        self.title('Diabepie')
        width  = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        
        # Size of original user 1536x864
        self.widthConst  = width/1536
        self.heightConst = height/864
        
        # Spanish
        self.lang = 1 
        self.geometry("%dx%d" % (width, height))
        self.configure(bg = 'LightCyan2')

        icono = PhotoImage(file = 'CherriElOtorongo.png')
        self.iconphoto(True, icono)

        # Imagen de la pantalla de título
        self.img_titulo   = PhotoImage(file = 'CherriElOtorongo.png')
        self.fondo_titulo = Label(self, image = self.img_titulo, bg = 'LightCyan2')
        self.fondo_titulo.place(x = round((width - 269)*self.widthConst), y = round((height - 269)*self.heightConst))

        # Título
        self.titulo = Label(self, text = 'DiabePie', font = ('Courier New', 80), fg = 'navy', justify = CENTER, bg = 'LightCyan2')
        self.titulo.place(x = round(200 * self.widthConst), y = round(200 * self.widthConst))

        # Botones iniciales
        self.inicio   = Button(self, text = 'Iniciar programa', command = self.IniciarProceso, font = ('Courier New', 20), activebackground='black', activeforeground='LightCyan2', bg='CadetBlue3',fg='navy', justify=CENTER, width=30)
        self.idioma   = Button(self, text = 'Seleccionar Idioma', command = self.idioma, font = ('Courier New', 20), activebackground='black', activeforeground='LightCyan2', bg='CadetBlue3',fg='navy', justify=CENTER, width=30)
        self.creditos = Button(self, text = 'Créditos', command = self.ir_a_menu, font = ('Courier New', 20), activebackground='black', activeforeground='LightCyan2', bg='CadetBlue3',fg='navy', justify=CENTER, width=30)
        self.exit     = Button(self, text = 'Salir', command = self.ByeBye, font = ('Courier New', 20), activebackground='black', activeforeground='LightCyan2', bg='CadetBlue3',fg='navy', justify=CENTER, width=30)

        self.inicio.place  (x = round(200 * self.widthConst), y = round(400 * self.heightConst))
        self.idioma.place  (x = round(200 * self.widthConst), y = round(480 * self.heightConst))
        self.creditos.place(x = round(200 * self.widthConst), y = round(560 * self.heightConst))
        self.exit.place    (x = round(200 * self.widthConst), y = round(640 * self.heightConst))

        # Label de la mascota
        self.cheri = Label(self, text = 'Cheri el otorongo diabético', font = ('Courier New', 20), fg = 'navy', justify = CENTER, bg = 'LightCyan2')
        self.cheri.place(x = round((width - 280) * self.widthConst), y = round((height - 280) * self.heightConst))

        # Botones de idioma
        self.selecIdiomaLbl = Label(self, text = 'Seleccione Idioma', font = ('Courier New', 80), fg = 'navy', justify = CENTER, bg = 'LightCyan2')

        self.spanish = Button(self, text = 'Español', command = self.spanish, font = ('Courier New', 20), activebackground='black', activeforeground='LightCyan2', bg='CadetBlue3',fg='navy', justify=CENTER, width=30)
        self.quechua = Button(self, text = 'Quechua', command = self.quechua, font = ('Courier New', 20), activebackground='black', activeforeground='LightCyan2', bg='CadetBlue3',fg='navy', justify=CENTER, width=30)
        self.aimara  = Button(self, text = 'Aimara', command = self.aimara, font = ('Courier New', 20), activebackground='black', activeforeground='LightCyan2', bg='CadetBlue3',fg='navy', justify=CENTER, width=30)
        self.english = Button(self, text = 'English', command = self.english, font = ('Courier New', 20), activebackground='black', activeforeground='LightCyan2', bg='CadetBlue3',fg='navy', justify=CENTER, width=30)


        # Selección de imagen
        self.selecI = Label(self, text = 'Seleccione la imagen a procesar', font = ('Courier New', 40), fg = 'navy', bg = 'LightCyan2')

        # Botón para abrir archivo
        self.pieI = Button(self, text = 'Pie izquierdo', command = lambda:self.abrirImg(1), font = ('Courier New', 20), activebackground='black', activeforeground='LightCyan2', bg='CadetBlue3',fg='navy', justify=CENTER, width=15)
        self.pieD = Button(self, text = 'Pie derecho', command   = lambda:self.abrirImg(2), font = ('Courier New', 20), activebackground='black', activeforeground='LightCyan2', bg='CadetBlue3',fg='navy', justify=CENTER, width=15)

        # Mostrar la imagen
        self.imgPieI = Label(self)
        self.imgPieD = Label(self)
        
        # Error
        self.error = Label(self, text = '', fg = 'navy', font = ('Coruier New', 30))

        # Procesar la imagen
        self.proceso = Button(self, text = 'Procesar Imagen ->', command = self.procesar, font = ('Courier New', 15), activebackground='black', activeforeground='LightCyan2', bg='CadetBlue3',fg='navy', justify=CENTER, width=30)

        # Volver a inicio
        self.fin = Button(self, text = 'Finalizar', command = self.byeANDmenu, font = ('Courier New', 15), activebackground='black', activeforeground='LightCyan2', bg='CadetBlue3',fg='navy', justify=CENTER, width=30)

        # Activar alarma
        self.TrigAlarm = Button(self, text = 'Activar alarma', command = self.alarma, font = ('Courier New', 15), activebackground='black', activeforeground='LightCyan2', bg='CadetBlue3',fg='navy', justify=CENTER, width=30)
        self.alarm     = Label(self, text = 'Alerta. Úlceras detectadas', fg = 'navy', font = ('Coruier New', 30))

        
        # Imagenes
        self.imagesList   = [(None, None), (None, None), (None, None), (None, None)]

        self.ExitoFallo     = Label(self, text = 'Imagen guardada con éxito', fg = 'navy', font = ('Coruier New', 20))
        
        # Cargando
        self.cargando_gif = []
        
        i = 0
        while 1:
            try:
                image = PhotoImage(file = 'cargando.gif', format = "gif -index " + str(i))            
                self.cargando_gif.append(image)
                i = i + 1
            except:
                break

        # Guardar en escritorio
        self.guardar = Button(self, text = 'Guardar Imagen', command = self.save, font = ('Courier New', 15), activebackground='black', activeforeground='LightCyan2', bg='CadetBlue3',fg='navy', justify=CENTER, width=30)
        
        self.totalFrames = i - 1
        self.delay = 0.1
        self.cargando = Label(self, image = self.cargando_gif[0])
        
    def IniciarProceso(self):
        self.inicio.place_forget()
        self.titulo.place_forget()
        self.idioma.place_forget()
        self.fondo_titulo.place_forget()
        self.creditos.place_forget()
        self.cheri.place_forget()

        self.selecI.place(x = round(200 * self.widthConst), y = round(100 * self.heightConst))
        self.pieI.place(  x = round(200 * self.widthConst), y = round(200 * self.heightConst))
        self.pieD.place(  x = round(1000* self.widthConst), y = round(200 * self.heightConst))

    def idioma(self):
        self.inicio.place_forget()
        self.titulo.place_forget()
        self.idioma.place_forget()
        self.fondo_titulo.place_forget()
        self.creditos.place_forget()
        self.cheri.place_forget()

        self.selecIdiomaLbl.place(x = round(200 * self.widthConst), y = round(200 * self.heightConst))
        self.spanish.place(       x = round(200 * self.widthConst), y = round(400 * self.heightConst))
        self.quechua.place(       x = round(200 * self.widthConst), y = round(480 * self.heightConst))
        self.aimara.place(        x = round(200 * self.widthConst), y = round(560 * self.heightConst))
        self.english.place(       x = round(200 * self.widthConst), y = round(640 * self.heightConst))

    def spanish(self):
        # Translation
        self.lang = 1

        self.inicio.config(        text = 'Iniciar programa')
        self.idioma.config(        text = 'Seleccionar Idioma')
        self.creditos.config(      text = 'Créditos')
        self.cheri.config(         text = 'Cheri el otorongo diabético')
        self.selecIdiomaLbl.config(text = 'Seleccione Idioma')
        self.selecI.config(        text = 'Seleccione la imagen a procesar')
        self.pieI.config(          text = 'Pie Izquierdo')
        self.pieD.config(          text = 'Pie Derecho')
        self.proceso.config(       text = 'Procesar Imagen ->')
        self.fin.config(           text = 'Finalizar')
        self.guardar.config(       text = 'Guardar Imagen')
        self.exit.config(          text = 'Cerrar')
        # Bye Bye and back to main menu
        self.byeANDmenu()

    def english(self):
        self.lang = 2

        self.inicio.config(        text = 'Start program')
        self.idioma.config(        text = 'Select language')
        self.creditos.config(      text = 'Credits')
        self.cheri.config(         text = 'Cheri the diabetic jaguar')
        self.selecIdiomaLbl.config(text = 'Select language')
        self.selecI.config(        text = 'Select image to process')
        self.pieI.config(          text = 'Left Foot')
        self.pieD.config(          text = 'Right Foot')
        self.proceso.config(       text = 'Process Image ->')
        self.fin.config(           text = 'End')
        self.guardar.config(       text = 'Save image')
        self.exit.config(          text = 'Close')        
        self.byeANDmenu()

    def quechua(self):
        self.lang = 3

        self.inicio.config(text         = 'Qallariy')
        self.idioma.config(text         = 'Simita akllay')
        self.creditos.config(text       = 'Créditos nisqakuna')
        self.cheri.config(text          = 'Cheri chay otorongo diabeteswan')
        self.selecIdiomaLbl.config(text = 'Simita akllay')
        self.selecI.config(text         = 'Imahinata akllay ruwanapaq')
        self.pieI.config(text           = 'Lloq’e chaki')
        self.pieD.config(text           = 'Paña chaki')
        self.proceso.config(text        = 'Proceso nisqa siq’i ->')
        self.fin.config(text            = 'Tukuy')
        self.guardar.config(text        = 'Waqaychay Siqi')
        self.exit.config(          text = 'Wisq ay')
        self.byeANDmenu()

    def aimara(self):
        self.lang = 4

        self.inicio.config(text         = 'Qalltaña')
        self.idioma.config(text         = 'Aru ajlliñani')
        self.creditos.config(text       = 'Créditos ukanaka')
        self.cheri.config(text          = 'Cheri uka otorongo ukax diabetes usuniwa', font = ('Courier New', 8))
        self.selecIdiomaLbl.config(text = 'Aru ajlliñani')
        self.selecI.config(text         = 'Uñacht’awi ajlliñani lurañataki')
        self.pieI.config(text           = 'Ch’iqa kayu')
        self.pieD.config(text           = 'Kupi kayu')
        self.proceso.config(text        = 'Proceso uñacht’awi ->')
        self.fin.config(text            = 'Tukuña')
        self.guardar.config(text        = 'Jamuqat imaña')
        self.exit.config(          text = 'Llawkataña')
        
        self.byeANDmenu()
        
    def byeANDmenu(self):
        self.selecIdiomaLbl.place_forget()
        self.inicio.place_forget()
        self.idioma.place_forget()
        self.creditos.place_forget()
        self.creditos.place_forget()
        self.spanish.place_forget()
        self.english.place_forget()
        self.quechua.place_forget()
        self.aimara.place_forget()

        self.fin.place_forget()
        self.guardar.place_forget()
        self.selecI.place_forget()
        self.imgPieI.place_forget()
        self.imgPieD.place_forget()

        self.alarm.place_forget()
        self.TrigAlarm.place_forget()
        
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()

        self.fondo_titulo.place(x = round((width - 269)*self.widthConst),   y = round((height - 269)*self.heightConst))
        self.titulo.place      (x = round(200 * self.widthConst),           y = round(200 * self.widthConst))
        self.inicio.place      (x = round(200 * self.widthConst),           y = round(400 * self.heightConst))
        self.idioma.place      (x = round(200 * self.widthConst),           y = round(480 * self.heightConst))
        self.creditos.place    (x = round(200 * self.widthConst),           y = round(560 * self.heightConst))
        self.cheri.place       (x = round((width - 280) * self.widthConst), y = round((height - 280) * self.heightConst))
        self.exit.place        (x = round(200 * self.widthConst),           y = round(640 * self.heightConst))

    def abrirImg(self, buttonNum):
        self.file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    
        if self.file_path:
            try:
                self.figura = Image.open(self.file_path)
                self.figura.thumbnail((300, 300))

                # Aquí almaceno la importante
                photo = ImageTk.PhotoImage(self.figura)
                
                # Display the image
                self.error.config(text = "")  # Clear any previous error message
                if buttonNum == 1:
                    self.imgPieI.config(image = photo)
                    self.imgPieI.image = photo
                    self.imgPieI.place(x = round(400 * self.widthConst), y = round(300 * self.heightConst))
                    self.imagesList[0] = (self.figura, photo)

                if buttonNum == 2:
                    self.imgPieD.config(image = photo)
                    self.imgPieD.image = photo
                    self.imgPieD.place(x = round(900 * self.widthConst), y = round(300 * self.heightConst))
                    self.imagesList[1] = (self.figura, photo)

                if (self.imagesList[0] is not (None, None)) and (self.imagesList[1] is not (None, None)):
                    self.proceso.place(x = round(1000 * self.widthConst), y = round(700 * self.heightConst))

            except (OSError, IOError, ValueError):
                # If the file is not a valid image
                if self.lang == 1:
                    self.error.config(text = "Error: Tipo de archivo no compatible", fg = "navy")
                else:
                    if self.lang == 2:
                        self.error.config(text = 'Error: Uncompatible file', fg = 'navy')
                    else:
                        if self.lang == 3:
                            self.error.config(text = 'Pantasqa: Mana yanapasqa willañiqi laya', fg = 'navy')
                        else:
                            if self.lang == 4:
                                self.error.config(text = 'Pantjasiw: Jan yanapt’at qillqat kasta', fg = 'navy')
                                
                self.imgPieI.config(image = "")  # Clear any previous image
                self.imgPieD.config(image = "")  # Clear any previous image
                self.error.place(x =round(400 * self.widthConst), y = round(400 * self.heightConst))

    def procesar(self):
        # Save image
        
        if self.lang == 1:
            self.selecI.config(text = 'Procesando...')
        else:
            if self.lang == 2:
                self.selecI.config(text = 'Processing...')
            else:
                if self.lang == 3:
                    self.selecI.config(text = 'Procesamiento nisqa...')
                else:
                    if self.lang == 4:
                        self.selecI.config(text = 'Ukaxa lurawiwa...')
                        
        self.pieI.place_forget()
        self.pieD.place_forget()
        self.imgPieI.place_forget()
        self.imgPieD.place_forget()
        self.proceso.place_forget()

        self.granAlgoritmo()

    def granAlgoritmo(self):
        # Muestro pantalla de carga
        self.cargando.place(x = round(600 * self.widthConst), y = round(300 * self.widthConst))
        
        _thread.start_new_thread(self.infinite,())

        # En lo que corre el algoritmo
        self.algoritmo_thread = threading.Thread(target = self.segmentacion_siames)
        self.algoritmo_thread.start()
        self.check_algorithm_status()
        
    def segmentacion_siames(self):
        # Lo grande va aquí
        time.sleep(5)

        self.imagesList[2] = self.imagesList[0]
        self.imagesList[3] = self.imagesList[1]



    def infinite(self):
        i=0
        while 1:
            self.cargando.configure(image=self.cargando_gif[i])
            i=(i+1)%self.totalFrames
            time.sleep(self.delay)
            
    def save(self):
        # Create the respective directory for desktop
        desktop_path = os.path.expanduser("~/Desktop")
        img_dir = os.path.join(desktop_path, "DiabePie - Images")

        if not os.path.exists(img_dir):
            os.makedirs(img_dir)


        # Create the acquisiton directory
        current_time = datetime.datetime.now()

        acq_dir_name = "ACQ-{}".format(current_time.strftime("%Y-%m-%d_%H-%M-%S"))
        acq_dir_path = os.path.join(img_dir, acq_dir_name)

        os.makedirs(acq_dir_path)

        file_names = {
                        (1, 1): "Izquierdo sin procesar.png",
                        (1, 2): "Derecho sin procesar.png",
                        (1, 3): "Izquierdo procesado.png",
                        (1, 4): "Derecho procesado.png",
                        (2, 1): "Unprocessed left.png",
                        (2, 2): "Unprocessed right.png",
                        (2, 3): "Processed left.png",
                        (2, 4): "Processed right.png",
                        (3, 1): "Lluqui mana t’aqwirispa.png",
                        (3, 2): "Paña mana t’aqwirispa.png",
                        (3, 3): "Lluqui t’aqwisqa.png",
                        (3, 4): "Paña t’aqwisqa.png",
                        (4, 1): "Ch’iqa jan uñakipata.png",
                        (4, 2): "Kupi jan uñakipata.png",
                        (4, 3): "Ch’iqa uñakipata.png",
                        (4, 4): "Kupi uñakipata.png",
                    }

        
        for i, (self.figura, _) in enumerate(self.imagesList, start = 1):
            if self.figura:
                name = file_names.get((self.lang, i), f"ImagePie_{current_time}.png")
                default_name = f"ImagePie_{current_time}.png"
                try:
                    self.figura.save(os.path.join(acq_dir_path, name), "PNG")
            
                    self.ExitoFallo.config(text = 'Imagen guardada con exito')
                except Exception as e:
                    # To do: display this in a label x2
                    self.ExitoFallo.config(text = 'Imagen guardada con exito')
                self.ExitoFallo.place(x = round(400 * self.widthConst), y = round(620 * self.widthConst))
                
    def check_algorithm_status(self):
        if self.algoritmo_thread.is_alive():
            self.after(100, self.check_algorithm_status)  # Check every 100 milliseconds
        else:
            self.cargando.place_forget()  # Hide the loading GIF when the algorithm is done
            self.fin.place(x = round(200*self.widthConst), y = round(700*self.heightConst))
            self.guardar.place(x = round(600 * self.widthConst), y = round(700 * self.heightConst))
            self.TrigAlarm.place(x = round(1000 * self.widthConst), y = round(700 * self.heightConst))
            # self.imgPieI.place(x = 400, y = 300)

            izqRes = self.imagesList[2]
            derRes = self.imagesList[3]

            
            if izqRes[1] == derRes[1]:
                # Son iguales
                self.error.config(text = 'Son Iguales')
            else:
                # Son diferentes
                self.error.config(text = 'Son Diferentes')

            resultados = {(1): 'Resultados', (2): 'Results', (3):'Tukusqakuna', (4):'Utjirinaka'}
            self.selecI.config(text = resultados.get(self.lang))

    def alarma(self):
        self.alarm.place(x = round(400 * self.widthConst), y = round(620 * self.widthConst))
    
    def ir_a_menu(self):
        self.inicio.place_forget()
        self.titulo.place_forget()
        self.idioma.place_forget()
        self.fondo_titulo.place_forget()
        self.creditos.place_forget()
        self.cheri.place_forget()

    def ByeBye(self):
        self.destroy()

if __name__ == '__main__':
    window = DiabeApp()
    window.mainloop()
