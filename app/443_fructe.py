from flask import Flask, url_for
from lib.biblioteca_fructe import *

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    ret = "<h1>Fructe</h1>"
    
    ret += f"<a href={url_for('view_acai')}>Acai - Belu FLorentina-Alexandra</a> <br/>"
    ret += f"<a href={url_for('view_ananas')}>Ananas - Nechita Ioana-Valeria</a> <br/>"

    return ret

@app.route('/ananas', methods=['GET'])
def view_ananas():
	culoare = culoare_ananas()
	descriere = descriere_ananas()

	ret = "<h1>Ananas</h1>"

	#Linkuri
	ret += f"<a href={url_for('index')}>[fructe]</a> | "
	ret += f"<a href={url_for('view_culoare_ananas')}>[culoare]</a> | "
	ret += f"<a href={url_for('view_descriere_ananas')}>[descriere]</a>"

	ret += "<h2>Descriere: </h2>"

	ret += descriere

	ret += "<h2>Culoare: </h2>"
	ret += culoare



	return ret


@app.route('/ananas/culoare', methods=['GET'])
def view_culoare_ananas():
    culoare = culoare_ananas()

    ret = "<h1>Culoarea ananas:</h1>"
    ret += f"<a href={url_for('index')}>[fructe]</a> | "
    ret += f"<a href={url_for('view_ananas')}>[ananas]</a> <br/> <br/>"
    ret += culoare

    return ret

@app.route('/ananas/descriere', methods=['GET'])
def view_descriere_ananas():
    descriere = descriere_ananas()

    ret = "<h1>Descriere ananas:</h1>"
    ret += f"<a href={url_for('index')}>[fructe]</a> | "
    ret += f"<a href={url_for('view_ananas')}>[ananas]</a> <br/> <br/>"
    ret += descriere

    return ret

    
@app.route('/acai', methods=['GET'])
def view_acai():
	culoare = culoare_acai()
	descriere = descriere_acai() 
	
	ret = "<h1>Acai</h1>"
	
	#Linkuri
	ret += f"<a href={url_for('index')}>[fructe]</a> | "
	ret += f"<a href={url_for('view_culoare_acai')}>[culoare]</a> | "
	ret += f"<a href={url_for('view_descriere_acai')}>[descriere]</a>"
	
	ret += "<h2>Descriere: </h2>"
	
	ret += descriere 
	
	ret += "<h2>Culoare: </h2>"
	ret += culoare
	
	
	
	return ret


@app.route('/acai/culoare', methods=['GET'])
def view_culoare_acai():
    culoare = culoare_acai()  
    
    ret = "<h1>Culoarea acai:</h1>"
    ret += f"<a href={url_for('index')}>[fructe]</a> | "
    ret += f"<a href={url_for('view_acai')}>[acai]</a> <br/> <br/>"
    ret += culoare
    
    return ret

@app.route('/acai/descriere', methods=['GET'])
def view_descriere_acai():
    descriere = descriere_acai()  
    
    ret = "<h1>Descriere acai:</h1>"
    ret += f"<a href={url_for('index')}>[fructe]</a> | "
    ret += f"<a href={url_for('view_acai')}>[acai]</a> <br/> <br/>"
    ret += descriere
    
    return ret
    
    
    
if __name__ == '__main__':
    app.run(host='127.0.0.1')
