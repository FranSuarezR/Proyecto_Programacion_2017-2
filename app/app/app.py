from flask import Flask, render_template, request, redirect, url_for, session
import time
import requests
app = Flask(__name__)
app.config.update(DEBUG=True, SECRET_KEY='1234', USERNAME='Admin', PASSWORD='ALL')
@app.route('/', methods = ['GET','POST']) 
def regist():
	"""
	Descripcion: Pagina principal de la pagina web, esta enlazada al HTML "main.html", en esta pestaña se encuantra el registro y el inicio de sesion
	entrada: recibe los datos desde el html, estos datos son los usuarios y las contraseñas
	"""
	error1 = ''
	error2 = ''
	bien = ''
	if(request.method == "POST"):
#Aqui empieza el codigo del registro de usuarios
		if(request.form['ONE'] == "Registrarse"):
			if(request.form['username'] != "" and request.form['password'] != ""):
				if(request.form['password'] == request.form['password2']):
					usr = open("usuarios.txt", "r")
					pswr = open("contrasenas.txt", "r")
					for item in usr.readlines():
						if not item[:-1] == request.form["username"]:
							Usuarios = open("usuarios.txt", "a")
							Contrasenas = open("contrasenas.txt", "a")
							Usuarios.write(request.form["username"]+'\n')
							Contrasenas.write(request.form["password"]+'\n')
							bien = 'Su usuario se registro exitosamente'
							file = open("ArchivosContactos/contactos_"+str(request.form['username'])+".txt", "w")
							file.close()
							session['user'] = request.form['username']
							return redirect(url_for("chat"))
						else:
							error2 = 'El usuario ya se encuantra en uso'
							return render_template("main.html", error2=error2, bien=bien)
				else:
					error2 = 'Las contraseñas no coinciden'
					return render_template("main.html", error2=error2, bien=bien)
			else:
				error2 = 'Debe llenar los campos vacios'
				return render_template("main.html", error2=error2, bien=bien)
#Aqui empiza el codigo del inicio de sesion
		if request.form['ONE'] == "Entrar":
			if(request.form['username2'] != "" and request.form['password3'] != ""):
				if(request.form['username2'] != "" and request.form['password3'] != ""):
					usr2 = open("usuarios.txt", "r")
					pswr2 = open("contrasenas.txt", "r")
					texto1 = usr2.readlines()
					texto2 = pswr2.readlines()
					usr2.close()
					pswr2.close()
					a = request.form['username2']
					b = request.form['password3']
					session['user'] = request.form['username2']
					lista_usr = []
					i = 0
					while(i < len(texto1)):
						frase = texto1[i]
						i = i + 1
						lista_usr = lista_usr + frase.split("\n")
					lista_pswr = []
					k = 0
					while(k < len(texto2)):
						frase2 = texto2[k]
						k = k + 1
						lista_pswr = lista_pswr + frase2.split("\n")
					if(a in lista_usr):
						if(b in lista_pswr):
							if(lista_usr.index(a) == lista_pswr.index(b)):
								return redirect(url_for("chat"))
							else:
								error1 = "Usuario o contrasena incorrectos, intente de nuevo"
								return render_template("main.html", error=error1, bien=bien)
						else:
							error1 = "Usuario o contrasena incorrectos, intente de nuevo"
							return render_template("main.html", error1=error1, bien=bien)
					else:
						error1 = "Usuario o contrasena incorrectos, intente de nuevo"
						return render_template("main.html", error1=error1, bien=bien)
				else:
					error1 = "Usuario o contrasena incorrectos, intente de nuevo"
					return render_template("main.html", error1=error1, bien=bien)
			else:
				error1 = 'Debe llenar los campos vacios'
				return render_template("main.html", error1=error1, bien=bien)
	return render_template("main.html", error1=error1, bien=bien, error2=error2)

