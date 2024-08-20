from colorama import Fore, init

init()


class View:
    def alert(self, msg):
        print("\n")
        print(Fore.RED + msg)
        self.reset()

    def info(self, msg):
        print(Fore.BLUE + msg)
        self.reset()

    def ok(self, msg):
        print("\n" + Fore.GREEN + msg + "...........................OK")
        self.reset()

    def reset(self):
        print(Fore.RESET)
