CREATE TABLE IF NOT EXISTS animal (
    animal_id UUID PRIMARY KEY,
    name TEXT NOT NULL,
    status status_enum NOT NULL DEFAULT 'active',
    person_id UUID NOT NULL,

    CONSTRAINT fk_animal_person
        FOREIGN KEY (person_id)
        REFERENCES person(person_id)
        ON DELETE CASCADE
);