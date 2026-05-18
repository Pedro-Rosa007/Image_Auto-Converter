from customtkinter import *
import customtkinter as ctk
from tkinter import messagebox, filedialog




class Application(ctk.CTk):

    def __init__(self):
        super().__init__()

        
        from main import Backend
        self.services = Backend()
        self.pasta_saida_label = None
        self.builder()



    def builder(self):

        self.initializer()



    def initializer(self):

        set_appearance_mode("light")
        self.centralizar_janela(900, 600)
        self.title("Auto-Converter by Tremura")
        self.button()



    def centralizar_janela(janela, largura=0, altura=0):
        
        janela.update_idletasks()
        
   
        largura_tela = janela.winfo_screenwidth()
        altura_tela = janela.winfo_screenheight()
        

        pos_x = int((largura_tela / 2) - (largura / 2))
        pos_y = int((altura_tela / 2) - (altura / 2))
        

        janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")


    def button(self):


        self.labels = CTkLabel(
            self,
            text="FORMATOS ACEITOS: avif, heic, heif, webp, raw, jpg, jpeg",
            font= ("Segoe UI", 20, "bold"),
            text_color="black"
        )
        self.labels.place(relx = 0.05, rely= 0.1, relwidth = 0.9, relheight = 0.08)

        # Botão para escolher pasta de saída
        self.escolher_pasta_btn = CTkButton(
            self,
            corner_radius= 15,
            bg_color="transparent",
            fg_color="#FF6B35",
            text="ESCOLHER PASTA DE SAÍDA",
            text_color="white",
            font= ("Segoe UI", 12, "bold"),
            hover_color="#E85A2F",
            command= lambda: self.escolher_pasta_saida()
        )
        self.escolher_pasta_btn.place(relx = 0.29, rely= 0.22, relwidth = 0.4, relheight = 0.08)

        # Label para mostrar a pasta selecionada
        self.pasta_saida_label = CTkLabel(
            self,
            text="Pasta padrão: image/convertidas",
            font= ("Segoe UI", 11),
            text_color="gray"
        )
        self.pasta_saida_label.place(relx = 0.05, rely= 0.32, relwidth = 0.9, relheight = 0.06)

        self.converter = CTkButton(
            self,
            corner_radius= 20,
            bg_color="transparent",
            fg_color="blue",
            text="CONVERTER",
            text_color="white",
            font= ("Segoe UI", 14, "bold"),
            hover_color="#03929c",
            command= lambda: self.services.converter_e_limpar(self)
        )
        self.converter.place(relx = 0.35, rely= 0.52, relwidth = 0.3, relheight = 0.1)

    def escolher_pasta_saida(self):
        """Abre o diálogo para escolher pasta de saída e atualiza o label"""
        pasta = self.services.escolher_pasta_saida(parent=self)
        if pasta:
            self.pasta_saida_label.configure(text=f"Pasta selecionada: {pasta}")

        



        


if __name__ == "__main__":
    app = Application()
    app.mainloop()