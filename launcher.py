#!/usr/bin/env python3
"""
888888 8888b.  Yb    dP .dP"Y8 
88__    8I  Yb  Yb  dP  `Ybo."  
88""    8I  dY   YbdP   o.`Y8b 
888888 8888Y"     YP    8bodP' 

© Elburgo Tecnoclub - Martin Ortiz.
© Elburgo Data Visualization Software.
-- @Version: 1.0-BETA
-- @data: 3/13/2023
"""

import os
import sys

from edvs import MainWindow
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    # Fixes high dpi issues and scaling over 100
    os.environ["QT_FONT_DPI"] = "96" 
    
    # Start the application
    app = QApplication(sys.argv) 

    # Start the main window
    window = MainWindow() 

    # Start the event loop 
    sys.exit(app.exec())