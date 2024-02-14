from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        apellido = request.form.get("apellido")

        try:
            numero1 = float(request.form.get("numero1"))
            numero2 = float(request.form.get("numero2"))

            suma = numero1 + numero2
            resta = numero1 - numero2
            producto = numero1 * numero2
            division = numero1 / numero2 if numero2 != 0 else "Error: División por cero"
        except ValueError:
            return render_template("error.html", message="Por favor, ingresa números válidos.")

        saludo = f"Hola, {nombre} {apellido}! Es un placer saludarte."

        return render_template("resultado.html", saludo=saludo, suma=suma, resta=resta, producto=producto, division=division)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
