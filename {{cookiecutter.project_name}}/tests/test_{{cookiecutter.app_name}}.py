from {{cookiecutter.app_name}} import __version__


def test_version():
    assert __version__ == "{{cookiecutter.app_version}}"
