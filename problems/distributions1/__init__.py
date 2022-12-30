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

@check50.check()
def greeting():
    """distro family names succeeds"""
    check50.run("bash distributions1.sh").stdout("The Red Hat Family\nRHEL\nCentOS\nFedora\nOracle Linux\n\nThe SUSE Family\nSLES\nopenSUSE\n\nThe Debian Family\nDebian\nUbuntu\nLinux Mint").exit()
