"""Autogenerated SQLAlchemy models based on OpenAlchemy models."""
# pylint: disable=no-member,useless-super-delegation

import typing

import sqlalchemy
from sqlalchemy import orm

from open_alchemy import models


class DivisionDict(typing.TypedDict, total=False):
    """TypedDict for properties that are not required."""

    id: typing.Optional[int]
    name: typing.Optional[str]


class Division(models.Division):  # type: ignore
    """SQLAlchemy model."""

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
        kwargs = {}
        if id is not None:
            kwargs["id"] = id
        if name is not None:
            kwargs["name"] = name

        super().__init__(**kwargs)

    @classmethod
    def from_dict(
        cls, id: typing.Optional[int] = None, name: typing.Optional[str] = None
    ) -> "Division":
        """Construct from a dictionary (eg. a POST payload)."""
        kwargs = {}
        if id is not None:
            kwargs["id"] = id
        if name is not None:
            kwargs["name"] = name

        return super().from_dict(**kwargs)

    def to_dict(self) -> DivisionDict:
        """Convert to a dictionary (eg. to send back for a GET request)."""
        return super().to_dict()


class _EmployeeDictBase(typing.TypedDict, total=True):
    """TypedDict for properties that are required."""

    id: int
    name: str


class EmployeeDict(_EmployeeDictBase, total=False):
    """TypedDict for properties that are not required."""

    division: "DivisionDict"


class Employee(models.Employee):  # type: ignore
    """SQLAlchemy model."""

    # SQLAlchemy properties
    __table__: sqlalchemy.Table
    __tablename__: str
    query: orm.Query

    # Model properties
    id: int
    name: str
    division: "Division"

    def __init__(
        self, id: int, name: str, division: typing.Optional["Division"] = None
    ) -> None:
        """Construct."""
        kwargs = {"id": id, "name": name}
        if division is not None:
            kwargs["division"] = division

        super().__init__(**kwargs)

    @classmethod
    def from_dict(
        cls, id: int, name: str, division: typing.Optional["DivisionDict"] = None
    ) -> "Employee":
        """Construct from a dictionary (eg. a POST payload)."""
        kwargs = {"id": id, "name": name}
        if division is not None:
            kwargs["division"] = division

        return super().from_dict(**kwargs)

    def to_dict(self) -> EmployeeDict:
        """Convert to a dictionary (eg. to send back for a GET request)."""
        return super().to_dict()