from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.font import BOLD

from calculos_vertedero  import (
    DisVertedero,
    Cotas,
    parametrosTrap,
    parametrosRect,
    y2_DesnivelTrap,
    y2_Desnivelrec
)

from calculos_partidor import (
    calculo_partidor,
    partidor_movil
)

interfaz=Tk()
interfaz.title('DISEÑO ESTRUCTURAS HIDRAULICAS')
# interfaz.geometry("800x500")
w = 800
h = 500
# Central la ventana a la pantalla
ws = interfaz.winfo_screenwidth()  # ancho de la pantalla
hs = interfaz.winfo_screenheight()  # alto de la pantalla

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# Asignar el tamaño y la posicion de la ventana
interfaz.geometry('%dx%d+%d+%d' % (w, h, x, y))
interfaz.resizable(width=False, height=False)
### IMAGENES

fondo = PhotoImage(file = "canal2.png")
fondo2=Label(interfaz, image=fondo).place(x=0,y=0)
logo=PhotoImage(file="logo.png")
logoR=logo.subsample(2,2)
logoDis=Label(interfaz, image=logoR).place(x=320,y=30)


##-------------------------------------VENTANA VERTEDERO----------------------------
q=DoubleVar()
pendiente=DoubleVar()
b=DoubleVar()
z=DoubleVar()
n=DoubleVar()
ca=DoubleVar()
Hd=DoubleVar()
Hc=DoubleVar()

RS=DoubleVar()
RLt=DoubleVar()
RA=DoubleVar()
RT=DoubleVar()
Ra=DoubleVar()
RAng=DoubleVar()
RL3=DoubleVar()
RL2=DoubleVar()
RQv=DoubleVar()
RVv=DoubleVar()
Ry2=DoubleVar()
Rca=DoubleVar()
Rcb=DoubleVar()
Rcd=DoubleVar()
Rcc=DoubleVar()
seleccion=DoubleVar()
Ry1=DoubleVar()
Rvel=DoubleVar()
RBl=DoubleVar()
RFr=DoubleVar()
Ryc=DoubleVar()
RE1=DoubleVar()
Rdesnivel=DoubleVar()

def calcular():
    ##Calculo del DisVertedero
    HdCalc = Hd.get()
    qCalc = q.get()
    bCalc = b.get()
    zCalc = z.get()
    HcCalc=Hc.get()
    nCalc= n.get()
    pendienteCalc=pendiente.get()

    tipoEstructura=seleccion.get()
    if tipoEstructura==1:
        valorTirante = parametrosRect(qCalc,nCalc,pendienteCalc,bCalc,HcCalc)
        
    else:
        valorTirante=parametrosTrap(qCalc,nCalc,pendienteCalc,bCalc,zCalc,HcCalc)
    
    valoresDisVertedero = DisVertedero(valorTirante[0],HdCalc, qCalc, bCalc, zCalc)
    RS.set(valoresDisVertedero[0])
    RT.set(valoresDisVertedero[1])
    RLt.set(valoresDisVertedero[2])
    RA.set(valoresDisVertedero[3])
    RL3.set(abs(valoresDisVertedero[4]))
    RAng.set(valoresDisVertedero[5])
    RQv.set(valoresDisVertedero[6])
    RVv.set(valoresDisVertedero[7])
    
    # cotas
    caCalc= ca.get()
    valoresCotas= Cotas(caCalc,HdCalc, valoresDisVertedero[0])
    Rca.set(valoresCotas[0])
    Rcb.set(valoresCotas[1])
    Rcc.set(valoresCotas[2])
    Rcd.set(valoresCotas[3])
    RL2.set(0.40)
    
    if tipoEstructura==1: #rectangular 
        valores_y2_Desnivel=y2_Desnivelrec(valoresDisVertedero[6],nCalc,pendienteCalc,bCalc,valorTirante[0],qCalc,HdCalc)
        print("calculo de la opcion 1")
    else:
        valores_y2_Desnivel= y2_DesnivelTrap(valoresDisVertedero[6],nCalc,pendienteCalc,bCalc,zCalc,valorTirante[0],qCalc,HdCalc)
        print("calculo de la opcion 2")

    Ry1.set(valorTirante[0])
    Rvel.set(valorTirante[1])
    RBl.set(valorTirante[2])
    RFr.set(valorTirante[3])
    Ryc.set(valorTirante[4])
    Ry2.set(valores_y2_Desnivel[0])
    RE1.set(valores_y2_Desnivel[1])
    Rdesnivel.set(valores_y2_Desnivel[2])


def v2():
   
    ventana2=Toplevel()
    
    w = 1280
    h = 760

    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    ventana2.geometry('%dx%d+%d+%d' % (w, h, x, y))
    ventana2.title("Diseño vertedero pico de pato")

    #------------------------
    #Para Pruebas. Quitar

    def key2(event):
        if str(event.char) == 'q' or str(event.char) == 'Q':
            ventana2.quit()

    ventana2.bind("<Key>", key)

