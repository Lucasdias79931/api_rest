CREATE TABLE IF NOT EXISTS images (
    image_id UUID PRIMARY KEY,
    animal_id UUID,
    person_id UUID,
    file_path TEXT NOT NULL,

    CONSTRAINT fk_image_animal
        FOREIGN KEY (animal_id)
        REFERENCES animal(animal_id)
        ON DELETE CASCADE,

    CONSTRAINT fk_image_person
        FOREIGN KEY (person_id)
        REFERENCES person(person_id)
        ON DELETE CASCADE
);
