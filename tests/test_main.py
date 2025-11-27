import package_name.main as m


def test_build_greeting_trims_whitespace():
    assert m.build_greeting("  Codex  ") == "Hello from Codex!"


def test_main_prints_and_returns(capsys):
    message = m.main("Template")
    captured = capsys.readouterr()
    assert message == "Hello from Template!"
    assert "Hello from Template!" in captured.out


def test_cli_accepts_name(capsys):
    exit_code = m.cli(["--name", "CLI User"])
    assert exit_code == 0
    captured = capsys.readouterr()
    assert "CLI User" in captured.out
