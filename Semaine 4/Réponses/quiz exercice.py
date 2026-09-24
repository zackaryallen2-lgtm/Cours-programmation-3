from PySide6.QtWidgets import (QApplication, QMainWindow, QHBoxLayout, QPushButton, QWidget, QDialog,
                               QLabel, QVBoxLayout, QRadioButton, QButtonGroup, QCheckBox, QGridLayout, QComboBox,
                               QLineEdit, QProgressBar)
from PySide6.QtGui import QIcon, QColor, QPixmap
from PySide6.QtCore import QPropertyAnimation, Property

import sys


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
        self.question_1 = BoutonQuestions()
        self.question_1.setIcon(icone_1)
        self.question_1.clicked.connect(self.chercher_dialogue_1)
        self.disposition.addWidget(self.question_1)

        icone_2 = QIcon("./2.png")
        self.question_2 = BoutonQuestions()
        self.question_2.setIcon(icone_2)
        self.question_2.clicked.connect(self.chercher_dialogue_2)
        self.disposition.addWidget(self.question_2)

        icone_3 = QIcon("./3.png")
        self.question_3 = BoutonQuestions()
        self.question_3.setIcon(icone_3)
        self.question_3.clicked.connect(self.chercher_dialogue_3)
        self.disposition.addWidget(self.question_3)

        icone_4 = QIcon("./4.png")
        self.question_4 = BoutonQuestions()
        self.question_4.setIcon(icone_4)
        self.question_4.clicked.connect(self.chercher_dialogue_4)
        self.disposition.addWidget(self.question_4)

        icone_5 = QIcon("./5.png")
        self.question_5 = BoutonQuestions()
        self.question_5.setIcon(icone_5)
        self.question_5.clicked.connect(self.chercher_dialogue_5)
        self.disposition.addWidget(self.question_5)

        # Barre de Progression
        self.barre_progression = QProgressBar()
        self.barre_progression.setMinimum(0)
        self.barre_progression.setMaximum(5)
        self.disposition.addWidget(self.barre_progression)
        self.avancement = 0

        # Complétion du quiz
        self.sortie = BoutonQuestions("Sortie")
        icone_sortie = QIcon("./sortie.png")
        self.sortie.setIcon(icone_sortie)
        self.sortie.clicked.connect(self.sortir)
        self.disposition.addWidget(self.sortie)

    def chercher_dialogue_1(self):
        dialogue = Question1(self)
        dialogue.exec()

        self.entree_utilisateur = dialogue.get_data()

        if self.entree_utilisateur:
            self.question_1.setEnabled(False)
            self.question_1.stop_flash()
            self.avancement += 1
            self.barre_progression.setValue(self.avancement)
        else:
            self.question_1.flash()

    def chercher_dialogue_2(self):
        dialogue = Question2(self)
        dialogue.exec()

        self.entree_utilisateur = dialogue.get_data()

        if self.entree_utilisateur:
            self.question_2.setEnabled(False)
            self.question_2.stop_flash()
            self.avancement += 1
            self.barre_progression.setValue(self.avancement)
        else:
            self.question_2.flash()

    def chercher_dialogue_3(self):
        dialogue = Question3(self)
        dialogue.exec()

        self.entree_utilisateur = dialogue.get_data()

        if self.entree_utilisateur:
            self.question_3.setEnabled(False)
            self.question_3.stop_flash()
            self.avancement += 1
            self.barre_progression.setValue(self.avancement)
        else:
            self.question_3.flash()

    def chercher_dialogue_4(self):
        dialogue = Question4()
        dialogue.exec()

        self.entree_utilisateur = dialogue.get_data()

        if self.entree_utilisateur:
            self.question_4.setEnabled(False)
            self.question_4.stop_flash()
            self.avancement += 1
            self.barre_progression.setValue(self.avancement)
        else:
            self.question_4.flash()

    def chercher_dialogue_5(self):
        dialogue = Question5()
        dialogue.exec()

        self.entree_utilisateur = dialogue.get_data()

        if self.entree_utilisateur:
            self.question_5.setEnabled(False)
            self.question_5.stop_flash()
            self.avancement += 1
            self.barre_progression.setValue(self.avancement)
        else:
            self.question_5.flash()

    def sortir(self):
        if self.barre_progression.value() == self.barre_progression.maximum():
            self.sortie.stop_flash()
            self.reussite = FenetreDeReussite()
            self.reussite.show()
            self.close()
        else:
            self.sortie.setText("Veuillez Compléter le quiz avant de quitter!")
            self.sortie.flash()


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


