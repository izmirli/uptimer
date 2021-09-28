"""Console script for uptimer."""
import sys
import time
import click
from uptimer.helpers import check_url, colorize_status


@click.command()
@click.argument("urls", nargs=-1, required=True)  # , help='One or more URLs to check')
@click.option("--daemon", "-d", default=False, is_flag=True)  # , help='Activate daemon - continually check given URLs')
@click.option("--interval", "-i", default=5)  # , help='time in secounds for daemon mode interval')
def main(urls, daemon: bool = False, interval: int = 5):
    """Check given URLs and output HTTP respond status code.

    :param urls: URL (or a tuple with multiple URLs) to check
    :type urls: str or tuple(str)
    :param daemon: if true check continually each 5 seconds, defaults to False.
    :type daemon: bool, optional
    :param interval: Interval in secounds for daemon mode chekes, defaults to 5 sec.
    :type interval: int, optional
    """
    while True:
        for url in urls:
            status_code = check_url(url)
            if status_code:
                colorize_status(url, status_code)
        if not daemon:
            break
        time.sleep(interval)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
