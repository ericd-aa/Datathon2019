from tkinter import *
from joblib import load
import numpy as np



canvas_width=1200
canvas_height=700
os=0  #offset


master = Tk()
master.title( "Analisis de Patologia de Rinon" )
master.geometry("1200x700")
w1 = Canvas(master, 
           width=canvas_width, 
           height=canvas_height,
           bg="#ffffff")

w1.pack(expand = YES, fill = BOTH)
w1.create_text(290,20,text='ANALISIS DE PATOLOGIA BASADO EN PRUEBA DE ORINA',font="Bahnschrift 16 bold ", fill="#000000")

#Edad
edad=Label(master, text='Edad:', bg="#ffffff", font="Bahnschrift 13")
edad.place(x=15, y=65+os)
edadEntry=Entry(master, bd=3, width=5)
edadEntry.place(x=70,y=70+os)

#Albumina
al=IntVar()
alb=Label(master, text='Albúmina:', bg="#ffffff", font="Bahnschrift 13")
al0=Radiobutton(master, text='0', variable=al, value=0,bg="#ffffff",font="Bahnschrift 12")
al1=Radiobutton(master, text='1', variable=al, value=1,bg="#ffffff",font="Bahnschrift 12")
al2=Radiobutton(master, text='2', variable=al, value=2,bg="#ffffff",font="Bahnschrift 12")
al3=Radiobutton(master, text='3', variable=al, value=3,bg="#ffffff",font="Bahnschrift 12")
al4=Radiobutton(master, text='4', variable=al, value=4,bg="#ffffff",font="Bahnschrift 12")
al5=Radiobutton(master, text='5', variable=al, value=5,bg="#ffffff",font="Bahnschrift 12")
ald=Radiobutton(master, text='Desconocido', variable=al, value=-1,bg="#ffffff",font="Bahnschrift 12")
alb.place(x=240, y=70+os)
al0.place(x=330,y=70+os)
al1.place(x=330,y=95+os)
al2.place(x=330,y=120+os)
al3.place(x=330,y=145+os)
al4.place(x=330,y=170+os)
al5.place(x=330,y=195+os)
ald.place(x=330,y=220+os)

#Azucar
su=IntVar()
azc=Label(master, text='Azúcar:', bg="#ffffff", font="Bahnschrift 13")
az0=Radiobutton(master, text='0', variable=su, value=0,bg="#ffffff",font="Bahnschrift 12")
az1=Radiobutton(master, text='1', variable=su, value=1,bg="#ffffff",font="Bahnschrift 12")
az2=Radiobutton(master, text='2', variable=su, value=2,bg="#ffffff",font="Bahnschrift 12")
az3=Radiobutton(master, text='3', variable=su, value=3,bg="#ffffff",font="Bahnschrift 12")
az4=Radiobutton(master, text='4', variable=su, value=4,bg="#ffffff",font="Bahnschrift 12")
az5=Radiobutton(master, text='5', variable=su, value=5,bg="#ffffff",font="Bahnschrift 12")
azd=Radiobutton(master, text='Desconocido', variable=su, value=-1,bg="#ffffff",font="Bahnschrift 12")
azc.place(x=550, y=70+os)
az0.place(x=620,y=70+os)
az1.place(x=620,y=95+os)
az2.place(x=620,y=120+os)
az3.place(x=620,y=145+os)
az4.place(x=620,y=170+os)
az5.place(x=620,y=195+os)
azd.place(x=620,y=220+os)

#Gravedad Especifica
sg=IntVar()
ges=Label(master, text='Gravedad\nEspecífica:', bg="#ffffff", font="Bahnschrift 13")
ge0=Radiobutton(master, text='1.005', variable=sg, value=1.005,bg="#ffffff",font="Bahnschrift 12")
ge1=Radiobutton(master, text='1.010', variable=sg, value=1.010,bg="#ffffff",font="Bahnschrift 12")
ge2=Radiobutton(master, text='1.015', variable=sg, value=1.015,bg="#ffffff",font="Bahnschrift 12")
ge3=Radiobutton(master, text='1.020', variable=sg, value=1.020,bg="#ffffff",font="Bahnschrift 12")
ge4=Radiobutton(master, text='1.025', variable=sg, value=1.025,bg="#ffffff",font="Bahnschrift 12")
ged=Radiobutton(master, text='Desconocido', variable=sg, value=-1,bg="#ffffff",font="Bahnschrift 12")
ges.place(x=820, y=70+os)
ge0.place(x=920,y=70+os)
ge1.place(x=920,y=95+os)
ge2.place(x=920,y=120+os)
ge3.place(x=920,y=145+os)
ge4.place(x=920,y=170+os)
ged.place(x=920,y=195+os)

