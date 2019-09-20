"""Tests for merge allOf helper."""


import pytest

from openapi_sqlalchemy import helpers


@pytest.mark.helper
def test_not_all_of():
    """
    GIVEN spec that does not have the allOf statement
    WHEN merge_all_of is called with the spec
    THEN the spec is returned.
    """
    spec = {"key": "value"}

    return_spec = helpers.merge_all_of(spec=spec, schemas={})

    assert return_spec == {"key": "value"}


@pytest.mark.helper
def test_single():
    """
    GIVEN spec that has allOf statement with a single spec
    WHEN merge_all_of is called with the spec
    THEN the spec in allOf is returned.
    """
    spec = {"allOf": [{"key": "value"}]}

    return_spec = helpers.merge_all_of(spec=spec, schemas={})

    assert return_spec == {"key": "value"}


@pytest.mark.helper
def test_multiple():
    """
    GIVEN spec that has multiple specs under allOf
    WHEN merge_all_of is called with the spec
    THEN the merged spec of all specs under allOf is returned.
    """
    spec = {"allOf": [{"key_1": "value_1"}, {"key_2": "value_2"}]}

    return_spec = helpers.merge_all_of(spec=spec, schemas={})

    assert return_spec == {"key_1": "value_1", "key_2": "value_2"}


@pytest.mark.helper
def test_multiple_same_key():
    """
    GIVEN spec that has multiple specs under allOf with the same key
    WHEN merge_all_of is called with the spec
    THEN the value of the last spec is assigned to the key in the returned spec.
    """
    spec = {"allOf": [{"key": "value_1"}, {"key": "value_2"}]}

    return_spec = helpers.merge_all_of(spec=spec, schemas={})

    assert return_spec == {"key": "value_2"}


@pytest.mark.helper
def test_nested_all_of():
    """
    GIVEN spec that has allOf statement with an allOf statement with a single spec
    WHEN merge_all_of is called with the spec
    THEN the spec in allOf is returned.
    """
    spec = {"allOf": [{"allOf": [{"key": "value"}]}]}

    return_spec = helpers.merge_all_of(spec=spec, schemas={})

    assert return_spec == {"key": "value"}


@pytest.mark.helper
def test_ref():
    """
    GIVEN spec that has allOf statement with $ref to another spec
    WHEN merge_all_of is called with the spec
    THEN the $ref spec in allOf is returned.
    """
    spec = {"allOf": [{"$ref": "#/components/schemas/RefSchema"}]}
    schemas = {"RefSchema": {"key": "value"}}

    return_spec = helpers.merge_all_of(spec=spec, schemas=schemas)

    assert return_spec == {"key": "value"}


@pytest.mark.helper
def test_ref_all_of():
    """
    GIVEN spec that has allOf statement with $ref to another spec with an allOf
        statement with a spec
    WHEN merge_all_of is called with the spec
    THEN the allOf $ref spec in allOf is returned.
    """
    spec = {"allOf": [{"$ref": "#/components/schemas/RefSchema"}]}
    schemas = {"RefSchema": {"allOf": [{"key": "value"}]}}

    return_spec = helpers.merge_all_of(spec=spec, schemas=schemas)

    assert return_spec == {"key": "value"}