#Datos de entrada
  
    SeccionTrans = Label(ventana2,text = "SECCIÓN TRANSVERSAL", font = ("arial",9,"bold")).place(x = 220,y = 20)
    DatosEntradaC =  Label(ventana2,text = "DATOS DE ENTRADA",font = ("arial",9,"bold")).place(x = 50,y = 100)
    Qd = Label(ventana2,text = "Caudal de diseño [Qd, m³/s]").place(x = 30,y = 130)
    Qdtext = Entry(ventana2,textvariable = q).place(x = 185,y = 130, width = 35)
    bL = Label(ventana2,text = "Base del canal [b, m]").place(x = 30,y = 150)
    btext = Entry(ventana2,textvariable =  b).place(x = 185,y = 150, width = 35)
    zL = Label(ventana2,text = "Talud [z]").place(x = 30,y = 170)
    ztext = Entry(ventana2,textvariable = z).place(x = 185,y = 170, width = 35)
    RugosidadL = Label(ventana2,text = "Rugosidad [n]").place(x = 30,y = 190)
    Rugosidadtext = Entry(ventana2,textvariable = n).place(x = 185,y = 190, width = 35)
    Sl = Label(ventana2,text = "Pendiente [s]").place(x = 30,y = 210)
    Stext = Entry(ventana2,textvariable = pendiente).place(x = 185,y = 210, width = 35)
    Hm = Label(ventana2,text = "Altura muros [Hm, m]").place(x = 30,y = 230)
    Hmtext = Entry(ventana2,textvariable = Hc).place(x = 185,y = 230, width = 35)

    separador = ttk.Separator(ventana2, orient = HORIZONTAL).place(relx = 0.03, rely = 0.12, relwidth = 0.40)
    separador = ttk.Separator(ventana2, orient = HORIZONTAL).place(relx = 0.04, rely = 0.37, relwidth = 0.18)
    separador = ttk.Separator(ventana2, orient = HORIZONTAL).place(relx = 0.27, rely = 0.37, relwidth = 0.18)
    separador = ttk.Separator(ventana2, orient = VERTICAL).place(relx = 0.25, rely = 0.15,relheight = 1)
    separador = ttk.Separator(ventana2, orient = VERTICAL).place(relx = 0.46, rely = 0.03,relheight = 20)

    cota = Label(ventana2,text = "Cota A").place(x = 30,y = 290)
    cotatext = Entry(ventana2, textvariable = ca).place(x = 185,y = 290, width = 35)
    Hdl = Label(ventana2,text = "Carga Hidráulica ").place(x = 30,y = 310)
    Hdtext = Entry(ventana2,textvariable = Hd).place(x = 185,y = 310, width = 35)
    Hdl = Label(ventana2,text = " [ΔH, 0.05-0.10m]").place(x = 30,y = 330)
    
    #Resultados
    resultadoscanal = Label(ventana2,text = "RESULTADOS",font = ("arial",9,"bold")).place(x = 410,y = 100)
    y1 = Label(ventana2,text = "Tirante normal [y1, m]").place(x = 350,y = 130)
    y1text = Entry(ventana2,textvariable = Ry1).place(x = 480,y = 130, width = 35)
    yc = Label(ventana2,text = "Tirante crítico [yc, m]").place(x = 350,y = 150)
    yctext = Entry(ventana2,textvariable = Ryc).place(x = 480,y = 150, width = 35)
    Vc = Label(ventana2,text = "Velocidad [V, m/s]").place(x = 350,y = 170)
    Vctext = Entry(ventana2,textvariable = Rvel).place(x = 480,y = 170, width = 35)
    asterisco = Label(ventana2,text = "*", fg = ("red"),font = ("bond")).place(x = 340,y = 170)
    Bl = Label(ventana2,text = "Borde libre [Bl, m]").place(x = 350,y = 190)
    Bltext = Entry(ventana2, textvariable = RBl).place(x = 480,y = 190, width = 35)
    Nfroude = Label(ventana2,text = "Número de froude [F]").place(x = 350,y = 210)
    Nfroudetext = Entry(ventana2,textvariable = RFr).place(x = 480,y = 210, width = 35)
    EnergiaL = Label(ventana2,text = "Energía Específica [E1]").place(x = 350,y = 230)
    EnergiaLtext = Entry(ventana2,textvariable = RE1).place(x = 480,y = 230, width = 35)
    energiaL = Label(ventana2,text = "[m-kg/kg]").place(x = 350,y = 250)
    angulo = Label(ventana2,text = "Ángulo [θ]").place(x = 350,y = 290)
    angulotext = Entry(ventana2,textvariable = RAng).place(x = 480,y = 290, width = 35)
    asterisco = Label(ventana2,text = "*", fg = ("red"),font = ("bond")).place(x = 340,y = 290)
    sc = Label(ventana2,text = "Altura vertedero[Hv, m]").place(x = 350,y = 310)
    sctext = Entry(ventana2,textvariable = RS).place(x = 480,y = 310, width = 35)
    Lt = Label(ventana2,text = "Longitud total [Lt, m]").place(x = 350,y = 330)
    Lttext = Entry(ventana2,textvariable = RLt).place(x = 480,y = 330, width = 35)
    L3l = Label(ventana2,text = "Longitud 1 [L1, m]").place(x = 350,y = 350)
    L3text = Entry(ventana2,textvariable = RA).place(x = 480,y = 350, width = 35)
    L2l = Label(ventana2,text =  "Longitud 2 [L2, m]").place(x = 350,y = 370)
    L2ltext = Entry(ventana2,textvariable = RL2).place(x = 480,y = 370,width = 35)
    L3l = Label(ventana2,text =  "Longitud 3 [L3, m]").place(x = 350,y = 390)
    L3text = Entry(ventana2,textvariable = RL3).place(x = 480,y = 390, width = 35)
    Tl = Label(ventana2,text = "Ancho de entrada[T, m]").place(x = 350,y = 410)
    Ttext = Entry(ventana2,textvariable = RT).place(x = 480,y = 410, width = 35)
    TiranteF = Label(ventana2,text = "Tirante final [y2, m]").place(x = 350,y = 430)
    TiranteFAtext = Entry(ventana2,textvariable = Ry2).place(x = 480,y = 430, width = 35)
    desnivel = Label(ventana2,text = "Desnivel [ΔZ, m]").place(x = 350,y = 450)
    desniveltext = Entry(ventana2,textvariable = Rdesnivel).place(x = 480,y = 450, width = 35)
    Qvl = Label(ventana2,text = "Caudal  [Qv, m³/s]").place(x = 350,y = 470)
    Qvtext = Entry(ventana2,textvariable = RQv).place(x = 480,y = 470, width = 35)
    Vv = Label(ventana2,text = "Velocidad [Vv, m/s]").place(x = 350,y = 490)
    Vvtext = Entry(ventana2,textvariable = RVv).place(x = 480,y = 490, width = 35)
