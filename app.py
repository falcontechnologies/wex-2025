from flask import Flask, render_template
from database import Session, Subscription

app = Flask(__name__)

@app.route('/')
def home():
    session = Session()
    subscriptions = session.query(Subscription).all()
    
    #dictionary to store information about user and subscription
    data = []
    
    for sub in subscriptions:
        data.append({
            "user_id": sub.user_id,
            "name": sub.name,
            "service_provider": sub.service_provider,
            "start_date": sub.start_date.strftime('%Y-%m-%d') if sub.start_date else "N/A",
            "expiry_date": sub.expiry_date.strftime('%Y-%m-%d') if sub.start_date else "N/A",
            "is_trial": "Yes" if sub.is_trial else "No",
            "is_recurring": "Yes" if sub.is_recurring else "No",
            "payment_frequency": sub.payment_frequency,
            "cost": f"${sub.cost:.2f}",
            "status": sub.status,
            "subscription_type": sub.subscription_type,
            "created_at": sub.created_at.strftime('%Y-%m-%d') if sub.created_at else "N/A"
        })
    session.close()
    return render_template('index.html', subscriptions = data)

if __name__ == '__main__':
    app.run(debug=True)