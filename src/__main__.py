from sys import argv
from .common import App

app = App()

if __name__ == "__main__":
    app.sync(*argv[1:])