# COTAS
    CotaA = Label(ventana2,text = "Cota A").place(x = 350,y = 510)
    CotaAtext = Entry(ventana2,textvariable = Rca).place(x = 480,y = 510, width = 35)
    CotaB = Label(ventana2,text = "Cota B").place(x = 350,y = 530)
    CotaBtext = Entry(ventana2,textvariable = Rcb).place(x = 480,y = 530, width = 35)
    CotaC = Label(ventana2,text = "Cota C").place(x = 350,y = 550)
    CotaCtext = Entry(ventana2,textvariable = Rcc).place(x = 480,y = 550, width = 35)
    CotaD = Label(ventana2,text = "Cota D").place(x = 350,y = 570)
    CotaDtext = Entry(ventana2,textvariable = Rcd).place(x = 480,y = 570, width = 35)
    SeccionT = Label(ventana2,text = "ESQUEMAS",font = ("arial",9,"bold")).place(x = 900,y = 20) 
    mnsj = Label(ventana2,text = "* Condiciones de diseño:",font = ("arial",11,"bold"),fg = ("red")).place(x = 350,y = 600) 
    mnsj1 = Label(ventana2,text = " V ≤ 1.0 m/s",font = ("arial",9,"bold")).place(x = 400,y = 620) 
    mnsj2 = Label(ventana2,text = " 45° < θ < 70°",font = ("arial",9,"bold")).place(x = 400,y = 640) 
    mnsj3 = Label(ventana2,text = " En caso de no cumplirse, verificar",font = ("arial",9,)).place(x = 340,y = 660) 
    mnsj4 = Label(ventana2,text = "relación entre Qd y b, y/o modificar ΔH",font = ("arial",9,)).place(x = 340,y = 680) 
#BOTON CALCULAR 
    Calcular = Button(ventana2, text = "Calcular",command = calcular).place(x = 120,y = 360)

#RADIO BUTTON
    
    rad1 =  Radiobutton(ventana2,text = "Rectangular",variable = seleccion,value = 1,font = ("Gabriola",14)).place(x = 190,y = 40)
    rad2 = Radiobutton(ventana2,text = "Trapezoidal",variable = seleccion,value = 2,font = ("Gabriola",14)).place(x = 310,y = 40)

#Imágenes en ventana 2 con label correspondientes

    canalTr = PhotoImage(file = "canaltrapez.png")
    canalTrr = canalTr.subsample(9)
    canalTr2 = Label(ventana2,image = canalTrr).place(x = 10,y = 460)
    tit1 = Label(ventana2,text = "ESQUEMA",font = ("arial",9,"bold")).place(x = 120,y = 400)
    tit1 = Label(ventana2,text = "SECCIÓN TRANSVERSAL DEL CANAL",font = ("arial",9,"bold")).place(x = 50,y = 430)
    tit2 = Label(ventana2,text = "VERTEDERO PICO DE PATO VISTA PLANTA",font = ("arial",9,"bold")).place(x = 820,y = 60)
    ppRect = PhotoImage(file = "ppatorec.png")
    ppRectr = ppRect.subsample(11)
    ppPerfil2 = Label(ventana2,image = ppRectr).place(x = 640,y = 120)
    ppatoTr = PhotoImage(file = "ppatoTr.png")
    ppTrr = ppatoTr.subsample(11) 
    ppatoTr2 = Label(ventana2,image = ppTrr).place(x = 930,y = 120)
    tit11 = Label(ventana2,text = "sección rectangular", font = ("Gabriola",14)).place(x = 700,y = 300)
    tit12 = Label(ventana2,text = "sección trapezoidal",font = ("Gabriola",14)).place(x = 980,y = 300)
    tit2 = Label(ventana2,text = "VERTEDERO PICO DE PATO VISTA PERFIL",font = ("arial",9,"bold")).place(x = 820,y = 390)
    ppPerfil = PhotoImage(file = "vertederoPICOPATO.png")
    ppPerfilr = ppPerfil.subsample(5) 
    ppPerfil2 = Label(ventana2,image = ppPerfilr).place(x = 750,y = 420)
    ventana2.resizable(width=False, height=False)
    ventana2.mainloop()

