import sys
from PyQt5.QtWidgets import QApplication
from model.sinusoidal_model import SinusoidalModel
from view.sinusoidal_view import SinusoidalView
from controller.sinusoidal_controller import SinusoidalController

def main():
    app = QApplication(sys.argv)
    
    model = SinusoidalModel()
    view = SinusoidalView(controller=None)
    controller = SinusoidalController(model, view)
    
    view.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
