#!/usr/bin/python
# coding : Utf-8
from flask import Flask, render_template, request
import fct_app 


#lancement de l'application
app = Flask(__name__)  

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/recherche/',methods = ['post'])
def bonjour():
	result=request.form
	p = result['prenom']
	return render_template("recherche.html", prenom=p)

@app.route('/pokedex/')
def pokedex():
	liste, nombre = fct_app.liste_pokemon()
	tableau = fct_app.ItemTable(liste, classes =['table' , 'table-bordered'])
	return render_template("liste_pokemon.html", liste=liste,nombre=nombre, table=tableau)

@app.route('/pokedex/1/')
def page_gen():
	liste = fct_app.gen_pokemon(1)
	tableau = fct_app.ItemTable(liste, classes =['table' , 'table-bordered'])
	return render_template("gen_pokemon.html", gen=1,liste =liste,table=tableau)

@app.route('/pokedex/2/')
def page_gen2():
	liste = fct_app.gen_pokemon(2)
	tableau = fct_app.ItemTable(liste, classes =['table' , 'table-bordered'])
	return render_template("gen_pokemon.html", gen=2,liste =liste,table=tableau)

@app.route('/pokedex/3/')
def page_gen3():
	liste = fct_app.gen_pokemon(3)
	tableau = fct_app.ItemTable(liste, classes =['table' , 'table-bordered'])
	return render_template("gen_pokemon.html", gen=3,liste =liste,table=tableau)

@app.route('/pokedex/4/')
def page_gen4():
	liste = fct_app.gen_pokemon(4)
	tableau = fct_app.ItemTable(liste, classes =['table' , 'table-bordered'])
	return render_template("gen_pokemon.html", gen=4,liste =liste,table=tableau)

@app.route('/pokedex/5/')
def page_gen5():
	liste = fct_app.gen_pokemon(5)
	tableau = fct_app.ItemTable(liste, classes =['table' , 'table-bordered'])
	return render_template("gen_pokemon.html", gen=5,liste =liste,table=tableau)

@app.route('/pokedex/6/')
def page_gen6():
	liste = fct_app.gen_pokemon(6)
	tableau = fct_app.ItemTable(liste, classes =['table' , 'table-bordered'])
	return render_template("gen_pokemon.html", gen=6,liste =liste,table=tableau)

@app.route('/pokedex/7/')
def page_gen7():
	liste = fct_app.gen_pokemon(7)
	tableau = fct_app.ItemTable(liste, classes =['table' , 'table-bordered'])
	return render_template("gen_pokemon.html", gen=7,liste =liste,table=tableau)

@app.route('/pokedex/8/')
def page_gen8():
	liste = fct_app.gen_pokemon(8)
	tableau = fct_app.ItemTable(liste, classes =['table' , 'table-bordered'])
	return render_template("gen_pokemon.html", gen=8,liste =liste,table=tableau)


if __name__ == '__main__':
    app.run(debug=True, port=2745) 