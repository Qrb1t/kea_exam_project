import pymysql

from flask import (
    flash, redirect, render_template, request, url_for, jsonify
)
from config import mysql, app

@app.route('/rsvp', methods=['GET'])
def rsvp_get():
    return render_template('rsvp.html')

@app.route('/rsvp', methods=['POST'])
def rsvp_post():
    try:
        if request.method == 'POST':
            name = request.form['name']
            if request.form['attending_yes']:
                attending = 1
            else:
                attending = 0
            db = mysql.connect()
            cursor = db.cursor()
            error = None

            if not name:
                error = 'Navn skal udfyldes.'
            elif not attending:
                error = 'Du skal svare om du kan komme.'

            if error is None:
                cursor.execute(
                    "INSERT INTO guests (name, attending) VALUES (%s, %s)",
                    (name, attending),
                )
                db.commit()
                return redirect(url_for("guestlist"))
        
            flash(error)
        
        return render_template('rsvp.html')
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        db.close()

@app.route('/guestlist')
def guestlist():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        sqlQuery = 'SELECT name, attending FROM guests'
        cursor.execute(sqlQuery)
        guestRows = cursor.fetchall()
        respone = jsonify(guestRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
    
    #return render_template('guestlist.html')

if __name__ == '__main__':
    app.run()