# Data Model

## Entity 1: User

| Field | Type | Description |
|---|---|---|
| user_id | UUID | Unique user identifier |
| name | String | User full name |
| email | String | User email address |
| password_hash | String | Encrypted password |
| created_at | DateTime | Account creation date |

---

## Entity 2: StartupProject

| Field | Type | Description |
|---|---|---|
| project_id | UUID | Unique project identifier |
| user_id | UUID | Project owner |
| title | String | Startup title |
| description | Text | Startup idea description |
| industry | String | Startup category |
| created_at | DateTime | Creation timestamp |

---

## Entity 3: AIResult

| Field | Type | Description |
|---|---|---|
| result_id | UUID | Unique AI result identifier |
| project_id | UUID | Related startup project |
| summary | Text | AI-generated startup summary |
| competitor_analysis | Text | Competitor insights |
| roadmap | Text | MVP roadmap |
| generated_at | DateTime | Generation timestamp |

---

# Entity Relationships

## User -> StartupProject
One user can own multiple startup projects.

## StartupProject -> AIResult
One startup project can contain multiple AI-generated results.

---

# Database Notes

## Recommended Database
- PostgreSQL
- SQLite for MVP testing

## Security Considerations
- Password hashing required
- User project isolation enforced
- Authentication validation required

## Scalability Notes
- AI result history may grow rapidly
- Indexing recommended for projects
- Export logs may require archival