#Presion sanguinea
ps=Label(master, text='Presion \nsanguinea:', bg="#ffffff", font="Bahnschrift 13")
ps.place(x=5, y=110+os)
psEntry=Entry(master, bd=3, width=7)
psEntry.place(x=95,y=120+os)
psUnits=Label(master, text='mmHg', bg="#ffffff", font="Bahnschrift 13")
psUnits.place(x=130,y=120+os)

#Globulos Rojos
rbc=IntVar()
grs=Label(master, text='Glóbulos\nRojos:', bg="#ffffff", font="Bahnschrift 13")
grn=Radiobutton(master, text='Normal', variable=rbc, value=1,bg="#ffffff",font="Bahnschrift 12")
gra=Radiobutton(master, text='Anormal', variable=rbc, value=0,bg="#ffffff",font="Bahnschrift 12")
grd=Radiobutton(master, text='Desconocido', variable=rbc, value=-1,bg="#ffffff",font="Bahnschrift 12")
grs.place(x=240, y=285+os)
grn.place(x=330, y=285+os)
gra.place(x=330, y=310+os)
grd.place(x=330, y=335+os)

#Celulas de pus
pc=IntVar()
cps=Label(master, text='Células\nde pus:', bg="#ffffff", font="Bahnschrift 13")
cpn=Radiobutton(master, text='Normal', variable=pc, value=1,bg="#ffffff",font="Bahnschrift 12")
cpa=Radiobutton(master, text='Anormal', variable=pc, value=0,bg="#ffffff",font="Bahnschrift 12")
cpd=Radiobutton(master, text='Desconocido', variable=pc, value=-1,bg="#ffffff",font="Bahnschrift 12")
cps.place(x=550, y=285+os)
cpn.place(x=620, y=285+os)
cpa.place(x=620, y=310+os)
cpd.place(x=620, y=335+os)

#Grupos de celulas de pus
pcc=IntVar()
gcps=Label(master, text='Grupos de\ncélulas\nde pus:', bg="#ffffff", font="Bahnschrift 13")
gcpp=Radiobutton(master, text='Presente', variable=pcc, value=1,bg="#ffffff",font="Bahnschrift 12")
gcpn=Radiobutton(master, text='No presente', variable=pcc, value=0,bg="#ffffff",font="Bahnschrift 12")
gcpd=Radiobutton(master, text='Desconocido', variable=pcc, value=-1,bg="#ffffff",font="Bahnschrift 12")
gcps.place(x=820, y=285+os)
gcpp.place(x=920, y=285+os)
gcpn.place(x=920, y=310+os)
gcpd.place(x=920, y=335+os)

#Bacteria
ba=IntVar()
btl=Label(master, text='Bacteria:', bg="#ffffff", font="Bahnschrift 13")
btp=Radiobutton(master, text='Presente', variable=ba, value=1,bg="#ffffff",font="Bahnschrift 12")
btn=Radiobutton(master, text='No presente', variable=ba, value=0,bg="#ffffff",font="Bahnschrift 12")
btd=Radiobutton(master, text='Desconocido', variable=ba, value=-1,bg="#ffffff",font="Bahnschrift 12")
btl.place(x=240, y=395+os)
btp.place(x=330, y=400+os)
btn.place(x=330, y=425+os)
btd.place(x=330, y=450+os)

#Glucosa en la sangre
glcl=Label(master, text='Glucosa\nen la sangre:', bg="#ffffff", font="Bahnschrift 13")
glcl.place(x=5, y=170+os)
bgrEntry=Entry(master, bd=3, width=7)
bgrEntry.place(x=105,y=190+os)
glcUnits=Label(master, text='mgs/dL', bg="#ffffff", font="Bahnschrift 13")
glcUnits.place(x=140,y=190+os)

#Urea en la sangre
buL=Label(master, text='Urea\nen la sangre:', bg="#ffffff", font="Bahnschrift 13")
buL.place(x=5, y=230+os)
buEntry=Entry(master, bd=3, width=7)
buEntry.place(x=105,y=250+os)
buUnits=Label(master, text='mgs/dL', bg="#ffffff", font="Bahnschrift 13")
buUnits.place(x=140,y=250+os)

#Nivel de Creatinina
scl=Label(master, text='Nivel de\ncreatinina:', bg="#ffffff", font="Bahnschrift 13")
scl.place(x=5, y=290+os)
scEntry=Entry(master, bd=3, width=7)
scEntry.place(x=105,y=310+os)
scUnits=Label(master, text='mgs/dL', bg="#ffffff", font="Bahnschrift 13")
scUnits.place(x=140,y=310+os)

