from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import RetriveSummoners
import CreateTeams


def setup_line_widgets(widget_list):
    y = 25
    x = 50
    index = 0
    for i in widget_list:
        i.resize(225, 25)
        i.move(x, y)
        if index == 4:
            y = -15
            x = 325
        y += 40
        i.setPlaceholderText("Summoner {}".format(index+1))
        index += 1


def exit_app():
    app.closeAllWindows()


class SummonerInput(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setMinimumSize(QSize(600, 400))
        self.setWindowTitle("Summoner Input")
        self.retrieve_button = QPushButton('Create Teams', self)
        self.retrieve_button.resize(200, 50)
        self.retrieve_button.move(200, 350)
        self.retrieve_button.clicked.connect(self.retrieve)
        self.summoner1 = QLineEdit(self)
        self.summoner2 = QLineEdit(self)
        self.summoner3 = QLineEdit(self)
        self.summoner4 = QLineEdit(self)
        self.summoner5 = QLineEdit(self)
        self.summoner6 = QLineEdit(self)
        self.summoner7 = QLineEdit(self)
        self.summoner8 = QLineEdit(self)
        self.summoner9 = QLineEdit(self)
        self.summoner10 = QLineEdit(self)
        self.username_input_list = [self.summoner1, self.summoner2, self.summoner3, self.summoner4, self.summoner5,
                                    self.summoner6, self.summoner7, self.summoner8, self.summoner9, self.summoner10]
        setup_line_widgets(self.username_input_list)

    def retrieve(self):
        usernames = []
        for i in self.username_input_list:
            usernames.append(i.text())
        summoner_list = RetriveSummoners.main(usernames)
        teams = CreateTeams.main(summoner_list)
        exit_app()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    start_window = SummonerInput()
    start_window.show()
    sys.exit(app.exec_())