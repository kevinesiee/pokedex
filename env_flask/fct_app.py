#!/usr/bin/python
# coding : Utf-8

#importation des packages nécessaire pour interroger la database
import pymongo 
from pymongo import MongoClient 
from flask_table import Table,Col
import matplotlib.pyplot as plt
import numpy as np 

#connexion au cluster 0
cluster=MongoClient("mongodb+srv://kevint:hedencorei5@cluster0-qtcx2.mongodb.net/test?retryWrites=true&w=majority")
#choix de la database 
db=cluster["pokedex"]
#choix de la collection où on va stocker tous les pokemons
collection=db["pokemons"]



def liste_pokemon():
	'''
	Fonction interrogeant la database et retourne une liste
	de dictionnaires contenant les informations sur les pokemons
	'''
	L = []
	i=0 #compte le nombre de pokémons
	num = "0"
	for doc in collection.find():
		dic={"numero":doc["numero"],"nom":doc["nom"],"PV":doc["PV"],"attaque":doc["attaque"],"defense":doc["defense"],"attaque_speciale":doc["attaque_speciale"],"defense_speciale":doc["defense_speciale"],"vitesse":doc["vitesse"],"total":doc["total"],"moyenne":doc["moyenne"]}
		if num==doc["numero"]: #cette condition est nécessaire pour enlever les différentes versions d'un même pokémon
			continue
		else:
			L.append(dic)
			i+=1
		num = doc["numero"]
	return L,i

def gen_pokemon(gen):
	"""
		Retourne la liste de pokémons selon la génération passée en paramètre
	"""
	L,i = liste_pokemon()
	prem = 0
	dern = 0
	liste = []
	if int(gen)<1 or int(gen)>8:
		return 'Cette génération n\'existe pas. Il y\'a aujourd\'hui 8 générations de pokemons'
	elif int(gen)==1:
		liste= L[0:151]
		return liste
	elif int(gen)==2:
		liste= L[151:251]
		return liste
	elif int(gen)==3:
		liste= L[251:386]
		return liste
	elif int(gen) == 4:
		liste= L[386:493]
		return liste
	elif int(gen)==5:
		liste= L[493:649]
		return liste
	elif int(gen)==6:
		liste= L[649:721]
		return liste
	elif int(gen)==7:
		liste= L[721:809]
		return liste
	else:
		liste= L[809:890]
		return liste


#déclaration du tableau
#permet de créer un tableau avec les caratéristiques des pokémons
class ItemTable(Table):
	numero=Col('numero')
	nom=Col('nom')
	PV=Col("PV")
	attaque=Col("attaque")
	defense=Col("defense")
	attaque_speciale=Col("attaque_speciale")
	defense_speciale=Col("defense_speciale")
	vitesse=Col("vitesse")
	total=Col("total")
	moyenne=Col("moyenne")


def meilleur(gen):
	"""
		fonction qui trie dans l'ordre croissant les pokémons d'une génération selon leur pouvoir total
	"""
	L = gen_pokemon(gen)
	liste = []
	for e in L:
		liste.append([e["nom"],int(e["total"])])
	liste = sorted(liste, key=lambda colonnes:colonnes[1])
	return liste

def graphe(gen):
	"""
		crée un graphe qui montre le top 3 de chaque pokemon selon la génération 
	"""
	L=meilleur(gen)
	total = [i[1] for i in L]
	nom = [i[0] for i in L]
	total = total[::-1]
	nom = nom[::-1]
	#on prend que les 15 premiers 
	nom = nom[0:3]
	x_pos = np.arange(len(nom))
	total = total[0:3]
	plt.bar(x_pos, total, alpha=0.5)
	plt.xticks(x_pos, nom)
	plt.ylabel('pouvoir')
	plt.title('Top 3 des pokémons de la génération '+str(gen))
	plt.savefig("static/image/topgeneration_"+str(gen)+".png")
	print("terminé")


 	