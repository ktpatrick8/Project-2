from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import PyMongo
from sqlalchemy import create_engine
import sqlalchemy

rds_connection_string = f"postgres://zsjitnfqerggpe:27480e06806e4393e3e237d266c536ba9b0f7408ac6272551cfa665e694de859@ec2-52-204-113-104.compute-1.amazonaws.com:5432/d63qhs1d38oqh0"
engine = create_engine(f'postgres://zsjitnfqerggpe:27480e06806e4393e3e237d266c536ba9b0f7408ac6272551cfa665e694de859@ec2-52-204-113-104.compute-1.amazonaws.com:5432/d63qhs1d38oqh0')

# Create an instance of Flask
app = Flask(__name__)

# Route to render index.html template using 
@app.route("/")
def welcome():
    return (
        f"Available Routes:<br/>"
        f"/year2015<br/>"
        f"/year2016<br/>"
        f"/year2017<br/>"
        f"/year2018<br/>"
        f"/year2019<br/>"
    )

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

if __name__ == "__main__":
    app.run(debug=True)
