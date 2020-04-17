# trouvetontrain | Thibaut DAVID

Projet Trouve Ton Train, permet d'afficher les horaries de train pour un trajet et une date voulue grace à l'API de la scnf.
Ce projet est composé de deux serveur, un sur Django, qui permet d'éxecuter la partie front ansi que l'API SOAP et un sur Flask,
qui sert de serveur pour l'API rest.

## Acceder au site : http://thibautdavid.pythonanywhere.com/

###T élécharger et lancer le projet

Ce projet fontionne avec Python 3.7, il est nécessaire de l'installer avant de lancer ce projet

#####C loner le répertoire git
```
git clone https://github.com/ThibautDavid-USMB/trouvetontrain.git
```
##### Placer vous à l'intérieur du dossier et créer un environnement virtuel
```
python3.7 -m venv myvenv
myvenv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```
##### Lancer le serveur Django (localhost:8000)
```
python .\manage.py runserver
```
##### Lancer le serveur flask (localhost:5000)
```
python .\pryx.py
```
##### Depuis un navigateur connectez-vous sur : http://localhost:8000/
