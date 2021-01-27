from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import PyMongo
from sqlalchemy import create_engine
import sqlalchemy

#################################################
# Database Setup
#################################################

rds_connection_string = f"postgres://zsjitnfqerggpe:27480e06806e4393e3e237d266c536ba9b0f7408ac6272551cfa665e694de859@ec2-52-204-113-104.compute-1.amazonaws.com:5432/d63qhs1d38oqh0"
engine = create_engine(f'postgres://zsjitnfqerggpe:27480e06806e4393e3e237d266c536ba9b0f7408ac6272551cfa665e694de859@ec2-52-204-113-104.compute-1.amazonaws.com:5432/d63qhs1d38oqh0')

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

# Route to render index.html template using 
@app.route("/", methods=["GET"])
def home():
    return render_template('index2.html')

@app.route("/year2015")
def year2015():
    result = {}
    result_set = engine.execute('select * from year2015')
    countries = []
    for row in result_set:
        data = {}
        data['Name'] = row.country
        data["Rank"] = row.happiness_rank
        data["Score"] = row.happiness_score
        data["Economy"] = row.economy
        data['Family'] = row.family
        data['Health'] = row.health
        data['Freedom'] = row.freedom
        data['Trust'] = row.trust
        data['Generosity'] = row.generosity

        # countries['Countries'] = data
        countries.append(data)


    result["Countries"] = countries

    return jsonify(result)

@app.route("/year2016")
def year2016():
    result = {}
    result_set = engine.execute('select * from year2016')
    countries = []
    for row in result_set:
        data = {}
        data['Name'] = row.country
        data["Rank"] = row.happiness_rank
        data["Score"] = row.happiness_score
        data["Economy"] = row.economy
        data['Family'] = row.family
        data['Health'] = row.health
        data['Freedom'] = row.freedom
        data['Trust'] = row.trust
        data['Generosity'] = row.generosity

        countries.append(data)


    result["Countries"] = countries

    return jsonify(result)

@app.route("/year2017")
def year2017():
    result = {}
    result_set = engine.execute('select * from year2017')
    countries = []
    for row in result_set:
        data = {}
        data['Name'] = row.country
        data["Rank"] = row.happiness_rank
        data["Score"] = row.happiness_score
        data["Economy"] = row.economy
        data['Family'] = row.family
        data['Health'] = row.health
        data['Freedom'] = row.freedom
        data['Trust'] = row.trust
        data['Generosity'] = row.generosity

        countries.append(data)


    result["Countries"] = countries

    return jsonify(result)

@app.route("/year2018")
def year2018():
    result = {}
    result_set = engine.execute('select * from year2018')
    countries = []
    for row in result_set:
        data = {}
        data['Name'] = row.country
        data["Rank"] = row.happiness_rank
        data["Score"] = row.happiness_score
        data["Economy"] = row.economy
        data['Family'] = row.family
        data['Health'] = row.health
        data['Freedom'] = row.freedom
        data['Trust'] = row.trust
        data['Generosity'] = row.generosity

        countries.append(data)


    result["Countries"] = countries

    return jsonify(result)

@app.route("/year2019")
def year2019():
    result = {}
    result_set = engine.execute('select * from year2019')
    countries = []
    for row in result_set:
        data = {}
        data['Name'] = row.country
        data["Rank"] = row.happiness_rank
        data["Score"] = row.happiness_score
        data["Economy"] = row.economy
        data['Family'] = row.family
        data['Health'] = row.health
        data['Freedom'] = row.freedom
        data['Trust'] = row.trust
        data['Generosity'] = row.generosity

        countries.append(data)


    result["Countries"] = countries

    return jsonify(result)

@app.route("/happiness")
def happiness():
    result = {}
    result_set = engine.execute('''select * from year2015 \
        UNION select * from year2016\
        UNION select * from year2017\
        ORDER BY country''')
    countries = []
    for row in result_set:
        if row.country in countries:
            ""
        else:
            countries.append(row.country)
    result["Countries"] = countries           
    for row in result_set:
        data = {}
        data['Year'] = row.year
        data['Name'] = row.country
        data["Rank"] = row.happiness_rank
        data["Score"] = row.happiness_score
        data["Economy"] = row.economy
        data['Family'] = row.family
        data['Health'] = row.health
        data['Freedom'] = row.freedom
        data['Trust'] = row.trust
        data['Generosity'] = row.generosity
        countries.append(data)
    # result["Countries"] = countries 

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
