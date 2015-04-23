from flask import Flask
from flask import render_template
from kmeans import KMeans
import json

app = Flask(__name__)
app.debug = True


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/urf/')
def urf_games():
    print "problems in the jungle"

    my_kmeans = KMeans()
    results = []
    results.append({"Control" : my_kmeans.calculate('control')})
    results.append({'Damage' : my_kmeans.calculate('damage')})
    results.append({'Economy' : my_kmeans.calculate('economy')})
    results.append({'Kils' : my_kmeans.calculate('kills')})
    results.append({'Multi Kills': my_kmeans.calculate('multi_kills')})

    return render_template('urf.html', data=results)


if __name__ == '__main__':
    app.run()
