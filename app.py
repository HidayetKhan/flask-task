from flask import Flask,jsonify
app = Flask(__name__)

@app.route('/check_odd_even/<int:number>',methods=['GET'])
def odd_even(number):
    res={'number':number,'type':'even' if number % 2 == 0 else 'odd'}
    return jsonify(res)


if __name__=='__main__':
    app.run(debug=True,port=5000)