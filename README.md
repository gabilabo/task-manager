# 📝 Task Manager (Flask)

Application web simple de gestion de tâches développée avec **Flask**.  
Elle permet d’ajouter, supprimer et marquer des tâches comme complétées via une interface web légère.

---

## 🚀 Fonctionnalités

- ➕ Ajouter une tâche  
- ✅ Marquer une tâche comme terminée  
- ❌ Supprimer une tâche  
- 🎨 Interface simple avec HTML/CSS  

---

## 🛠️ Technologies utilisées

- Python  
- Flask  
- HTML / CSS  

---

## 📂 Structure du projet

```
task-manager/
│── app.py
│── requirements.txt
│── templates/
│     └── index.html
│── static/
│     └── style.css
```

---

## ▶️ Installation et exécution

1. Cloner le repository :

```bash
git clone https://github.com/gabilabo/task-manager.git
cd task-manager
```

2. Créer un environnement virtuel :

```bash
python3 -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

3. Installer les dépendances :

```bash
pip install -r requirements.txt
```

4. Lancer l’application :

```bash
python app.py
```

5. Ouvrir dans le navigateur :

```
http://127.0.0.1:5000
```

---

## ⚠️ Limites du projet

Les tâches sont stockées en mémoire (liste Python).  
Elles sont donc perdues à chaque redémarrage de l’application.

👉 Une version avec base de données sera développée dans un prochain projet.

---

## 🎯 Objectif du projet

Ce projet a été réalisé dans le cadre de mon apprentissage du développement web avec Flask.  
Il permet de comprendre les bases :

- routes  
- formulaires  
- gestion des données  
- structure d’une application web  

---

## 👨‍💻 Auteur

Gabriel Santos  
Étudiant en informatique – Université Lumière Lyon 2