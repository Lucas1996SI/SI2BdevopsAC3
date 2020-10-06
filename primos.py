import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def nao_entre_em_panico():
    a = 100
    b = 1
    c = 1
    n = 3
    pr = '2,'

    while c < a:
        primo = 1
        for i in range(2, n):
            if n % i == 0:
                primo = 0
                break
        if(primo):
            pr = pr + str(n) + ','
            c += 1
            if(c % 10 == 0):
                pr = pr + '<br>'
        n += 1
    return pr

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
