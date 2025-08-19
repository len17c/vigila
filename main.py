import os
import time
from flask import *

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def inicio():
  datos = []
  if request.method == "POST":
    vig = request.form['id']
    sec = request.form['seccion']
    est = request.form['estado']
    ano = request.form['anotaciones']
    guardar(vig, sec, est, ano)
    
  return render_template("index.html")

@app.route("/resumen")
def resumen():
  datos = []
  archivo = open('log.csv', 'r')
  for linea in archivo:
    dato = linea.split(';')
    datos.append({"fecha": dato[0], "vigilante": dato[1], "seccion": dato[2], "estado": dato[3], "anotacion": dato[4]})
  archivo.close()
  return render_template("resumen.html", datos = datos)

def guardar(a, b, c, d):
  fecha = time.strftime("%d/%m/%Y %H:%M:%S")
  archivo = open('log.csv', 'a')
  archivo.write(f'{fecha};{a};{b};{c};{d}\n')
  archivo.close()

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))