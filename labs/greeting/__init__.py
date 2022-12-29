import check50

@check50.check()
def exists():
    """greeting.sh exists"""
    check50.exists("greeting.sh")

@check50.check()
def greeting():
    """greeting succeeds"""
    check50.run("bash greeting.sh").stdout("Hello, Linux!").exit()
