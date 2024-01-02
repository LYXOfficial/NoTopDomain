import base64
print(base64.b64encode("""QMainWindow *{
	font-family:"Microsoft YaHei","Microsoft YaHei";
}
#centralwidget{
	margin-top:0;
	background-color: aliceblue;
}
QPushButton,QToolButton{
	padding-left: 7px;
	padding-right:7px;
	padding-top:5px;
	padding-bottom:5px;
	height:1em;
	border:none;
	background-color: #eeebeb;
	border: 1px solid #c0c0c0;
	border-radius:5px;
}
QToolButton{
	padding:3px;
}
QPushButton:hover,QToolButton:hover{
	background-color:rgb(228, 228, 228);
}
QPushButton:pressed,QToolButton:pressed{
	background-color:rgb(208, 208, 208);
}
QLineEdit{
	height:1.3em;
}
QCheckBox{
	margin:1px;
}
QTabBar::tab{
	background:transparent;
	border:none;
	padding:5px;
	margin:4px;
	height:1.1em;
}
QTabBar::tab:hover{
	color:#555555;
}
QTabBar::tab:selected{
	border-bottom:2px solid #70bfed;
}
QTabWidget::pane{
	border-radius:10px;
	background-color:#ffffff;
	border: 1px solid #ddd;
	padding:2px;
	margin:0 2px 2px 2px;
}
/* QCheckBox::indicator{
	border-radius:2px;
	border:0.5px solid gray;
	padding:2px;
}
QCheckBox::indicator:checked{
	background-color:#0460da;
	border-color:#ccc;
	position:relative;
} */
QLineEdit,QTextEdit,QPlainTextEdit{
	border-radius:5px;
	border:1px solid #bbb;
	selection-background-color:#70bfed;
}
QGroupBox{
	border-radius:10px;
	border:1px solid #ccc;
	color:#5b7372;
	font-size:15px;
	/* padding-top:15px; */
	font-family:"Microsoft YaHei";
	background-color: white;
}
#groupBox,#groupBox_13,#groupBox_12,#groupBox_8,#groupBox_2,#groupBox_4,#groupBox_3,#groupBox_5,#groupBox_6,#groupBox_9{
	padding-top:25px;
}
QGroupBox::title{
	subcontrol-origin:margin;
	padding:10px 10px;
	background:transparent;
}
QMenuBar::item{
	border-radius:5px;
	padding:2px 8px;
	background-color:white;
}
QMenuBar::item:selected{
	background-color:#ddd;
}
QMenuBar{
	background-color:white;
}
QLineEdit:focus,QTextEdit:focus,QPlainTextEdit:focus{
	border-color:#70bfed;
}
#widget_2{
	background-color: rgb(46, 161, 255);
}
#label_21,#ver{
	color:white
}
#widget_4 QRadioButton{
	margin:5px;
	padding-left:-2px;
	font-size:17px;
}
#widget_4 QRadioButton:!checked:hover{
	color:rgb(231, 231, 231);
}
#widget_4 QRadioButton:!checked{
	color:white;
	border-left: 4px solid transparent;
}
#widget_4 QRadioButton:checked:hover{
	color:rgb(213, 178, 142);
}
#widget_4 QRadioButton:checked{
	color:rgb(255, 206, 171);
	border-left: 4px solid rgb(255, 206, 171);
}
#widget_4 QRadioButton::indicator{
	width: 0px;
	height: 0px;
}
#closeWin{
	height:30px;
	width:24px;
	font-size:35px;
	padding-top:-3px;
	border-radius: 16px;
	margin:0;
	color: white;
	background: transparent;
	border:none;
}
#closeWin:hover{
	background-color: rgba(255, 0, 0, 0.8);
}
#closeWin:pressed{
	background-color: rgba(147, 84, 84, 0.8);
}
#minWin{
	height:30px;
	width:24px;
	font-size:35px;
	padding-top:-3px;
	border-radius: 16px;
	margin:0;
	color: white;
	background: transparent;
	border:none;
}
#ExitProcess{
	margin: 0;
	color: white;
	background: transparent;
	border:none;
	max-height:24px;
	width:24px;
	padding:8px 6px;
	border-radius: 16px;
}
#minWin:hover,#ExitProcess:hover{
	background-color: rgba(128, 128, 128, 0.6);
}
#minWin:pressed,#ExitProcess:hover{
	background-color: rgba(93, 93, 93, 0.7);
}
#startButton:!hover,#Reset:!hover{
	background-color: white;
}
#KillTD,#HangUpTD,#GBWindowed,#CloseGB{
	margin:6px;
	border-radius:28px;
	font-size:15px;
	background-color:transparent;
	border:1px solid #d8d8d8;
}
#KillTD:hover,#HangUpTD:hover,#GBWindowed:hover,#CloseGB:hover{
	background-color: #d8d8d8;
}
#KillTD:pressed,#HangUpTD:pressed,#GBWindowed:pressed,#CloseGB:pressed{
	background-color: #cacaca;
}
#lineEdit_2{
	margin:0 5px;
}
QLineEdit{
	padding:0 10px;
}
#stTSK,#UninstallTopDomain{
	padding:6px 5px;
	font-size:14px;
}
#KillTD:enabled{
	color:#8f0000;
}
#HangUpTD:enabled{
	color:#395a86;
}
#GBWindowed:enabled{
	color:#73833b;
}
#CloseGB:enabled{
	color:#af991f;
}
#groupBox_4 QLineEdit{
	height:30px;
	font-size:14px;
	margin:0 20px;
}
#groupBox_4 QLabel{
	height:30px;
	font-size:15px;
	margin:0 20px;
}
#groupBox_3 QLabel{
	font-size:15px;
}
#GBBB QLabel,#jhhhh QLabel{
	font-size:15px;
}
#stTSK,#UninstallTopDomain{
	font-size:15px;
}
#widget{
	background-color: #BBADA0;
	border:none;
}
#buttonbox{
	background-color: #BBADA0;
	border:none;
}
#Reset,#startButton{
	border: none;
}
#helpButton{
	color:white;
	background-color:rgb(46, 161, 255);
	border:none;
	border-radius:30px;
	font-size:35px;
}
#helpButton:hover{
	background-color:rgb(41, 133, 209);
}
QTextEdit,QPlainTextEdit,QTextBrowser{
	border-radius:10px;
	background-color:transparent;
	padding:10px;
}
#helpMd{
	background-color:white;
}
#capWindow{
	font-size:18px;
}
#groupBox_6 QPushButton{
	padding:7px;
}
#pushButton_2,#reStart{
	padding:8px;
	font-size:17px;
}
#logLabel{
	padding:10px 20px;
	background-color:#000000;
	color:white;
	background:#88000000;
	border-radius:19px;
}
#logpro::groove{
	background:transparent;
	border:none;
}
#logpro::sub-page{
	border-radius:1px;
	background:white;
}
#logpro::handle{
	width:0;
	height:0;
	background:transparent;
}
#groupBox{
	min-height:180px;
}""".encode()))