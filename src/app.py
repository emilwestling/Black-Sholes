from src.Blacksholes import heatmap_gen
from flask import Flask, render_template, request
import matplotlib
matplotlib.use('Agg')

app = Flask(__name__, template_folder='../templates',
            static_folder='../static')


@app.route('/', methods=['GET', 'POST'])
def index():
    # Default values
    K = 100
    r = 0.05
    sigma = 0.2

    if request.method == 'POST':
        K = float(request.form.get('K', K))
        r = float(request.form.get('r', r))
        sigma = float(request.form.get('sigma', sigma))

    # Generate the heatmaps
    call_img_base64 = heatmap_gen(K, r, sigma, 'call')
    put_img_base64 = heatmap_gen(K, r, sigma, 'put')

    return render_template('index.html',
                           call_heatmap=call_img_base64,
                           put_heatmap=put_img_base64,
                           K=K,
                           r=r,
                           sigma=sigma)


if __name__ == '__main__':
    app.run(debug=True)
