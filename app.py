from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analytics',
    'location': 'Pune, India',
    'salary': 'Rs. 1,00,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Banglore, India'
  },
  {
    'id': 3,
    'title': 'Web Developer',
    'location': 'delhi, India'
  },
  {
    'id': 4,
    'title': 'PHP developer',
    'location': 'Mumbai, India',
    'salary': 'Rs. 3,00,000'
  },
]


@app.route("/")
def hello_harshal():
  return render_template('home.html', jobs=JOBS, page_name='Sample')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
