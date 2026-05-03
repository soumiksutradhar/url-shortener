from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()	# creating SQLAlchemy instance

class Expense(db.Model):	# this class will represent a table in the database
	__tablename__ = "Expenses"
	
	id = db.Column(db.Integer, primary_key=True)
	amount = db.Column(db.Float, nullable=False)
	category = db.Column(db.String(50), nullable=False)
	note = db.Column(db.String(200), nullable=False)
	date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
	created_at = db.Column(db.DateTime, default=datetime.utcnow)
	
	def to_dict(self):	# this function will convert a row object into a Python dictionary as Flask needs one to output the JSON
		return {
			'id' : self.id,
			'amount' : self.amount,
			'category' : self.category,
			'note' : self.note,
			'date' : self.date.isoformat(),
			'created_at' : self.created_at.isoformat()
		}
