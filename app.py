from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    subscriptions = [
        {"name": "Netflix", "price": "$19.99", "renewal_date": "2025-04-01"},
        {"name": "Spotify", "price": "$9.99", "renewal_date": "2025-04-10"},
        {"name": "Amazon Prime", "price": "$12.99", "renewal_date": "2025-04-15"}
    ]
    return render_template('index.html', subscriptions = subscriptions)

if __name__ == '__main__':
    app.run(debug=True)