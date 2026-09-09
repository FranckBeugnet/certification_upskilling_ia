import json
import os
import random

def load_qcm_sets(directory):
    qcm_files = [f for f in os.listdir(directory) if f.endswith('.json')]
    return qcm_files

def run_qcm(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        questions = json.load(f)
    
    # Mélanger les questions pour plus de diversité
    random.shuffle(questions)
    
    score = 0
    total = len(questions)
    
    print(f"\n--- Lancement du QCM : {os.path.basename(filepath)} ---")
    print(f"Nombre de questions : {total}\n")
    
    for i, q in enumerate(questions, 1):
        print(f"Question {i}/{total} : {q['question']}")
        
        options = q['options']
        # Mélanger les options
        options_melangees = options.copy()
        random.shuffle(options_melangees)
        
        for j, opt in enumerate(options_melangees, 1):
            print(f"  {j}. {opt}")
            
        choix = ""
        while not (choix.isdigit() and 1 <= int(choix) <= len(options)):
            choix = input("Votre choix (numéro) : ")
            
        reponse_utilisateur = options_melangees[int(choix) - 1]
        
        if reponse_utilisateur == q['answer']:
            print("✅ Bonne réponse !")
            score += 1
        else:
            print("❌ Mauvaise réponse.")
            print(f"La bonne réponse était : {q['answer']}")
            
        print(f"Explication : {q['explanation']}\n")
            
    print(f"--- Fin du QCM ---")
    print(f"Votre score : {score}/{total} ({(score/total)*100:.1f}%)\n")

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    print("Bienvenue dans le module de préparation à la certification IA ! 🚀")
    
    while True:
        qcm_files = load_qcm_sets(current_dir)
        if not qcm_files:
            print("Aucun fichier JSON de QCM trouvé dans ce dossier.")
            break
            
        print("Sélectionnez le set de questions que vous souhaitez réviser :")
        for i, f in enumerate(qcm_files, 1):
            print(f"  {i}. {f}")
        print(f"  0. Quitter")
        
        choix = input("\nVotre choix : ")
        
        if choix == '0':
            print("Bonnes révisions ! À bientôt.")
            break
        elif choix.isdigit() and 1 <= int(choix) <= len(qcm_files):
            fichier_choisi = os.path.join(current_dir, qcm_files[int(choix)-1])
            run_qcm(fichier_choisi)
        else:
            print("Choix invalide, veuillez réessayer.\n")

if __name__ == "__main__":
    main()
