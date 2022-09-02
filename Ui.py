import os
import sys

from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog, QPushButton, QLabel, QComboBox, QToolTip, QMessageBox

from Db import Db
from Pic import Pic
from check import check_month, check_num


class Ui(QWidget):
    def __init__(self):
        super(Ui, self).__init__()
        QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

        self.label1 = QLabel('起始日期', self)
        self.label2 = QLabel('结束日期', self)
        self.label3 = QLabel('', self)
        self.combobox1 = QComboBox(self)
        self.combobox2 = QComboBox(self)
        self.combobox3 = QComboBox(self)
        self.combobox4 = QComboBox(self)
        self.combobox5 = QComboBox(self)
        self.combobox6 = QComboBox(self)
        self.button1 = QPushButton('保存路径', self)
        self.button2 = QPushButton('生成截图', self)

        self.file_path = None
        self.num = 1
        self.days = None
        self.ui()

    def ui(self):
        width = 250
        height = 100
        interval = 150
        window_width = 1500
        window_height = 1200
        year_list = [str(i) for i in range(2022, 2030)]
        month_list = [str(i) for i in range(1, 13)]
        day_list = [str(i) for i in range(1, 32)]

        self.label1.setGeometry(0, 0, width, 100)
        self.label1.setAlignment(Qt.AlignCenter)

        self.label2.setGeometry(0, 150, width, height)
        self.label2.setAlignment(Qt.AlignCenter)

        self.combobox1.addItems(year_list)
        self.combobox1.setGeometry(width + interval, 0, width, height)

        self.combobox2.addItems(month_list)
        self.combobox2.setGeometry(width * 2 + interval * 2, 0, width, height)
        self.combobox2.activated.connect(lambda: self.change_days(2))

        self.combobox3.addItems(day_list)
        self.combobox3.setGeometry(width * 3 + interval * 3, 0, width, height)

        self.combobox4.addItems(year_list)
        self.combobox4.setGeometry(width + interval, interval, width, height)

        self.combobox5.addItems(month_list)
        self.combobox5.setGeometry(width * 2 + interval * 2, interval, width, height)
        self.combobox5.activated.connect(lambda: self.change_days(5))

        self.combobox6.addItems(day_list)
        self.combobox6.setGeometry(width * 3 + interval * 3, interval, width, height)

        self.button1.setGeometry(0, interval * 2, width, height)
        self.button1.clicked.connect(self.file_dialog)

        self.label3.setGeometry(width + interval, interval * 2, window_width - width - interval, height)
        self.label3.setText(os.path.abspath('./'))

        self.button2.setGeometry(int((window_width - width) / 2), interval * 5, width, height)
        self.button2.clicked.connect(self.check_make)

        desktop = QApplication.desktop()
        x = int(desktop.width() / 2 - window_width / 2)
        y = int(desktop.height() / 2 - window_height / 2)
        self.setGeometry(x, y, window_width, window_height)
        self.setWindowTitle('keep打卡')
        QToolTip.setFont(QFont('微软雅黑'))
        self.setWindowIcon(QIcon('pic/天气下雨.jpg'))
        self.show()

    def file_dialog(self):
        self.file_path = QFileDialog.getExistingDirectory(self, '选择保存路径', 'E:/')
        self.label3.setText(self.file_path)

    def change_days(self, box_id):
        if box_id == 2:
            text = self.combobox2.currentText()
            num = check_month(self.combobox1.currentText(), text)
            self.combobox3.clear()
            day_list = [str(i) for i in range(1, num + 1)]
            self.combobox3.addItems(day_list)
        elif box_id == 5:
            text = self.combobox5.currentText()
            num = check_month(self.combobox4.currentText(), text)
            self.combobox6.clear()
            day_list = [str(i) for i in range(1, num + 1)]
            self.combobox6.addItems(day_list)

    def refresh_days(self):
        year_start = self.combobox1.currentText()
        month_start = self.combobox2.currentText()
        day_start = self.combobox3.currentText()
        year_end = self.combobox4.currentText()
        month_end = self.combobox5.currentText()
        day_end = self.combobox6.currentText()
        self.days = ((year_start, month_start, day_start), (year_end, month_end, day_end))
        self.num = check_num(self.days[0], self.days[1])

    def make_pics(self):
        self.file_path = self.label3.text()
        db = Db()
        db_data = db.get_disdata(self.num)
        pic = Pic()
        pic.edit_pics(tb_datas=db_data, days=self.days, file_path=self.file_path)
        self.end_make()

    def check_make(self):
        self.refresh_days()
        if self.num <= 0:
            self.hint_error()
        else:
            self.make_pics()

    def end_make(self):
        reply = QMessageBox.information(self, '提示', f'{self.num}张打卡已生成', QMessageBox.Ok)

    def hint_error(self):
        reply = QMessageBox.information(self, '提示', '结束日期大于开始日期', QMessageBox.Ok)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Ui()
    sys.exit(app.exec_())
