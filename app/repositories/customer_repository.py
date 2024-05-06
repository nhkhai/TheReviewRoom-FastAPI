import uuid

import sqlalchemy
from app.models.customer import Customer
from app.repositories.repository_session import RepositorySession


class CustomerRepository:
    def __init__(self, repository_session: RepositorySession) -> None:
        self.repo_session = repository_session

    def _get_session(self):
        return self.repo_session.get_session()

    async def create_customer(self, customer: Customer):
        try:
            async with self._get_session() as session:
                async with session.begin():
                    id = str(uuid.uuid4())

                    await session.execute(
                        Customer.__table__.insert().values(
                            id=id,
                            first_name=customer.first_name,
                            last_name=customer.last_name,
                            email=customer.email,
                            phone_number=customer.phone_number,
                        )
                    )
        except sqlalchemy.exc.IntegrityError as e:
            pass
