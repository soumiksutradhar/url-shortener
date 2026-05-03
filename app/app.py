from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, Expense
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql://postgres:postgres@localhost:5432/expensedb')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/expenses', methods=['GET'])
def get_expenses():
    expenses = Expense.query.order_by(Expense.date.desc()).all()
    return jsonify([e.to_dict() for e in expenses])

@app.route('/expenses', methods=['POST'])
def add_expense():
    data = request.get_json()
    expense = Expense(
        amount=data['amount'],
        category=data['category'],
        note=data.get('note', ''),
        date=datetime.strptime(data['date'], '%Y-%m-%d')
    )
    db.session.add(expense)
    db.session.commit()
    return jsonify(expense.to_dict()), 201

@app.route('/expenses/<int:id>', methods=['DELETE'])
def delete_expense(id):
    expense = Expense.query.get_or_404(id)
    db.session.delete(expense)
    db.session.commit()
    return jsonify({'message': 'Expense deleted'}), 200

@app.route('/expenses/summary', methods=['GET'])
def get_summary():
    expenses = Expense.query.all()
    summary = {}
    for e in expenses:
        summary[e.category] = summary.get(e.category, 0) + e.amount
    return jsonify(summary)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
