import calculator
import pytest

def test_add():
    assert calculator.calculate(2, 3, "add") == 5
    assert calculator.calculate(-1, 1, "add") == 0
    assert calculator.calculate(-1, -100, "add") == -101

# Add more functional tests for subtract, multiply, and divide

def test_terminal_output(capsys):
    calculator.calculate(10, 2, "multiply")
    captured = capsys.readouterr()
    assert captured.out == "Result: 20\n"
    
    calculator.calculate(-10, -2, "multiply")
    captured = capsys.readouterr()
    assert captured.out == "Result: 20\n"

def test_argument_passing(monkeypatch):
    monkeypatch.setattr("sys.argv", ["calculator.py", "6", "2", "divide"])
    assert calculator.calculate(6, 2, "divide") == 3.0
    
    monkeypatch.setattr("sys.argv", ["calculator.py", "6", "0", "divide"])
    with pytest.raises(ValueError) as excinfo:
        calculator.calculate(6, 0, "divide")
        assert str(excinfo.value) == "Cannot divide by zero"
        
# Add more tests to cover edge cases and negative scenarios