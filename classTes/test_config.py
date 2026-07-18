
import cards
from typer.testing import CliRunner
import os
def run_cards(*params):
    runner = CliRunner()
    result = runner.invoke(cards.cli.app, params)
    return result.output.strip()

def test_path_home(monkeypatch, tmp_path):
    full_cards_dir = tmp_path / "cards_db"

    def fake_home():
        return tmp_path
    monkeypatch.setattr(cards.cli.pathlib.Path, "home", fake_home)
    assert run_cards("config") == str(full_cards_dir)


def test_path_home(monkeypatch, tmp_path):
    full_cards_dir = tmp_path / "cards_db"
    print("my new temp path in runtime:", full_cards_dir)

    def fake_home():
        return tmp_path
    
    monkeypatch.setattr(cards.cli.pathlib.Path, "home", fake_home)
    assert run_cards("config") == str(full_cards_dir)


def test_path_env(monkeypatch, tmp_path):

    monkeypatch.setenv("CARDS_DB_DIR", str(tmp_path))
    new_var = os.getenv("CARDS_DB_DIR", "")
    print("my new env var in runtime:", new_var)
    assert run_cards("config") == str(tmp_path)
    

