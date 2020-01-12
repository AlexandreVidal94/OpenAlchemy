"""Autogenerated SQLAlchemy models based on OpenAlchemy models."""
# pylint: disable=no-member,super-init-not-called,unused-argument

import typing

import sqlalchemy
from sqlalchemy import orm

from open_alchemy import models


class DivisionDict(typing.TypedDict, total=False):
    """TypedDict for properties that are not required."""

    id: typing.Optional[int]
    name: typing.Optional[str]


class TDivision(typing.Protocol):
    """SQLAlchemy model protocol."""

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    id: typing.Optional[int]
    name: typing.Optional[str]

    def __init__(
        self, id: typing.Optional[int] = None, name: typing.Optional[str] = None
    ) -> None:
        """Construct."""
        ...

    @classmethod
    def from_dict(
        cls, id: typing.Optional[int] = None, name: typing.Optional[str] = None
    ) -> "TDivision":
        """Construct from a dictionary (eg. a POST payload)."""
        ...

    def to_dict(self) -> DivisionDict:
        """Convert to a dictionary (eg. to send back for a GET request)."""
        ...


Division: TDivision = models.Division  # type: ignore


class EmployeeDict(typing.TypedDict, total=True):
    """TypedDict for properties that are required."""

    id: int
    name: str
    division: "DivisionDict"


class TEmployee(typing.Protocol):
    """SQLAlchemy model protocol."""

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    id: int
    name: str
    division: "TDivision"

    def __init__(self, id: int, name: str, division: "TDivision") -> None:
        """Construct."""
        ...

    @classmethod
    def from_dict(cls, id: int, name: str, division: "DivisionDict") -> "TEmployee":
        """Construct from a dictionary (eg. a POST payload)."""
        ...

    def to_dict(self) -> EmployeeDict:
        """Convert to a dictionary (eg. to send back for a GET request)."""
        ...


Employee: TEmployee = models.Employee  # type: ignore
