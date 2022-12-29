import check50

@check50.check()
def hello_world():
  """hello world"""
  check50.run("bash greeting.sh").stdout("Hello, Linux!", regex=False).exit(0)
