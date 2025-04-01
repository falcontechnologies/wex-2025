INSERT INTO user (id, email, phone_number, username, password, role, created_at, last_login) VALUES
(1, 'user1@example.com', '123-456-7890', 'user1', 'hashedpassword1', 'customer', CURRENT_TIMESTAMP, NULL),
(2, 'user2@example.com', '987-654-3210', 'user2', 'hashedpassword2', 'customer', CURRENT_TIMESTAMP, NULL);

INSERT INTO subscription (id, user_id, name, service_provider, start_date, expiry_date, is_trial, is_recurring, payment_frequency, cost, status, subscription_type, created_at) VALUES
(1, 1, 'Netflix Premium', 'Netflix', '2024-01-01', '2025-01-01', 0, 1, 'Monthly', 19.99, 'Active', 'Streaming', CURRENT_TIMESTAMP),
(2, 1, 'Spotify Family', 'Spotify', '2024-02-01', '2025-02-01', 0, 1, 'Monthly', 14.99, 'Active', 'Music', CURRENT_TIMESTAMP),
(3, 1, 'Amazon Prime', 'Amazon', '2024-03-01', '2025-03-01', 0, 1, 'Yearly', 139.00, 'Active', 'Shopping', CURRENT_TIMESTAMP),
(4, 2, 'Disney+ Basic', 'Disney+', '2024-01-15', '2025-01-15', 0, 1, 'Monthly', 7.99, 'Active', 'Streaming', CURRENT_TIMESTAMP),
(5, 2, 'Apple Music', 'Apple', '2024-04-01', '2025-04-01', 0, 1, 'Monthly', 9.99, 'Active', 'Music', CURRENT_TIMESTAMP),
(6, 1, 'HBO Max', 'HBO', '2024-05-01', '2025-05-01', 1, 1, 'Monthly', 15.99, 'Active', 'Streaming', CURRENT_TIMESTAMP),
(7, 2, 'YouTube Premium', 'Google', '2024-06-01', '2025-06-01', 0, 1, 'Monthly', 11.99, 'Active', 'Streaming', CURRENT_TIMESTAMP),
(8, 1, 'New York Times', 'NYT', '2024-07-01', '2025-07-01', 0, 1, 'Monthly', 4.99, 'Active', 'News', CURRENT_TIMESTAMP),
(9, 2, 'Adobe Creative Cloud', 'Adobe', '2024-08-01', '2025-08-01', 0, 1, 'Yearly', 599.99, 'Active', 'Software', CURRENT_TIMESTAMP),
(10, 2, 'Dropbox Plus', 'Dropbox', '2024-09-01', '2025-09-01', 0, 1, 'Monthly', 11.99, 'Active', 'Cloud Storage', CURRENT_TIMESTAMP);
