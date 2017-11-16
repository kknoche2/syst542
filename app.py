from flask import Flask, render_template, request, redirect, url_for, flash
import os
import pandas as pd
import numpy as np
import sqlite3
from forms import PropertyForm

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
conn = sqlite3.connect('dss.db', check_same_thread=False)


def flash_errors(form):
	for field, errors in form.errors.items():
		for error in errors:
			flash(u"Error in the %s field - %s" % (
				getattr(form, field).label.text, error
				))
			print(getattr(form, field).label.text, error)


@app.route('/', methods=['GET','POST'])
def index():
	form = PropertyForm(request.form)
	if request.method == 'POST':
		if form.validate():
			# Add row to database
			cursor = conn.cursor()
			cursor.execute("INSERT INTO propertyDetails VALUES(?, ?, ?, ?, ?, ?)",
								(request.form['price'],
								 request.form['address'],
								 request.form['zip'],
								 request.form['deposit'],
								 request.form['depreciation'],
								 request.form['resale_value']))
			conn.commit()

			# Display database contents (including new row)
			query_string = "SELECT * FROM propertyDetails"
			df = pd.read_sql(query_string,conn)

			html_table = df.to_html(classes="table", index=False, justify='center', border=None)

			#return render_template('index.html', table=html_table)
			return redirect(url_for('index'))
		else:
			flash_errors(form)
			return redirect(url_for('index'))

	# if not post - display database contents
	query_string = "SELECT * FROM propertyDetails"
	df = pd.read_sql(query_string,conn)

	html_table = df.to_html(classes="table", index=False, justify='center', border=None)

	#wtform = PropertyForm(address=u'123 Fake Street')

	return render_template('index.html', table=html_table, wtform=form)


if __name__ == '__main__':
	app.run()