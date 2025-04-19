import tkinter as tk

def calculer_imc():
    try:
        poids = float(entry_poids.get())
        taille = float(entry_taille.get()) / 100  # convert cm to m
        imc = poids / (taille ** 2)
        label_resultat.config(text=f"Votre IMC est : {imc:.2f}")
    except:
        label_resultat.config(text="Entrez des valeurs valides.")

root = tk.Tk()
root.title("Calculateur d'IMC")

tk.Label(root, text="Poids (kg) :").pack()
entry_poids = tk.Entry(root)
entry_poids.pack()

tk.Label(root, text="Taille (cm) :").pack()
entry_taille = tk.Entry(root)
entry_taille.pack()

tk.Button(root, text="Calculer l'IMC", command=calculer_imc).pack(pady=10)
label_resultat = tk.Label(root, text="")
label_resultat.pack()

root.mainloop()
