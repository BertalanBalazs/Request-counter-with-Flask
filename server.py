from flask import Flask, redirect, render_template
app = Flask(__name__)

counts = {
    'GET': 0,
    'POST': 0,
    'DELETE': 0,
    'PUT': 0
}

@app.route('/')
def route_main():
    return render_template('index.html', counts=counts)


@app.route('/request-counter')
def route_request_counter():
    global counts
    if request
    counts
    return redirect('/')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        debug=True,
    )