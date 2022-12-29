import check50

@check50.check()
def exists():
    """greeting.c exists"""
    check50.exists("greeting.c")
    
@check50.check()
def hello_world():
  """hello linux"""
  check50.run("bash greeting.c").stdout("Hello, Linux!", regex=False).exit(0)
