from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    base_imponible = ''
    iva = ''
    total = ''
    error = ''

    if request.method == 'POST':
        cantidad = request.form.get('cantidad', type=float)
        iva_rate = request.form.get('iva_rate', type=float)

        if cantidad is None or iva_rate is None:
            error = 'Por favor, introduce una cantidad y selecciona un IVA.'
        elif cantidad < 0:
            error = 'La cantidad no puede ser negativa.'
        elif iva_rate not in (4, 10, 21):
            error = 'El IVA debe ser 4%, 10% o 21%.'
        else:
            base_imponible = cantidad
            iva = cantidad * iva_rate / 100
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
                max-width: 500px;
                margin: 50px auto;
                background-color: #fff;
                padding: 20px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            .form-group {
                margin-bottom: 15px;
            }
            .form-group label {
                display: block;
                margin-bottom: 5px;
            }
            .form-group input, .form-group select {
                width: 100%;
                padding: 8px;
                box-sizing: border-box;
            }
            .form-group button {
                width: 100%;
                padding: 10px;
                background-color: #28a745;
                color: #fff;
                border: none;
                cursor: pointer;
            }
            .form-group button:hover {
                background-color: #218838;
            }
            .result {
                margin-top: 20px;
                font-size: 1.2em;
                color: #333;
            }
            .error {
                margin-top: 20px;
                font-size: 1.2em;
                color: #dc3545;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Calculadora de IVA</h1>
            <form method="post">
                <div class="form-group">
                    <label for="cantidad">Cantidad (sin IVA):</label>
                    <input type="number" id="cantidad" name="cantidad" step="0.01" min="0" required>
                </div>
                <div class="form-group">
                    <label for="iva_rate">IVA:</label>
                    <select id="iva_rate" name="iva_rate" required>
                        <option value="4">4%</option>
                        <option value="10">10%</option>
                        <option value="21">21%</option>
                    </select>
                </div>
                <div class="form-group">
                    <button type="submit">Calcular</button>
                </div>
            </form>
            {% if error %}
                <div class="error">{{ error }}</div>
            {% endif %}
            {% if total != '' %}
                <div class="result">
                    <p>Base Imponible: {{ "%.2f"|format(base_imponible) }} €</p>
                    <p>IVA: {{ "%.2f"|format(iva) }} €</p>
                    <p>Total: {{ "%.2f"|format(total) }} €</p>
                </div>
            {% endif %}
        </div>
        <script>
            document.querySelector('form').addEventListener('submit', function(event) {
                const cantidad = parseFloat(document.getElementById('cantidad').value);
                const iva_rate = parseFloat(document.getElementById('iva_rate').value);
                if (isNaN(cantidad) || isNaN(iva_rate)) {
                    event.preventDefault();
                    alert('Por favor, introduce una cantidad y selecciona un IVA.');
                }
            });
        </script>
    </body>
    </html>
    '''

    return render_template_string(html, base_imponible=base_imponible, iva=iva, total=total, error=error)

if __name__ == "__main__":
    app.run(debug=True)