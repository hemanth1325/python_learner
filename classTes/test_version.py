# import subprocess

import cards

# def test_version():
#     process = subprocess.run(["cards", "--version"], capture_output=True, text=True)
#     output = process.stdout.rstrip()

#     assert output == cards.__version__


def test_version_v2(capsys):
    cards.cli.version()
    output = capsys.readouterr().out.strip()
    assert output == cards.__version__

def test_normal():
    print("\nnormal test")

def test_disabled(capsys):
    with capsys.disabled():
        print("\nthis should print even without -s")
    