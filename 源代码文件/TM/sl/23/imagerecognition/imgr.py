# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imgr.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QFileDialog

import json
import base64
import urllib
import urllib.request

""" 你的 APPID AK SK """
# http://ai.baidu.com/docs#/OCR-Pricing/top 申请地址

# API_KEY 为官网获取的AK， SECRET_KEY 为官网获取的SK


API_KEY = '官网获取的AK'
SECRET_KEY = '官网获取的SK'

#qt自动生成的UI类
class Ui_Form(object):
    def setupUi(self, Form):
        #设置窗体名称
        Form.setObjectName("Form")
        # 设置窗体大小
        Form.resize(724, 489)
        # 创建显示要识别图片控件
        self.image = QtWidgets.QLabel(Form)
        # 设置控件大小
        self.image.setGeometry(QtCore.QRect(96, 140, 311, 301))
        # 设置黑色边框
        self.image.setStyleSheet("border-width: 1px;border-style: solid;border-color: rgb(0, 0, 0);")
        # 设置图片显示控件名称
        self.image.setObjectName("image")
        # 创建窗体
        self.widget = QtWidgets.QWidget(Form)
        # 窗体大小
        self.widget.setGeometry(QtCore.QRect(110, 50, 221, 31))
        # 设置名称
        self.widget.setObjectName("widget")
        # 创建布局容器控件
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        # 设置容器中内容边距
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        # 设置名称
        self.horizontalLayout.setObjectName("horizontalLayout")
        # 创建文字显示控件
        self.label = QtWidgets.QLabel(self.widget)
        # 设置名称
        self.label.setObjectName("label")
        # 把文字显示控件添加到布局容器中
        self.horizontalLayout.addWidget(self.label)
        # 在窗体里创建选择内容控件
        self.comboBox = QtWidgets.QComboBox(self.widget)
        # 设置名称
        self.comboBox.setObjectName("comboBox")
        # 添加子标题有多少分类添加几个
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        # 把下拉选择控件添加到布局容器中
        self.horizontalLayout.addWidget(self.comboBox)
        # 创建窗体
        self.widget1 = QtWidgets.QWidget(Form)
        # 创建窗体大小
        self.widget1.setGeometry(QtCore.QRect(96, 90, 318, 31))
        # 创建名称
        self.widget1.setObjectName("widget1")
        # 新建横向布局
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        # 新建按钮
        self.pushButton = QtWidgets.QPushButton(self.widget1)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.widget2 = QtWidgets.QWidget(Form)
        self.widget2.setGeometry(QtCore.QRect(450, 50, 201, 401))
        self.widget2.setObjectName("widget2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.widget2)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        # 设置内容自动换行
        self.label_3.setWordWrap(True)
        # 设置黑色边框
        self.label_3.setStyleSheet("border-width: 1px;border-style: solid;border-color: rgb(0, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        # 自动生成的ui控件 处理方法
        self.retranslateUi(Form)
        # 自动生成的  关联信号槽
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        # 设置窗体内容
        Form.setWindowTitle(_translate("Form", "图像识别工具"))
        # 设置文字控件显示内容
        self.label.setText(_translate("Form", "选择识别类型："))
        # 设置下拉控件选项内容
        self.comboBox.setItemText(0, _translate("Form", "银行卡"))
        self.comboBox.setItemText(1, _translate("Form", "植物"))
        self.comboBox.setItemText(2, _translate("Form", "动物"))
        self.comboBox.setItemText(3, _translate("Form", "通用票据"))
        self.comboBox.setItemText(4, _translate("Form", "营业执照"))
        self.comboBox.setItemText(5, _translate("Form", "身份证"))
        self.comboBox.setItemText(6, _translate("Form", "车牌号"))
        self.comboBox.setItemText(7, _translate("Form", "驾驶证"))
        self.comboBox.setItemText(8, _translate("Form", "行驶证"))
        self.comboBox.setItemText(9, _translate("Form", "车型"))
        self.comboBox.setItemText(10, _translate("Form", "Logo"))
        # 设置控件显示文字
        self.label_2.setText(_translate("Form", "选择要识别的图片："))
        # 设置按钮显示的文字
        self.pushButton.setText(_translate("Form", "选择..."))
        # 设置文本控件显示内容
        self.label_3.setText(_translate("Form", "显示识别结果"))
        # 设置按钮内容
        self.pushButton_2.setText(_translate("Form", "复制到剪切版"))
        # 为按钮设置方法
        self.pushButton.clicked.connect(self.openfile)
        # 为按钮设置点击方法
        self.pushButton_2.clicked.connect(self.copyText)
    # 复制文字到剪贴板方法
    def copyText(self):
        # 复制文字到剪贴板
        clipboard = QApplication.clipboard()
        # 设置复制的内容
        clipboard.setText(self.label_3.text())
    # 打开文件选择对话框方法
    def openfile(self):
        # 启动选择文件对话空，查找jpg以及png图片
        self.download_path = QFileDialog.getOpenFileName(self.widget1, "选择要识别的图片", "/", "Image Files(*.jpg *.png)")
        # 判断是否选择图片
        if not self.download_path[0].strip():
            # 没有选择图片
            pass
        else:
            # 选择图片执行以下内容
            # 设置图片路径
            self.lineEdit.setText(self.download_path[0])
            # 理由pixmap解析图片
            pixmap = QPixmap(self.download_path[0])
            # 等比例缩放图片
            scaredPixmap = pixmap.scaled(QSize(311, 301), aspectRatioMode=Qt.KeepAspectRatio)
            # 设置图片
            self.image.setPixmap(scaredPixmap)
            # 判断选择的类型 根据类型做相应的图片处理
            self.image.show()
            # 判断选择的类型
            self.typeTp()
            pass

    # 判断选择的类型 进行相应处理
    def typeTp(self):
        # 银行卡识别
        if self.comboBox.currentIndex() == 0:
            self.get_bankcard(self.get_token())
            pass
        # 植物识别
        elif self.comboBox.currentIndex() == 1:
            self.get_plant(self.get_token())
            pass
        # 动物识别
        elif self.comboBox.currentIndex() == 2:
            self.get_animal(self.get_token())
            pass
        #通用票据识别识别
        elif self.comboBox.currentIndex() == 3:
            self.get_vat_invoice(self.get_token())
            pass
        # 营业执照识别
        elif self.comboBox.currentIndex() == 4:
            self.get_business_licensev(self.get_token())
            pass
        # 身份证识别
        elif self.comboBox.currentIndex() == 5:
            self.get_idcard(self.get_token())
            pass
        # 车牌号识别
        elif self.comboBox.currentIndex() == 6:
            self.get_license_plate(self.get_token())
            pass
        # 驾驶证识别
        elif self.comboBox.currentIndex() == 7:
            self.get_driving_license(self.get_token())
            pass
        # 行驶证识别
        elif self.comboBox.currentIndex() == 8:
            self.get_vehicle_license(self.get_token())
            pass
        # 车型识别
        elif self.comboBox.currentIndex() == 9:
            self.get_car(self.get_token())
            pass
        # Logo识别
        elif self.comboBox.currentIndex() == 10:
            self.get_logo(self.get_token())
            pass
        pass

    # 百度提供方法 获取token
    def get_token(self):
        # client_id 为官网获取的AK， client_secret 为官网获取的SK
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + API_KEY + '&client_secret=' + SECRET_KEY
        # 发送请求
        request = urllib.request.Request(host)
        # 添加请求头
        request.add_header('Content-Type', 'application/json; charset=UTF-8')
        # 获取返回内容
        response = urllib.request.urlopen(request)
        # 读取返回内容
        content = response.read()
        # 判断内容是否为空
        if (content):
            # 打印内容
            print(content)
            # 打印token
            print(json.loads(content)['access_token'])
            # 使用json解析出token 设置token
            self.access_token = json.loads(content)['access_token']
            # 返回token
            return self.access_token
    # 0 银行卡识别
    def get_bankcard(self, access_token):
        request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/bankcard"
        # 二进制方式打开图片文件
        f = self.get_file_content(self.download_path[0])
        img = base64.b64encode(f)
        params = {"image": img}
        params = urllib.parse.urlencode(params).encode('utf-8')
        request_url = request_url + "?access_token=" + access_token
        request = urllib.request.Request(url=request_url, data=params)
        request.add_header('Content-Type', 'application/x-www-form-urlencoded')
        response = urllib.request.urlopen(request)
        content = response.read()
        if content:
            # 解析返回数据
            bankcards = json.loads(content)
            # 输出返回结果
            strover = '识别结果：\n'
            # 捕捉异常判断是否正确返回信息
            try:
                # 判断银行卡类型
                if bankcards['result']['bank_card_type']==0:
                    bank_card_type='不能识别'
                elif bankcards['result']['bank_card_type']==1:
                    bank_card_type = '借记卡'
                elif bankcards['result']['bank_card_type'] == 2:
                    bank_card_type = '信用卡'
                strover += '  卡号：{} \n  银行：{} \n  类型：{} \n'.format(bankcards['result']['bank_card_number'], bankcards['result']['bank_name'],bank_card_type)
            # 错误的时候提示错误原因
            except BaseException:
                error_msg = bankcards['error_msg']
                strover += '  错误：\n {} \n '.format(error_msg)
            # 设置识别显示结果
            self.label_3.setText(strover)
    # 1植物识别
    def get_plant(self, access_token):
        request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/plant"
        # 二进制方式打开图片文件
        f = self.get_file_content(self.download_path[0])
        # 转换图片
        img = base64.b64encode(f)
        # 拼接图片参数
        params = {"image": img}
        params = urllib.parse.urlencode(params).encode('utf-8')
        # 请求地址
        request_url = request_url + "?access_token=" + access_token
        # 发送请求传递图片参数
        request = urllib.request.Request(url=request_url, data=params)
        # 添加访问头部
        request.add_header('Content-Type', 'application/x-www-form-urlencoded')
        # 接收返回内容
        response = urllib.request.urlopen(request)
        # 读取返回内容
        content = response.read()
        # 内容判断
        if content:
            plants = json.loads(content)
            strover = '识别结果：\n'
            try:
                i = 1
                for plant in plants['result']:
                    strover += '{} 植物名称：{} \n'.format(i, plant['name'])
                    i += 1
            except BaseException:
                error_msg = plants['error_msg']
                strover += '  错误：\n {} \n '.format(error_msg)
            self.label_3.setText(strover)
    # 2动物识别
    def get_animal(self, access_token):
        request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/animal"
        # 二进制方式打开图片文件
        f = self.get_file_content(self.download_path[0])
        img = base64.b64encode(f) # 转换图片
        # 拼接图片参数
        params = {"image": img, "top_num": 6}
        params = urllib.parse.urlencode(params).encode('utf-8')
        # 请求地址
        request_url = request_url + "?access_token=" + access_token
        # 发送请求传递图片参数
        request = urllib.request.Request(url=request_url, data=params)
        # 添加访问头部
        request.add_header('Content-Type', 'application/x-www-form-urlencoded')
        response = urllib.request.urlopen(request)# 接收返回内容
        content = response.read()# 读取返回内容
        if content: # 内容判断
            animals = json.loads(content)
            strover = '识别结果：\n'
            try:
                i = 1
                for animal in animals['result']:
                   strover += '{} 动物名称：{} \n'.format(i, animal['name'])
                   i += 1
            except BaseException:
                error_msg = animals['error_msg']
                strover += '  错误：\n {} \n '.format(error_msg)
            self.label_3.setText(strover)
    # 3 通用票据识别
    def get_vat_invoice(self, access_token):
        request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/receipt"
        # 二进制方式打开图片文件
        f = self.get_file_content(self.download_path[0])
        img = base64.b64encode(f)
        params = {"image": img}
        params = urllib.parse.urlencode(params).encode('utf-8')
        request_url = request_url + "?access_token=" + access_token
        request = urllib.request.Request(url=request_url, data=params)
        request.add_header('Content-Type', 'application/x-www-form-urlencoded')
        response = urllib.request.urlopen(request)
        content = response.read()
        if content:
            receipts = json.loads(content)
            strover = '识别结果：\n'
            try:
                words_result=receipts['words_result']
                for word_result in words_result:
                    #票据内容
                    InvoiceType =word_result['words']
                    strover += ' {} '.format(InvoiceType)
            except BaseException:
                error_msg = receipts['error_msg']
                strover += '  错误：\n {} \n '.format(error_msg)
            self.label_3.setText(strover)
    # 4 营业执照识别
    def get_business_licensev(self,access_token):
        request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/business_license"
        # 二进制方式打开图片文件
        f = self.get_file_content(self.download_path[0])
        img = base64.b64encode(f)
        params = {"image": img}
        params = urllib.parse.urlencode(params).encode('utf-8')
        request_url = request_url + "?access_token=" + access_token
        request = urllib.request.Request(url=request_url, data=params)
        request.add_header('Content-Type', 'application/x-www-form-urlencoded')
        response = urllib.request.urlopen(request)
        content = response.read()
        if content:
            business_licenses = json.loads(content)
            strover = '识别结果：\n'
            try:
                words_result=business_licenses['words_result']
                # 单位名称
                Unit_name = words_result['单位名称']['words']
                strover += '  单位名称：\n  {} \n '.format(Unit_name)
                # 法人
                legal_person = words_result['法人']['words']
                strover += '  法人：{} \n '.format(legal_person)
                # 有效期
                Term_of_validity = words_result['有效期']['words']
                strover += '  有效期：{} \n '.format(Term_of_validity)
                # 证件编号
                ID_number = words_result['证件编号']['words']
                strover += '  证件编号：{} \n '.format(ID_number)
                # 社会信用代码
                Social_Credit_Code = words_result['社会信用代码']['words']
                strover += '  社会信用代码：{} \n '.format(Social_Credit_Code)
                # 地址
                address = words_result['地址']['words']
                strover += '  地址：\n{}\n '.format(address)
            except BaseException:
                error_msg = business_licenses['error_msg']
                strover += '  错误：\n  {} \n '.format(error_msg)
            self.label_3.setText(strover)

    #5 身份证识别
    def get_idcard(self, access_token):
        request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/idcard"
        # 二进制方式打开图片文件
        f = self.get_file_content(self.download_path[0])
        img = base64.b64encode(f)
        params = {"image": img, "id_card_side": "front"}
        params = urllib.parse.urlencode(params).encode('utf-8')
        request_url = request_url + "?access_token=" + access_token
        request = urllib.request.Request(url=request_url, data=params)
        request.add_header('Content-Type', 'application/x-www-form-urlencoded')
        response = urllib.request.urlopen(request)
        content = response.read()
        if content:
            idcards = json.loads(content)
            strover = '识别结果：\n'
            try:
                words_result = idcards['words_result']
                # 公民身份号码
                Citizenship_number = words_result['公民身份号码']['words']
                strover += '  公民身份号码：\n{} \n '.format(Citizenship_number)
                # 民族
                Nation = words_result['民族']['words']
                strover += '  民族：{} \n '.format(Nation)
                # 姓名
                Full_name = words_result['姓名']['words']
                strover += '  姓名：{} \n '.format(Full_name)
                # 住址
                address = words_result['住址']['words']
                strover += '  住址：\n{} \n '.format(address)
            except BaseException:
                error_msg = idcards['error_msg']
                strover += '  错误：\n  {} \n '.format(error_msg)
            # 显示识别结果
            self.label_3.setText(strover)
    #6 车牌号识别
    def get_license_plate(self, access_token):
        request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/license_plate"
        # 二进制方式打开图片文件
        f = self.get_file_content(self.download_path[0])
        img = base64.b64encode(f)
        params = {"image": img}
        params = urllib.parse.urlencode(params).encode('utf-8')
        request_url = request_url + "?access_token=" + access_token
        request = urllib.request.Request(url=request_url, data=params)
        request.add_header('Content-Type', 'application/x-www-form-urlencoded')
        response = urllib.request.urlopen(request)
        content = response.read()
        if content:
            license_plates = json.loads(content)
            strover = '识别结果：\n'
            try:
                words_result = license_plates['words_result']
                # 车牌号
                number = words_result['number']
                strover += '  车牌号：{} \n '.format(number)
            except BaseException:
                error_msg = license_plates['error_msg']
                strover += '  错误：\n  {} \n '.format(error_msg)
            self.label_3.setText(strover)
    #7 驾驶证识别
    def get_driving_license(self, access_token):
        request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/driving_license"
        # 二进制方式打开图片文件
        f = self.get_file_content(self.download_path[0])
        img = base64.b64encode(f)
        params = {"image": img}
        params = urllib.parse.urlencode(params).encode('utf-8')
        request_url = request_url + "?access_token=" + access_token
        request = urllib.request.Request(url=request_url, data=params)
        request.add_header('Content-Type', 'application/x-www-form-urlencoded')
        response = urllib.request.urlopen(request)
        content = response.read()
        if content:
            driving_licenses = json.loads(content)
            strover = '识别结果：\n'
            try:
                words_result = driving_licenses['words_result']
                # 证号
                Citizenship_number = words_result['证号']['words']
                strover += '  证号： {} \n '.format(Citizenship_number)
                # 准驾车型
                Full_name = words_result['准驾车型']['words']
                strover += ' 准驾车型：{} \n '.format(Full_name)
                # 姓名
                name = words_result['姓名']['words']
                strover += ' 姓名： {} \n '.format(name)
                # 国籍
                nationality = words_result['国籍']['words']
                strover += ' 国籍： {} \n '.format(nationality)
                # 出生日期
                date_of_birth = words_result['出生日期']['words']
                strover += ' 出生日期： {} \n '.format(date_of_birth)
                # 性别
                sex = words_result['性别']['words']
                strover += ' 性别： {} \n '.format(sex)
                # 初次领证日期
                first_certificate_date = words_result['初次领证日期']['words']
                strover += ' 初次领证日期： {} \n '.format(first_certificate_date)
                # 有效期限
                Nation = words_result['有效期限']['words']
                # 到期日期
                to = words_result['至']['words']
                strover += ' 有效期限：{}至{}\n '.format(Nation,to)
                # 住址
                address = words_result['住址']['words']
                strover += ' 住址：\n{} \n '.format(address)
            except BaseException:
                error_msg = driving_licenses['error_msg']
                strover += '  错误：\n  {} \n '.format(error_msg)
            self.label_3.setText(strover)

    #8 行驶证识别
    def get_vehicle_license(self, access_token):
        request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/vehicle_license"
        # 二进制方式打开图片文件
        f = self.get_file_content(self.download_path[0])
        img = base64.b64encode(f)
        params = {"image": img}
        params = urllib.parse.urlencode(params).encode('utf-8')
        request_url = request_url + "?access_token=" + access_token
        request = urllib.request.Request(url=request_url, data=params)
        request.add_header('Content-Type', 'application/x-www-form-urlencoded')
        response = urllib.request.urlopen(request)
        content = response.read()
        if content:
            vehicle_licenses = json.loads(content)
            strover = '识别结果：\n'
            try:
                words_result = vehicle_licenses['words_result']
                # 品牌型号
                brand_model = words_result['品牌型号']['words']
                strover += '  品牌型号： {} \n '.format(brand_model)
                # 发证日期
                date_of_certification = words_result['发证日期']['words']
                strover += ' 发证日期：{} \n '.format(date_of_certification)
                # 使用性质
                use_nature = words_result['使用性质']['words']
                strover += ' 使用性质： {} \n '.format(use_nature)
                # 发动机号码
                engine_number = words_result['发动机号码']['words']
                strover += ' 发动机号码： {} \n '.format(engine_number)
                # 注册日期
                date_of_registration = words_result['注册日期']['words']
                strover += ' 注册日期： {} \n '.format(date_of_registration)
                # 号牌号码
                number_number = words_result['号牌号码']['words']
                strover += ' 号牌号码： {} \n '.format(number_number)
                # 车辆识别代号
                vehicle_identification = words_result['车辆识别代号']['words']
                strover += ' 车辆识别代号： {} \n '.format(vehicle_identification)
                # 车辆类型
                vehicle_type = words_result['车辆类型']['words']
                strover += ' 车辆类型： {} \n '.format(vehicle_type)
                # 所有人
                owner = words_result['所有人']['words']
                strover += ' 所有人：\n{} \n '.format(owner)
                # 住址
                address = words_result['住址']['words']
                strover += ' 住址：\n{} \n '.format(address)
            except BaseException:
                error_msg = vehicle_licenses['error_msg']
                strover += '  错误：\n  {} \n '.format(error_msg)
            self.label_3.setText(strover)

    # 9获取车型信息
    def get_car(self, access_token):
        request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/car"
        # 二进制方式打开图片文件
        f = self.get_file_content(self.download_path[0])
        img = base64.b64encode(f)
        params = {"image": img, "top_num": 5}
        params = urllib.parse.urlencode(params).encode('utf-8')
        request_url = request_url + "?access_token=" + access_token
        request = urllib.request.Request(url=request_url, data=params)
        request.add_header('Content-Type', 'application/x-www-form-urlencoded')
        response = urllib.request.urlopen(request)
        content = response.read()
        if content:
            cars = json.loads(content)
            strover = '识别结果：\n'
            try:
                i = 1
                for car in cars['result']:
                    strover += '{} 车型：{} \n  年份：{} \n'.format(i, car['name'], car['year'])
                    i += 1
            except BaseException:
                error_msg = cars['error_msg']
                strover += '  错误：\n  {} \n '.format(error_msg)
            self.label_3.setText(strover)

    # 10获取logo信息
    def get_logo(self, access_token):
        request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/logo"
        # 二进制方式打开图片文件
        f = self.get_file_content(self.download_path[0])
        img = base64.b64encode(f)
        params = {"custom_lib": False, "image": img}
        params = urllib.parse.urlencode(params).encode('utf-8')
        request_url = request_url + "?access_token=" + access_token
        request = urllib.request.Request(url=request_url, data=params)
        request.add_header('Content-Type', 'application/x-www-form-urlencoded')
        response = urllib.request.urlopen(request)
        content = response.read()
        if content:
            logos = json.loads(content)
            strover = '识别结果：\n'
            try:
                i = 1
                for logo in logos['result']:
                    strover += '{} Logo名称：{} \n'.format(i, logo['name'])
                    i += 1
            except BaseException:
                error_msg = logos['error_msg']
                strover += '  错误：\n  {} \n '.format(error_msg)
            self.label_3.setText(strover)

    # 读取图片
    def get_file_content(self, filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

# 程序主方法
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    # 初始化窗体
    ui = Ui_Form()
    # 调用创建窗体方法
    ui.setupUi(MainWindow)
    # 显示窗体
    MainWindow.show()
    sys.exit(app.exec_())
