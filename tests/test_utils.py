import json


def test_read_json_operation(tmp_path):
    test_file = tmp_path / "test_file_json"

    data = {"key": "value", "number": 123}
    with open(test_file, "w") as f:
        json.dump(data, f)

    with open(test_file, "r") as f:
        read_data = json.load(f)

    assert read_data == data
