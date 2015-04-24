from flask import Flask
from flask import render_template
from kmeans import KMeans
from flask import request
import json

app = Flask(__name__)
app.debug = True


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/urf/')
def urf_games():
    my_kmeans = KMeans()
    results = []
    results.append({"Control: Wards placed/Wards destroyed" : my_kmeans.calculate('control')})
    results.append({'Damage: Physical/Magic/True' : my_kmeans.calculate('damage')})
    results.append({'Economy: Gold Earned/Gold Spent' : my_kmeans.calculate('economy')})
    results.append({'Kills: Kills/Deaths/Assists' : my_kmeans.calculate('kills')})
    results.append({'Multi Kills: Combo Kills/Killing Sprees/Largest Killing Spree': my_kmeans.calculate('multi_kills')})

    return render_template('results.html', data=results)

@app.route('/results/', methods=['POST'])
def games():
    print request.form['stats']
    my_kmeans = KMeans(request.form['stats'])
    results = []
    results.append({"Control: Wards placed/Wards destroyed" : my_kmeans.calculate('control')})
    results.append({'Damage: Physical/Magic/True' : my_kmeans.calculate('damage')})
    results.append({'Economy: Gold Earned/Gold Spent' : my_kmeans.calculate('economy')})
    results.append({'Kills: Kills/Deaths/Assists' : my_kmeans.calculate('kills')})
    results.append({'Multi Kills: Combo Kills/Killing Sprees/Largest Killing Spree': my_kmeans.calculate('multi_kills')})

    return render_template('results.html', data=results)



if __name__ == '__main__':
    app.run()
