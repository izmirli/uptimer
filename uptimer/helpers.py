"""Helper functions for UpTimer packge."""
from typing import Optional
import click
import requests


def check_url(url: str) -> Optional[int]:
    """Send HEAD request to the url and return the HTTP status code.

    :param url: URL to check
    :type url: str
    :return: HTTP status code
    :rtype: Optional[int]
    """
    try:
        response = requests.head(url)
    except requests.exceptions.ConnectionError as ex:
        click.echo(f"ConnectionError: Can't reach {url} URL!\nInfo: {ex}")
        return None
    return response.status_code


def colorize_status(url: str, status: int) -> None:
    """Print the URL and status in color to the terminal.

    :param url: URL to print
    :type url: str
    :param status: status used to determine the color of the output
    :type status: str
    """
    colors = {
        2: "green",
        3: "yellow",
        4: "bright_red",
        5: "red",
    }
    click.secho(f"{url} -> {status}", fg=colors.get(status // 100, "magenta"))
