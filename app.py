from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOBS = [{
 "id": 1,
 "title": "Data Scientist",
 "location": "Remote",
 "salary": "12000.00"
}, {
 "id": 2,
 "title": "Front Engineer",
 "location": "Remote",
 "salary": "12000.00"
}, {
 "id": 3,
 "title": "Back Engineer",
 "location": "Remote",
 "salary": "12000.00"
}]


@app.route("/")
def hello_jackie():
	return render_template('home.html', jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
	return jsonify(JOBS)


if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
