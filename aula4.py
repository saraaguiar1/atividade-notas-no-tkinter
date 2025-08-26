import tkinter as tk 
from tkinter import messagebox 

def verificar_nota():
    nota_texto = entry_nota.get()

    if nota_texto.replace(".", "", 1).isdigit():
        nota = float(nota_texto)

        if nota == 10:
            resultado = "Parabens nota máxima!"
        elif nota >= 9 and nota <= 9.9:
            resultado = "Quase perfeito!"
        elif nota >= 0 and nota <= 4.9:
            resultado = "Reprovado com baixa nota."

        messagebox.showinfo("Resultado", f"Situação: {resultado}")
    else:
        messagebox.showerror("Erro", "Digite um número válido.") 

root = tk.Tk()
root.title("Verificador de Nota")
root.geometry("300x200")
root.configure(bg="#E06CA6")

tk.Label(root, text= "Digite a nota do aluno:", bg= "#FF00AA", fg= "black", font=("Arial", 11, "bold")).pack(pady=10)
entry_nota = tk.Entry(root)
entry_nota.pack(pady=5)

tk.Button(root, text="Verificar", command=verificar_nota, bg="blue", font=("Arial", 11, "bold")).pack(pady=15)

root.mainloop()            

            
