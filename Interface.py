from tkinter import *


def limpar(nome_e, idade_e, contato_e, tipo_cont_e, vet, texto):
    temporario = [nome_e.get(), idade_e.get(), contato_e.get(), tipo_cont_e.get()]
    nome_e.delete(0, END)
    idade_e.delete(0, END)
    contato_e.delete(0, END)
    tipo_cont_e.delete(0, END)
    if '' not in temporario:
        vet.append(temporario)
        texto.set(f"Os dados de {temporario[0]} foram salvos.")
    else:
        texto.set("Informações insuficientes.\nPreencha todos os campos.")


def janela():
    # Criação da janela de interface.
    rook = Tk()
    rook.title("Interface")
    rook.configure(background="#4F4F4F")
    rook.geometry("500x500")
    rook.resizable(True, True)
    rook.maxsize(width=700, height=700)
    rook.minsize(width=400, height=400)

    # Variaveis
    info = []
    texto_resposta = StringVar()

    # Criação de um frm para a janela.
    frm = Frame(rook, bd=4, bg='#E0FFFF', highlightbackground='#DCDCDC', highlightthickness=3)
    frm.place(relx=0.02, rely=0.02, relwidth=0.95, relheight=0.95)

    # Criando caixas de entrada de texto.

    altura_rel = 0.08
    Label(frm, text="Nome").place(relx=0.05, rely=altura_rel)
    nome_entry = Entry(frm)
    nome_entry.pack()
    nome_entry.place(relx=0.05, rely=altura_rel*2, relwidth=0.5)

    Label(frm, text="Idade").place(relx=0.05, rely=altura_rel*3)
    idade_entry = Entry(frm)
    idade_entry.place(relx=0.05, rely=altura_rel*4, relwidth=0.5)

    Label(frm, text="Contato").place(relx=0.05, rely=altura_rel*5)
    contato_entry = Entry(frm)
    contato_entry.place(relx=0.05, rely=altura_rel*6, relwidth=0.5)

    Label(frm, text="Tipo de Contato").place(relx=0.05, rely=altura_rel*7)
    tipo_contato_entry = Entry(frm)
    tipo_contato_entry.place(relx=0.05, rely=altura_rel*8, relwidth=0.5)

    # Criar Botão salvar e fechar.
    close_button = Button(frm, text="Fechar", bd=2, bg="white", fg="black", command=rook.destroy)
    close_button.place(relx=0.7, rely=altura_rel*8, relwidth=0.25)

    save_button = Button(frm, text="Salvar", bd=2, bg="white", fg="black",
                         command=lambda: [limpar(nome_entry, idade_entry, contato_entry,
                                                 tipo_contato_entry, info, texto_resposta)])

    save_button.place(relx=0.7, rely=altura_rel*2, relwidth=0.25)

    # Caixa de informação.
    Label(frm, textvariable=texto_resposta, fg="black").place(relx=0.05, rely=altura_rel*9, relheight=0.24, relwidth=0.9)

    rook.update()
    rook.mainloop()

    return info
