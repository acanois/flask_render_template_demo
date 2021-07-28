from flask import Flask, render_template, jsonify, request

from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

app = Flask(__name__)

engine = create_engine('sqlite:///hawaii.sqlite')
Base = automap_base()
Base.prepare(engine, reflect=True)
session = Session(engine)

station_table = Base.classes.station

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/get-all-stations', methods=['GET'])
def get_all_stations():
    stations = session.query(station_table).all()
    session.close()
    res_object = []  # Empty response object
    for station in stations:
        print(station)
        res_object.append({
            'id': station.id,
            'station': station.station,
            'name': station.name,
            'prcp': station.latitude,
            'tobs': station.longitude,
        })

    return render_template('display_data.html', res_object=res_object)

if __name__ == "__main__":
    app.run(debug=True)