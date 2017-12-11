from flask import Flask, render_template
import serial, time, json

ser = serial.Serial('COM3', 115200)

app = Flask(__name__)
#COUNT = 5

@app.route("/")
def hello():
    return render_template("Webpage.html")

@app.route("/temp")
def serial1():
	# f = open('data.txt','r')
	# data = f.read()
	# f.close()
	ser.write("{'topic':'value'}")
	time(0.01)
    data = ser.readline()
    return json.dumps({"temp":data})

@app.route("/H")
def contolon():
    ser = serial.Serial('COM6', 9600)
    time.sleep(1)
    ser.write('H')
    print "HIGH\n"
    return "LED ON"

@app.route("/L")
def controloff():
    ser = serial.Serial('COM6', 9600)
    time.sleep(1)
    ser.write('L')
    print "LOW\n"
    return "LED OFF"

def get_value():
	return json.dumps()

if __name__ == "__main__":
    app.run()

