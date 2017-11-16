from flask import Flask, render_template, request
import os
import pandas as pd
import numpy as np
import sqlite3

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
conn = sqlite3.connect('dss.db', check_same_thread=False)


@app.route('/', methods=['GET','POST'])
def index():
	if request.method == 'POST':
		# Add row to database
		cursor = conn.cursor()
		cursor.execute("INSERT INTO propertyDetails VALUES(?, ?, ?)",
							(request.form['price'],
							 request.form['address'],
							 request.form['zip']))
		conn.commit()

		# Display database contents (including new row)
		query_string = "SELECT * FROM propertyDetails"
		df = pd.read_sql(query_string,conn)

		html_table = df.to_html(classes="table", index=False, justify='center', border=None)

		return render_template('index.html', table=html_table)

	# if not post - display database contents
	query_string = "SELECT * FROM propertyDetails"
	df = pd.read_sql(query_string,conn)

	html_table = df.to_html(classes="table", index=False, justify='center', border=None)

	return render_template('index.html', table=html_table)


if __name__ == '__main__':
	app.run()