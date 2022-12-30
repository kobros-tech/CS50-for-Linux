import check50

@check50.check()
def exists():
    """distributions1.sh exists"""
    check50.exists("distributions1.sh")

@check50.check()
def greeting():
    """distro family names succeeds"""
    solution = open("solution.txt", "r")
    check50.run("bash distributions1.sh").stdout(solution.read()).exit()
