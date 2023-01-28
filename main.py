import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PassGen import Ui_MainWindow
import random


class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.Generate_But.clicked.connect(self.SetPassword)
        self.ui.PasswordLength_Sld.valueChanged.connect(self.SetLenght)
        self.ui.DecryptionTryPerSecond_Sld.valueChanged.connect(self.SetTry)


    def GeneratePassword(self):
        latin = ["a", "b", "c", "d", "e", 
                "f", "g", "h", "i", "j", 
                "k", "l", "m", "n", "o", 
                "p", "q", "r", "s", "t", 
                "u", "v", "w", "x", "y", 
                "z", "A", "B", "C", "D", 
                "E", "F", "G", "H", "I", 
                "J", "K", "L", "M", "N", 
                "O", "P", "Q", "R", "S", 
                "T", "U", "V", "W", "X", 
                "Y", "Z"]
        cyrillic = ["а", "б", "в", "г", "д", 
                    "е", "ё", "ж", "з", "и", 
                    "й", "к", "л", "м", "н", 
                    "о", "п", "р", "с", "т", 
                    "у", "ф", "х", "ц", "ч", 
                    "ш", "щ", "ъ", "ы", "ь", 
                    "э", "ю", "я", "А", "Б", 
                    "В", "Г", "Д", "Е", "Ё", 
                    "Ж", "З", "И", "Й", "К", 
                    "Л", "М", "Н", "О", "П", 
                    "Р", "С", "Т", "У", "Ф", 
                    "Х", "Ц", "Ч", "Ш", "Щ", 
                    "Ъ", "Ы", "Ь", "Э", "Ю", 
                    "Я"]
        nums = [str(i) for i in range(10)]
        spec = ["=", "-", "+", "_", ")", "(", "*", "&", "|", "^", "?", "%", "$", "#", "@", "!", ",", ".", "\\", "/", "\"", ":", ";", "]", "[", "{", "}", "<", ">", "~", "`", "'"]
        
        symbols = []
        if self.ui.Latin_Chb.isChecked():
            symbols.append(latin)
        if self.ui.Cyrilic_Chb.isChecked():
            symbols.append(cyrillic)
        if self.ui.Number_Chb.isChecked():
            symbols.append(nums)
        if self.ui.SpecialSymbols_Chb.isChecked():
            symbols.append(spec)
        
        if symbols == []:
            return "Выберите символы =>"
        # if int(self.label_2.text()) == 0:
        #     return "Выберите длинну пароля \/"
        Sequence = ""
        while len(Sequence) != int(self.ui.PasswordLengthNumber_Lab.text()):
            S = random.choice(symbols)
            Sequence += random.choice(S)
        
        self.SetTime(sum([len(i) for i in symbols]))
        return Sequence

    def SetPassword(self):
        self.ui.Password_Lab.setText(self.GeneratePassword())

    def SetLenght(self):
        self.ui.PasswordLengthNumber_Lab.setText(str(self.ui.PasswordLength_Sld.value()))

    def SetTry(self):
        self.ui.DecryptionTryPerSecondNumber_Lab.setText(str(self.ui.DecryptionTryPerSecond_Sld.value()))

    def SetTime(self, symbolsCoint):
        seconds = (symbolsCoint**self.ui.PasswordLength_Sld.value()) // self.ui.DecryptionTryPerSecond_Sld.value()
        if seconds//60//60//24//365 >= 7_500_000_000:
            answer = "Поверь, к этому моменту твой пароль уже никому не понадобится"
        elif seconds == 0:
            answer = "1c"
        else:
            answer = str(seconds) + "c " if seconds < 60 else str(seconds//60) + "м " + str(seconds%60) + "с " if seconds//60 < 60 else str(seconds//60//60) + "ч " +  str(seconds//60%60) + "м " + str(seconds%60) + "с " if seconds//60//60 < 24 else str(seconds//60//60//24) + "д " +  str(seconds//60//60%24) + "ч " +  str(seconds//60%60) + "м " + str(seconds%60) + "с " if seconds//60//60//24 < 365 else str(seconds//60//60//24//365) + "л " + str(seconds//60//60//24%365) + "д " +  str(seconds//60//60%24) + "ч " +  str(seconds//60%60) + "м " + str(seconds%60) + "с " 
        self.ui.DecryptionTimeAnswer_Lab.setText(answer)

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())