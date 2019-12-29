"""Tests for backref helpers."""

import pytest

from open_alchemy import exceptions
from open_alchemy import types
from open_alchemy.helpers import backref

# The following table shows the relationship type and whether the back reference is an
# array
# +--------------+----------+-----------------+-----------+---------------------+
# | type         | is array | referenced from | uselist   | secondary           |
# +==============+==========+=================+===========+=====================+
# | many to one  | True     | object          | None/True | None                |
# +--------------+----------+-----------------+-----------+---------------------+
# | one to one   | False    | object          | False     | None                |
# +--------------+----------+-----------------+-----------+---------------------+
# | one to many  | False    | array           | None      | None                |
# +--------------+----------+-----------------+-----------+---------------------+
# | many to many | True     | array           | None      | <association table> |
# +--------------+----------+-----------------+-----------+---------------------+


class TestCalculateSchema:
    """Tests for _calculate_schema."""

    # pylint: disable=protected-access

    @staticmethod
    @pytest.mark.helper
    def test_invalid():
        """
        GIVEN artifacts with None BackReferenceArtifacts
        WHEN _calculate_schema is called with the artifacts
        THEN MissingArgumentError is raised.
        """
        artifacts = types.ObjectArtifacts(
            spec={},
            fk_column="fk_column",
            relationship=types.RelationshipArtifacts(
                model_name="RefModel", back_reference=None, secondary=None
            ),
        )

        with pytest.raises(exceptions.MissingArgumentError):
            backref._calculate_schema(
                artifacts=artifacts, ref_from_array=False, model_name="Model"
            )

    @staticmethod
    @pytest.mark.parametrize(
        "ref_from_array, uselist, secondary, expected_schema",
        [
            (
                False,
                None,
                None,
                {"type": "array", "items": {"type": "object", "x-de-$ref": "Model"}},
            ),
            (
                False,
                True,
                None,
                {"type": "array", "items": {"type": "object", "x-de-$ref": "Model"}},
            ),
            (False, False, None, {"type": "object", "x-de-$ref": "Model"}),
            (True, None, None, {"type": "object", "x-de-$ref": "Model"}),
            (
                False,
                None,
                "association",
                {"type": "array", "items": {"type": "object", "x-de-$ref": "Model"}},
            ),
        ],
        ids=[
            "from object uselist None",
            "from object uselist True",
            "from object uselist False",
            "from array secondary None",
            "from array secondary set",
        ],
    )
    @pytest.mark.helper
    def test_valid(ref_from_array, uselist, secondary, expected_schema):
        """
        GIVEN whether referenced from array, uselist, secondary, model name
        WHEN _calculate_schema is called with the parameters
        THEN the given expected schema is returned.
        """
        artifacts = types.ObjectArtifacts(
            spec={},
            fk_column="fk_column",
            relationship=types.RelationshipArtifacts(
                model_name="RefModel",
                back_reference=types.BackReferenceArtifacts(
                    property_name="model", uselist=uselist
                ),
                secondary=secondary,
            ),
        )

        returned_schema = backref._calculate_schema(
            artifacts=artifacts, ref_from_array=ref_from_array, model_name="Model"
        )

        assert returned_schema == expected_schema
