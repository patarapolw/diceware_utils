import os

from webdemo import dicewareapp

if __name__ == '__main__':
    if 'DYNO' in os.environ:
        dicewareapp.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    else:
        dicewareapp.run(host='localhost', port=8080, debug=True)
