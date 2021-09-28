"""Tests for `uptimer` package."""
import pytest
import requests
import click
import sys
import re

from click.testing import CliRunner

from uptimer import __version__
from uptimer.helpers import check_url, colorize_status
from uptimer import cli


def test_version():
    assert __version__ == '0.1.0'


def mock_response_object(code):
    resp = requests.Response()
    resp.status_code = code
    return resp


def test_check_url(mocker):
    mocker.patch("requests.head", return_value=mock_response_object(200))
    assert check_url("dummy_url") == 200

    mocker.patch("requests.head", return_value=mock_response_object(404))
    assert check_url("dummy_url") == 404

    with pytest.raises(TypeError):
        check_url()


def test_colorize_status(mocker):
    mocker.patch("click.secho")
    url = "http://dummy.url"
    status_code = 200
    colorize_status(url, status_code)
    # click.secho.assert_calles()
    click.secho.assert_called_with(f"{url} -> {status_code}", fg="green")


@pytest.mark.skipif(
    sys.platform == "win32", reason="Testing colorized output doesn't work on Windows"
)
@pytest.mark.parametrize(
    "code, color",
    [
        (200, "green"),
        (304, "yellow"),
        (404, "bright_red"),
        (500, "red"),
        (1, "magenta"),
    ]
)
def test_check_one_url(mocker, code, color):
    url = "http://dummy.url"
    mocker.patch("requests.head", return_value=mock_response_object(code))
    runner = CliRunner()
    result = runner.invoke(cli.main, [url], color=True)
    expected_message = click.style(f"{url} -> {code}", fg=color)
    assert result.output == f"{expected_message}\n"


def test_check_multiple_urls(mocker):
    test_info = ({'url': "dummyurl1", 'code': 200}, {'url': "dummyurl2", 'code': 500}, )
    mocker.patch(
        "requests.head",
        side_effect=[mock_response_object(item['code']) for item in test_info]
    )
    runner = CliRunner()
    result = runner.invoke(cli.main, [item['url'] for item in test_info], color=True)
    expected_output = ''.join([f"{item['url']} -> {item['code']}\n" for item in test_info])
    assert result.output == expected_output


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main, ['https://google.com'])
    assert result.exit_code == 0
    assert re.search(r'https://google\.com -> (200|301)', result.output)
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert re.search(r'--help\s+Show this message and exit\.', help_result.output, re.I)
