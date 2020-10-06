import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def nao_entre_em_panico():
    primos = "2"
    num =  3
    cont = 0
    primo = True
    while(cont < 99):
        for i in range(2, num-1, 1 ):
            if num % i == 0:
                primo = False
        if primo:
            primos += "," + str(num)
            cont += 1
            if(cont % 10 == 0):
                primos = primos + '<br>'
        num += 1
        primo = True

    return primos

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    #lucas