##-------------------------------------VENTANA PARTIDOR PROPORCIONAL----------------------
'''
Datos de entrada para el Canal entrante Ce, Canal pasante Cp
y Canal saliente o lateral Cl
'''
# Q = lambda text: text.isdecimal()
Q = DoubleVar() 
y_var = DoubleVar()
b = DoubleVar()
z = DoubleVar()
long_vertedero = DoubleVar()
n = DoubleVar()
cota_A = DoubleVar()
s = DoubleVar()
angulo = DoubleVar()
Qp = DoubleVar()
yp = DoubleVar()
bp = DoubleVar()
zp = DoubleVar()
Qs = DoubleVar()
ys = DoubleVar()
bs = DoubleVar()
zs = DoubleVar()
cota_B = DoubleVar()
cota_C = DoubleVar()


'''
Datos de salida para el Canal entrante Ce, Canal pasante Cp
y Canal saliente o lateral Cl
'''
vel_rect = DoubleVar()
vel_trape = DoubleVar()
ener_rect = DoubleVar() 
ener_trape = DoubleVar() 
ycrt_rect = DoubleVar() 
ycrt_trape = DoubleVar()
ecrt_rect = DoubleVar() 
ecrt_trape = DoubleVar() 
froude_rect = DoubleVar()
froude_trape = DoubleVar() 
long_transicion = DoubleVar() 
tirante_partidor = DoubleVar()
altura_vert = DoubleVar() 
carga_partidor = DoubleVar() 
ancho_vert = DoubleVar()
long_vert = DoubleVar() 
long_saliente = DoubleVar() 
long_pasante = DoubleVar() 
espesor = DoubleVar() 
long_colchon = DoubleVar()
trans_pasante = DoubleVar()
trans_saliente = DoubleVar()
carga_pasante = DoubleVar() 
carga_saliente = DoubleVar()
opcion = DoubleVar()
tipo = DoubleVar()
cota_1 = DoubleVar()
cota_2 = DoubleVar()
cota_3 = DoubleVar()
cota_4 = DoubleVar()
cota_5 = DoubleVar()
angulo_movil = DoubleVar()




def partidor():
    entrada_Q = Q.get()
    entrada_y = y_var.get()
    entrada_b = b.get()
    entrada_z = z.get()
    entrada_long_vertedero = long_vertedero.get()
    entrada_n = n.get()
    entrada_cotaA = cota_A.get()
    entrada_s = s.get()
    entrada_angulo = angulo.get()
    entrada_Qp = Qp.get()
    entrada_yp = yp.get()
    entrada_bp = bp.get()
    entrada_zp = zp.get()
    entrada_Qs = Qs.get()
    entrada_ys = ys.get()
    entrada_bs = bs.get()
    entrada_zs = zs.get()
    canal_trapezoidal = opcion.get()
    fijo = tipo.get()
    entrada_cotaB = cota_B.get()
    entrada_cotaC = cota_C.get()



    #Canal trapezoidal
    print(canal_trapezoidal)
    resultado_partidor = calculo_partidor(entrada_Q, entrada_y, entrada_b, entrada_z, entrada_long_vertedero, entrada_n, entrada_cotaA, entrada_s, entrada_Qp, entrada_yp, entrada_bp, entrada_zp, entrada_Qs, entrada_ys, entrada_bs, entrada_zs, entrada_angulo, entrada_cotaB, entrada_cotaC)

    if canal_trapezoidal == 2:
        vel_trape.set(resultado_partidor['vel_trape'])
        ener_trape.set(resultado_partidor['ener_trape']) 
        ycrt_trape.set(resultado_partidor['tirante_crt'])
        ecrt_trape.set(resultado_partidor['ener_crt']) 
        long_transicion.set(resultado_partidor['long_transicion1'])
        tirante_partidor.set(resultado_partidor['tirante_partidor'])
        trans_pasante.set(resultado_partidor['long_transpa'])
        trans_saliente.set(resultado_partidor['long_transsa'])
    
    if fijo == 2:
        resultado_movil = partidor_movil(entrada_Q, entrada_y, entrada_b, entrada_z, entrada_long_vertedero, entrada_n, entrada_cotaA, entrada_s, entrada_Qp, entrada_yp, entrada_bp, entrada_zp, entrada_Qs, entrada_ys, entrada_bs, entrada_zs, entrada_angulo, entrada_cotaB, entrada_cotaC)
        carga_partidor.set(resultado_movil['carga_movil']) 
        angulo_movil.set(resultado_movil['angulo_final'])
    else:
        angulo_movil.set('')
        carga_partidor.set(resultado_partidor['carga_hidrau']) 
        

    vel_rect.set(resultado_partidor['velocidad'])
    ener_rect.set(resultado_partidor['energia_especifica']) 
    ycrt_rect.set(resultado_partidor['tirante_critico']) 
    ecrt_rect.set(resultado_partidor['energia_critica']) 
    froude_rect.set(resultado_partidor['numero_froude'])
    altura_vert.set(resultado_partidor['altura_verte'])
    ancho_vert.set(resultado_partidor['ancho_verte'])
    long_vert.set(resultado_partidor['max_vertedero']) 
    long_saliente.set(resultado_partidor['long_saliente']) 
    long_pasante.set(resultado_partidor['long_pasante']) 
    espesor.set(resultado_partidor.get('espesor','')) 
    long_colchon.set(resultado_partidor.get('long_colchon', ''))
    cota_3.set(resultado_partidor.get('cota_3',''))
    carga_pasante.set(resultado_partidor['carga_pasante']) 
    carga_saliente.set(resultado_partidor['carga_saliente'])
    cota_1.set(resultado_partidor['cota_1'])
    cota_2.set(resultado_partidor['cota_2'])
    cota_4.set(resultado_partidor['cota_4'])
    cota_5.set(resultado_partidor['cota_5'])

        
