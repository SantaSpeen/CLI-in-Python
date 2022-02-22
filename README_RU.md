# CLI in Python

## Консольная оболочка для программ на Python3

### Как запускать

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

### Использование вывода

* Базовое использование вывода 

```python
from console import Console

cli = Console(prompt_in=">", prompt_out="]:")

cli.log("cli.og")
cli.write("cli.write")

# Output
# ]: cli.og
# ]: cli.write
```

* Использование вывода с `logging`

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

* Использование вывода с `print()` и `console.log`

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

Если вы используете IDE, можно обновить `builtins.pyi`, что бы она не ругалась на отсутствие `console.*` используя `scr/builtins_fix.pyi`. <br/>
Скопируйте всё из `builtins_fix.pyi` и вставте в `builtins.pyi` на `131` линию, перед `class type(object)`.

## Ссылки

* [Мой Telegram](https://t.me/SantaSpeen "SantaSpeen"): https://t.me/SantaSpeen

Используемые в поектах: 

* [Python-CLI-Game-Engine](https://github.com/SantaSpeen/Python-CLI-Game-Engine)
