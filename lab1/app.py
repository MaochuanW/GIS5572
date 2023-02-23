import psycopg2
from flask import Flask, jsonify
from psycopg2 import sql
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

@app.route('/get_polygon', methods=['GET'])
def get_polygon():
    conn= psycopg2.connect(host = '35.223.186.20',
                             database = 'lab0',
                             user = 'postgres',
                             password = '139571Wang!')

    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(sql.SQL("SELECT mytable, ST_AsGeoJSON(geom)::json AS geometry FROM mytable WHERE id = %s"), (1,))
    result = cur.fetchone()
    cur.close()
    conn.close()
    return jsonify(result)