def v3():
    ventana3 = Toplevel()

    w = 1280
    h = 760

    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    ventana3.geometry('%dx%d+%d+%d' % (w, h, x, y))
    
    ventana3.title("Diseño partidor proporcional")

    #Label's para datos de entrada
    SeccionTrans = Label(ventana3,text = "SECCIÓN TRANSVERSAL", font = ("arial",9,"bold")).place(x = 240, y = 20)
    entrante_rotulo =  Label(ventana3,text = "DATOS CANAL ENTRANTE",font = ("arial",9,"bold")).place(x = 60,y = 100)
    Q_rotulo = Label(ventana3, text = "Caudal entrante [Qe, m³/s]").place(x = 30, y = 130)
    y_rotulo = Label(ventana3, text = "Tirante [y, m]").place(x = 30, y = 150)
    b_rotulo = Label(ventana3, text = "Base del canal [b, m]").place(x = 30, y = 170)
    z_rotulo = Label(ventana3, text = "Talud [z]").place(x = 30, y = 190)
    #Solo se pide para canal trapezoidal
    long_vertedero_rotulo = Label(ventana3, text = "Longitud vertedero [Lv, m]").place(x = 30, y = 210)
    angulo_rotulo = Label(ventana3, text = "Ángulo de transición").place(x = 30, y = 230)
    n_rotulo = Label(ventana3, text = "Rugosidad [n]").place(x = 30, y = 250)
    s_rotulo = Label(ventana3, text = "Pendiente [s]").place(x = 30, y = 270)
    cota_rotulo = Label(ventana3, text = "Cota A").place(x = 30, y = 290)
    pasante_rotulo =  Label(ventana3,text = "DATOS CANAL PASANTE",font = ("arial",9,"bold")).place(x = 60,y = 320)
    Qp_rotulo = Label(ventana3, text = "Caudal [Qp, m³/s]").place(x = 30, y = 350)
    yp_rotulo = Label(ventana3, text = "Tirante [yp, m]").place(x = 30, y = 370)
    bp_rotulo = Label(ventana3, text = "Base del canal [bp, m]").place(x = 30, y = 390)
    zp_rotulo = Label(ventana3, text = "Talud [zp]").place(x = 30, y = 410)
    cotaB_rotulo = Label(ventana3, text = "Cota B").place(x = 30, y = 430)
    saliente_rotulo =  Label(ventana3,text = "DATOS CANAL SALIENTE",font = ("arial",9,"bold")).place(x = 60,y = 460)
    Qs_rotulo = Label(ventana3, text = "Caudal [Qs, m³/s]").place(x = 30, y = 490)
    ys_rotulo = Label(ventana3, text = "Tirante [ys, m]").place(x = 30, y = 510)
    bs_rotulo = Label(ventana3, text = "Base del canal [bs, m]").place(x = 30, y = 530)
    zs_rotulo = Label(ventana3, text = "Talud [zs]").place(x = 30, y = 550)
    cotaC_rotulo = Label(ventana3, text = "Cota C").place(x = 30, y = 570)
    
    Q_input = Entry(ventana3, textvariable = Q).place(x = 185, y = 130, width = 35)
    y_input = Entry(ventana3, textvariable = y_var).place(x = 185, y = 150, width = 35)
    b_input = Entry(ventana3, textvariable = b).place(x = 185, y = 170, width = 35)
    z_input = Entry(ventana3, textvariable = z).place(x = 185, y = 190, width = 35)
    #Solo se pide para canal trapezoidal 
    long_vertedero_input = Entry(ventana3, textvariable = long_vertedero).place(x = 185, y = 210, width = 35)
    angulo_input = Entry(ventana3, textvariable = angulo).place(x = 185, y = 230, width = 35)
    n_input = Entry(ventana3, textvariable = n).place(x = 185, y = 250, width = 35)
    s_input = Entry(ventana3, textvariable = s).place(x = 185, y = 270, width = 35)
    cotaA_input = Entry(ventana3, textvariable = cota_A).place(x = 185, y = 290, width = 35)
    Qp_input = Entry(ventana3, textvariable = Qp).place(x = 185, y = 350, width = 35)
    yp_input = Entry(ventana3, textvariable = yp).place(x = 185, y = 370, width = 35)
    bp_input = Entry(ventana3, textvariable = bp).place(x = 185, y = 390, width = 35)
    zp_input = Entry(ventana3, textvariable = zp).place(x = 185, y = 410, width = 35)
    cotaB_input = Entry(ventana3, textvariable = cota_B).place(x = 185, y = 430, width = 35)
    
    Qs_input = Entry(ventana3, textvariable = Qs).place(x = 185, y = 490, width = 35)
    ys_input = Entry(ventana3, textvariable =  ys).place(x = 185, y = 510, width = 35)
    bs_input = Entry(ventana3, textvariable =  bs).place(x = 185, y = 530, width = 35)
    zs_input = Entry(ventana3, textvariable =  zs).place(x = 185, y = 550, width = 35)
    cotaC_input = Entry(ventana3, textvariable = cota_C).place(x = 185, y = 570, width = 35)

    #Label's para datos de salidas
    #Canal trapezoidal
    rotulo_trapezoidal = Label(ventana3,text = "RESULTADOS CANAL ENTRANTE TRAPEZOIDAL",font = ("arial",9,"bold")).place(x = 340,y = 100)
    vel_trape_rotulo = Label(ventana3,text = "Velocidad [V, m/s]").place(x = 350,y = 140) 
    ener_trape_rotulo = Label(ventana3,text = "Energía específica [E, m]").place(x = 350,y = 160)  
    ycrt_trape_rotulo = Label(ventana3,text = "Tirante crítico [yc, m]").place(x = 350,y = 180)
    ecrt_trape_rotulo = Label(ventana3,text = "Energía crítica [Ecrt, m]").place(x = 350,y = 200)  
    tirante_partidor_rotulo = Label(ventana3,text = "Tirante partidor [yp, m]").place(x = 350,y = 220) 
    long_transicion_rotulo = Label(ventana3,text = "Longitud transición [Lt, m]").place(x = 350,y = 240)  
    trans_pasante_rotulo = Label(ventana3,text = "Longitud transición pasante [Ltp, m]").place(x = 350,y = 260) 
    trans_saliente_rotulo = Label(ventana3,text = "Longitud transición saliente [Lts, m]").place(x = 350,y = 280)
    vel_trape_output = Entry(ventana3,textvariable = vel_trape).place(x = 560, y = 140, width = 35)
    ener_trape_output = Entry(ventana3,textvariable = ener_trape).place(x = 560, y = 160, width = 35)
    ycrt_trape_output = Entry(ventana3,textvariable = ycrt_trape).place(x = 560, y = 180, width = 35)
    ecrt_trape_output = Entry(ventana3,textvariable = ecrt_trape).place(x = 560, y = 200, width = 35)
    tirante_partidor_output = Entry(ventana3,textvariable = tirante_partidor).place(x = 560, y = 220, width = 35)    
    long_transicion_output = Entry(ventana3,textvariable = long_transicion).place(x = 560, y = 240, width = 35)
    trans_pasante_output = Entry(ventana3,textvariable = trans_pasante).place(x = 560, y = 260, width = 35)
    trans_saliente_output = Entry(ventana3,textvariable = trans_saliente).place(x = 560, y = 280, width = 35)

    #Canal rectangular
    asterisco = Label(ventana3,text = "*", fg = ("red"),font = ("bond")).place(x = 330,y = 320)
    rotulo_rectangular = Label(ventana3,text = "RESULTADOS CANAL ENTRANTE RECTANGULAR",font = ("arial",9,"bold")).place(x = 340,y = 320)
    vel_rect_rotulo = Label(ventana3,text = "Velocidad [V, m/s]").place(x = 350,y = 350) 
    ener_rect_rotulo = Label(ventana3,text = "Energía específica [E, m]").place(x = 350,y = 370)  
    ycrt_rect_rotulo = Label(ventana3,text = "Tirante crítico [yc, m]").place(x = 350,y = 390)  
    ecrt_rect_rotulo = Label(ventana3,text = "Energía crítica [Ecrt, m]").place(x = 350,y = 410)  
    froude_rect_rotulo = Label(ventana3,text = "No. Froude [F]").place(x = 350,y = 430)
    vel_rect_output = Entry(ventana3,textvariable = vel_rect).place(x = 560, y = 350, width = 35)
    ener_rect_output = Entry(ventana3,textvariable = ener_rect).place(x = 560, y = 370, width = 35)
    ycrt_rect_output = Entry(ventana3,textvariable = ycrt_rect).place(x = 560, y = 390, width = 35)
    ecrt_rect_output = Entry(ventana3,textvariable = ecrt_rect).place(x = 560, y = 410, width = 35)
    froude_rect_output = Entry(ventana3,textvariable = froude_rect).place(x = 560, y = 430, width = 35)
   
    #Partidor
    rotulo_partidor = Label(ventana3,text = "RESULTADOS PARTIDOR",font = ("arial",9,"bold")).place(x = 690, y = 100)
    angulo_movil_rotulo = Label(ventana3,text = "Ángulo de inclinación [º]").place(x = 640, y = 120)
    altura_vert_rotulo = Label(ventana3,text = "Altura vertedero [Hv, m]").place(x = 640, y = 140)  
    carga_partidor_rotulo = Label(ventana3,text = "Carga hidruálica [Hcrt, m]").place(x = 640, y = 160)  
    ancho_vert_rotulo = Label(ventana3,text = "Ancho vertedero [Wv, m]").place(x = 640, y = 180) 
    long_vert_rotulo = Label(ventana3,text = "Longitud Máxima vertedero [Lv, m]").place(x = 640, y = 200)  
    long_pasante_rotulo = Label(ventana3,text = "Ancho para Qp [b2, m]").place(x = 640, y = 220)  
    long_saliente_rotulo = Label(ventana3,text = "Ancho para Qs [b3, m]").place(x = 640, y = 240)  
    espesor_rotulo = Label(ventana3,text = "Profundida del colchón [Δz, m]").place(x = 640, y = 260)  
    long_colchon_rotulo = Label(ventana3,text = "Longitud del colchón [Lc, m]").place(x = 640, y = 280) 
    carga_pasante_rotulo = Label(ventana3,text = "Carga hidruálica [Hp, m]").place(x = 640, y = 300)  
    carga_saliente_rotulo = Label(ventana3,text = "Carga hidruálica [Hs, m]").place(x = 640, y = 320)
    cota1_rotulo = Label(ventana3,text = "Cota 1 [m]").place(x = 640, y = 340)
    cota2_rotulo = Label(ventana3,text = "Cota 2 [m]").place(x = 640, y = 360)
    cota3_rotulo = Label(ventana3,text = "Cota 3 [m]").place(x = 640, y = 380)
    cota4_rotulo = Label(ventana3,text = "Cota 4 [m]").place(x = 640, y = 400)
    cota5_rotulo = Label(ventana3,text = "Cota 5 [m]").place(x = 640, y = 420)
    
    angulo_movil_output = Entry(ventana3,textvariable = angulo_movil).place(x = 850, y = 120, width = 35)
    altura_vert_output = Entry(ventana3,textvariable = altura_vert).place(x = 850, y = 140, width = 35)
    carga_partidor_output = Entry(ventana3,textvariable = carga_partidor).place(x = 850, y = 160, width = 35)
    ancho_vert_output = Entry(ventana3,textvariable = ancho_vert).place(x = 850, y = 180, width = 35)
    long_vert_output = Entry(ventana3,textvariable = long_vert).place(x = 850, y = 200, width = 35)
    long_pasante_output = Entry(ventana3,textvariable = long_pasante).place(x = 850, y = 220, width = 35)
    long_saliente_output = Entry(ventana3,textvariable = long_saliente).place(x = 850, y = 240, width = 35)
    espesor_output = Entry(ventana3,textvariable = espesor).place(x = 850,  y = 260, width = 35)
    long_colchon_output = Entry(ventana3,textvariable = long_colchon).place(x = 850, y = 280, width = 35)
    carga_pasante_output = Entry(ventana3,textvariable = carga_pasante).place(x = 850, y = 300, width = 35)
    carga_saliente_output = Entry(ventana3,textvariable = carga_saliente).place(x = 850, y = 320, width = 35)
    cota1_output = Entry(ventana3,textvariable = cota_1).place(x = 850, y = 340, width = 35)
    cota2_output = Entry(ventana3,textvariable = cota_2).place(x = 850, y = 360, width = 35)
    cota3_output = Entry(ventana3,textvariable = cota_3).place(x = 850, y = 380, width = 35)
    cota4_output = Entry(ventana3,textvariable = cota_4).place(x = 850, y = 400, width = 35)
    cota5_output = Entry(ventana3,textvariable = cota_5).place(x = 850, y = 420, width = 35)

    #Separadores
    ttk.Separator(ventana3, orient = HORIZONTAL).place(relx = 0.03, rely = 0.12, relwidth = 0.66)
    ttk.Separator(ventana3, orient = HORIZONTAL).place(relx = 0.04, rely = 0.42, relwidth = 0.18)
    ttk.Separator(ventana3, orient = HORIZONTAL).place(relx = 0.04, rely = 0.60, relwidth = 0.18)
    ttk.Separator(ventana3, orient = HORIZONTAL).place(relx = 0.28, rely = 0.42, relwidth = 0.18)
    ttk.Separator(ventana3, orient = HORIZONTAL).place(relx = 0.28, rely = 0.60, relwidth = 0.18)
    ttk.Separator(ventana3, orient = HORIZONTAL).place(relx = 0.51, rely = 0.60, relwidth = 0.18)
    ttk.Separator(ventana3, orient = HORIZONTAL).place(relx = 0.72, rely = 0.60, relwidth = 0.24)
    ttk.Separator(ventana3, orient = VERTICAL).place(relx = 0.24, rely = 0.15, relheight = 1)
    ttk.Separator(ventana3, orient = VERTICAL).place(relx = 0.49, rely = 0.15, relheight = 0.45)
    ttk.Separator(ventana3, orient = VERTICAL).place(relx = 0.71, rely = 0.02, relheight = 0.58)

    #Condiciones para llevar a cabo el calculo
    Label(ventana3,text = "CONDICIONES DE DISEÑO",font = ("arial",11,"bold"),fg = ("black")).place(x = 990,y = 40) 
    Label(ventana3,text = "✔ No. Froude < 0.45 → Para garantizar flujo subcritico ",font = ("arial",9,)).place(x = 930,y = 70) 
    Label(ventana3,text = "    antes de la división de caudal",font = ("arial",9,)).place(x = 930,y = 90) 
    Label(ventana3,text = "✔ H1 ÷ H2 < 0.8 → Existe flujo libre en el canal pasante",font = ("arial",9,)).place(x = 930,y = 110) 
    Label(ventana3,text = "✔ H1 ÷ H3 < 0.8 → Existe flujo libre en el canal saliente",font = ("arial",9,)).place(x = 930,y = 130) 
    Label(ventana3,text = "✔ Hv < 0.3 → No es necesario determinar Lc y espesor",font = ("arial",9,)).place(x = 930,y = 150)
    Label(ventana3,text = "    del colchón amortiguador ya que Av es menor a 0.3 cm",font = ("arial",9,)).place(x = 930,y = 170)
    Label(ventana3,text = "✱", fg = ("red"),font = ("arial" , 9, )).place(x = 930,y = 220)
    Label(ventana3,text = "Cuando se elija un sección trasnversal trapezoidal",font = ("arial",9,)).place(x = 950,y = 220) 
    Label(ventana3,text = "aquí aparecera la información para el vertedero",font = ("arial",9,)).place(x = 950,y = 240) 
    Label(ventana3,text = "Nota:",fg = ("red"), font = ("arial",11, "bold")).place(x = 930,y = 270) 
    Label(ventana3,text = "Los esquemas de las secciones transversales se",font = ("arial",9,)).place(x = 976,y = 270) 
    Label(ventana3,text = "encuentran en el respectivo manual de usuario ",font = ("arial",9,)).place(x = 976,y = 290) 
    

    #Botones
    boton_calcular = Button(ventana3, text = "Calcular",command = partidor).place(x = 100,y = 620)
    boton_trapezoidal =  Radiobutton(ventana3, text = "Rectangular", variable = opcion, value = 1, font = ("Gabriola",14)).place(x = 190, y = 40)
    boton_rectangular = Radiobutton(ventana3,text = "Trapezoidal",variable = opcion, value = 2, font = ("Gabriola",14)).place(x = 310, y = 40)
    Radiobutton(ventana3,text = "Fijo",variable = tipo, value = 1, font = ("Gabriola",14)).place(x = 550, y = 40)
    Radiobutton(ventana3,text = "Movíl",variable = tipo, value = 2, font = ("Gabriola",14)).place(x = 650, y = 40)
    Label(ventana3, text = "TIPO DE PARTIDOR",font = ("arial",9,"bold")).place(x = 580,y = 20)
   
    #Imágenes en ventana 3 con label correspondientes
    imagen_partidor = PhotoImage(file = "partidor.png")
    imagen_parti = imagen_partidor.subsample(6) 
    partidor_planta = Label(ventana3, image = imagen_parti).place(x = 920, y = 460)
    Label(ventana3, text = "VISTA DE PERFIL",font = ("arial",9,"bold")).place(x = 320,y = 520)
    Label(ventana3, text = "Y PLANTA DEL",font = ("arial",9,"bold")).place(x = 320,y = 540)
    Label(ventana3, text = "DEL PARTIDOR",font = ("arial",9,"bold")).place(x = 320,y = 560)
    imagen_ppartidor = PhotoImage(file = "perfilPartidor.png")
    imagen_pparti = imagen_ppartidor.subsample(5) 
    partidor_perfil = Label(ventana3, image = imagen_pparti).place(x = 430, y = 470)


    ventana3.resizable(width=False, height=False)
    ventana3.mainloop()


##---------BOTONES Y LABEL--------
Mensaje= Label(interfaz, text= "DISEÑO DE ESTRUCTURAS HIDRÁULICAS:", font=("garamond",16)).place(x=200,y=230)
button1 = Button(interfaz, text="Vertedero pico de pato",font=("calibri",14),command=v2).place(x=200,y=310)
button2 = Button(interfaz, text="Partidor proporcional",font=("Calibri",14),command=v3).place(x=430,y=310)

#------------------------
#Para Pruebas. Quitar

def key(event):
    if str(event.char) == 'q' or str(event.char) == 'Q':
        interfaz.quit()


interfaz.bind("<Key>", key)

#------------------------

interfaz.mainloop()