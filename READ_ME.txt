Le fichier env_flask correspond à mon environnement virtuel (pour le lancer il faut ouvrir un cmd avec le chemin suivant qui mène à l'environnement virtuel et taper "Scripts\Activate.bat").

Dans ce document vous trouverez plusieurs dossiers : 
- Lib : correspond aux bibliothèques que j'ai utilisé 
- Scripts et _pycache_ : des dossiers à l'environnement virtuel 
- static : tous les fichiers statiques nécessaires à l'application Flask tels que les images et les fichiers CSS (j'ai essayé d'intégrer du javascript mais je ne suis pas arrivé)
- template : tous les templates nécessaires à ma page Web

Enfin voici le fonctionnement de tous les fichiers python : 
- image_pokemon.py : un programme qui permet de télécharger tous les images souhaités (ici des pokémons) et les enregistre dans le dossier indiqué
- remplissage_database.py : un programme pour scraper des données sur le web à l'aide de beautifulSoup et les stock dans une base de données noSQL (mongoDB)
- fct_app.py : un fichier qui contient des programmes qui sont appelés dans l'application Flask
- app.py : le fichier qu'il faudra lancer pour exécuter l'application Flask. C'est dans ce fichier que vous trouverez les routes de chaque page


