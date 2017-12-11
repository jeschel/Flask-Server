from flask import Flask, render_template
import serial, time, json

app = Flask(__name__)
#COUNT = 5


@app.route("/")
def hello():
    return render_template("Temperature.html")

@app.route("/temp")
def serial1():
    f = open('data.txt','r')
    data = f.read()
    f.close()
    return json.dumps({"temp":data})

@app.route("/H")
def contolon():
    ser = serial.Serial('COM6', 9600)
    ser.write('H')
    print "HIGH\n"
    time.sleep(1)
    return "LED ON"

@app.route("/L")
def controloff():
    ser = serial.Serial('COM6', 9600)
    ser.write('L')
    print "LOW\n"
    time.sleep(1)
    return "LED OFF"


if __name__ == "__main__":
    app.run()

