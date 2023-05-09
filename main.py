import tkinter as tk

def pgcd(a, b):
    while b:
        a, b = b, a % b
    return a

def diviseurs(n):
    diviseurs = []
    for i in range(1, n+1):
        if n % i == 0:
            diviseurs.append(i)
    return diviseurs

def calculer_diviseurs():
    # Récupération des valeurs entrées par l'utilisateur
    a = int(champ_a.get())
    b = int(champ_b.get())
    
    # Calcul du PGCD avec l'algorithme d'Euclide
    pgcd_resultat = pgcd(a, b)
    
    # Calcul de la liste de tous les diviseurs
    diviseurs_a = diviseurs(a)
    diviseurs_b = diviseurs(b)
    
    # Intersection des listes de diviseurs pour obtenir les diviseurs communs
    diviseurs_communs = list(set(diviseurs_a).intersection(set(diviseurs_b)))
    
    # Affichage des résultats dans les labels correspondants
    label_pgcd.config(text=f"Le PGCD de {a} et {b} est {pgcd_resultat}")
    label_diviseurs.config(text=f"Les diviseurs communs de {a} et {b} sont {diviseurs_communs}")

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Calcul des diviseurs communs")

# Création des widgets
label_a = tk.Label(fenetre, text="Nombre a : ")
champ_a = tk.Entry(fenetre)
label_b = tk.Label(fenetre, text="Nombre b : ")
champ_b = tk.Entry(fenetre)
bouton_calculer = tk.Button(fenetre, text="Calculer", command=calculer_diviseurs)
label_pgcd = tk.Label(fenetre)
label_diviseurs = tk.Label(fenetre)

# Placement des widgets dans la fenêtre
label_a.grid(row=0, column=0)
champ_a.grid(row=0, column=1)
label_b.grid(row=1, column=0)
champ_b.grid(row=1, column=1)
bouton_calculer.grid(row=2, column=0, columnspan=2)
label_pgcd.grid(row=3, column=0, columnspan=2)
label_diviseurs.grid(row=4, column=0, columnspan=2)

# Lancement de la boucle principale de la fenêtre
fenetre.mainloop()
