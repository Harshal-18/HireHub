from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Software Engineer',
        'location': 'New York, NY',
        'salary': '$120,000 - $150,000',
        'description': 'Develop and maintain web applications.'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'San Francisco, CA',
        'salary': '$130,000 - $160,000',
        'description': 'Analyze and interpret complex data sets.'
    },
    {
        'id': 3,
        'title': 'Product Manager',
        'location': 'Remote',
        'salary': '$110,000 - $140,000',
        'description': 'Lead product development teams.'
    }
]


@app.route("/")
def hello_world():
    return render_template("home.html", jobs=JOBS, company_name="HireHub") 

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=2000, debug=True)