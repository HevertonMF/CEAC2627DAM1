from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculadora de IVA</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
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
            color: #333;
        }
        form {
            display: flex;
            flex-direction: column;
        }
        label {
            margin-top: 10px;
        }
        input, select {
            padding: 10px;
            margin-top: 5px;
        }
        button {
            padding: 10px;
            margin-top: 20px;
            background-color: #28a745;
            color: #fff;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #218838;
        }
        .result {
            margin-top: 20px;
            font-size: 1.2em;
            color: #333;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Calculadora de IVA</h1>
        <form method="post">
            <label for="amount">Cantidad:</label>
            <input type="number" id="amount" name="amount" step="0.01" required>
            <label for="iva">IVA:</label>
            <select id="iva" name="iva" required>
                <option value="4">4%</option>
                <option value="10">10%</option>
                <option value="21">21%</option>
            </select>
            <button type="submit">Calcular</button>
        </form>
        {% if result %}
        <div class="result">
            <p>Base Imponible: {{ result.base_imponible }}</p>
            <p>IVA: {{ result.iva }}</p>
            <p>Total: {{ result.total }}</p>
        </div>
        {% endif %}
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        amount = request.form['amount']
        iva = request.form['iva']
        if amount.isdigit():
            amount = float(amount)
            base_imponible = amount / (1 + float(iva) / 100)
            iva_amount = amount - base_imponible
            total = amount
            result = {
                'base_imponible': f'{base_imponible:.2f}',
                'iva': f'{iva_amount:.2f}',
                'total': f'{total:.2f}'
            }
        else:
            result = {'error': 'Introduce un número válido'}
    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(debug=True)
