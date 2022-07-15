import sys, os, time
from PyQt5.QtWidgets import QApplication, QListWidget, QCheckBox, QMainWindow, QPushButton, QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(500, 500, 600, 600)
        self.setWindowTitle('Cleaning dyna result')
        self.fld_open_key = 0

        self.key_k = 1
        self.key_lsflog = 1
        self.key_binout = 1
        self.key_d3dump = 1
        self.key_d3thdt = 1
        self.key_dynain = 1
            # key_dynain_ini = 1
        self.key_mes0000 = 1
        # self.key_messag = 1
        self.key_runrsf = 1
        self.key_status = 1
        self.key_glstat = 1
        self.key_cfile = 1
        self.remainlist_filter = ['d3plot', 'd3plot01', 'd3plot05', 'd3plot10', 'd3plot15', 'd3plot20', 'd3plot25',
        'd3plot30', 'd3plot35', 'd3plot40', 'd3plot45', 'd3plot50', 'd3plot55', 'd3plot60',
        'd3plot65', 'd3plot70', 'd3plot75', 'd3plot80', 'd3plot85', 'd3plot90', 'd3plot95',
        'd3plot100', 'd3plot105', 'd3plot110', 'd3plot115', 'd3plot120', 'd3plot125', 'd3plot130',
        'd3plot135', 'd3plot140', 'd3plot145', 'd3plot150', 'd3plot155', 'd3plot160', 'd3plot165', 'd3plot170', 'd3plot175',
        'd3plot180', 'd3plot185', 'd3plot190', 'd3plot195', 'd3plot200', 'd3plot205', 'd3plot210', 'd3plot215', 'd3plot220',
        'd3plot225', 'd3plot230', 'd3plot235', 'd3plot240', 'd3plot245', 'd3plot250', 'd3plot255', 'd3plot260', 'd3plot265', 'd3plot270',
        'd3plot275', 'd3plot280', 'd3plot285', 'd3plot290', 'd3plot295', 'd3plot300', 'd3plot305', 'd3plot310', 'd3plot315', 'd3plot320',
        'd3plot325', 'd3plot330', 'd3plot335', 'd3plot340', 'd3plot345', 'd3plot350', 'd3plot355', 'd3plot360', 'd3plot365',
        'd3plot370', 'd3plot375', 'd3plot380', 'd3plot385', 'd3plot390', 'd3plot395', 'd3plot400', 'd3plot405', 'd3plot410',
        'd3plot415', 'd3plot420', 'd3plot425', 'd3plot430', 'd3plot435', 'd3plot440', 'd3plot445', 'd3plot450', 'd3plot455', 'd3plot460',
        'd3plot465', 'd3plot470', 'd3plot475', 'd3plot480', 'd3plot485', 'd3plot490', 'd3plot495', 'd3plot500', 'd3plot505', 'd3plot510',
        'd3plot515', 'd3plot520', 'd3plot525', 'd3plot530', 'd3plot535', 'd3plot540', 'd3plot545', 'd3plot550', 'd3plot555',
        'd3plot560', 'd3plot565', 'd3plot570', 'd3plot575', 'd3plot580', 'd3plot585', 'd3plot590', 'd3plot595', 'd3plot600',
        'd3plot605', 'd3plot610', 'd3plot615', 'd3plot620', 'd3plot625', 'd3plot630', 'd3plot635', 'd3plot640', 'd3plot645', 'd3plot650',
        'd3plot655', 'd3plot660', 'd3plot665', 'd3plot670', 'd3plot675', 'd3plot680', 'd3plot685', 'd3plot690', 'd3plot695', 'd3plot700']
        self.removelist = []
        self.remainlist_full = []
        self.check_path = ''

        self.listwidget = QListWidget(self)
        self.listwidget.resize(600, 500)
        self.listwidget.move(0, 100)

        self.fld_btn = QPushButton(self)
        self.fld_btn.move(20, 5)
        self.fld_btn.setText('Select folder')
        self.fld_btn.clicked.connect(self.fld_open)

        self.delete_btn = QPushButton(self)
        self.delete_btn.move(130, 5)
        self.delete_btn.setText('Cleaning')
        self.delete_btn.clicked.connect(self.removeFile)

        self.cb = QCheckBox('k file', self)
        self.cb.move(20, 40)
        self.cb.toggle()

        self.cb1 = QCheckBox('lsflog', self)
        self.cb1.move(100, 40)
        self.cb1.toggle()

        self.cb2 = QCheckBox('binout', self)
        self.cb2.move(180, 40)
        self.cb2.toggle()

        self.cb3 = QCheckBox('d3dump', self)
        self.cb3.move(260, 40)
        self.cb3.toggle()

        self.cb4 = QCheckBox('d3thdt', self)
        self.cb4.move(340, 40)
        self.cb4.toggle()

        self.cb5 = QCheckBox('dynain', self)
        self.cb5.move(420, 40)
        self.cb5.toggle()

        self.cb6 = QCheckBox('mes0000', self)
        self.cb6.move(500, 40)
        self.cb6.toggle()

        self.cb7 = QCheckBox('runrsf', self)
        self.cb7.move(20, 65)
        self.cb7.toggle()

        self.cb8 = QCheckBox('status', self)
        self.cb8.move(100, 65)
        self.cb8.toggle()

        self.cb9 = QCheckBox('glstat', self)
        self.cb9.move(180, 65)
        self.cb9.toggle()

        self.cb10 = QCheckBox('cfile', self)
        self.cb10.move(260, 65)
        self.cb10.toggle()

    def fld_open(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Directory")
        self.check_path = folder
        # self.file_gathering()
        # time.sleep(1)
        file_list = self.file_list()
        for ii, name in enumerate(file_list):
            self.listwidget.insertItem(ii, name)
        self.fld_open_key = 1

    def file_list(self):
        file_list = []
        if not self.check_path == '':
            for (path,dir,files) in os.walk(self.check_path):
                for elem in files :
                    file_list.append(elem)
        return file_list
                    
    def file_gathering(self):
        if not self.check_path == '':
            # self.check_path = 'E:\\d3plot_backup\\1. Drop\\GDOR3'

            d3plot_list = []

            for (path,dir,files) in os.walk(self.check_path):
                for elem in files :
                    if 'd3plot' in elem:
                        try:
                            d3plot_list.append(elem.split('.')[1])
                        except:
                            d3plot_list.append(elem.split('.')[0])

            pos = []
            for i in range(len(d3plot_list)):
                if d3plot_list[i] == 'd3plot':
                    pos.append(i)
            pos.append(len(d3plot_list))

            for pp in pos:
                if not pp == 0:
                    self.remainlist_filter.append(d3plot_list[pp - 1]) 

            for (path,dir,files) in os.walk(self.check_path):
                for elem in files :
                    # if 'd3plot' in elem:
                    #     try:
                    #         self.remainlist_full.append(elem.split('.')[1])
                    #     except:
                    #         self.remainlist_full.append(elem.split('.')[0])
                    if self.key_k == 1:
                        try:
                            if 'k' == elem.split('.')[1] or 'key' == elem.split('.')[1] or 'dyn' == elem.split('.')[1]:
                                self.remainlist_filter.append(elem)
                        except:
                            if 'k' == elem.split('.')[0] or 'key' == elem.split('.')[0] or 'dyn' == elem.split('.')[0]:
                                self.remainlist_filter.append(elem)
                    if self.key_lsflog == 1:
                        try:
                            if 'lsflog' in elem.split('.')[1]:
                                self.remainlist_filter.append(elem)
                        except:
                            if 'lsflog' in elem.split('.')[0]:
                                self.remainlist_filter.append(elem)
                    if self.key_binout == 1:
                        try:
                            if 'binout' in elem.split('.')[1]:
                                self.remainlist_filter.append(elem)
                        except:
                            if 'binout' in elem.split('.')[0]:
                                self.remainlist_filter.append(elem)
                    if self.key_d3dump == 1:
                        try:
                            if 'd3dump' in elem.split('.')[1]:
                                self.remainlist_filter.append(elem)
                        except:
                            if 'd3dump' in elem.split('.')[0]:
                                self.remainlist_filter.append(elem)
                    if self.key_d3thdt == 1:
                        try:
                            if 'd3thdt' in elem.split('.')[1]:
                                self.remainlist_filter.append(elem)
                        except:
                            if 'd3thdt' in elem.split('.')[0]:
                                self.remainlist_filter.append(elem)
                    if self.key_dynain == 1:
                        try:
                            if 'dynain' in elem.split('.')[1]:
                                self.remainlist_filter.append(elem)
                        except:
                            if 'dynain' in elem.split('.')[0]:
                                self.remainlist_filter.append(elem)
                    if self.key_mes0000 == 1:
                        try:
                            if 'mes0000' in elem.split('.')[1]:
                                self.remainlist_filter.append(elem)
                        except:
                            if 'mes0000' in elem.split('.')[0]:
                                self.remainlist_filter.append(elem)
                    if self.key_runrsf == 1:
                        try:
                            if 'runrsf' in elem.split('.')[1]:
                                self.remainlist_filter.append(elem)
                        except:
                            if 'runrsf' in elem.split('.')[0]:
                                self.remainlist_filter.append(elem)
                    if self.key_status == 1:
                        try:
                            if 'status' in elem.split('.')[1]:
                                self.remainlist_filter.append(elem)
                        except:
                            if 'status' in elem.split('.')[0]:
                                self.remainlist_filter.append(elem)
                    if self.key_glstat == 1:
                        try:
                            if 'glstat' in elem.split('.')[1]:
                                self.remainlist_filter.append(elem)
                        except:
                            if 'glstat' in elem.split('.')[0]:
                                self.remainlist_filter.append(elem)
                    if self.key_cfile == 1:
                        try:
                            if 'cfile' in elem.split('.')[1]:
                                self.remainlist_filter.append(elem)
                        except:
                            if 'cfile' in elem.split('.')[0]:
                                self.remainlist_filter.append(elem)

                    self.remainlist_full.append(elem)
        print('dd')

    def check_state(self):
        if self.cb.isChecked() == True:
            self.key_k = 1
        else:
            self.key_k = 0
        if self.cb1.isChecked() == True:
            self.key_lsflog = 1
        else:
            self.key_lsflog = 0
        if self.cb2.isChecked() == True:
            self.key_binout = 1
        else:
            self.key_binout = 0
        if self.cb3.isChecked() == True:
            self.key_d3dump = 1
        else:
            self.key_d3dump = 0
        if self.cb4.isChecked() == True:
            self.key_d3thdt = 1
        else:
            self.key_d3thdt = 0
        if self.cb5.isChecked() == True:
            self.key_dynain = 1
        else:
            self.key_dynain = 0
        if self.cb6.isChecked() == True:
            self.key_mes0000 = 1
        else:
            self.key_mes0000 = 0
        if self.cb7.isChecked() == True:
            self.key_runrsf = 1
        else:
            self.key_runrsf = 0
        if self.cb8.isChecked() == True:
            self.key_status = 1
        else:
            self.key_status = 0
        if self.cb9.isChecked() == True:
            self.key_glstat = 1
        else:
            self.key_glstat = 0
        if self.cb10.isChecked() == True:
            self.key_cfile = 1
        else:
            self.key_cfile = 0

    def removeFile(self):
        if self.fld_open_key == 1:
            self.check_state()
            self.file_gathering()
            self.removelist = list(set(self.remainlist_full) - set(self.remainlist_filter))

            lend = len(self.removelist)
            for (path,dir,files) in os.walk(self.check_path):
                for elem in files :
                    for oo in self.removelist:
                        if elem == oo:
                            print('remove  ' + elem)
                    # try:
                    #     elems = elem.split('.')[1]
                    #     for oo in self.removelist:
                    #         if elems in oo:
                    #             print('remove  ' + elem)
                    # except:
                    #     elems = elem.split('.')[0]
                    #     if elems in self.removelist:
                    #         print('remove  ' + elem)
            time.sleep(3)
            file_list = self.file_list()
            for ii, name in enumerate(file_list):
                self.listwidget.insertItem(ii, name)
        else:
            return

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.setFixedSize(600, 600)
    main.show()
    sys.exit(app.exec_())