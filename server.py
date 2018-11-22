from flask import Flask, redirect, render_template, request


app = Flask(__name__)


@app.route('/')
def route_main():
    return render_template('index.html')


@app.route('/request-counter', methods=['GET', 'POST', 'DELETE', 'PUT'])
def route_request_counter():
    counts = import_data()
    counts[request.method] += 1
    export_data(counts)
    return redirect('/')


@app.route('/statistics')
def route_statistic():
    counts = import_data()
    return render_template('statistics.html',counts=counts)



def export_data(dict):
    with open('request_counts.txt', 'w') as data:
        for key, value in dict.items():
            data.write(f'{key}: {value}\n')



def import_data():
    d = {}
    with open("request_counts.txt") as f:
        for line in f:
            key, val = line.strip().split(':', 1)
            d[key] = int(val)
    print(d)
    return d


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        debug=True,
    )