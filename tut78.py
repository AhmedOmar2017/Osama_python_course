#------------------------------------------------
#----- Modules => Install External Packages -----
#------------------------------------------------

# [1] Modules vs package
# [2] External Packages Download from internet
# [3] You Can install packages via package manager PIP -Python install package
# [4] PIP install  The package and its Dependencies
# [5] Modules List "https://docs.python.org/3/py-modindex.html"
# [6] Packages and modules Dictionary "https://pypi.org/"
# [7] PIP manual "https://pip.pypa.io/en/stable/reference/pip_intall/" replaced by "https://pip.pypa.io/en/stable/cli/pip_install/"
#-----------------------------------------------------------------------------------------------------------------------------------


# [1] pip --version
# [2] pip list
# [3] pip install "package's name"  => "pip install termcolor" my use  for specific version "pip install termcolor == 1.0.1" or range of versions  "pip install termcolor >= 1.0.1"greater than or equal
# [4] pip install pip --upgrade ==> python.exe -m pip install --upgrade pip
import pyfiglet , termcolor

print(dir(pyfiglet))
print(pyfiglet.figlet_format("Ahmed"))
print(termcolor.colored("Ahmed", color="red"))

print(termcolor.colored(pyfiglet.figlet_format("Ahmed"), color="yellow"))


