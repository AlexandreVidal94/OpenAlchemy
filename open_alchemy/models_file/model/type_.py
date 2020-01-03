"""Functions for calculating the type."""

from open_alchemy import exceptions
from open_alchemy import helpers

from .. import types


def model(*, artifacts: types.ColumnSchemaArtifacts) -> str:
    """
    Calculate the Python type of a column.

    Args:
        artifacts: The artifacts from the schema of the column.

    Returns:
        The equivalent Python type.

    """
    # Determine underlying type
    return_type = "str"
    if artifacts.type == "integer":
        return_type = "int"
    if artifacts.type == "number":
        return_type = "float"
    if artifacts.type == "boolean":
        return_type = "bool"
    if artifacts.type == "object":
        return_type = f'"{artifacts.de_ref}"'
    if artifacts.type == "array":
        return f'typing.Sequence["{artifacts.de_ref}"]'
    if artifacts.format == "binary":
        return_type = "bytes"
    if artifacts.format == "date":
        return_type = "datetime.date"
    if artifacts.format == "date-time":
        return_type = "datetime.datetime"

    # Determine whether the type is optional
    optional = helpers.calculate_nullable(
        nullable=artifacts.nullable,
        generated=artifacts.generated is True,
        required=artifacts.required,
    )
    if optional:
        return f"typing.Optional[{return_type}]"
    return return_type


def typed_dict(*, artifacts: types.ColumnSchemaArtifacts) -> str:
    """
    Calculate the Python type of a column for a TypedDict.

    Args:
        artifacts: The artifacts from the schema of the column.

    Returns:
        The equivalent Python type for the TypedDict.

    """
    # Calculate type the same way as for the model
    model_type = model(artifacts=artifacts)

    # Modify the type in case of object or array
    if artifacts.type in {"object", "array"}:
        if artifacts.de_ref is None:
            raise exceptions.MissingArgumentError(
                "The schema for the property of an object reference must include "
                "x-de-$ref with the name of the model being referenced."
            )
        model_type = model_type.replace(artifacts.de_ref, f"{artifacts.de_ref}Dict")

    return model_type


def args(*, artifacts: types.ColumnSchemaArtifacts) -> str:
    """
    Calculate the Python type of a column for the arguments of __init__ and from_dict.

    Args:
        artifacts: The artifacts from the schema of the column.

    Returns:
        The equivalent Python type for the argument for the column.

    """
    model_type = model(artifacts=artifacts)

    # Add optional if not required unless already optional
    if not artifacts.required and not model_type.startswith("typing.Optional["):
        return f"typing.Optional[{model_type}]"
    return model_type
