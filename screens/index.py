from tkinter import *
from tkinter import messagebox


class SampleApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.switch_frame(MainWindow)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            print("Destroy")
            self._frame.cv.destroy()
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class MainWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.master.title("Sistema de Compra de Passagens UniSant'Anna")
        self.masterBackgroundImage = PhotoImage(file="img/inicial.png")
        self.masterBackgroundWidth = self.masterBackgroundImage.width()
        self.masterBackgroundHeight = self.masterBackgroundImage.height()

        self.master.geometry("%dx%d+0+0" % (self.masterBackgroundWidth, self.masterBackgroundHeight))
        self.cv = Canvas(width=self.masterBackgroundWidth, height=self.masterBackgroundHeight)
        self.cv.pack(side='top', fill='both', expand='yes')
        self.cv.create_image(0, 0, image=self.masterBackgroundImage, anchor='nw')

        self.buttonContinue = Button(self.cv, text="Iniciar", font=('arial', 15, 'bold'), width=30, height=5,
                                     command=lambda: master.switch_frame(FirstWindow))
        self.buttonContinue.pack(side="right", padx=30, pady=30, anchor="se", expand=True)


class FirstWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.master.title("Sistema de Compra de Passagens UniSant'Anna")
        self.masterBackgroundImage = PhotoImage(file="img/tela1.png")
        self.masterBackgroundWidth = self.masterBackgroundImage.width()
        self.masterBackgroundHeight = self.masterBackgroundImage.height()

        self.master.geometry("%dx%d+0+0" % (self.masterBackgroundWidth, self.masterBackgroundHeight))
        self.cv = Canvas(width=self.masterBackgroundWidth, height=self.masterBackgroundHeight)
        self.cv.pack(side='top', fill='both', expand='yes')
        self.cv.create_image(0, 0, image=self.masterBackgroundImage, anchor='nw')

        self.centerFrame = Frame(self.cv, width=500, height=500)
        self.centerFrame.pack(side='top', pady=290, anchor='center')

        self.titleLabel = Label(self.centerFrame, font=('arial', 25), width=20, text="Bem vindo")
        self.titleLabel.grid(row=0, column=0)
        
        self.descriptionLabel = Label(self.centerFrame, font=('arial', 15), width=45, text="Escolha uma das opções abaixo")
        self.descriptionLabel.grid(row=1, column=0)

        self.centerButtonsText = ('Compra de Passagem', 'Compra de Bagagem', 'Check-in')
        self.buttonComprar = Button(self.centerFrame, width=20, height=3, text=self.centerButtonsText[0],
                                    font=('arial', 15, 'bold'), command=lambda: master.switch_frame(SecondWindow))
        self.buttonComprar.grid(row=2, column=0, pady= 10, padx=25, sticky=S)

        self.buttonBagagem = Button(self.centerFrame, width=20, height=3, text=self.centerButtonsText[1],
                                    font=('arial', 15, 'bold'), command=lambda: master.switch_frame(Bagagens))
        self.buttonBagagem.grid(row=3, column=0, pady=10, padx=25, sticky=S)

        self.buttonCheckin = Button(self.centerFrame, width=20, height=3, text=self.centerButtonsText[2],
                                    font=('arial', 15, 'bold'), command=lambda: master.switch_frame(CheckIn))
        self.buttonCheckin.grid(row=4, column=0, pady= 10, padx=25, sticky=S)


class SecondWindow(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master=master)

        # Configuração da janela principal
        self.master.title('Check-In')
        self.masterBackgroundImage = PhotoImage(file="img/checkin.png")
        self.masterBackgroundWidth = self.masterBackgroundImage.width()
        self.masterBackgroundHeight = self.masterBackgroundImage.height()

        self.master.geometry("%dx%d+50+30" % (self.masterBackgroundWidth, self.masterBackgroundHeight))
        self.cv = Canvas(width=self.masterBackgroundWidth, height=self.masterBackgroundHeight)
        self.cv.pack(side='top', fill='both', expand='yes')
        self.cv.create_image(0, 0, image=self.masterBackgroundImage, anchor='nw')

        self.buttonBack = Button(self.cv, text="<", font=('arial', 15, 'bold'),
                                 command=lambda: master.switch_frame(FirstWindow))
        self.buttonBack.pack(side='top', anchor='nw')


