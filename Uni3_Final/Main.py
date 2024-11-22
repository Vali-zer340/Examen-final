from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")
    
@app.route('/formu1', methods=['GET','POST'])
def formu1():
    resultado = None
    descuento15 = 15
    descuento25 = 25
    if request.method == 'POST':
        dato1 = request.form.get('dato1')
        dato2 = request.form.get('dato2')
        dato3 = request.form.get('dato3')
    
        if not (dato1 and dato2 and dato3):
            resultado = {"error": "Por favor completa todos los campos."}
        else:
            try:
                dato2 = int(dato2)
                dato3 = int(dato3)
                resultado = procesar_dato1(dato1,dato2,dato3,descuento15,descuento25)
            except ValueError:
                resultado = {'Error': 'Ingresa valor valido'}
    
    return render_template('formulario1.html', resultado = resultado)

@app.route("/formu2", methods=['GET','POST'])
def formu2():   
    resultado = None
    if request.method == 'POST':
        dato4 = request.form.get('dato4')
        dato5 = request.form.get('dato5')

        if dato4 and dato5:
            resultado = resultado = procesar_dato2(dato4, dato5)
        else:
            resultado = "Por favor, completa todos los campos."
    
    return render_template('formulario2.html', resultado=resultado)




def procesar_dato1(dato1,dato2,dato3,descuento15,descuento25):
        
        precio_por_tarro = 9000
        total_sin_descuento = dato3 * precio_por_tarro
        descuento_calculado = 0

        if dato2 >= 18 and dato2 <= 30:
            descuento_calculado = (total_sin_descuento * descuento15) / 100
        else:
            if dato2 > 30:
                descuento_calculado = (total_sin_descuento * descuento25) / 100


        total_con_descuento = total_sin_descuento - descuento_calculado

        return {
        "nombre": dato1,
        "total_sin_descuento": total_sin_descuento,
        "descuento": descuento_calculado,
        "total_con_descuento": total_con_descuento,
    }





def procesar_dato2(dato4,dato5):
    

    juan = 'Bienvenido administrador Juan'

    pepe = 'Bienvenido Usuario Pepe'

    if dato4 == 'juan' and dato5 == 'admin':
        return juan
    else:
        if dato4 == 'pepe' and dato5 == 'user':
            return pepe
        else:
            return 'Usuario o Contraseña Incorrectos'

if __name__ == '__main__':
    app.run()
