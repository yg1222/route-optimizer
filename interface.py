from PySide6 import QtWidgets, QtCore
from PySide6.QtGui import QIcon, QImage, QPixmap
from PySide6.QtUiTools import QUiLoader
from ui_main import Ui_MainWindow, QImage
from ui_htu import Ui_htuWidget
import pyperclip
import webbrowser
from optimizer import get_optimization, get_api_key


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
  def __init__(self, app, rtn_data):
    super().__init__()
    self.rtn_data = rtn_data
    self.setupUi(self)
    self.app = app
    self.setWindowTitle("Route Optimizer")
    self.setMaximumSize(700, 776)
    self.setMinimumSize(700, 776)
    self.btnLearnMore.clicked.connect(self.how_to_use)
    self.btnOptimize.clicked.connect(self.optimize_button)
    self.btnCopyLink.clicked.connect(self.copy_maps)
    self.btnOpenMaps.clicked.connect(self.open_maps)
    self.actionRefresh.triggered.connect(self.refresh)
    self.actionCopy.triggered.connect(self.copy)
    self.actionCut.triggered.connect(self.cut)
    self.actionPaste.triggered.connect(self.paste)
    self.actionHow_to_Use.triggered.connect(self.how_to_use)
    self.actionAbout.triggered.connect(self.about)
    self.actionUndo.triggered.connect(self.undo)
    self.actionRedo.triggered.connect(self.redo)
    self.actionQuit.triggered.connect(self.quit_app)
    
  

  # Methods
  def how_to_use(self):    
    print("how to use")
    # Shows the htuWidget
    self.window = QtWidgets.QWidget()
    self.ui = Ui_htuWidget()
    self.ui.setupUi(self.window)
    self.window.setMaximumSize(523, 643)
    self.window.setMinimumSize(523, 643)
    self.window.show()    

  def optimize_button(self):
    print("Optimize button clicked!")
    # Getting text from txtInputAddresses as a list of addresses
    self.input_addresses = self.txtInputAddresses.toPlainText()
    if self.input_addresses:
      self.input_addresses = self.input_addresses.splitlines()
      self.input_addresses = [line.strip() for line in self.input_addresses]
      print(self.input_addresses)
      # Performs the optimization, passes the data to self.rtn_data dictionary
      try:
        self.rtn_data = get_optimization(self.input_addresses)
      except Exception as e:
        print("Did not get optimized data, check for api_key. Error: "+ str(e))

      if self.rtn_data and 'lined_output' in self.rtn_data:
        self.txtOptimizedAddresses.setText(self.rtn_data['lined_output'])
      else:
        QtWidgets.QMessageBox.information(self, "Unable to open Maps", "There was an error running or displaying the optimization results.")
        
  def open_maps(self):
    if 'full_url' in self.rtn_data:
      webbrowser.open(self.rtn_data['full_url'])
    else:
      QtWidgets.QMessageBox.information(self, "Unable to open Maps", "There was an error running or displaying the optimization results.")
          
    print("Opem Maps button clicked!")

  def copy_maps(self):
    if 'full_url' in self.rtn_data:
      pyperclip.copy(self.rtn_data['full_url'])
      print("coppied url")
    print("Copy Maps button clicked!")

  def refresh(self):
    self.txtInputAddresses.setText("")
    self.txtOptimizedAddresses.setText("")
    self.rtn_data = {}
    print("refresh")
    
  def copy(self):
    self.txtInputAddresses.copy()
    print("copy")
    
  def cut(self):
    self.txtInputAddresses.cut()
    print("cut")
    
  def paste(self):
    self.txtInputAddresses.paste()    
    print("paste")
    
  def undo(self):
    self.txtInputAddresses.undo()
    print("undo")
    
  def redo(self):
    self.txtInputAddresses.redo()
    print("redo")  

  def about(self):
    print("about")
    QtWidgets.QMessageBox.information(self, "About Route Optimizer", "This app efficiently organizes given addresses by calculating the shortest routes between them, minimizing travel time and distance. \nIt utilizes a geolocation service to convert addresses to latitude and longitude coordinates. \nUsing a graph algorithm, the app then determines the optimal order of the addresses for the user, ensuring a time and cost-effective sequence for their journey.")

  def quit_app(self):
    print("quit")
    self.app.quit()
    