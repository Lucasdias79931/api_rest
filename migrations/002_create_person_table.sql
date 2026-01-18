CREATE TABLE IF NOT EXISTS person (
    person_id UUID PRIMARY KEY,
    name TEXT NOT NULL,
    status status_enum NOT NULL DEFAULT 'active'
);
