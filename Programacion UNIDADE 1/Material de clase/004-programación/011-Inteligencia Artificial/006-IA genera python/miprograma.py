from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    base_imponible = ''
    iva = ''
    total = ''
    error = ''

    if request.method == 'POST':
        cantidad = request.form.get('cantidad', type=float)
        tipo_iva = request.form.get('tipo_iva')

        if cantidad is None or cantidad <= 0:
            error = 'La cantidad debe ser un número mayor que cero.'
        else:
            if tipo_iva == '4':
                iva = cantidad * 0.04
            elif tipo_iva == '10':
                iva = cantidad * 0.10
            elif tipo_iva == '21':
                iva = cantidad * 0.21
            else:
                error = 'Selecciona un tipo de IVA válido.'

            base_imponible = cantidad
            total = base_imponible + iva

    html = '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Calculadora de IVA</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                margin: 0;
                padding: 0;
            }
            .container {
                width: 80%;
                margin: 50px auto;
                background-color: #fff;
                padding: 20px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            h1 {
                text-align: center;
                color: #333;
            }
            form {
                display: flex;
                flex-direction: column;
                align-items: center;
            }
            label {
                margin-top: 10px;
                font-size: 16px;
                color: #555;
            }
            input, select {
                padding: 10px;
                margin-top: 5px;
                width: 80%;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            button {
                padding: 10px 20px;
                margin-top: 20px;
                background-color: #28a745;
                color: #fff;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
            button:hover {
                background-color: #218838;
            }
            .result {
                margin-top: 20px;
                font-size: 18px;
                color: #333;
            }
            .error {
                margin-top: 20px;
                font-size: 16px;
                color: #dc3545;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Calculadora de IVA</h1>
            <form method="post">
                <label for="cantidad">Cantidad:</label>
                <input type="number" id="cantidad" name="cantidad" step="0.01" required>
                <label for="tipo_iva">Tipo de IVA:</label>
                <select id="tipo_iva" name="tipo_iva" required>
                    <option value="4">4%</option>
                    <option value="10">10%</option>
                    <option value="21">21%</option>
                </select>
                <button type="submit">Calcular</button>
            </form>
            {% if error %}
                <div class="error">{{ error }}</div>
            {% endif %}
            {% if base_imponible and iva and total %}
                <div class="result">
                    Base Imponible: {{ base_imponible }}<br>
                    IVA: {{ iva }}<br>
                    Total: {{ total }}
                </div>
            {% endif %}
        </div>
    </body>
    </html>
    '''

    return render_template_string(html, base_imponible=base_imponible, iva=iva, total=total, error=error)

if __name__ == "__main__":
    app.run(debug=True)