#Nivel de Sodio
sodl=Label(master, text='Nivel de\nsodio:', bg="#ffffff", font="Bahnschrift 13")
sodl.place(x=5, y=350+os)
sodEntry=Entry(master, bd=3, width=7)
sodEntry.place(x=105,y=370+os)
sodUnits=Label(master, text='mEq/l', bg="#ffffff", font="Bahnschrift 13")
sodUnits.place(x=140,y=370+os)

#Nivel de Potasio
potl=Label(master, text='Nivel de\npotasio:', bg="#ffffff", font="Bahnschrift 13")
potl.place(x=5, y=410+os)
potEntry=Entry(master, bd=3, width=7)
potEntry.place(x=105,y=430+os)
potUnits=Label(master, text='mEq/l', bg="#ffffff", font="Bahnschrift 13")
potUnits.place(x=140,y=430+os)

#Hemoglobina
hemol=Label(master, text='Hemoglobina:', bg="#ffffff", font="Bahnschrift 13")
hemol.place(x=5, y=490+os)
hemoEntry=Entry(master, bd=3, width=7)
hemoEntry.place(x=125,y=490+os)
hemoUnits=Label(master, text='mEq/l', bg="#ffffff", font="Bahnschrift 13")
hemoUnits.place(x=160,y=490+os)

#Hipertensión
htn=IntVar()
htnl=Label(master, text='Hipertensión:', bg="#ffffff", font="Bahnschrift 13")
htny=Radiobutton(master, text='Si', variable=htn, value=1,bg="#ffffff",font="Bahnschrift 12")
htnn=Radiobutton(master, text='No ', variable=htn, value=0,bg="#ffffff",font="Bahnschrift 12")
htnd=Radiobutton(master, text='Desconocido', variable=htn, value=-1,bg="#ffffff",font="Bahnschrift 12")
htnl.place(x=550,y=395+os)
htny.place(x=670, y=400+os)
htnn.place(x=670, y=425+os)
htnd.place(x=670, y=450+os)

#Diabetes 
dm=IntVar()
dml=Label(master, text='Diabetes:', bg="#ffffff", font="Bahnschrift 13")
dmy=Radiobutton(master, text='Si', variable=dm, value=1,bg="#ffffff",font="Bahnschrift 12")
dmn=Radiobutton(master, text='No ', variable=dm, value=0,bg="#ffffff",font="Bahnschrift 12")
dmd=Radiobutton(master, text='Desconocido', variable=dm, value=-1,bg="#ffffff",font="Bahnschrift 12")
dml.place(x=820,y=395+os)
dmy.place(x=920,y=400+os)
dmn.place(x=920,y=425+os)
dmd.place(x=920,y=450+os)

#Enfermedad de Arterias Coronarias
cad=IntVar()
cadl=Label(master, text='Enfermedad\nde las\narterias\ncoronarias:', bg="#ffffff", font="Bahnschrift 13")
cady=Radiobutton(master, text='Si', variable=cad, value=1,bg="#ffffff",font="Bahnschrift 12")
cadn=Radiobutton(master, text='No ', variable=cad, value=0,bg="#ffffff",font="Bahnschrift 12")
cadd=Radiobutton(master, text='Desconocido', variable=cad, value=-1,bg="#ffffff",font="Bahnschrift 12")
cadl.place(x=235,y=490+os)   
cady.place(x=330,y=495+os)
cadn.place(x=330,y=520+os)
cadd.place(x=330,y=545+os)

#Apetito
appet=IntVar()
appetl=Label(master, text='Apetito:', bg="#ffffff", font="Bahnschrift 13")
appetg=Radiobutton(master, text='Bueno', variable=appet, value=1,bg="#ffffff",font="Bahnschrift 12")
appetp=Radiobutton(master, text='Malo', variable=appet, value=0,bg="#ffffff",font="Bahnschrift 12")
appetd=Radiobutton(master, text='Desconocido', variable=appet, value=-1,bg="#ffffff",font="Bahnschrift 12")
appetl.place(x=550,y=490+os)
appetg.place(x=620,y=495+os)
appetp.place(x=620,y=520+os)
appetd.place(x=620,y=545+os)

#Edema
pe=IntVar()
pel=Label(master, text='Edema:', bg="#ffffff", font="Bahnschrift 13")
pey=Radiobutton(master, text='Si', variable=pe, value=1,bg="#ffffff",font="Bahnschrift 12")
pen=Radiobutton(master, text='No ', variable=pe, value=0,bg="#ffffff",font="Bahnschrift 12")
ped=Radiobutton(master, text='Desconocido', variable=pe, value=-1,bg="#ffffff",font="Bahnschrift 12")
pel.place(x=820,y=490+os)
pey.place(x=920,y=495+os)
pen.place(x=920,y=520+os)
ped.place(x=920,y=545+os)

