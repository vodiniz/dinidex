# Form implementation generated from reading ui file 'Dinidex_alternative.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_DiniDex(object):
    def setupUi(self, DiniDex):
        DiniDex.setObjectName("DiniDex")
        DiniDex.resize(920, 860)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/icon/program_icon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        DiniDex.setWindowIcon(icon)
        DiniDex.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(DiniDex)
        self.centralwidget.setObjectName("centralwidget")
        self.pokemon_logo = QtWidgets.QWidget(self.centralwidget)
        self.pokemon_logo.setGeometry(QtCore.QRect(0, -40, 300, 200))
        self.pokemon_logo.setStyleSheet("image: url(resources/logo/pokemon_logo.png);\n"
"background:transparent;")
        self.pokemon_logo.setObjectName("pokemon_logo")
        self.background = QtWidgets.QWidget(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 901, 871))
        self.background.setStyleSheet("background-color: rgb(206, 76, 62);\n"
"\n"
"")
        self.background.setObjectName("background")
        self.evolution_line_widget = QtWidgets.QWidget(self.background)
        self.evolution_line_widget.setGeometry(QtCore.QRect(260, 480, 631, 371))
        self.evolution_line_widget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:8px;\n"
"")
        self.evolution_line_widget.setObjectName("evolution_line_widget")
        self.evo1_type1 = QtWidgets.QLabel(self.evolution_line_widget)
        self.evo1_type1.setGeometry(QtCore.QRect(10, 240, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.evo1_type1.setFont(font)
        self.evo1_type1.setStyleSheet("image: url(resources/pokemon_type_icon/grass_type.png);\n" #MUDAR AQUI PARA UMA VARIAVEL DO TIPO DO POKEMON
"background-color: transparent;")
        self.evo1_type1.setText("")
        self.evo1_type1.setObjectName("evo1_type1")
        self.evo1_type2 = QtWidgets.QLabel(self.evolution_line_widget)
        self.evo1_type2.setGeometry(QtCore.QRect(80, 240, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.evo1_type2.setFont(font)
        self.evo1_type2.setStyleSheet("image: url(resources/pokemon_type_icon/poison_type.png);\n" #MUDAR AQUI PARA UMA VARIAVEL DO TIPO DO POKEMON
"background-color: transparent;")
        self.evo1_type2.setText("")
        self.evo1_type2.setObjectName("evo1_type2")
        self.evo_detail_1_2 = QtWidgets.QLabel(self.evolution_line_widget)
        self.evo_detail_1_2.setGeometry(QtCore.QRect(170, 150, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.evo_detail_1_2.setFont(font)
        self.evo_detail_1_2.setObjectName("evo_detail_1_2")
        self.evolution1_sprite = QtWidgets.QLabel(self.evolution_line_widget)
        self.evolution1_sprite.setGeometry(QtCore.QRect(10, 100, 140, 140))
        self.evolution1_sprite.setStyleSheet("image: url(resources/sprites/1.png);\n" #MUDAR AQUI PARA UMA VARIAVEL DA SPRITE COM NUMERO DA DEX.
"")
        self.evolution1_sprite.setText("")
        self.evolution1_sprite.setObjectName("evolution1_sprite")
        self.evolution2_sprite = QtWidgets.QLabel(self.evolution_line_widget)
        self.evolution2_sprite.setGeometry(QtCore.QRect(230, 100, 140, 140))
        self.evolution2_sprite.setStyleSheet("image: url(resources/sprites/2.png);\n" #MUDAR AQUI PARA UMA VARIAVEL DA SPRITE COM NUMERO DA DEX.
"background:transparent;\n"
"")
        self.evolution2_sprite.setText("")
        self.evolution2_sprite.setObjectName("evolution2_sprite")
        self.evolution3_sprite = QtWidgets.QLabel(self.evolution_line_widget)
        self.evolution3_sprite.setGeometry(QtCore.QRect(460, 100, 140, 140))
        self.evolution3_sprite.setStyleSheet("image: url(resources/sprites/3.png);\n"
"background:transparent;\n"
"")
        self.evolution3_sprite.setText("")
        self.evolution3_sprite.setObjectName("evolution3_sprite")
        self.evo2_type2_2 = QtWidgets.QLabel(self.evolution_line_widget)
        self.evo2_type2_2.setGeometry(QtCore.QRect(240, 240, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.evo2_type2_2.setFont(font)
        self.evo2_type2_2.setStyleSheet("image: url(resources/pokemon_type_icon/grass_type.png);\n" #MUDAR AQUI PARA UMA VARIAVEL COM O TYPE1_TYPE 
"background-color: transparent;")
        self.evo2_type2_2.setText("")
        self.evo2_type2_2.setObjectName("evo2_type2_2")
        self.evo2_type2 = QtWidgets.QLabel(self.evolution_line_widget)
        self.evo2_type2.setGeometry(QtCore.QRect(310, 240, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.evo2_type2.setFont(font)
        self.evo2_type2.setStyleSheet("image: url(resources/pokemon_type_icon/poison_type.png);\n" #MUDAR AQUI PARA UMA VARIAVEL COM O TYPE1_TYPE DO POKEMON
"background-color: transparent;")
        self.evo2_type2.setText("")
        self.evo2_type2.setObjectName("evo2_type2")
        self.evo3_type1 = QtWidgets.QLabel(self.evolution_line_widget)
        self.evo3_type1.setGeometry(QtCore.QRect(460, 240, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.evo3_type1.setFont(font)
        self.evo3_type1.setStyleSheet("image: url(resources/pokemon_type_icon/grass_type.png);\n" #MUDAR AQUI PARA UMA VARIAVEL COM O TYPE1_TYPE  DO POKEMON
"background-color: transparent;")
        self.evo3_type1.setText("")
        self.evo3_type1.setObjectName("evo3_type1")
        self.evo3_type2 = QtWidgets.QLabel(self.evolution_line_widget)
        self.evo3_type2.setGeometry(QtCore.QRect(530, 240, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.evo3_type2.setFont(font)
        self.evo3_type2.setStyleSheet("image: url(resources/pokemon_type_icon/poison_type.png);\n" #MUDAR AQUI PARA UMA VARIAVEL COM O TYPE1_TYPE  DO POKEMON
"background-color: transparent;")
        self.evo3_type2.setText("")
        self.evo3_type2.setObjectName("evo3_type2")
        self.arrow_evo_2_4 = QtWidgets.QLabel(self.evolution_line_widget)
        self.arrow_evo_2_4.setGeometry(QtCore.QRect(390, 170, 51, 31))
        self.arrow_evo_2_4.setStyleSheet("image: url(resources/arrow/default_right_arrow.png);\n"
"background-color: transparent;")
        self.arrow_evo_2_4.setText("")
        self.arrow_evo_2_4.setObjectName("arrow_evo_2_4")
        self.evo_detail_2_3 = QtWidgets.QLabel(self.evolution_line_widget)
        self.evo_detail_2_3.setGeometry(QtCore.QRect(400, 150, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.evo_detail_2_3.setFont(font)
        self.evo_detail_2_3.setObjectName("evo_detail_2_3")
        self.arrow_evo_1_2 = QtWidgets.QLabel(self.evolution_line_widget)
        self.arrow_evo_1_2.setGeometry(QtCore.QRect(170, 170, 51, 31))
        self.arrow_evo_1_2.setStyleSheet("image: url(resources/arrow/default_right_arrow.png);\n"
"background-color: transparent;")
        self.arrow_evo_1_2.setText("")
        self.arrow_evo_1_2.setObjectName("arrow_evo_1_2")
        self.evolution3_sprite.raise_()
        self.evolution1_sprite.raise_()
        self.evo1_type1.raise_()
        self.evo1_type2.raise_()
        self.evo_detail_1_2.raise_()
        self.evolution2_sprite.raise_()
        self.evo2_type2_2.raise_()
        self.evo2_type2.raise_()
        self.evo3_type1.raise_()
        self.evo3_type2.raise_()
        self.arrow_evo_2_4.raise_()
        self.evo_detail_2_3.raise_()
        self.arrow_evo_1_2.raise_()
        self.label_type1 = QtWidgets.QLabel(self.background)
        self.label_type1.setGeometry(QtCore.QRect(5, 440, 115, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_type1.setFont(font)
        self.label_type1.setStyleSheet("image: url(resources/pokemon_type_icon/grass_type.png);\n"
"background-color: transparent;")
        self.label_type1.setText("")
        self.label_type1.setObjectName("pokemon_type1")
        self.label_type2 = QtWidgets.QLabel(self.background)
        self.label_type2.setGeometry(QtCore.QRect(120, 440, 115, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_type2.setFont(font)
        self.label_type2.setStyleSheet("image: url(resources/pokemon_type_icon/poison_type.png);\n"
"background-color: transparent;")
        self.label_type2.setText("")
        self.label_type2.setObjectName("pokemon_type2")
        self.sprite_pokemon = QtWidgets.QWidget(self.background)
        self.sprite_pokemon.setGeometry(QtCore.QRect(20, 170, 221, 221))
        self.sprite_pokemon.setStyleSheet("image: url(resources/sprites/1.png);\n"
"background:transparent;\n"
"")
        self.sprite_pokemon.setObjectName("sprite_pokemon")
        self.stats_widget = QtWidgets.QWidget(self.background)
        self.stats_widget.setGeometry(QtCore.QRect(500, 210, 391, 261))
        self.stats_widget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:8px;\n"
"")
        self.stats_widget.setObjectName("stats_widget")
        self.label_hp = QtWidgets.QLabel(self.stats_widget)
        self.label_hp.setGeometry(QtCore.QRect(10, 20, 80, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_hp.setFont(font)
        self.label_hp.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_hp.setObjectName("label_hp")
        self.label_attack = QtWidgets.QLabel(self.stats_widget)
        self.label_attack.setGeometry(QtCore.QRect(10, 60, 80, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_attack.setFont(font)
        self.label_attack.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_attack.setObjectName("label_attack")
        self.label_defense = QtWidgets.QLabel(self.stats_widget)
        self.label_defense.setGeometry(QtCore.QRect(10, 100, 80, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_defense.setFont(font)
        self.label_defense.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_defense.setObjectName("label_defense")
        self.label_spattack = QtWidgets.QLabel(self.stats_widget)
        self.label_spattack.setGeometry(QtCore.QRect(10, 140, 80, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_spattack.setFont(font)
        self.label_spattack.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_spattack.setObjectName("label_spattack")
        self.label_spdefense = QtWidgets.QLabel(self.stats_widget)
        self.label_spdefense.setGeometry(QtCore.QRect(10, 180, 80, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_spdefense.setFont(font)
        self.label_spdefense.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_spdefense.setObjectName("label_spdefense")
        self.label_speed = QtWidgets.QLabel(self.stats_widget)
        self.label_speed.setGeometry(QtCore.QRect(10, 220, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_speed.setFont(font)
        self.label_speed.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_speed.setObjectName("label_speed")
        self.label_defense_bar = QtWidgets.QLabel(self.stats_widget)
        self.label_defense_bar.setGeometry(QtCore.QRect(140, 110, 140, 6))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_defense_bar.setFont(font)
        self.label_defense_bar.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"border-radius: 3px;")
        self.label_defense_bar.setText("")
        self.label_defense_bar.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_defense_bar.setObjectName("label_defense_bar")
        self.label_spattack_bar = QtWidgets.QLabel(self.stats_widget)
        self.label_spattack_bar.setGeometry(QtCore.QRect(140, 150, 140, 6))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_spattack_bar.setFont(font)
        self.label_spattack_bar.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"border-radius: 3px;")
        self.label_spattack_bar.setText("")
        self.label_spattack_bar.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_spattack_bar.setObjectName("label_spattack_bar")
        self.label_spdefense_bar = QtWidgets.QLabel(self.stats_widget)
        self.label_spdefense_bar.setGeometry(QtCore.QRect(140, 190, 140, 6))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_spdefense_bar.setFont(font)
        self.label_spdefense_bar.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"border-radius: 3px;")
        self.label_spdefense_bar.setText("")
        self.label_spdefense_bar.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_spdefense_bar.setObjectName("label_spdefense_bar")
        self.label_speed_bar = QtWidgets.QLabel(self.stats_widget)
        self.label_speed_bar.setGeometry(QtCore.QRect(140, 230, 140, 6))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_speed_bar.setFont(font)
        self.label_speed_bar.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"border-radius: 3px;")
        self.label_speed_bar.setText("")
        self.label_speed_bar.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_speed_bar.setObjectName("label_speed_bar")
        self.label_attack_bar = QtWidgets.QLabel(self.stats_widget)
        self.label_attack_bar.setGeometry(QtCore.QRect(140, 70, 140, 6))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_attack_bar.setFont(font)
        self.label_attack_bar.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"border-radius: 3px;")
        self.label_attack_bar.setText("")
        self.label_attack_bar.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_attack_bar.setObjectName("label_attack_bar")
        self.label_hp_bar = QtWidgets.QLabel(self.stats_widget)
        self.label_hp_bar.setGeometry(QtCore.QRect(140, 30, 140, 6))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_hp_bar.setFont(font)
        self.label_hp_bar.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"border-radius: 3px;")
        self.label_hp_bar.setText("")
        self.label_hp_bar.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_hp_bar.setObjectName("label_hp_bar")
        self.label_hp_stat = QtWidgets.QLabel(self.stats_widget)
        self.label_hp_stat.setGeometry(QtCore.QRect(90, 20, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_hp_stat.setFont(font)
        self.label_hp_stat.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_hp_stat.setObjectName("label_hp_stat")
        self.label_attack_stat = QtWidgets.QLabel(self.stats_widget)
        self.label_attack_stat.setGeometry(QtCore.QRect(90, 60, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_attack_stat.setFont(font)
        self.label_attack_stat.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_attack_stat.setObjectName("label_attack_stat")
        self.label_defense_stat = QtWidgets.QLabel(self.stats_widget)
        self.label_defense_stat.setGeometry(QtCore.QRect(90, 100, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_defense_stat.setFont(font)
        self.label_defense_stat.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_defense_stat.setObjectName("label_defense_stat")
        self.label_spattack_stat = QtWidgets.QLabel(self.stats_widget)
        self.label_spattack_stat.setGeometry(QtCore.QRect(90, 140, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_spattack_stat.setFont(font)
        self.label_spattack_stat.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_spattack_stat.setObjectName("label_spattack_stat")
        self.label_spdefense_stat = QtWidgets.QLabel(self.stats_widget)
        self.label_spdefense_stat.setGeometry(QtCore.QRect(90, 180, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_spdefense_stat.setFont(font)
        self.label_spdefense_stat.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_spdefense_stat.setObjectName("label_spdefense_stat")
        self.label_speed_stat = QtWidgets.QLabel(self.stats_widget)
        self.label_speed_stat.setGeometry(QtCore.QRect(90, 220, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_speed_stat.setFont(font)
        self.label_speed_stat.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_speed_stat.setObjectName("label_speed_stat")
        self.abilities_widget = QtWidgets.QWidget(self.background)
        self.abilities_widget.setGeometry(QtCore.QRect(260, 350, 230, 121))
        self.abilities_widget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:8px;\n"
"")
        self.abilities_widget.setObjectName("abilities_widget")
        self.abilities_title = QtWidgets.QLabel(self.abilities_widget)
        self.abilities_title.setGeometry(QtCore.QRect(0, 1, 230, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.abilities_title.setFont(font)
        self.abilities_title.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.abilities_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.abilities_title.setObjectName("abilities_title")
        self.na_ability1 = QtWidgets.QLabel(self.abilities_widget)
        self.na_ability1.setGeometry(QtCore.QRect(0, 60, 115, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.na_ability1.setFont(font)
        self.na_ability1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.na_ability1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.na_ability1.setObjectName("na_ability1")
        self.nability_title = QtWidgets.QLabel(self.abilities_widget)
        self.nability_title.setGeometry(QtCore.QRect(0, 30, 115, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nability_title.setFont(font)
        self.nability_title.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.nability_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.nability_title.setObjectName("nability_title")
        self.na_ability2 = QtWidgets.QLabel(self.abilities_widget)
        self.na_ability2.setGeometry(QtCore.QRect(0, 90, 115, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.na_ability2.setFont(font)
        self.na_ability2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.na_ability2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.na_ability2.setObjectName("na_ability2")
        self.hability_title = QtWidgets.QLabel(self.abilities_widget)
        self.hability_title.setGeometry(QtCore.QRect(115, 30, 115, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hability_title.setFont(font)
        self.hability_title.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.hability_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.hability_title.setObjectName("hability_title")
        self.ha_ability1 = QtWidgets.QLabel(self.abilities_widget)
        self.ha_ability1.setGeometry(QtCore.QRect(115, 60, 115, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.ha_ability1.setFont(font)
        self.ha_ability1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.ha_ability1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ha_ability1.setObjectName("ha_ability1")
        self.description_widget = QtWidgets.QWidget(self.background)
        self.description_widget.setGeometry(QtCore.QRect(260, 210, 230, 131))
        self.description_widget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:8px;\n"
"")
        self.description_widget.setObjectName("description_widget")
        self.description_title = QtWidgets.QLabel(self.description_widget)
        self.description_title.setGeometry(QtCore.QRect(0, 0, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.description_title.setFont(font)
        self.description_title.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.description_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.description_title.setObjectName("description_title")
        self.description_text = QtWidgets.QLabel(self.description_widget)
        self.description_text.setGeometry(QtCore.QRect(10, 40, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.description_text.setFont(font)
        self.description_text.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.description_text.setWordWrap(True)
        self.description_text.setObjectName("description_text")
        self.pokedex_pokemon = QtWidgets.QWidget(self.background)
        self.pokedex_pokemon.setGeometry(QtCore.QRect(15, 400, 211, 31))
        self.pokedex_pokemon.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius:10px;")
        self.pokedex_pokemon.setObjectName("pokedex_pokemon")
        self.name_pokemon = QtWidgets.QLabel(self.pokedex_pokemon)
        self.name_pokemon.setGeometry(QtCore.QRect(50, 0, 160, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.name_pokemon.setFont(font)
        self.name_pokemon.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius:10px;")
        self.name_pokemon.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.name_pokemon.setObjectName("name_pokemon")
        self.dex_number = QtWidgets.QLabel(self.pokedex_pokemon)
        self.dex_number.setGeometry(QtCore.QRect(10, 0, 40, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dex_number.setFont(font)
        self.dex_number.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius:10px;")
        self.dex_number.setObjectName("dex_number")
        self.scrollmoves = QtWidgets.QScrollArea(self.background)
        self.scrollmoves.setGeometry(QtCore.QRect(9, 480, 241, 371))
        self.scrollmoves.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:12px;\n"
"")
        self.scrollmoves.setWidgetResizable(True)
        self.scrollmoves.setObjectName("scrollmoves")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 241, 371))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.moves_title = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.moves_title.setGeometry(QtCore.QRect(120, 0, 120, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.moves_title.setFont(font)
        self.moves_title.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.moves_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.moves_title.setObjectName("moves_title")
        self.move1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.move1.setGeometry(QtCore.QRect(120, 20, 120, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.move1.setFont(font)
        self.move1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.move1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.move1.setObjectName("move1")
        self.level_title = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.level_title.setGeometry(QtCore.QRect(0, 0, 120, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.level_title.setFont(font)
        self.level_title.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.level_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.level_title.setObjectName("level_title")
        self.level_move1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.level_move1.setGeometry(QtCore.QRect(0, 20, 120, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.level_move1.setFont(font)
        self.level_move1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.level_move1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.level_move1.setObjectName("level_move1")
        self.scrollmoves.setWidget(self.scrollAreaWidgetContents)
        self.search_bar = QtWidgets.QLineEdit(self.background)
        self.search_bar.setGeometry(QtCore.QRect(260, 130, 631, 40))
        self.search_bar.setStyleSheet("color: rgb(68, 68, 68);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;")
        self.search_bar.setObjectName("search_bar")
        self.scrollmoves.raise_()
        self.pokedex_pokemon.raise_()
        self.stats_widget.raise_()
        self.evolution_line_widget.raise_()
        self.label_type1.raise_()
        self.label_type2.raise_()
        self.sprite_pokemon.raise_()
        self.abilities_widget.raise_()
        self.description_widget.raise_()
        self.search_bar.raise_()
        self.background.raise_()
        self.pokemon_logo.raise_()
        DiniDex.setCentralWidget(self.centralwidget)

        self.retranslateUi(DiniDex)
        QtCore.QMetaObject.connectSlotsByName(DiniDex)

    def retranslateUi(self, DiniDex):
        _translate = QtCore.QCoreApplication.translate
        DiniDex.setWindowTitle(_translate("DiniDex", "Dinidex - A simple Pokedex"))
        self.evo_detail_1_2.setText(_translate("DiniDex", "Level 16"))
        self.evo_detail_2_3.setText(_translate("DiniDex", "Level 32"))
        self.label_hp.setText(_translate("DiniDex", "Hp"))
        self.label_attack.setText(_translate("DiniDex", "Attack"))
        self.label_defense.setText(_translate("DiniDex", "Defense"))
        self.label_spattack.setText(_translate("DiniDex", "Sp. Attack"))
        self.label_spdefense.setText(_translate("DiniDex", "Sp.Defense"))
        self.label_speed.setText(_translate("DiniDex", "Speed"))
        self.label_hp_stat.setText(_translate("DiniDex", "70"))
        self.label_attack_stat.setText(_translate("DiniDex", "70"))
        self.label_defense_stat.setText(_translate("DiniDex", "70"))
        self.label_spattack_stat.setText(_translate("DiniDex", "70"))
        self.label_spdefense_stat.setText(_translate("DiniDex", "70"))
        self.label_speed_stat.setText(_translate("DiniDex", "70"))
        self.abilities_title.setText(_translate("DiniDex", "Abilities"))
        self.na_ability1.setText(_translate("DiniDex", "Overgrown"))
        self.nability_title.setText(_translate("DiniDex", "Normal Abilities"))
        self.na_ability2.setText(_translate("DiniDex", "Ability 2"))
        self.hability_title.setText(_translate("DiniDex", "Hidden Ability"))
        self.ha_ability1.setText(_translate("DiniDex", "Chlorophyll"))
        self.description_title.setText(_translate("DiniDex", "Description"))
        self.description_text.setText(_translate("DiniDex", "There is a plant seed on its back right from the day this Pok??mon is born. The seed slowly grows larger. "))
        self.name_pokemon.setText(_translate("DiniDex", "Bulbasaur"))
        self.dex_number.setText(_translate("DiniDex", "#001"))
        self.moves_title.setText(_translate("DiniDex", "Moves"))
        self.move1.setText(_translate("DiniDex", "Tackle"))
        self.level_title.setText(_translate("DiniDex", "Level"))
        self.level_move1.setText(_translate("DiniDex", "1"))
        self.search_bar.setText(_translate("DiniDex", "Digite o nome ou o n??mero correspondente ao POKEDEX do pokemon."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DiniDex = QtWidgets.QMainWindow()
    ui = Ui_DiniDex()
    ui.setupUi(DiniDex)
    DiniDex.show()
    sys.exit(app.exec())
