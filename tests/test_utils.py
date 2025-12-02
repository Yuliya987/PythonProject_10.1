import json
from unittest.mock import mock_open

import pytest
import requests

from src.utils import read_json_operation


@pytest.fixture
def sample_data():
    return [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]


def test_file_not_exists():
    with requests.patch("os.path.exists", return_value=False):
        result = read_json_operation("non_existent.json")
        assert result == []


def test_successful_read(sample_data):
    with requests.patch("os.path.exists", return_value = True):
        with requests.patch("builtins.open", mock_open(read_data=json.dumps(sample_data))):
            with requests.patch("json.load", return_value = sample_data):
                result = read_json_operation("data.json")
                assert result == sample_data


def test_json_decode_error():
    with requests.patch("os.path.exists", return_value = True):
        with requests.patch("builtins.open", mock_open(read_data="invalid")):
            with requests.patch("json.load", side_effect=json.JSONDecodeError("Error", "doc", 0)):
                result = read_json_operation("data.json")
                assert result == []
