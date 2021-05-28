from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

import Class

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    Class.RecommendApps('kucing', 'imut')
    main_ui = Class.MainApps()
    main_ui.setup(MainWindow)

    MainWindow.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('close')