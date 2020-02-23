import cv2 #pour le traitement d'image
import numpy as np 
import urllib.request  #pour les requêtes http 
import time #afin de mesurer le temps de téléchargement

debut=time.time()
for i in range (1, 891): #tous les pokémons du numéro 1 à 890
	url = 'https://assets.pokemon.com/assets/cms2/img/pokedex/detail/'+'{:03d}'.format(i)+'.png' #on formate le i afin d'avoir 001 au lieu de 1
	request = urllib.request.Request(url) #on fait la requête 
	response = urllib.request.urlopen(request) #on ouvre la page
	binary_str = response.read() # on reçoit des données binaires 
	#il faut convertir le strung binaire en une image et cela se fait en deux étapes
	byte_array = bytearray(binary_str) #transformation en tableau
	numpy_array = np.asarray(byte_array, dtype="uint8")
	image = cv2.imdecode(numpy_array, cv2.IMREAD_UNCHANGED)
	cv2.imwrite("static/image/"+'{:003d}'.format(i)+'.png',image)
	print("Sauvegardé "+'{:003d}'.format(i)+'.png')
fin = time.time()

print("terminé")
print("Durée du téléchargement : "+str(fin - debut)+"sec") #433.8621416091919sec soit un peu plus de 7min