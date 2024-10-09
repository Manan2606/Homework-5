'''test_arithemetic.py'''
from app.commands.arithmetic import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

def test_add_command(monkeypatch, capfd):
    """Test the AddCommand with input 5 and 3."""
    inputs = iter(['5', '3'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    command = AddCommand()
    command.execute()
    out, _ = capfd.readouterr()
    assert "The result of adding 5 and 3 is 8" in out

def test_add_invalid_input(monkeypatch, capfd):
    """Test AddCommand with invalid input."""
    inputs = iter(['abc', '3'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    command = AddCommand()
    command.execute()
    out, _ = capfd.readouterr()
    assert "Invalid input" in out

def test_subtract_command(monkeypatch, capfd):
    """Test the SubtractCommand with input 5 and 3."""
    inputs = iter(['5', '3'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    command = SubtractCommand()
    command.execute()
    out, _ = capfd.readouterr()
    assert "The result of subtracting 3 from 5 is 2" in out

def test_subtract_negative_result(monkeypatch, capfd):
    """Test SubtractCommand resulting in negative output."""
    inputs = iter(['3', '5'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    command = SubtractCommand()
    command.execute()
    out, _ = capfd.readouterr()
    assert "The result of subtracting 5 from 3 is -2" in out

def test_multiply_command(monkeypatch, capfd):
    """Test the MultiplyCommand with input 5 and 3."""
    inputs = iter(['5', '3'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    command = MultiplyCommand()
    command.execute()
    out, _ = capfd.readouterr()
    assert "The result of multiplying 5 and 3 is 15" in out

def test_multiply_with_zero(monkeypatch, capfd):
    """Test MultiplyCommand with one operand being zero."""
    inputs = iter(['5', '0'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    command = MultiplyCommand()
    command.execute()
    out, _ = capfd.readouterr()
    assert "The result of multiplying 5 and 0 is 0" in out

def test_divide_command(monkeypatch, capfd):
    """Test the DivideCommand with input 6 and 3."""
    inputs = iter(['6', '3'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    command = DivideCommand()
    command.execute()
    out, _ = capfd.readouterr()
    assert "The result of dividing 6 by 3 is 2" in out

def test_divide_by_zero_command(monkeypatch, capfd):
    """Test the DivideCommand when dividing by zero."""
    inputs = iter(['6', '0'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    command = DivideCommand()
    command.execute()
    out, _ = capfd.readouterr()
    assert "Cannot divide by zero" in out

def test_divide_invalid_input(monkeypatch, capfd):
    """Test DivideCommand with invalid input."""
    inputs = iter(['abc', '3'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    command = DivideCommand()
    command.execute()
    out, _ = capfd.readouterr()
    assert "Invalid input" in out