class Bagagens(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master=master)

        # Configuração da janela principal
        self.master.title('Check-In')
        self.masterBackgroundImage = PhotoImage(file="img/bagagens.png")
        self.masterBackgroundWidth = self.masterBackgroundImage.width()
        self.masterBackgroundHeight = self.masterBackgroundImage.height()

        self.master.geometry("%dx%d+50+30" % (self.masterBackgroundWidth, self.masterBackgroundHeight))
        self.cv = Canvas(width=self.masterBackgroundWidth, height=self.masterBackgroundHeight)
        self.cv.pack(side='top', fill='both', expand='yes')
        self.cv.create_image(0, 0, image=self.masterBackgroundImage, anchor='nw')

        self.buttonBack = Button(self.cv, text="<", font=('arial', 15, 'bold'),
                                 command=lambda: master.switch_frame(FirstWindow))
        self.buttonBack.pack(side='top', anchor='nw')

        self.centerFrame = Frame(self.cv, width=500, height=500)
        self.centerFrame.pack(side='top', pady=290, anchor='center')

        self.titleFrame = Frame(self.centerFrame, width=500, height=200)
        self.titleFrame.pack(side='top', anchor='center')

        self.titleLabel = Label(self.titleFrame, font=('arial', 25), width=20, text="Compra de Bagagens")
        self.titleLabel.grid(row=0, column=0)

        self.localizador = StringVar()
        self.localizadorLabel = Label(self.titleFrame, font=('arial', 15), width=45,
                                      text="Digite o código localizador da sua passagem")
        self.localizadorLabel.grid(row=1, column=0)
        self.localizadorEntry = Entry(self.titleFrame, width=50, textvariable=self.localizador)
        self.localizadorEntry.grid(row=2, column=0, pady=10, padx=25, sticky=S)

        self.descriptionLabel = Label(self.titleFrame, font=('arial', 15), width=45,
                                      text="Selecione a empresa aérea")
        self.descriptionLabel.grid(row=3, column=0)

        self.contentFrame = Frame(self.centerFrame, width=500, height=300)
        self.contentFrame.pack(side='top', anchor='center')

        self.azulImage = PhotoImage(file="img/azul_bagagem.png")
        self.buttonAzul = Button(self.contentFrame, image=self.azulImage,
                                 command=lambda: self.selectEmpresa("azul"))
        self.buttonAzul.grid(row=2, column=0, pady=10, padx=25, sticky=S)

        self.aviancaImage = PhotoImage(file="img/avianca_bagagem.png")
        self.buttonAvianca = Button(self.contentFrame, image=self.aviancaImage,
                                    command=lambda: self.selectEmpresa("avianca"))
        self.buttonAvianca.grid(row=2, column=1, pady=10, padx=25, sticky=S)

        self.passaredoImage = PhotoImage(file="img/passaredo_bagagem.png")
        self.buttonPassaredo = Button(self.contentFrame, image=self.passaredoImage,
                                      command=lambda: self.selectEmpresa("passaredo"))
        self.buttonPassaredo.grid(row=3, column=0, pady=10, padx=25, sticky=S)

        self.tamImage = PhotoImage(file="img/tam_bagagem.png")
        self.buttonTam = Button(self.contentFrame, image=self.tamImage,
                                command=lambda: self.selectEmpresa("tam"))
        self.buttonTam.grid(row=3, column=1, pady=10, padx=25, sticky=S)

        self.golImage = PhotoImage(file="img/gol_bagagem.png")
        self.buttonGol = Button(self.contentFrame, image=self.golImage,
                                command=lambda: self.selectEmpresa("gol"))
        self.buttonGol.grid(row=4, column=0, pady=10, padx=25, sticky=S)

    def selectEmpresa(self, empresa):
        localizador = self.localizadorEntry.get()
        if empresa.lower() == "azul" and localizador != "":
            self.centerFrame.destroy()
            self.centerFrame = Frame(self.cv, width=500, height=500)
            self.centerFrame.pack(side='top', pady=290, anchor='center')

            self.titleFrame = Frame(self.centerFrame, width=500, height=200)
            self.titleFrame.pack(side='top', anchor='center')

            self.titleLabel = Label(self.titleFrame, font=('arial', 25), width=20, text="Compra de Bagagens")
            self.titleLabel.grid(row=0, column=0)

            self.descriptionLabel = Label(self.titleFrame, font=('arial', 15), width=45,
                                          text="Selecione uma das opções abaixo")
            self.descriptionLabel.grid(row=1, column=0)

            self.contentFrame = Frame(self.centerFrame, width=500, height=300)
            self.contentFrame.pack(side='top', anchor='center')

            self.azul10Image = PhotoImage(file="img/azul_bagagem_preco/azul_10.png")
            self.button10Azul = Button(self.contentFrame, image=self.azul10Image)
            self.button10Azul.grid(row=2, column=0, pady=10, padx=25, sticky=S)

            self.azul20Image = PhotoImage(file="img/azul_bagagem_preco/azul_20.png")
            self.button20Azul = Button(self.contentFrame, image=self.azul20Image)
            self.button20Azul.grid(row=2, column=1, pady=10, padx=25, sticky=S)

            self.azul30Image = PhotoImage(file="img/azul_bagagem_preco/azul_30.png")
            self.button30Azul = Button(self.contentFrame, image=self.azul30Image)
            self.button30Azul.grid(row=3, column=0, pady=10, padx=25, sticky=S)

        elif empresa.lower() == "avianca" and localizador != "":
            print(empresa)
        elif empresa.lower() == "passaredo" and localizador != "":
            print(empresa)
        elif empresa.lower() == "tam" and localizador != "":
            print(empresa)
        elif empresa.lower() == "gol" and localizador != "":
            print(empresa)
        else:
            self.messageBox = messagebox.showinfo("Localizador não preenchido", "Por favor, preencha o localizador")


