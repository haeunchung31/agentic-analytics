# Data Privacy & Security Rules

**Priority**: CRITICAL.

## PII (Personally Identifiable Information)
- **Definition**: Names, emails, phone numbers, SSN, precise coords.
- **Rule**: NEVER select PII columns in raw format.
- **Action**: Use `MD5()` or similar hashing if unique identifiers are needed.

## Read-Only Enforcement
- The SQL Agent must strictly adhere to `SELECT` only.
- No `INSERT`, `UPDATE`, `DELETE`, `DROP`, `TRUNCATE`, `ALTER`.
- Any attempt to modify data should be flagged immediately.

## Data Sharing
- Do not output raw user lists in the final report.
- Aggregate data whenever possible (e.g., "count of users" vs "list of users").
