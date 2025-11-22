from src.decorators import log


def test_log_2(capsys):
    @log(None)
    def my_function():
        result = my_function()
        assert result == "Expected Result"
        return result


    my_function(1, 2)
    captured = capsys.readouterr()
    assert "my_function ok" in captured.out


def test_log():
    @log(filename="mylog.txt")
    def my_function():
        result = my_function()
        assert result == "Expected Result"
        return result

    my_function()
    with open("mylog.txt", "a") as file:
        log_content = file.read()

    assert "my_function ok" in log_content
