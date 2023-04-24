from StateMachine.App import App
from sys import exit


def main():
    app = App()
    ret = app.run()
    exit(ret)


if __name__ == "__main__":
    main()
