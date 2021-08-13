from flask import Flask, render_template, redirect

# Configure application
app = Flask(__name__)

proj = [
    {
        'image': "https://upload.wikimedia.org/wikipedia/commons/3/31/Seal_of_the_Metropolitan_Police_Department_of_the_District_of_Columbia.svg",
        'description' : 'My first interactive dashboard. Metropolitan Police Department Data Dashboard showcasing arrest and stop public data.',
        'link' : "https://mpd-dash-app.herokuapp.com/",
        'title' : 'MPD Data Dashboard',
        'small_text':'long load time',
        'github':'https://github.com/AlexGhanem/MPD_analysis'
    },
    {
        'image': "https://www.svgrepo.com/show/261900/presentation-financial.svg",
        'description' : 'A dashboard that summarizes financial data from multiple APIs for any given S&P 500 company. More features coming soon.',
        'link' : "https://financials-dash.herokuapp.com/",
        'title' : 'Financial Dashboard',
        'github':'https://github.com/AlexGhanem/financial_dash',
    },
    {
        'image': "https://pic.onlinewebfonts.com/svg/img_463275.png",
        'description' : 'My first fully coded and fully loaded portfolio website built from scratch using the Flask framework, HTML and CSS (with a dash of Bootstrap).',
        'link' : "/",
        'title' : 'Personal Website',
        'github':'https://github.com/AlexGhanem/personal_website'
    },
     {
        'image': "https://firms.modaps.eosdis.nasa.gov/images/lance_logo.png",
        'description' : "First project using Google Studio's seamless integration with BigQuery. The data consists of 13million+ fire incidents from 2018 to 2020 which made BigQuery the ideal home for such a large dataset.",
        'link' : "/fires",
        'title' : "NASA FIRMS fire data dashboard",
        'github':''
    },
]


@app.route('/', methods=['GET', 'POST']) 
def home():
    greeting = "Welcome to Alex's Portoflio"
    return render_template('home.html', greeting=greeting)


@app.route('/projects')
def projects():
    return render_template('projects.html', projects=proj)

@app.route('/timeline')
def timeline():
    return render_template('timeline.html')

@app.route('/fires')
def fires_page():
    return render_template('fires.html')

if __name__ == "__main__":
    app.run(debug=True)
