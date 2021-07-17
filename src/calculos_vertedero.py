import math
c=0.40
C=1.6

## Parámetros canal Rectangular:
error = 0.000000001
def parametrosRect(qCalc,nCalc,pendienteCalc,bCalc,HcCalc):
## tirante normal y1
    cte = (qCalc*nCalc) / (pendienteCalc**0.5)
    yi = 1
    y1 = 2
    cont = 1
    while abs(yi - y1) > error:
        yi = y1
        area = bCalc*yi 
        perimetro = bCalc+ 2*yi 
        fy = (area**(5/3) / perimetro**(2/3)) - cte
        d_area = bCalc
        d_perimetro = yi
        dfy = (((5/3)*area**(2/3)/perimetro**(2/3))*d_area) - (((2/3)*area**(5/3) / perimetro**(5/3)) * d_perimetro)
        y1 = yi - fy/dfy
        cont += 1
        if cont > 40:
            break    
## parámetros: velocidad, borde libre y número de Froude
    vel=qCalc/area
    borde_libre = HcCalc - y1
    froude=vel/(9.81*y1)**0.5
## tirante crítico yc
    yc= ((qCalc/bCalc)**2 / 9.81)**(1/3)
  
    return y1, vel,borde_libre,froude,yc

error = 0.000000001
## Parámetros canal trapezoidal:
def parametrosTrap(qCalc,nCalc,pendienteCalc,bCalc,zCalc,HcCalc):
 
    # global q
    # global pendiente
    # global b
    # global z
    # global Hd
    # global n
## tirante normal y1
    cte = (qCalc*nCalc) / (pendienteCalc**0.5)
    yi = 1
    y1 = 2
    cont = 1
    while abs(yi - y1) > error:

        yi = y1
        area = bCalc*yi + zCalc*yi**2
        perimetro = bCalc+ 2*yi *(1 + zCalc**2)**0.5 
        fy = (area**(5/3) / perimetro**(2/3)) - cte
        d_area = bCalc + 2*zCalc*yi
        d_perimetro = 2 * (1 + zCalc**2)**0.5
        dfy = (((5/3)*area**(2/3)/perimetro**(2/3))*d_area) - (((2/3)*area**(5/3) / perimetro**(5/3)) * d_perimetro)
        y1 = yi - fy/dfy
        cont += 1
        if cont > 40:
            break
## parámetros: velocidad, borde libre y número de Froude
    vel=qCalc/area
    borde_libre = HcCalc - y1
    froude= vel/(9.81*(bCalc*y1+zCalc*y1**2)/(bCalc+2*zCalc*y1))**0.5
## tirante crítico yc
    cte_yc = qCalc / (9.81**0.5)
    yo = 1
    yc = 2
    cont = 1
    
    while abs(yo - yc) > error:
        yo = yc
        area = bCalc*yo + zCalc*yo**2
        ancho_superficial = bCalc + (2*zCalc*yo) 
        fc = (area**(3/2) / ancho_superficial**(1/2)) - cte_yc
        d_area = bCalc + 2*zCalc*yo
        d_ancho_superficial = 2*zCalc
        dfc = ((((3/2) * (area / ancho_superficial)**0.5) * d_area) - (((1/2) * (area / ancho_superficial)**(3/2)) * d_ancho_superficial))
        yc = yo - fc/dfc
        cont += 1
    
        if cont > 40:
            break
       
    return y1,vel,borde_libre, froude,yc



####### Diseño  vertedero
def DisVertedero(y1,HdCalc, qCalc, bCalc, zCalc):
    
       #tirante_normal(q, n, s, b, z)
    S= round(y1-HdCalc,3)
    qunitario=round((1/0.7246)**(1/0.6704)*(HdCalc*100)**(1/0.6704),2)
    T= bCalc +2*zCalc*S
    Lt=round(qCalc/(qunitario/1000),3)
    L1= round((Lt-c)/2,3)  #A
    a=(T-c)/2 
    L3=round(abs((bCalc-T)/2),3) #H
    Aa=a/L1
    Angulo= round(math.acos(Aa),3)
    Ang= math.degrees(Angulo)
    Qv= round((C*Lt*HdCalc**(3/2)),3)
    Vv= round((qCalc/(HdCalc*Lt)),3)

    return S,T,Lt,L1,L3,Ang,Qv,Vv
        ## tirante final
def Cotas (caCalc,HdCalc, S):

    ca=caCalc
    cb = caCalc+S+HdCalc
    cc= ca+S
    cd= ca-HdCalc
    L2= 0.40

    return ca, cb, cc, cd, L2
    
def y2_Desnivelrec(Qv,nCalc,pendienteCalc,bCalc,y1,qCalc,HdCalc):
## tirante final y2 
    cte = (Qv*nCalc) / (pendienteCalc**0.5)
    yi = 1
    y2 = 2
    cont = 1
    while abs(yi - y2) > error:
        yi = y2
        area = bCalc*yi 
        perimetro = bCalc + 2*yi 
        fy2 = (area**(5/3) / perimetro**(2/3)) - cte
        d_area = bCalc 
        d_perimetro = yi
        dfy = (((5/3)*area**(2/3)/perimetro**(2/3))*d_area) - (((2/3)*area**(5/3) / perimetro**(5/3)) * d_perimetro)
        y2 = round(yi - fy2/dfy,3)
        cont += 1
        if cont > 40:
            break

## Energía específica
    Energia1= y1+((qCalc**2)/(2*9.81*(bCalc*y1)**2))
    Energia2= y2+((Qv**2)/(2*9.8*(bCalc*y2)**2))
    dif= Energia1-Energia2
    if (dif < HdCalc):
        desnivel=HdCalc

    else:
        desnivel=0
    
    return y2, Energia1, desnivel
def y2_DesnivelTrap(Qv,nCalc,pendienteCalc,bCalc,zCalc,y1,qCalc,HdCalc):
## tirante final y2
    cte = (Qv*nCalc) / (pendienteCalc**0.5)
    yi = 1
    y2 = 2
    cont = 1
    while abs(yi - y2) > error:
        yi = y2
        area = bCalc*yi + zCalc*yi**2
        perimetro = bCalc + 2*yi *(1 + zCalc**2)**0.5 
        fy2 = (area**(5/3) / perimetro**(2/3)) - cte
        d_area = bCalc + 2*zCalc*yi
        d_perimetro = 2 * (1 + zCalc**2)**0.5
        dfy = (((5/3)*area**(2/3)/perimetro**(2/3))*d_area) - (((2/3)*area**(5/3) / perimetro**(5/3)) * d_perimetro)
        y2 = yi - fy2/dfy
        cont += 1
        if cont > 40:
            break
    
## Energía específica
    Energia1= y1+((qCalc**2)/(2*9.8*(bCalc*y1+bCalc*y1**2)**2))
    Energia2= y2+((Qv**2)/(2*9.8*(bCalc*y2+bCalc*y2**2)**2))
    dif= Energia1-Energia2
    if (dif < HdCalc):
        desnivel=HdCalc

    else:
        desnivel=0
     
    return y2,Energia1,desnivel

