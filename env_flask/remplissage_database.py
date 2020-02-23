import pymongo 
from pymongo import MongoClient 
import requests 
import bs4 
import pandas as pd 
from bs4 import BeautifulSoup

#connexion au cluster 0
cluster = MongoClient("mongodb+srv://kevint:hedencorei5@cluster0-qtcx2.mongodb.net/test?retryWrites=true&w=majority")


#choix de la database 
db = cluster["pokedex"]
#choix de la collection
collection= db["pokemons"]

#pour insérer une donnée

url = 'https://www.pokepedia.fr/Liste_des_Pok%C3%A9mon_par_statistiques_de_base'

def pokemon_list(url):
	"""
		Scrape l'url établit plus haut et envoie les données qui nous intéresse dans la database mongoDB
	"""
	response = requests.get(url)
	#On récupère tout le code html de l'URL
	soup = BeautifulSoup(response.text, "lxml")
	#On prend que ce qui nous intéresse 
	poke = soup.find("tbody")
	pokedex = poke.find_all("td")
	liste = [] 
	for e in pokedex:
		liste.append(e.text)
	#nettoyage de la liste  
	liste = [x for x in liste if x] #on retire les espaces blancs

	i = 0
	ID=0
	while(i<len(liste)):
		ID = ID+1
		numero = liste[i]
		nom = liste[i+1]
		pv = liste[i+2]
		attaque = liste[i+3]
		defense = liste[i+4]
		attaque_speciale = liste[i+5]
		defense_speciale = liste[i+6]
		vitesse = liste[i+7]
		total = liste[i+8]
		moyenne = liste[i+9]
		moyenne=moyenne.strip('\n') #on supprime le \n à la fin de la donnée
		i = i+10
		post = {"_id":ID,"numero":numero,"nom":nom,"PV":pv,"attaque":attaque,"defense":defense,"attaque_speciale":attaque_speciale,"defense_speciale":defense_speciale,"vitesse":vitesse,"total":total,"moyenne":moyenne}
		#envoie des données à MongoDB 
		collection.insert_one(post)