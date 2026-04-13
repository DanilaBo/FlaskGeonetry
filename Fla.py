from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None

    if request.method == 'POST':
        try:
            shape = request.form['shape']
            precision = int(request.form.get('precision', 2))

            # Куб: V = a³
            if shape == 'cube':
                a = float(request.form['a'])
                result = a ** 3

            # Шар: V = 4/3 * π * r³
            elif shape == 'sphere':
                r = float(request.form['r'])
                result = (4 / 3) * 3.14159 * (r ** 3)

            # Цилиндр: V = π * r² * h
            elif shape == 'cylinder':
                r = float(request.form['r'])
                h = float(request.form['h'])
                result = 3.14159 * (r ** 2) * h

            result = round(result, precision)

        except (ValueError, KeyError):
            error = 'Ошибка: введите числа!'
        except Exception as e:
            error = f'Ошибка: {e}'

    return render_template('index.html', result=result, error=error)


if __name__ == '__main__':
    app.run(debug=True)