#Anemia
ane=IntVar()
anel=Label(master, text='Anemia:', bg="#ffffff", font="Bahnschrift 13")
aney=Radiobutton(master, text='Si', variable=ane, value=1,bg="#ffffff",font="Bahnschrift 12")
anen=Radiobutton(master, text='No ', variable=ane, value=0,bg="#ffffff",font="Bahnschrift 12")
aned=Radiobutton(master, text='Desconocido', variable=ane, value=-1,bg="#ffffff",font="Bahnschrift 12")
anel.place(x=550,y=570+os)
aney.place(x=620,y=575+os)
anen.place(x=620,y=600+os)
aned.place(x=620,y=625+os)

#Volúmen Celular
pcvl=Label(master, text='Volúmen\ncelular:', bg="#ffffff", font="Bahnschrift 13")
pcvl.place(x=5, y=540+os)
pcvEntry=Entry(master, bd=3, width=6)
pcvEntry.place(x=105,y=545+os)

#Glóbulos Blancos
wcl=Label(master, text='Glóbulos\nblancos:', bg="#ffffff", font="Bahnschrift 13")
wcl.place(x=5, y=600+os)
wcEntry=Entry(master, bd=3, width=7)
wcEntry.place(x=105,y=600+os)
wcUnits=Label(master, text='cells/cumm', bg="#ffffff", font="Bahnschrift 13")
wcUnits.place(x=143,y=600+os)

#Glóbulos Rojos
rcl=Label(master, text='Glóbulos\nrojos:', bg="#ffffff", font="Bahnschrift 13")
rcl.place(x=240, y=600+os)
rcEntry=Entry(master, bd=3, width=7)
rcEntry.place(x=330,y=600+os)
rcUnits=Label(master, text='cells/cumm', bg="#ffffff", font="Bahnschrift 13")
rcUnits.place(x=360,y=600+os)

def capturar():
	model=load('modelSVCLinear.joblib')

	data=np.ndarray((1,24))
	
	if edadEntry.get()=='':
		data[0][0]=-1
	else:
		data[0][0]=edadEntry.get()
	
	if psEntry.get()=='':
		data[0][1]=-1
	else:
		data[0][1]=psEntry.get()

	data[0][2]=sg.get()

	data[0][3]=al.get()

	data[0][4]=su.get()

	data[0][5]=rbc.get()

	data[0][6]=pc.get()

	data[0][7]=pcc.get()

	data[0][8]=ba.get()

	if bgrEntry.get()=='':
		data[0][9]=-1
	else:
		data[0][9]=bgrEntry.get()

	if buEntry.get()=='':
		data[0][10]=-1
	else:
		data[0][10]=buEntry.get()

	if scEntry.get()=='':
		data[0][11]=-1
	else:
		data[0][11]=scEntry.get()


	if sodEntry.get()=='':
		data[0][12]=-1
	else:
		data[0][12]=sodEntry.get()

	if potEntry.get()=='':
		data[0][13]=-1
	else:
		data[0][13]=potEntry.get()

	if hemoEntry.get()=='':
		data[0][14]=-1
	else:
		data[0][14]=hemoEntry.get()

	if pcvEntry.get()=='':
		data[0][15]=-1
	else:
		data[0][15]=pcvEntry.get()

	if wcEntry.get()=='':
		data[0][16]=-1
	else:
		data[0][16]=wcEntry.get()

	if rcEntry.get()=='':
		data[0][17]=-1
	else:
		data[0][17]=rcEntry.get()

	data[0][18]=htn.get()

	data[0][19]=dm.get()

	data[0][20]=cad.get()

	data[0][21]=appet.get()

	data[0][22]=pe.get()

	data[0][23]=ane.get()

	pred=model.predict(data)

	win=Toplevel(master)
	win.title('Predicciones')
	win.geometry( "600x200" )
	if int(pred)==1:
		text='\n\nRiesgo de padecer una enfermedad crónica en el riñón'
	else:
		text='\n\nSin riesgo de padecer una enfermedad crónica en el riñón'

	l1=Label(win, text=text )
	l1.pack(anchor=CENTER)
	l1.config(font=("Bahnschrift",16))

btn1 = Button(master,text="Capturar",command=capturar ,height='2',width='17', bg="#47beed", activeforeground="#67b8a5", font="Bahnschrift 13")
btn1.place(x=900, y=600)



master.mainloop()