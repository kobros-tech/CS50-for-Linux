import check50

@check50.check()
def exists():
    """greeting.sh exists"""
    check50.exists("greeting.sh")
    
@check50.check()
def hello_world():
  """hello linux"""
  check50.run("bash greeting.sh").stdout("Hello, Linux!", regex=False).exit(0)
