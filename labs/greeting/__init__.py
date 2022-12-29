import check50
import check50.c

@check50.check()
def exists():
    """greeting exists"""
    check50.exists("greeting")

@check50.check(compiles)
def emma():
    """greeting succeeds"""
    check50.run("bash greeting").stdout("Hello, Linux!").exit()

