from .isochrones import Isochrones
from qgis.PyQt.QtWidgets import QMessageBox

class IrkutskAnalyzer:
    def __init__(self, iface):
        self.iface = iface
        self.isochrones = Isochrones(iface)
    
    def initGui(self):
        self.action = QAction("Анализ Иркутска", self.iface.mainWindow())
        self.action.triggered.connect(self.run_irkutsk_analysis)
        self.iface.addToolBarIcon(self.action)
    
    def run_irkutsk_analysis(self):
        """Специальный анализ для Иркутска с предустановками"""
        QMessageBox.information(None, "Анализ Иркутска", 
                               "Запускаем анализ с параметрами:\n"
                               "- Скорость: 5 км/ч\n"
                               "- Интервалы: 5, 10, 15 мин\n"
                               "- Данные: УДС Иркутска")
        self.isochrones.run()