class Question2(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Question 2")

        # Création de la disposition de la question
        self.disposition = QVBoxLayout()
        self.label = QLabel(f"Quelle est la racine carré de 4?")
        self.disposition.addWidget(self.label)
        self.setLayout(self.disposition)

        # Création des réponses
        self.disposition_reponses = QGridLayout()
        self.reponse_1 = QCheckBox("3")
        self.reponse_2 = QCheckBox("2")
        self.reponse_3 = QCheckBox("5")
        self.reponse_4 = QCheckBox("1")

        self.disposition.addLayout(self.disposition_reponses)
        self.disposition_reponses.addWidget(self.reponse_1, 0, 0)
        self.disposition_reponses.addWidget(self.reponse_2, 0, 1)
        self.disposition_reponses.addWidget(self.reponse_3, 1, 0)
        self.disposition_reponses.addWidget(self.reponse_4, 1, 1)

        self.groupe_reponses = QButtonGroup()
        self.groupe_reponses.addButton(self.reponse_1)
        self.groupe_reponses.addButton(self.reponse_2)
        self.groupe_reponses.addButton(self.reponse_3)
        self.groupe_reponses.addButton(self.reponse_4)

        # Ajout des options pour quitter et confirmer
        self.disposition_ok_annuler = QHBoxLayout()
        self.disposition.addLayout(self.disposition_ok_annuler)
        self.bouton_ok = QPushButton("Ok")
        self.bouton_ok.clicked.connect(self.accept)  # Ferme le dialogue et renvoie QDialog.Accepted (1)
        self.disposition_ok_annuler.addWidget(self.bouton_ok)
        self.bouton_annuler = QPushButton("Annuler")
        self.bouton_annuler.clicked.connect(self.reject)  # Ferme le dialogue et renvoie QDialog.Rejected (0)
        self.disposition_ok_annuler.addWidget(self.bouton_annuler)

    def get_data(self):
        if self.groupe_reponses.checkedButton() == self.reponse_2:
            return True
        return False


class Question3(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Question 3")

        # Création question
        self.disposition = QVBoxLayout()
        self.label = QLabel("Quelle est la couleur du partie libérale?")
        self.setLayout(self.disposition)
        self.disposition.addWidget(self.label)

        # Création réponses
        self.reponses = QComboBox()
        self.reponses.addItem("bleu")
        self.reponses.addItem("blanc")
        self.reponses.addItem("rouge")
        self.disposition.addWidget(self.reponses)

        # Ajout des options pour quitter et confirmer
        self.disposition_ok_annuler = QHBoxLayout()
        self.disposition.addLayout(self.disposition_ok_annuler)
        self.bouton_ok = QPushButton("Ok")
        self.bouton_ok.clicked.connect(self.accept)  # Ferme le dialogue et renvoie QDialog.Accepted (1)
        self.disposition_ok_annuler.addWidget(self.bouton_ok)
        self.bouton_annuler = QPushButton("Annuler")
        self.bouton_annuler.clicked.connect(self.reject)  # Ferme le dialogue et renvoie QDialog.Rejected (0)
        self.disposition_ok_annuler.addWidget(self.bouton_annuler)

    def get_data(self):
        if self.reponses.currentText() == "rouge":
            return True
        return False


class Question4(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Question 4")

        # Création de la disposition du dialogue
        self.disposition = QVBoxLayout()
        self.label = QLabel("Que font 3*5?")
        self.disposition.addWidget(self.label)
        self.setLayout(self.disposition)

        # Création de la réponse
        self.reponse = QLineEdit()
        self.reponse.setText("Entrez votre réponse")
        self.disposition.addWidget(self.reponse)

        # Ajout des options pour quitter et confirmer
        self.disposition_ok_annuler = QHBoxLayout()
        self.disposition.addLayout(self.disposition_ok_annuler)
        self.bouton_ok = QPushButton("Ok")
        self.bouton_ok.clicked.connect(self.accept)  # Ferme le dialogue et renvoie QDialog.Accepted (1)
        self.disposition_ok_annuler.addWidget(self.bouton_ok)
        self.bouton_annuler = QPushButton("Annuler")
        self.bouton_annuler.clicked.connect(self.reject)  # Ferme le dialogue et renvoie QDialog.Rejected (0)
        self.disposition_ok_annuler.addWidget(self.bouton_annuler)

    def get_data(self):
        if self.reponse.text() == "15":
            return True
        return False


class Question5(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Question 5")

        # Disposition de la question
        self.disposition = QVBoxLayout()
        self.question = QLabel("Lequel de c'est éléments n'est pas une planète?")
        self.setLayout(self.disposition)
        self.disposition.addWidget(self.question)

        # Création des réponses
        self.reponse_1 = QRadioButton("Mars")
        self.reponse_2 = QRadioButton("Neptune")
        self.reponse_3 = QRadioButton("Pluton")

        self.groupe_reponses = QButtonGroup()
        self.groupe_reponses.addButton(self.reponse_1)
        self.groupe_reponses.addButton(self.reponse_2)
        self.groupe_reponses.addButton(self.reponse_3)

        self.disposition_reponses = QHBoxLayout()
        self.disposition_reponses.addWidget(self.reponse_1)
        self.disposition_reponses.addWidget(self.reponse_2)
        self.disposition_reponses.addWidget(self.reponse_3)
        self.disposition.addLayout(self.disposition_reponses)

        # Ajout des options pour quitter et confirmer
        self.disposition_ok_annuler = QHBoxLayout()
        self.disposition.addLayout(self.disposition_ok_annuler)
        self.bouton_ok = QPushButton("Ok")
        self.bouton_ok.clicked.connect(self.accept)  # Ferme le dialogue et renvoie QDialog.Accepted (1)
        self.disposition_ok_annuler.addWidget(self.bouton_ok)
        self.bouton_annuler = QPushButton("Annuler")
        self.bouton_annuler.clicked.connect(self.reject)  # Ferme le dialogue et renvoie QDialog.Rejected (0)
        self.disposition_ok_annuler.addWidget(self.bouton_annuler)

    def get_data(self):
        if self.groupe_reponses.checkedButton() == self.reponse_3:
            return True
        return False


class BoutonQuestions(QPushButton):

    def __init__(self, texte=None, parent=None):
        super().__init__(texte, parent)

        self._bg = QColor("#e0e0e0")
        self.animation = QPropertyAnimation(self, b"bg", self)
        self.animation.setDuration(1000)
        self.animation.setKeyValueAt(0.0, QColor("#e0e0e0"))
        self.animation.setKeyValueAt(0.5, QColor("#ff5555"))
        self.animation.setKeyValueAt(1.0, "#e0e0e0")
        self.animation.setLoopCount(-1)

    def get_bg(self):
        return self._bg

    def set_bg(self, couleur):
        self._bg = couleur
        self.setStyleSheet(f"background-color: {couleur.name()};")

    bg = Property(QColor, get_bg, set_bg)

    def flash(self):
        self.animation.start()

    def stop_flash(self):
        self.animation.stop()
        self.set_bg(QColor("#e0e0e0"))


class FenetreDeReussite(QMainWindow):

    def __init__(self):
        super().__init__()
        icone = QIcon("./Réussi.png")
        self.setWindowIcon(icone)
        self.setWindowTitle("Vous avez réussi!")

        # Création de la disposition de la fenêtre
        self.label = QLabel()
        self.image = QPixmap("./Réussi.png")
        self.image.setDevicePixelRatio(2)
        self.label.setPixmap(self.image)
        self.setCentralWidget(self.label)
        self.resize(512, 512)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    quiz = Quiz()
    quiz.show()
    sys.exit(app.exec())
