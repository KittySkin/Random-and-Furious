import json
import sys
import random

from PySide6 import QtCore, QtWidgets

NETFLIX_CATALOGUE = json.load(open('result.json'))['results']

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
        # Movie information display
        self.movie_info = QtWidgets.QTextBrowser()
        self.movie_info.setText("Magic Movie you are about to watch is...")
        self.movie_info.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.movie_info.setOpenExternalLinks(True)
        self.movie_info.setStyleSheet("border: none;")
        # Setting the app's theme
        self.setStyleSheet("background-color: #333; color: #fff;")
        # Setting the randomize button
        randomize_button = QtWidgets.QPushButton('Random Time!')
        randomize_button.clicked.connect(self.select_movie)
        # Adding widgets to layout
        layout.addWidget(self.movie_info)
        button_layout.addWidget(randomize_button)
        button_layout.addWidget(close_button)
        layout.addLayout(button_layout)
        # Setting the layout and resizing the window
        self.setLayout(layout)
        self.resize(400, 300)

    def select_movie(self):
        movie_to_watch = random.choice(self.movie_list)
        movie_title = f"<div style='text-align: center;'><b>{movie_to_watch['title']}</b><br><br>"
        movie_synopsis = f"{movie_to_watch['synopsis']}<br><br>"
        movie_url = f"<a href='https://www.netflix.com/watch/{movie_to_watch['netflix_id']}'>Watch on Netflix</a></div>"
        movie_info_text = movie_title + movie_synopsis + movie_url
        self.movie_info.setHtml(movie_info_text)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    random_and_furious = RandomAndFurious(NETFLIX_CATALOGUE)
    random_and_furious.show()
    sys.exit(app.exec())
