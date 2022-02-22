# CLI in Python

##### Версия для русских: [здесь](./README_RU.md)

## Command-line interface for programs on Python3

### How to run

```python
from console import Console
import platform
import getpass

cli = Console(prompt_in=">", prompt_out="]:")

def cli_echo(argv: list):
    """ Help message here """

    message = f"argv: {argv}"

    return message

def cli_uname():
    """ Print uname information. """

    uname = platform.uname()
    user = getpass.getuser()

    return f"{user}@{uname.node} -> {uname.system} {uname.release} ({uname.version})"

# Add commands
cli.add("help", cli_echo, echo=True)  # With echo
cli.add("uname", cli_uname)  # Without echo

cli.run()
```

### Usage output

* Basic output

```python
from console import Console

cli = Console(prompt_in=">", prompt_out="]:")

cli.log("cli.og")
cli.write("cli.write")

# Output
# ]: cli.og
# ]: cli.write
```

* With logging output usage

```python
from console import Console
import logging

cli = Console(prompt_in=">", prompt_out="]:")
logging.basicConfig(level=logging.NOTSET, format="%(asctime)s - %(name)-5s - %(levelname)-7s - %(message)s")

# All calls below will be implemented via Console
cli.logger_hook()
logging.debug("Debug log")
logging.warning('Warning log')
logging.error("Error log")
logging.info("Info log")

# Output
# ]: 2022-02-20 23:22:49,731 - root  - DEBUG   - Debug log
# ]: 2022-02-20 23:22:49,731 - root  - WARNING - Warning log
# ]: 2022-02-20 23:22:49,731 - root  - ERROR   - Error log
# ]: 2022-02-20 23:22:49,731 - root  - INFO    - Info log
```

* with `print()` and `console.log` output usage

```python
from console import Console

cli = Console(prompt_in=">", prompt_out="]:")

cli.builtins_hook()

# Output below from the hook
# After builtins_hook() => cli = console

print("print()")

console.write("console.write")
console.log("console.log")

console['[] log']
console << "<< log"

# Output
# ]: print()
# ]: console.write
# ]: console.log
# ]: [] log
# ]: << log
```

If you use IDE, you mast update `builtins.pyi` with `scr/builtins_fix.pyi`. <br/>
Copy all from `builtins_fix.pyi` and insert into `builtins.pyi` at line `131` below `class type(object)`.

## Links

* [Author's Telegram](https://t.me/SantaSpeen "SantaSpeen"): https://t.me/SantaSpeen

Used in: 

* [Python-CLI-Game-Engine](https://github.com/SantaSpeen/Python-CLI-Game-Engine)
