from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db
from typing import TYPE_CHECKING

class Author(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    books: Mapped[list["Book"]] = relationship(back_populates="author")

    def to_dict(self):
        author_as_dict = {
        "id" : self.id,
        "name": self.name
        }
    
        return author_as_dict

    @classmethod
    def from_dict(cls, author_data):
        new_author = Author(name=author_data["name"])

        return new_author
    
if TYPE_CHECKING:
    from .book import Book