class CheckIn(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master=master)

        # Configuração da janela principal
        self.master.title('Check-In')
        self.masterBackgroundImage = PhotoImage(file="img/checkin.png")
        self.masterBackgroundWidth = self.masterBackgroundImage.width()
        self.masterBackgroundHeight = self.masterBackgroundImage.height()
        
        self.master.geometry("%dx%d+50+30" % (self.masterBackgroundWidth, self.masterBackgroundHeight))
        self.cv = Canvas(width=self.masterBackgroundWidth, height=self.masterBackgroundHeight)
        self.cv.pack(side='top', fill='both', expand='yes')
        self.cv.create_image(0, 0, image=self.masterBackgroundImage, anchor='nw')

        self.buttonBack = Button(self.cv, text="<", font=('arial', 15, 'bold'),
                                 command=lambda: master.switch_frame(FirstWindow))
        self.buttonBack.pack(side='top', anchor='nw')

        # Adicionando widgets
        self.centerFrame = Frame(self.cv, width=500, height=500)
        self.centerFrame.pack(side='top', pady=290, anchor='center')

        self.titleLabel = Label(self.centerFrame, font=('arial', 25), width=20, text="Check-in")
        self.titleLabel.grid(row=0, column=0)
        
        self.descriptionLabel = Label(self.centerFrame, font=('arial', 15), width=45,
                                      text="Digite o código localizador da sua passagem")
        self.descriptionLabel.grid(row=1, column=0)

        self.localizador = StringVar()
        self.localizadorEntry = Entry(self.centerFrame, width=50, textvariable=self.localizador)
        self.localizadorEntry.grid(row=2, column=0, pady=10, padx=25, sticky=S)

        self.button = Button(self.centerFrame, text='Enter')
        self.button.bind("<Button-1>", self.print)
        self.button.grid(row=3, column=0, pady=10, padx=25, sticky=S)

    def voltar(self, event):
        self.master.destroy()
        window = FirstWindow()

    def print(self, event):
        if self.localizadorEntry.get() != "":
            self.messageBox = messagebox.showinfo("Ola", "Ola2")


if __name__ == '__main__':
    app = SampleApp()
    app.mainloop()