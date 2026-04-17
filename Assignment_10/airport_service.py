from flask import Flask, jsonify

app = Flask(__name__)

# Sample database (replace with real dataset if available)
airports = {
    "LFLL": {"name": "Lyon Saint-Exupery Airport", "city": "Lyon", "country": "FR"},
    "KJFK": {"name": "John F Kennedy International Airport", "city": "New York", "country": "US"}
}

@app.route("/airport/<icao>")
def get_airport(icao):
    airport = airports.get(icao.upper())
    if airport:
        return jsonify({
            "icao": icao.upper(),
            "name": airport["name"],
            "city": airport["city"],
            "country": airport["country"]
        })
    else:
        return jsonify({"error": "Airport not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
