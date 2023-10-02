from flask import Flask,render_template , jsonify


app = Flask(__name__)


JOBS = [
     {
          'id' :1,
          'title': 'Data Scientist',
          'location': 'Islamabad, Pakistan',
          'salary': '100,000',  
     },
     {
          'id' :2,
          'title': 'Data Analyst',
          'location': 'Lahore, Pakistan',
          'salary': '70,000',  
     },
     {
          'id' :3,
          'title': 'Frontend Developer',
          'location': 'Taxila, Pakistan',
          'salary': '60,000',  
     },
     {
          'id' :4,
          'title': 'full Stack Developer',
          'location': 'Rawalpindi, Pakistan',
          'salary': '$5,000',  
     }
]


 
@app.route('/')
def hello_world():
     return render_template('home.html',
                            jobs = JOBS)
     
@app.route('/jobs')
def list_jobs():
     return jsonify(JOBS)
 
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0' )