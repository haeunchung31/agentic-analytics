# Schema Context

**Note**: This file should be updated with actual table definitions as they are discovered.

## Datasets
- `app_db`: Application logs and user data.
- `sales_db`: Transactional data.
- `finance_db`: General Ledger and accounting data.

## Key Tables
### `sales_db.transactions`
- `transaction_id` (string): PK
- `user_id` (string): FK to users
- `amount` (double): Transaction value
- `status` (string): 'PENDING', 'COMPLETED', 'REFUNDED'
- `date` (timestamp): Transaction timestamp

### `app_db.users`
- `user_id` (string): PK
- `signup_date` (timestamp)
- `country` (string)
