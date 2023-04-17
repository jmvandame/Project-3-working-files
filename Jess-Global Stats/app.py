from flask import Flask, jsonify
from flask_cors import CORS
import numpy as np
import sqlalchemy
import pandas as pd
from sqlite3 import connect
from sqlalchemy import create_engine
import psycopg2
import sqlite3
import geoalchemy2
# from flask_sqlalchemy import SQLAlchemy
# 2. Create an app, being sure to pass __name__
app = Flask(__name__)
CORS(app)
@app.route("/")
def welcome():
    """List of all the available routes"""
    return(
        f"Available Routes for Global Covid-19 Vaccine Data:<br/>"
        f"/api/v1.0/Country<br/>"        
    )
@app.route("/api/v1.0/Country")
def Country():
    engine = create_engine('postgresql://postgres:addycole#422@localhost/world_vaccination_data')
    conn = engine.connect()
    result = conn.execute('select * from global_vaccine')
    data = [dict(row) for row in result]
    conn.close()
    return jsonify(data)
    
    
    
if __name__ == "__main__":
    app.run(debug=True)
    
    
    