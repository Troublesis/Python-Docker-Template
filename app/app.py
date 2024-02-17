import os
import time

from util import config, config_list, log


def main():
    print("hello world!")
    log.info("This is an info message")
    print(config("DEFAULT", "TEST"))
    print(config_list("DEFAULT", "TEST_LIST"))

    if "PASSWORD_FILE" in os.environ:
        with open(os.environ["PASSWORD_FILE"], "r") as f:
            password = f.read().strip()
            print(f"Password: {password}")
    time.sleep(2)


while True:
    main()
