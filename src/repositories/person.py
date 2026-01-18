from .repository import Repository
from ..dtos.person import PersonDTO
from ..models.poolconnect import pool
from psycopg.errors import UniqueViolation
from ..exeptions.exeptions import BusinessError

class PersonRepository(Repository[PersonDTO, str]):

    async def save(self, person_dto: PersonDTO) -> str | None:
        """
        Persist a person entity in the database.

        This method inserts a new person record into the database.
        If the operation is successful, the person_id is returned.
        """
        try:
            async with pool.connection() as conn:
                async with conn.cursor() as cur:
                    await cur.execute(
                        """
                        INSERT INTO person (person_id, name, status)
                        VALUES (%s, %s, %s)
                        """,
                        (
                            person_dto.person_id,
                            person_dto.name,
                            person_dto.status.value,
                        ),
                    )

                    return person_dto.person_id
        except UniqueViolation:
            raise BusinessError("Person already exists")

