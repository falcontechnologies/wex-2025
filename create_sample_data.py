from datetime import datetime, timedelta
from database import Session, Subscription

session = Session()

session.query(Subscription).delete()

def add_subscription(user_id, name, service_provider, days_ago, duration_days, trial, recurring, freq, cost, status, sub_type):
    start_date = datetime.now() - timedelta(days=days_ago)
    expiry_date = start_date + timedelta(days=duration_days)
    subscription = Subscription(
        user_id=user_id,
        name=name,
        service_provider=service_provider,
        start_date=start_date,
        expiry_date=expiry_date,
        is_trial=trial,
        is_recurring=recurring,
        payment_frequency=freq,
        cost=cost,
        status=status,
        subscription_type=sub_type,
        created_at=datetime.now()
    )
    session.add(subscription)
    
add_subscription(1, "Netflix", "Netflix Inc.", 30, 90, 0, 1, "monthly", 19.99, "active", "entertainment")
add_subscription(2, "Amazon Prime", "Amazon", 90, 365, 0, 1, "yearly", 139.00, "active", "shopping")
add_subscription(2, "Notion Pro", "Notion Labs", 10, 30, 0, 0, "monthly", 0.00, "cancelled", "productivity")
add_subscription(3, "Canva Premium", "Canva", 15, 30, 1, 1, "monthly", 12.95, "trial", "design")

session.commit()
session.close()