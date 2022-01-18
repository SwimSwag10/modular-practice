class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print(f"{bcolors.UNDERLINE}{bcolors.FAIL}{bcolors.BOLD}--- welcome [BLANK] ---{bcolors.ENDC}")

local_val = "magical unicorns"
def square(x):
    return x * x
class User:
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        return "hello"

# in the same file, add the following below the User class
print(square(5))
user = User("Anna")
print(user.name)
print(user.say_hello())
# all of the code in here is executed when the child.py file is run
print(__name__)

if __name__ == "__main__": # this identifies if the file is being executed on the parent imported file
    print(f"{bcolors.FAIL}Directly executed{bcolors.ENDC}")
else:
    print(f"{bcolors.FAIL}Child executed - The file is called: {bcolors.BOLD}{__name__}{bcolors.ENDC}")
  