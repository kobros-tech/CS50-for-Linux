import check50
import check50.c

@check50.check()
def exists():
    """greeting.sh exists"""
    check50.exists("greeting.sh")

@check50.check(compiles)
def hello():
    """greeting succeeds"""
    check50.run("bash greeting.sh").stdout("Hello, Linux!").exit()

