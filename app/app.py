from util import config, config_list, log

print("hello world!")
log.info("This is an info message")
print(config("DEFAULT", "TEST"))
print(config_list("DEFAULT", "TEST_LIST"))
