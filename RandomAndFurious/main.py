import sys
import random
from PySide6 import QtCore, QtGui, QtWidgets

MOVIE_LIST = [
    'The Fast and The Furious',
    '2 Fast 2 Furious',
    'Fast and Furious: Tokyo Drift',
    # 'Fast and Furious (4)',
    'Fast 5',
    'Fast and Furious 6',
    # 'Furious 7',
    'The Fate of the Furious',
    # 'F9',
    # 'Fast X',
    'Fast and Furious Presents: Hobbs & Shaw'
]

SECOND_LIST = [
    'No Manches Frida (Netflix)'
]


class RandomAndFurious(QtWidgets.QWidget):
    def __init__(self, movie_list: list):
        super().__init__()
        self.setWindowTitle('Random and Furious')
        self.movie_list = movie_list
        # Layout structure
        layout = QtWidgets.QVBoxLayout()
        button_layout = QtWidgets.QHBoxLayout()
        # Close button
        close_button = QtWidgets.QPushButton('Close')
        close_button.clicked.connect(self.close)
        # Movie to watch list
        self.movie_to_watch = QtWidgets.QTextBrowser()
        self.movie_to_watch.setText('Magic movie you are about to watch is...')
        self.movie_to_watch.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        # Setting the randomize button
        randomize_button = QtWidgets.QPushButton('Random Time!')
        randomize_button.clicked.connect(self.select_movie)
        # Adding all to the layout
        layout.addWidget(self.movie_to_watch)
        button_layout.addWidget(randomize_button)
        button_layout.addWidget(close_button)
        layout.addLayout(button_layout)
        # Setting the layout and resizing the window
        self.setLayout(layout)
        self.resize(400, 300)

    def select_movie(self):
        movie_to_watch = random.choice(self.movie_list)
        self.movie_to_watch.setText(movie_to_watch)
        self.movie_to_watch.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    random_and_furious = RandomAndFurious(MOVIE_LIST)
    random_and_furious.show()
    sys.exit(app.exec())
