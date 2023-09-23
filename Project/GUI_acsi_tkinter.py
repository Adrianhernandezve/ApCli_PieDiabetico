# Codigo App diabetica

from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import threading
import _thread
import datetime
import time

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
        self.configure(bg = 'dark turquoise')

        icono = PhotoImage(file = 'CherriElOtorongo.png')
        self.iconphoto(True, icono)

        # Imagen de la pantalla de título
        self.img_titulo = PhotoImage(file = 'CherriElOtorongo.png')
        self.fondo_titulo = Label(self, image = self.img_titulo, bg = 'dark turquoise')
        self.fondo_titulo.place(x = width - 269, y = height - 269)

        # Título
        self.titulo = Label(self, text = 'DiabePie', font = ('Courier New', 80), fg = 'red', justify = CENTER, bg = 'dark turquoise')
        self.titulo.place(x = 200, y = 200)

        # Botones iniciales
        self.inicio = Button(self, text = 'Iniciar programa', command = self.IniciarProceso, font = ('Courier New', 20), activebackground='black', activeforeground='dark turquoise', bg='yellow',fg='red', justify=CENTER, width=30)
        self.inicio.place(x = 200, y = 400)

        self.idioma = Button(self, text = 'Seleccionar Idioma', command = self.idioma, font = ('Courier New', 20), activebackground='black', activeforeground='dark turquoise', bg='yellow',fg='red', justify=CENTER, width=30)
        self.idioma.place(x = 200, y = 480)


        self.creditos = Button(self, text = 'Créditos', command = self.ir_a_menu, font = ('Courier New', 20), activebackground='black', activeforeground='dark turquoise', bg='yellow',fg='red', justify=CENTER, width=30)
        self.creditos.place(x = 200, y = 560)

        # Label de la mascota
        self.cheri = Label(self, text = 'Cheri el otorongo diabético', font = ('Courier New', 20), fg = 'red', justify = CENTER, bg = 'dark turquoise')
        self.cheri.place(x = width - 280, y = height - 280)

        # Botones de idioma
        self.selecIdiomaLbl = Label(self, text = 'Seleccione Idioma', font = ('Courier New', 80), fg = 'red', justify = CENTER, bg = 'dark turquoise')

        self.spanish = Button(self, text = 'Español', command = self.spanish, font = ('Courier New', 20), activebackground='black', activeforeground='dark turquoise', bg='yellow',fg='red', justify=CENTER, width=30)

        self.quechua = Button(self, text = 'Quechua', command = self.quechua, font = ('Courier New', 20), activebackground='black', activeforeground='dark turquoise', bg='yellow',fg='red', justify=CENTER, width=30)

        self.aimara = Button(self, text = 'Aimara', command = self.aimara, font = ('Courier New', 20), activebackground='black', activeforeground='dark turquoise', bg='yellow',fg='red', justify=CENTER, width=30)

        self.english = Button(self, text = 'English', command = self.english, font = ('Courier New', 20), activebackground='black', activeforeground='dark turquoise', bg='yellow',fg='red', justify=CENTER, width=30)


        # Selección de imagen
        self.selecI = Label(self, text = 'Seleccione la imagen a procesar', font = ('Courier New', 40), fg = 'red')

        # Botón para abrir archivo
        self.openF = Button(self, text = 'Abir Imagen', command = self.abrirImg, font = ('Courier New', 20), activebackground='black', activeforeground='dark turquoise', bg='yellow',fg='red', justify=CENTER, width=30)

        # Mostrar la imagen
        self.imgPie = Label(self)
        
        # Error
        self.error = Label(self, text = '', fg = 'red', font = ('Coruier New', 30))

        # Procesar la imagen
        self.proceso = Button(self, text = 'Procesar Imagen ->', command = self.procesar, font = ('Courier New', 15), activebackground='black', activeforeground='dark turquoise', bg='yellow',fg='red', justify=CENTER, width=30)

        # Volver a inicio
        self.fin = Button(self, text = 'Finalizar', command = self.byeANDmenu, font = ('Courier New', 15), activebackground='black', activeforeground='dark turquoise', bg='yellow',fg='red', justify=CENTER, width=30)

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
        self.guardar = Button(self, text = 'Guardar Imagen', command = self.save, font = ('Courier New', 15), activebackground='black', activeforeground='dark turquoise', bg='yellow',fg='red', justify=CENTER, width=30)
        
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
        self.openF.place(x = 200, y = 200)

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
        self.openF.config(text = 'Abir Imagen')
        self.proceso.config(text = 'Procesar Imagen ->')
        self.fin.config(text = 'Finalizar')
        self.guardar.config(text = 'Guardar Imagen')

        # Bye Bye and back to main menu
        self.byeANDmenu()

    def english(self):
        self.lang = 2

        self.inicio.config(text = 'Start program')
        self.idioma.config(text = 'Select language')
        self.creditos.config(text = 'Credits')
        self.cheri.config(text = 'Cheri the diabetic jaguar')
        self.selecIdiomaLbl.config(text = 'Select language')
        self.selecI.config(text = 'Select image to process')
        self.openF.config(text = 'Open File')
        self.proceso.config(text = 'Process Image ->')
        self.fin.config(text = 'End')
        self.guardar.config(text = 'Save image')
        
        self.byeANDmenu()

    def quechua(self):
        self.lang = 3

        self.inicio.config(text = 'Qallariy')
        self.idioma.config(text = 'Simita akllay')
        self.creditos.config(text = 'Créditos nisqakuna')
        self.cheri.config(text = 'Cheri chay otorongo diabeteswan')
        self.selecIdiomaLbl.config(text = 'Simita akllay')
        self.selecI.config(text = 'Imahinata akllay ruwanapaq')
        self.openF.config(text = 'Willayta kichay')
        self.proceso.config(text = 'Proceso nisqa siq’i ->')
        self.fin.config(text = 'Tukuy')
        self.guardar.config(text = 'Waqaychay Siqi')

        self.byeANDmenu()

    def aimara(self):
        self.lang = 4

        self.inicio.config(text = 'Qalltaña')
        self.idioma.config(text = 'Aru ajlliñani')
        self.creditos.config(text = 'Créditos ukanaka')
        self.cheri.config(text = 'Cheri uka otorongo ukax diabetes usuniwa', font = ('Courier New', 8))
        self.selecIdiomaLbl.config(text = 'Aru ajlliñani')
        self.selecI.config(text = 'Uñacht’awi ajlliñani lurañataki')
        self.openF.config(text = 'Jisk’a qillqata jist’araña')
        self.proceso.config(text = 'Proceso uñacht’awi ->')
        self.fin.config(text = 'Tukuña')
        self.guardar.config(text = 'Jamuqat imaña')
        
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

        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()

        self.fondo_titulo.place(x = width - 269, y = height - 269)
        self.titulo.place(x = 200, y = 200)
        self.inicio.place(x = 200, y = 400)
        self.idioma.place(x = 200, y = 480)
        self.creditos.place(x = 200, y = 560)
        self.cheri.place(x = width - 280, y = height - 280)
        
    def abrirImg(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    
        if self.file_path:
            try:
                self.figura = Image.open(self.file_path)

                # Aquí almaceno la importante
                photo = ImageTk.PhotoImage(self.figura)
                
                # Display the image
                self.imgPie.config(image = photo)
                self.imgPie.image = photo
                self.error.config(text = "")  # Clear any previous error message
                self.imgPie.place(x = 400, y = 300)
                self.proceso.place(x = 1000, y = 700)

            except (OSError, IOError, ValueError):
                # If the file is not a valid image
                if self.lang == 1:
                    self.error.config(text = "Error: Tipo de archivo no compatible", fg = "red")
                else:
                    if self.lang == 2:
                        self.error.config(text = 'Error: Uncompatible file', fg = 'red')
                    else:
                        if self.lang == 3:
                            self.error.config(text = 'Pantasqa: Mana yanapasqa willañiqi laya', fg = 'red')
                        else:
                            if self.lang == 4:
                                self.error.config(text = 'Pantjasiw: Jan yanapt’at qillqat kasta', fg = 'red')
                                
                self.imgPie.config(image = "")  # Clear any previous image
                self.error.place(x = 400, y = 400)

    def procesar(self):
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
                        
        self.openF.place_forget()
        self.imgPie.place_forget()
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


    def infinite(self):
        i=0
        while 1:
            self.cargando.configure(image=self.cargando_gif[i])
            i=(i+1)%self.totalFrames
            time.sleep(self.delay)
            
    def save(self):
        if self.imgPie.image:
            current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            default_name = f"ImagePie_{current_time}.png"
            file_path = filedialog.asksaveasfilename(defaultextension=".png", initialfile=default_name, filetypes=[("PNG files", "*.png")])
            if file_path:
                try:
                    self.figura.save(file_path)
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
            self.imgPie.place(x = 400, y = 300)

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
