import check50

@check50.check()
def exists():
    """distributions1.sh exists"""
    check50.exists("distributions2.sh")

@check50.check()
def exists():
    """distributions.txt exists"""
    check50.exists("distributions.txt")

@check50.check()
def greeting():
    """distro family names succeeds"""
    solution = open("/home/ubuntu/.local/share/check50/kobros-tech/cs50-for-linux/problems/distributions1/solution.txt", "r")
    check50.run("bash distributions2.sh").stdout(solution.read()).exit()