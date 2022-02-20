import logging
import os

from console import Console, ConsoleIO

# Init modules
cli = Console()  # Console(debug=True)
logging.basicConfig(level=logging.NOTSET, format="%(asctime)s - %(name)-5s - %(levelname)-7s - %(message)s")


def cli_print():
    """ How can I write text to the console? Read below! """
    cli.log("cli.og")
    cli.write("cli.write")

    print("\r...", end="\n\n\n")


def logger_preview():
    """ I use logging and want its output to be in the console! """
    cli.logger_hook()

    # All calls below will be implemented via Console

    logging.debug("Debug log")
    logging.warning('Warning log')
    logging.error("Error log")
    logging.info("Info log")

    print("\r...", end="\n\n\n")


def builtins_preview():
    """ I want print to be output like cli.log """

    # Output below without hook

    print("No builtins_hook here")
    print("No builtins_hook here, but file=cli, end=''", file=cli, end="")

    cli.builtins_hook()

    # Output below from the hook
    # After hook cli = console

    print("builtins_hook here")

    console.write("console.write")
    console.log("console.log")

    console['[] log']
    console << "<< log"

    ConsoleIO.write("\r...\n\n")  # Or console.get_IO.write("\r...\n\n")


def cli_echo(x: str):
    """ Help message here """

    message = "Echo message: " + x

    return message


def cli_error(x):
    """ Print error message """

    raise Exception("Test error message")


def cli_exit():
    """ Kill process """
    
    pid = os.getpid()
    os.system(f"kill {pid}")


def cli_mode():
    print("type help")

    cli.add("echo", cli_echo)
    cli.add("error", cli_error)
    cli.add("exit", cli_exit)

    cli.run()

    # Or you may use
    # cli.run_while(lambda: <some code>)


if __name__ == '__main__':
    cli_print()
    logger_preview()
    builtins_preview()
    cli_mode()
