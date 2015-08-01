from flask_frozen import Freezer
from menu import menu

freezer = Freezer(menu)

if __name__ == '__main__':
    freezer.freeze()
