from PySide6.QtWidgets import (QApplication, QMainWindow, QHBoxLayout, QPushButton, QWidget, QDialog,
                               QLabel, QVBoxLayout, QRadioButton, QButtonGroup)
from PySide6.QtGui import QIcon


class Quiz(QMainWindow):

    def __init__(self):
        super().__init__()
        self.entree_utilisateur = False

        # Disposition de la fenêtre
        widget_central = QWidget()
        self.setCentralWidget(widget_central)
        self.disposition = QVBoxLayout()
        widget_central.setLayout(self.disposition)
        self.setMinimumHeight(512)
        self.setMinimumWidth(512)
        self.setWindowTitle("Quiz!")
        icone = QIcon("./quiz.png")
        self.setWindowIcon(icone)

        # Création questions
        icone_1 = QIcon("./1.png")
        self.question_1 = QPushButton()
        self.question_1.setIcon(icone_1)
        self.question_1.clicked.connect(self.chercher_dialogue_1)
        self.disposition.addWidget(self.question_1)

        icone_2 = QIcon("./2.png")
        self.question_2 = QPushButton()
        self.question_2.setIcon(icone_2)
        self.disposition.addWidget(self.question_2)

        icone_3 = QIcon("./3.png")
        self.question_3 = QPushButton()
        self.question_3.setIcon(icone_3)
        self.disposition.addWidget(self.question_3)

        icone_4 = QIcon("./4.png")
        self.question_4 = QPushButton()
        self.question_4.setIcon(icone_4)
        self.disposition.addWidget(self.question_4)

        icone_5 = QIcon("./5.png")
        self.question_5 = QPushButton()
        self.question_5.setIcon(icone_5)
        self.disposition.addWidget(self.question_5)

        icone_6 = QIcon("./6.png")
        self.question_6 = QPushButton()
        self.question_6.setIcon(icone_6)
        self.disposition.addWidget(self.question_6)

    def chercher_dialogue_1(self):
        dialogue = Question1(self)
        resultat = dialogue.exec()

        if resultat == QDialog.Accepted:
            self.entree_utilisateur = dialogue.get_data()

        if self.entree_utilisateur:
            self.question_1.setEnabled(False)
        else:
            self.question_1.setStyleSheet()


class Question1(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Question 1")

        # Création de la disposition du Dialog
        self.disposition = QVBoxLayout()
        self.label = QLabel("Quelle est la capitale de la France?")
        self.disposition.addWidget(self.label)
        self.setLayout(self.disposition)

        # Ajout des réponses possibles
        self.disposition_reponse = QHBoxLayout()
        self.disposition.addLayout(self.disposition_reponse)
        self.reponse_1 = QRadioButton("Paris")
        self.reponse_2 = QRadioButton("Louvre")
        self.reponse_3 = QRadioButton("Londre")

        self.groupe_reponses = QButtonGroup()
        self.groupe_reponses.addButton(self.reponse_1)
        self.groupe_reponses.addButton(self.reponse_2)
        self.groupe_reponses.addButton(self.reponse_3)

        self.disposition_reponse.addWidget(self.reponse_1)
        self.disposition_reponse.addWidget(self.reponse_2)
        self.disposition_reponse.addWidget(self.reponse_3)

        # Ajout des options pour quitter et confirmer
        self.disposition_ok_annuler = QHBoxLayout()
        self.disposition.addLayout(self.disposition_ok_annuler)
        self.bouton_ok = QPushButton("Ok")
        self.bouton_ok.clicked.connect(self.accept)         # Ferme le dialogue et renvoie QDialog.Accepted (1)
        self.disposition_ok_annuler.addWidget(self.bouton_ok)
        self.bouton_annuler = QPushButton("Annuler")
        self.bouton_annuler.clicked.connect(self.reject)    # Ferme le dialogue et renvoie QDialog.Rejected (0)
        self.disposition_ok_annuler.addWidget(self.bouton_annuler)

    def get_data(self):
        if self.groupe_reponses.checkedButton() == self.reponse_1:
            return True
        return False


if __name__ == "__main__":
    app = QApplication()
    quiz = Quiz()
    quiz.show()
    app.exec()
