# Data Model

## Entity 1: User

| Field Name | Type | Description |
|---|---|---|
| user_id | UUID | Unique user identifier |
| name | String | Full user name |
| email | String | User email address |
| password_hash | String | Encrypted password |
| created_at | DateTime | Account creation timestamp |

---

## Entity 2: StartupProject

| Field Name | Type | Description |
|---|---|---|
| project_id | UUID | Unique project identifier |
| user_id | UUID | Owner reference |
| title | String | Startup idea title |
| description | Text | Startup description |
| industry | String | Startup category |
| created_at | DateTime | Creation timestamp |
| updated_at | DateTime | Last update timestamp |

---

## Entity 3: AIResult

| Field Name | Type | Description |
|---|---|---|
| result_id | UUID | Unique AI result identifier |
| project_id | UUID | Associated startup project |
| summary | Text | AI-generated summary |
| competitor_analysis | Text | Competitor insights |
| revenue_model | Text | Suggested revenue models |
| roadmap | Text | MVP roadmap |
| generated_at | DateTime | Generation timestamp |

---

## Entity Relationships

### User -> StartupProject
- One user can own many startup projects.
- Each project belongs to one user.

### StartupProject -> AIResult
- One project can have multiple AI-generated outputs.
- Each AI result belongs to one startup project.

---

# Data Storage Notes

## Database Choice
Recommended:
- PostgreSQL
- SQLite for MVP prototype

---

## Security Notes
- Passwords stored using hashing
- User access validation required
- Sensitive startup ideas protected

---

## Scalability Considerations
- AI results may grow rapidly
- Export history may require archiving
- Database indexing recommended for project retrieval