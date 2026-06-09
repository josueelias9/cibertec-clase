
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    # Cargar contador
    f = open("count.txt", "r")
    count = int(f.read())
    f.close()
    # Incrementar el contador
    count += 1
    # Actualizar
    f = open("count.txt", "w")
    f.write(str(count))
    f.close()
    # Pasar la variable actualizada a index.html
    return render_template("index.html", count=count)

@app.route("/ejemplo-json")
def ejemplo_json():
    return {"mensaje": "Hola, este es un ejemplo de respuesta JSON"}



@app.route("/mostrar-blog")
def mostrar_blog():
    return render_template("base.html")

if __name__ == "__main__":
    app.run()

