# CLI in Python

#### Версия для русских: [здесь](./README_RU.md)

## Command-line interface for programs on Python3

### How to run

```python
from console import Console
cli = Console(prompt_in=">", prompt_out="]:")

def cli_echo(x: str):
    """ Help message here """

    message = "Echo message: " + x

    return message

cli.add("help", cli_echo)  # Add commands

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

## Links

* [Author's Telegram](https://t.me/SantaSpeen "SantaSpeen"): https://t.me/SantaSpeen

Used in: 

* [Python-CLI-Game-Engine](https://github.com/SantaSpeen/Python-CLI-Game-Engine)
