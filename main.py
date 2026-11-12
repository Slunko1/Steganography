
import sys

from pathlib import Path
from PyQt6.QtWidgets import (
	QApplication, QDialog, QLabel
)
from PyQt6.QtGui import QFontDatabase, QPixmap
from PyQt6.QtCore import Qt
from PyQt6.uic import loadUi

import image_handling
import steganography

SCRIPT_DIR = Path(__file__).resolve().parent
UI_PATH = SCRIPT_DIR / "Steganography.ui"
FONT_PATH = SCRIPT_DIR / "ARCADECLASSIC.ttf"

class ImageLabel(QLabel):

	def __init__(self, parent=None):
		super().__init__(parent)
		self.setAcceptDrops(True)

	def dragEnterEvent(self, event):
		if event.mimeData().hasUrls():
			event.acceptProposedAction()

	def dropEvent(self, event):
		path = event.mimeData().urls()[0].toLocalFile()

		pixmap = QPixmap(path)

		self.setPixmap(
			pixmap.scaled(
				self.size(),
				Qt.AspectRatioMode.KeepAspectRatio,
				Qt.TransformationMode.SmoothTransformation
			)
		)


class UiScreen(QDialog):

	def __init__(self):
		super().__init__()
		loadUi(UI_PATH, self)

	def display_image(self, path):
		pixmap = QPixmap(str(path))

		self.ImageView.setPixmap(
			pixmap.scaled(
				self.ImageView.size(),
				Qt.AspectRatioMode.KeepAspectRatio,
				Qt.TransformationMode.SmoothTransformation
			)
		)

		self.ImageView.setFixedSize(
			pixmap.width(),
			pixmap.height()
		)

	def spracuj(self):
		if self.radioButton_Encrypt.isChecked():
			pass

		elif self.radioButton_Decrypt.isChecked():
			pass


if __name__ == "__main__":

	app = QApplication(sys.argv)

	QFontDatabase.addApplicationFont(str(FONT_PATH))

	ui = UiScreen()
	ui.setFixedSize(ui.size())
	ui.show()

	sys.exit(app.exec())
