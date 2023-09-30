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
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()

        # Spanish
        self.lang = 1 
        self.geometry("%dx%d" % (width, height))
        self.configure(bg = 'LightCyan2')

        icono = PhotoImage(file = 'CherriElOtorongo.png')
        self.iconphoto(True, icono)

        # Imagen de la pantalla de título
        self.img_titulo = PhotoImage(file = 'CherriElOtorongo.png')
        self.fondo_titulo = Label(self, image = self.img_titulo, bg = 'LightCyan2')
        self.fondo_titulo.place(x = width - 269, y = height - 269)

        # Título
        self.titulo = Label(self, text = 'DiabePie', font = ('Courier New', 80), fg = 'navy', justify = CENTER, bg = 'LightCyan2')
        self.titulo.place(x = 200, y = 200)

        # Botones iniciales
        self.inicio = Button(self, text = 'Iniciar programa', command = self.IniciarProceso, font = ('Courier New', 20), activebackground='black', activeforeground='LightCyan2', bg='CadetBlue3',fg='navy', justify=CENTER, width=30)
        self.inicio.place(x = 200, y = 400)

        self.idioma = Button(self, text = 'Seleccionar Idioma', command = self.idioma, font = ('Courier New', 20), activebackground='black', activeforeground='LightCyan2', bg='CadetBlue3',fg='navy', justify=CENTER, width=30)
        self.idioma.place(x = 200, y = 480)


        self.creditos = Button(self, text = 'Créditos', command = self.ir_a_menu, font = ('Courier New', 20), activebackground='black', activeforeground='LightCyan2', bg='CadetBlue3',fg='navy', justify=CENTER, width=30)
        self.creditos.place(x = 200, y = 560)

        # Label de la mascota
        self.cheri = Label(self, text = 'Cheri el otorongo diabético', font = ('Courier New', 20), fg = 'navy', justify = CENTER, bg = 'LightCyan2')
        self.cheri.place(x = width - 280, y = height - 280)

        # Botones de idioma
        self.selecIdiomaLbl = Label(self, text = 'Seleccione Idioma', font = ('Courier New', 80), fg = 'navy', justify = CENTER, bg = 'LightCyan2')

        self.spanish = Button(self, text = 'Español', command = self.spanish, font = ('Courier New', 20), activebackground='black', activeforeground='LightCyan2', bg='CadetBlue3',fg='navy', justify=CENTER, width=30)

        self.quechua = Button(self, text = 'Quechua', command = self.quechua, font = ('Courier New', 20), activebackground='black', activeforeground='LightCyan2', bg='CadetBlue3',fg='navy', justify=CENTER, width=30)

        self.aimara = Button(self, text = 'Aimara', command = self.aimara, font = ('Courier New', 20), activebackground='black', activeforeground='LightCyan2', bg='CadetBlue3',fg='navy', justify=CENTER, width=30)

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

        self.selecI.place(x = 200, y = 100)
        self.pieI.place(x = 200, y = 200)
        self.pieD.place(x = 1000, y = 200)

    def idioma(self):
        self.inicio.place_forget()
        self.titulo.place_forget()
        self.idioma.place_forget()
        self.fondo_titulo.place_forget()
        self.creditos.place_forget()
        self.cheri.place_forget()

        self.selecIdiomaLbl.place(x = 200, y = 200)
        self.spanish.place(x = 200, y = 400)
        self.quechua.place(x = 200, y = 480)
        self.aimara.place(x = 200, y = 560)
        self.english.place(x = 200, y = 640)

    def spanish(self):
        # Translation
        self.lang = 1

        self.inicio.config(text = 'Iniciar programa')
        self.idioma.config(text = 'Seleccionar Idioma')
        self.creditos.config(text = 'Créditos')
        self.cheri.config(text = 'Cheri el otorongo diabético')
        self.selecIdiomaLbl.config(text = 'Seleccione Idioma')
        self.selecI.config(text = 'Seleccione la imagen a procesar')
        self.pieI.config(text = 'Pie Izquierdo')
        self.pieD.config(text = 'Pie Derecho')
        self.proceso.config(text = 'Procesar Imagen ->')
        self.fin.config(text = 'Finalizar')
        self.guardar.config(text = 'Guardar Imagen')

        # Bye Bye and back to main menu
        self.byeANDmenu()

    def english(self):
        self.lang = 2

        self.inicio.config(text         = 'Start program')
        self.idioma.config(text         = 'Select language')
        self.creditos.config(text       = 'Credits')
        self.cheri.config(text          = 'Cheri the diabetic jaguar')
        self.selecIdiomaLbl.config(text = 'Select language')
        self.selecI.config(text         = 'Select image to process')
        self.pieI.config(text           = 'Left Foot')
        self.pieD.config(text           = 'Right Foot')
        self.proceso.config(text        = 'Process Image ->')
        self.fin.config(text            = 'End')
        self.guardar.config(text        = 'Save image')
        
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
        
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()

        self.fondo_titulo.place(x = width - 269, y = height - 269)
        self.titulo.place(x = 200, y = 200)
        self.inicio.place(x = 200, y = 400)
        self.idioma.place(x = 200, y = 480)
        self.creditos.place(x = 200, y = 560)
        self.cheri.place(x = width - 280, y = height - 280)
        
    def abrirImg(self, buttonNum):
        self.file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    
        if self.file_path:
            try:
                self.figura = Image.open(self.file_path)

                # Aquí almaceno la importante
                photo = ImageTk.PhotoImage(self.figura)
                
                # Display the image
                self.error.config(text = "")  # Clear any previous error message
                if buttonNum == 1:
                    self.imgPieI.config(image = photo)
                    self.imgPieI.image = photo
                    self.imgPieI.place(x = 400, y = 300)
                    self.imagesList[1] = (self.figura, photo)
                else:
                    self.imgPieD.config(image = photo)
                    self.imgPieD.image = photo
                    self.imgPieD.place(x = 900, y = 300)
                    self.imagesList[2] = (self.figura, photo)

                self.proceso.place(x = 1000, y = 700)

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
                self.error.place(x = 400, y = 400)

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
        self.cargando.place(x = 600, y = 300)
        
        _thread.start_new_thread(self.infinite,())

        # En lo que corre el algoritmo
        self.algoritmo_thread = threading.Thread(target = self.segmentacion_siames)
        self.algoritmo_thread.start()
        self.check_algorithm_status()
        
    def segmentacion_siames(self):
        # Lo grande va aquí
        time.sleep(5)

        self.imagesList[3] = self.imagesList[1]
        self.imagesList[4] = self.imagesList[2]



    def infinite(self):
        i=0
        while 1:
            self.cargando.configure(image=self.cargando_gif[i])
            i=(i+1)%self.totalFrames
            time.sleep(self.delay)
            
    def save(self):
        # Create the respective directory
        if not os.path.exists("Processed Images"):
            os.makedirs("Processed Images")

        # Create the acquisiton directory
        current_time = datetime.datetime.now()

        acq_dir_name = "ACQ-{}".format(current_time.strftime("%Y-%m-%d_%H-%M-%S"))
        acq_dir_path = os.path.join("Processed Images", acq_dir_name)

        os.makedirs(acq_dir_path)
        
        for i, (self.figura, _) in enumerate(self.imagesList, start = 1):
            if self.figura:
                if i == 1:
                    name = "Izquierdo sin procesar.png"
                else:
                    if i == 2:
                        name = "Derecho sin procesar.png"
                    else:
                        if i == 3:
                            name = "Izquierdo procesado.png"
                        else:
                            name = "Derecho procesado.png"

                default_name = f"ImagePie_{current_time}.png"
                try:
                    self.figura.save(os.path.join(acq_dir_path, name), "PNG")
            
                    # To do: display this in a label
                    print("Image saved successfully.")
                except Exception as e:
                    # To do: display this in a label x2
                    print("Error saving the image.")
                    
    def check_algorithm_status(self):
        if self.algoritmo_thread.is_alive():
            self.after(100, self.check_algorithm_status)  # Check every 100 milliseconds
        else:
            self.cargando.place_forget()  # Hide the loading GIF when the algorithm is done
            self.fin.place(x = 200, y = 700)
            self.guardar.place(x = 600, y = 700)
            # self.imgPieI.place(x = 400, y = 300)
            self.TrigAlarm.place(x = 1000, y = 700)

            izqRes = self.imagesList[3]
            derRes = self.imagesList[4]
            
            if izqRes[1] == derRes[1]:
                # Son iguales
                self.error.config(text = 'Son Iguales')
            else:
                # Son diferentes
                self.error.config(text = 'Son Diferentes')

            if self.lang == 1:
                self.selecI.config(text = 'Resultados')
            else:
                if self.lang == 2:
                    self.selecI.config(text = 'Results')
                else:
                    if self.lang == 3:
                        self.selecI.config(text = 'Tukusqakuna')
                    else:
                        if self.lang == 4:
                            self.selecI.config(text = 'Utjirinaka')

    def alarma(self):
        self.alarm.place(x = 400, y = 620)
    
    def ir_a_menu(self):
        self.inicio.place_forget()
        self.titulo.place_forget()
        self.idioma.place_forget()
        self.fondo_titulo.place_forget()
        self.creditos.place_forget()
        self.cheri.place_forget()


if __name__ == '__main__':
    window = DiabeApp()
    window.mainloop()