@app.route('/chat', methods = ['GET','POST']) 
def chat():
	"""
	Descripcion: pagina en a cual se encuentra el chat, esta enlazada a l HTML "chat.html", en esta pagina se puede escoger con que usuario se quiere chatear, aparacere el chat
	entrada: mensajes que el usuario quiera enviar, usuario con el que el usuario quiere chatear
	"""
	contactos = []
	nlist2 = []
	User = open("ArchivosContactos/contactos_"+str(session['user'])+".txt", "r")
	U = User.readlines()
	User.close()
	for usrs in U:
		contactos.append(usrs[:-1])
	if(request.method == "POST"):
		if(request.form['TWO'] == "Enviar"):
			pass
		if(request.form['TWO'] == "+"):
			return redirect(url_for("add"))
		if(request.form['TWO'] == "X"):
			session.pop('user', None)
			return redirect(url_for("regist"))
		if(request.form['contacto_chat'] != ""):
			nlist2 = []
			ntemp = []
			J = open("ArchivosChat/"+str(request.form['contacto_chat'])+"_"+str(session['user'])+".txt", "a")
			J.close()
			J = open("ArchivosChat/"+str(request.form['contacto_chat'])+"_"+str(session['user'])+".txt", "r")
			j = J.readlines()
			J.close()
			for s in j:
				ntemp.append(s[:-1])
			if(ntemp == []):
				f = open("ArchivosChat/"+str(session['user'])+"_"+str(request.form['contacto_chat'])+".txt", "r")
				G = f.readlines()
				f.close()
				for i in G:
					nlist2.append(i[:-1])
			else:
				f = open("ArchivosChat/"+str(request.form['contacto_chat'])+"_"+str(session['user'])+".txt", "r")
				G = f.readlines()
				f.close()
				for i in G:
					nlist2.append(i[:-1])
			f = open("ArchivosChat/"+str(session['user'])+"_"+str(request.form['contacto_chat'])+".txt", "a")
			f.close()
			if(request.form['TWO'] == "Enviar"):
				if(request.form['mensaje']!= ""):
					nlist2 = []
					ntemp = []
					J = open("ArchivosChat/"+str(request.form['contacto_chat'])+"_"+str(session['user'])+".txt", "a")
					J.close()
					J = open("ArchivosChat/"+str(request.form['contacto_chat'])+"_"+str(session['user'])+".txt", "r")
					j = J.readlines()
					J.close()
					for s in j:
						ntemp.append(s[:-1])
					if(ntemp == []):
						msj = open("ArchivosChat/"+str(session['user'])+"_"+str(request.form['contacto_chat'])+".txt", "a")
						message = (request.form['mensaje'])
						local = requests.get('http://ip-api.com/json/').json()
						L = local['country']
						msj.write(str(message) + "(Hora de envío: " + str(time.strftime("%H:%M:%S")) + ",Fecha: " + str(time.strftime("%d/%m/%Y")) + ", Lugar: " + str(L) + ")" + '\n')
						msj.close()
						f = open("ArchivosChat/"+str(session['user'])+"_"+str(request.form['contacto_chat'])+".txt", "r")
						G = f.readlines()
						f.close()
						for i in G:
							nlist2.append(i[:-1])
					else:
						msj = open("ArchivosChat/"+str(request.form['contacto_chat'])+"_"+str(session['user'])+".txt", "a")
						message = (request.form['mensaje'])
						local = requests.get('http://ip-api.com/json/').json()
						L = local['country']
						msj.write(str(message) + "(Hora de envío: " + str(time.strftime("%H:%M:%S")) + ",Fecha: " + str(time.strftime("%d/%m/%Y")) + ", Lugar: " + str(L) + ")" + '\n')
						msj.close()
						f = open("ArchivosChat/"+str(request.form['contacto_chat'])+"_"+str(session['user'])+".txt", "r")
						G = f.readlines()
						f.close()
						for i in G:
							nlist2.append(i[:-1])
					#return redirect(url_for("chat", contactos=contactos, nlist2=nlist2))
				else:
					return render_template("chat.html", contactos=contactos, nlist2=nlist2)
	return render_template("chat.html", contactos=contactos, nlist2=nlist2)

@app.route('/add', methods = ['GET','POST']) 
def add():
	"""
	Descripcion: pagina para añadir contactos, esta enlazada con el HTML "Add.html", en esta pagina aparecen todos los usuarios registrados, se tiene que escribir el nombre del usuario deseado para añadirlo a la lista de usuarios
	entrada: nombre del usuario que se va a agregar
	"""
	nlist = []
	b = ''
	User = open("usuarios.txt", "r")
	U = User.readlines()
	User.close()
	for usrs in U:
		nlist.append(usrs[:-1])
	b = nlist
	if(request.method == "POST"):
		if(request.form['TWO'] == "X"):
			return redirect(url_for("chat"))
		if(request.form['THREE'] == "Agregar" and request.form['agregar'] != ""):
			usuarios = []
			User = open("usuarios.txt", "r")
			U = User.readlines()
			User.close()
			for usrs in U:
				usuarios.append(usrs[:-1])
			contacto = request.form['agregar']
			if(contacto in b):
				f = open("ArchivosContactos/contactos_"+str(session['user'])+".txt", "a")
				f.write(str(contacto) + '\n')
				f.close()
			else:
				return render_template("Add.html", b=b)
		else:
			return render_template("Add.html", b=b)
	return render_template("Add.html", b=b)

if __name__ == '__main__':
	app.run(debug=True)