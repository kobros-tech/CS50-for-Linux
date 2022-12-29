import check50

@check50.check()
def exists():
    """greeting.txt exists"""
    check50.exists("greeting.txt")
    
@check50.check()
def hello_world():
  """hello linux"""
  check50.run("bash greeting.txt").stdout("Hello, Linux!", regex=False).exit(0)
