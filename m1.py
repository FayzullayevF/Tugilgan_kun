import os
os.system("clear")
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox, QVBoxLayout, QHBoxLayout, QComboBox, QCheckBox


class TugilganKun(QWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("font-size:20px")
        
        self.v_main_lay = QVBoxLayout()
        self.h_main_lay = QHBoxLayout()
        
        # self.ok_btn = QPushButton("OK")
        # self.h_main_lay.addWidget(self.ok_btn)
        # self.ok_btn.clicked.connect(self.OK)
        # self.setLayout(self.h_main_lay)
        self.lbl = QLabel("Tug'ilgan yilingizni tanlang")
        
        self.cmb = QComboBox()
        self.cmb1 = QComboBox()
        self.cmb2 = QComboBox()
        self.cmb3 = QComboBox()
        self.cmb4 = QComboBox()
        self.cmb5 = QComboBox()
        
        
        
        self.lst = ["1950", "1951", "1952", "1953", "1954", "1955", "1956", "1957", "1958", "1959", "1960", "1961", "1962", "1963", "1964", "1965", "1966", "1967", "1968", "1969","1970", "1971", "1972", "1973", "1974", "1975", "1976", "1977", "1978",
               "1979", "1980", "1981", "1982", "1983", "1984", "1985", "1986", "1987", "1988", "1989", "1990", "1991", "1992", "1993", "1994", "1995", "1996", "1997", "1998", "1999", "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", 
               "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024"]

        self.cmb.addItems(self.lst)
        self.cmb.activated[str].connect(self.Yil)
        
        self.v_main_lay.addWidget(self.lbl)
        self.v_main_lay.addWidget(self.cmb)
        self.setLayout(self.v_main_lay)
        
        self.lbl3 = QLabel("Millatingizni tanlang")
        self.lst3 = ["O'zbek", "Tojik", "Rus","Tatar","Qirg'iz","Qozoq","Turkman","Turk","Ispan","Nemis","Anglis","Arab","Xitoy","Hind"]
        self.cmb3.addItems(self.lst3)
        self.cmb3.activated[str].connect(self.Millat)
                
        self.v_main_lay.addWidget(self.lbl3)
        self.v_main_lay.addWidget(self.cmb3)
        self.setLayout(self.v_main_lay)
        
        self.lbl4 = QLabel("Jinsingizni tanlang")
        self.lst4 = ["Erkak", "Ayol", "Yaxshimas lekin 😄 "]
        self.cmb4.addItems(self.lst4)
        self.cmb4.activated[str].connect(self.Jins)
                
        self.v_main_lay.addWidget(self.lbl4)
        self.v_main_lay.addWidget(self.cmb4)
        self.setLayout(self.v_main_lay)
        
        
        
        self.lst1 = ["Toshkent viloyati", "Samarqand viloyati", "Andijon viloyati", "Farg'ona viloyati", "Namangan viloyati", "Toshkent shahri", "Sirdaryo viloyati",
                "Jizzax viloyati", "Qashqadaryo viloyati", "Surxandaryo viloyati", "Xorazm viloyati", "Buxoro viloyati", "Navoiy viloyati"]
        
        self.lbl1 = QLabel("Tug'ilgan viloyatingizni tanlang")
        self.v_main_lay.addWidget(self.lbl1)
        self.setLayout(self.v_main_lay)
        self.cmb1.addItems(self.lst1)
        self.cmb1.activated[str].connect(self.Viloyat)
        self.v_main_lay.addWidget(self.cmb1)
        self.setLayout(self.v_main_lay)
        
        self.lbl2 = QLabel("Tug'ilgan tumaningizni tanlang")
        self.v_main_lay.addWidget(self.lbl2)
        self.setLayout(self.v_main_lay)
        
    def Yil(self,obj):
       with open("USER.txt", 'a') as f:
           f.write(f"Tug'ilgan yilingiz: {obj}\n")
    
    def Tuman(self,obj):
        with open("USER.txt", 'a') as f:
           f.write(f"Tug'ilgan tumaningiz: {obj}\n")
           
    def Millat(self,obj):
        with open("USER.txt", 'a') as f:
           f.write(f"Millatingiz: {obj}\n")
    
    def Jins(self,obj):
        with open("USER.txt", 'a') as f:
           f.write(f"Jinsingiz: {obj}\n")
           
    def Viloyat(self,obj):
        if obj == "Toshkent shahri":
            with open("USER.txt", 'a') as f:
               f.write(f"Tug'ilgan viloyatingiz: {obj}\n")
            self.lst2 = ["Chilonzor tumani", "Olmazor tumani", "Shayhontohur tumani", "Mirzo Ulug'bek tumani", "Bektemir tumani", "Mirobod tumani", "Sergeli tumani",
                "Uchtepa tumani", "Yakkasaroy tumani", "Yunusobot tumani", "Yangihayot tumani", "Yashnobod tumani"]
            self.cmb2.addItems(self.lst2)
            self.cmb2.activated[str].connect(self.Tuman)
            self.v_main_lay.addWidget(self.cmb2)
            self.setLayout(self.v_main_lay)
        elif obj == "Toshkent viloyati":
            with open("USER.txt", 'a') as f:
               f.write(f"Tug'ilgan viloyatingiz: {obj}\n")
            self.lst2 = ["Bekobod tumani", "Bo'ka tumani", "Bo'stonliq tumani", "Chinoz tumani", "Ohangaron tumani", "Oqqo'rg'on tumani", "O'rta Chirchiq tumani",
                "Parkent tumani", "Piskent tumani", "Qibray tumani", "Quyi Chirchiq tumani", "Yangiyo'l tumani", "Yuqori Chirchiq tumani"]
            self.cmb2.addItems(self.lst2)
            self.cmb2.activated[str].connect(self.Tuman)
            self.v_main_lay.addWidget(self.cmb2)
            self.setLayout(self.v_main_lay)
        elif obj == "Samarqand viloyati":
            with open("USER.txt", 'a') as f:
               f.write(f"Tug'ilgan viloyatingiz: {obj}\n")
            self.lst2 = ["Bulung'ur tumani", "Ishtixon tumani", "Jomboy tumani", "Kattaqo'rg'on tumani", "Narpay tumani", "Oqdaryo tumani", "Past Darg'om tumani",
                "Paxtachi tumani", "Payariq tumani", "Qo'shrabot tumani", "Toyloq tumani", "Samarqand tumani", "Urgut tumani"]
            self.cmb2.addItems(self.lst2)
            self.cmb2.activated[str].connect(self.Tuman)
            self.v_main_lay.addWidget(self.cmb2)
            self.setLayout(self.v_main_lay)
        elif obj == "Andijon viloyati":
            with open("USER.txt", 'a') as f:
               f.write(f"Tug'ilgan viloyatingiz: {obj}\n")
            self.lst2 = ["Andijon tumani", "Asaka tumani", "Baliqchi tumani", "Bo'ston tumani", "Buloqboshi tumani", "Izboskan tumani", "Jalaquduq tumani",
                "Marhamat tumani", "Oltinko'l tumani", "Paxtaobod tumani", "Qo'rg'ontepa tumani", "Shahrixon tumani", "Ulug'nor tumani","Xo'jaobod tumani"]
            self.cmb2.addItems(self.lst2)
            self.cmb2.activated[str].connect(self.Tuman)
            self.v_main_lay.addWidget(self.cmb2)
            self.setLayout(self.v_main_lay)
        elif obj == "Farg'ona viloyati":
            with open("USER.txt", 'a') as f:
               f.write(f"Tug'ilgan viloyatingiz: {obj}\n")
            self.lst2 = ["Bag'dod tumani", "Beshariq tumani", "Buvayda tumani", "Dang'ara tumani", "Farg'ona tumani", "Furqat tumani", "Oltiariq tumani",
                "O'zbekiston tumani", "Qo'shtepa tumani", "Quva tumani", "Rishton tumani", "So'x tumani", "Toshloq tumani","Uchko'prik tumani","Yozyovon tumani"]
            self.cmb2.addItems(self.lst2)
            self.cmb2.activated[str].connect(self.Tuman)
            self.v_main_lay.addWidget(self.cmb2)
            self.setLayout(self.v_main_lay)
        elif obj == "Namangan viloyati":
            with open("USER.txt", 'a') as f:
               f.write(f"Tug'ilgan viloyatingiz: {obj}\n")
            self.lst2 = ["Pop tumani", "Chortoq tumani", "Chust tumani", "Kosonsoy tumani", "Mingbuloq tumani", "Namangan tumani", "Norin tumani",
                "To'raqo'rg'on tumani", "Uchqo'rg'on tumani", "Uychi tumani", "Yangiqo'rg'on tumani"]
            self.cmb2.addItems(self.lst2)
            self.cmb2.activated[str].connect(self.Tuman)
            self.v_main_lay.addWidget(self.cmb2)
            self.setLayout(self.v_main_lay)
        elif obj == "Namangan viloyati":
            with open("USER.txt", 'a') as f:
               f.write(f"Tug'ilgan viloyatingiz: {obj}\n")
            self.lst2 = ["Pop tumani", "Chortoq tumani", "Chust tumani", "Kosonsoy tumani", "Mingbuloq tumani", "Namangan tumani", "Norin tumani",
                "To'raqo'rg'on tumani", "Uchqo'rg'on tumani", "Uychi tumani", "Yangiqo'rg'on tumani"]
            self.cmb2.addItems(self.lst2)
            self.cmb2.activated[str].connect(self.Tuman)
            self.v_main_lay.addWidget(self.cmb2)
            self.setLayout(self.v_main_lay)
        elif obj == "Sirdaryo viloyati":
            with open("USER.txt", 'a') as f:
               f.write(f"Tug'ilgan viloyatingiz: {obj}\n")
            self.lst2 = ["Boyovut tumani", "Guliston tumani", "Mirzaobod tumani", "Oqoltin tumani", "Sayxunobod tumani", "Sardoba tumani", "Sirdaryo tumani",
                "Xovos tumani"]
            self.cmb2.addItems(self.lst2)
            self.cmb2.activated[str].connect(self.Tuman)
            self.v_main_lay.addWidget(self.cmb2)
            self.setLayout(self.v_main_lay)
        elif obj == "Jizzax viloyati":
            with open("USER.txt", 'a') as f:
               f.write(f"Tug'ilgan viloyatingiz: {obj}\n")
            self.lst2 = ["Arnasoy tumani", "Baxmal tumani", "Do'stlik tumani", "Forish tumani", "G'allaorol tumani", "Mirzacho'l tumani", "Paxtakor tumani",
                "Sharof Rashidov tumani", "Yangiobod tumani", "Zafarobod tumani", "Zarbdor tumani", "Zomin tumani"]
            self.cmb2.addItems(self.lst2)
            self.cmb2.activated[str].connect(self.Tuman)
            self.v_main_lay.addWidget(self.cmb2)
            self.setLayout(self.v_main_lay)
        elif obj == "Qashqadaryo viloyati":
            with open("USER.txt", 'a') as f:
               f.write(f"Tug'ilgan viloyatingiz: {obj}\n")
            self.lst2 = ["Chiroqchi tumani", "Dehqonobod tumani", "G'uzor tumani", "Kasbi tumani", "Kitob tumani", "Koson tumani", "Mirishkor tumani",
                "Muborak tumani", "Nishon tumani", "Qamashi tumani", "Qarshi tumani", "Shahrisabz tumani","Yakkabog' tumani"]
            self.cmb2.addItems(self.lst2)
            self.cmb2.activated[str].connect(self.Tuman)
            self.v_main_lay.addWidget(self.cmb2)
            self.setLayout(self.v_main_lay)
        elif obj == "Surxandaryo viloyati":
            with open("USER.txt", 'a') as f:
               f.write(f"Tug'ilgan viloyatingiz: {obj}\n")
            self.lst2 = ["Angor tumani", "Bandixon tumani", "Boysun tumani", "Denov tumani", "Jarqo'rg'on tumani", "Muzrabot tumani", "Oltinsoy tumani",
                "Qiziriq tumani", "Qumqo'rg'on tumani", "Sariosiyo tumani", "Sherobod tumani", "Sho'rchi tumani","Termiz tumani","Uzun tumani"]
            self.cmb2.addItems(self.lst2)
            self.cmb2.activated[str].connect(self.Tuman)
            self.v_main_lay.addWidget(self.cmb2)
            self.setLayout(self.v_main_lay)
        elif obj == "Xorazm viloyati":
            with open("USER.txt", 'a') as f:
               f.write(f"Tug'ilgan viloyatingiz: {obj}\n")
            self.lst2 = ["Bog'ot tumani", "Gurlan tumani", "Hazorasp tumani", "Qo'shko'pir tumani", "Shovot tumani", "Urganch tumani", "Xiva tumani",
                "Xonqa tumani", "Yangiariq tumani", "Yangibozor tumani"]
            self.cmb2.addItems(self.lst2)
            self.cmb2.activated[str].connect(self.Tuman)
            self.v_main_lay.addWidget(self.cmb2)
            self.setLayout(self.v_main_lay)
        elif obj == "Buxoro viloyati":
            with open("USER.txt", 'a') as f:
               f.write(f"Tug'ilgan viloyatingiz: {obj}\n")
            self.lst2 = ["Buxoro tumani", "G'ijdivon tumani", "Jondor tumani", "Kogon tumani", "Olot tumani", "Peshku tumani", "Qorako'l tumani",
                "Qorovulbozor tumani", "Romitan tumani", "Shofirkon tumani","Vobkent tumani"]
            self.cmb2.addItems(self.lst2)
            self.cmb2.activated[str].connect(self.Tuman)
            self.v_main_lay.addWidget(self.cmb2)
            self.setLayout(self.v_main_lay)
        elif obj == "Navoiy viloyati":
            with open("USER.txt", 'a') as f:
               f.write(f"Tug'ilgan viloyatingiz: {obj}\n")
            self.lst2 = ["Karmana tumani", "Konimex tumani", "Navbahor tumani", "Kogon tumani", "Nurota tumani", "Qiziltepa tumani", "Tomdi tumani",
                "Uchquduq tumani", "Xatirchi tumani", "Shofirkon tumani","Vobkent tumani"]
            self.cmb2.addItems(self.lst2)
            self.cmb2.activated[str].connect(self.Tuman)
            self.v_main_lay.addWidget(self.cmb2)
            self.setLayout(self.v_main_lay)


app = QApplication([])
win = TugilganKun()
win.show()
app.exec_()