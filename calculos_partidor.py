import json
import math
import numpy as np


#Calculo del tirante critico por medio de la Ec. Manning
def tirante_crt_trape(Q, b, z):
    cte_yc = Q / (9.81**0.5)
    yo = 1
    yc = 2
    cont = 1
    error = 0.000000001
    
    while abs(yo - yc) > error:
        yo = yc
        area = (b + z*yo) * yo
        ancho_superficial = b + (2*z*yo) 
        fc = (area**(3/2) / ancho_superficial**(1/2)) - cte_yc
        d_area = b + 2*z*yo
        d_ancho_superficial = 2*z
        dfc = (((3/2) * (area / ancho_superficial)**0.5) * d_area) - (((1/2) * (area / ancho_superficial)**(3/2)) * d_ancho_superficial)
        yc = yo - fc/dfc
        cont += 1
    
        if cont > 40:
            break
    return yc


def calculo_partidor(Q, y, b, z, ancho, n, cota_A, s, Qp, yp, bp, zp, Qs, ys, bs, zs, angulo, cota_B, cota_C):
    array_return = {}
    gravedad = 9.81
    area = (b + z*y)*y
    super_libre = b + 2*z*y

    #Calculos del canal entrante para canal trapezoidal
    es_trapezoidal = False
    if z != 0:
        es_trapezoidal = True
        vel_trape = Q / area
        ener_trape = y + vel_trape**2 / (2*gravedad)
        tirante = tirante_crt_trape(Q, b, z)
        ener_crt = tirante * 3/2
        
        #Calculo transición de canal trapezoidal a canal rectangular
        espejo_1 = b + 2*z*y
        espejo_2 = b
        grados = angulo*math.pi / 180
        long_transicion1 = (espejo_1 - espejo_2) / (math.tan(grados)*2)

        #Calculo del nuevo tirante despues de la transición
        D = 1
        C = - ener_trape
        B = 0
        A = Q**2 / (ancho**2 * 2*gravedad)
        coeficientes = [D, C, B, A]
        raices = np.roots(coeficientes)
        tirante_partidor = max(raices)

        array_return['vel_trape'] = round(vel_trape, 3)
        array_return['ener_trape'] = round(ener_trape, 3)
        array_return['tirante_crt'] = round(tirante, 3)
        array_return['ener_crt'] = round(ener_crt, 3)
        array_return['long_transicion1'] = round(long_transicion1, 3)
        array_return['tirante_partidor'] = round(tirante_partidor, 3)

        #Datos después de la transición
        y = tirante_partidor
        z = 0
        area = (b + z*y)*y

    #Calculos del canal entrante para canal rectangular
    velocidad = Q / area
    prof_hidraulica = area / super_libre
    numero_froude = velocidad / (gravedad * prof_hidraulica) ** 0.5
    q_unitario = Q / b
    tirante_critico = (q_unitario**2 / gravedad) ** (1/3)
    energia_critica = tirante_critico * 3/2
    energia_especifica = y + velocidad**2 / (2*gravedad)
    #Calculos del partidor
    altura_verte = energia_especifica - energia_critica
    carga_hidrau = 1.5 * tirante_critico
    ancho_verte = 3.5 * tirante_critico
    long_vertedero = 10 * tirante_critico #máxima
    long_pasante = (Qp / Q) * b
    long_saliente = (Qs / Q) * b

    #Colchon del partidor
    if altura_verte > 0.3:
        espesor = altura_verte / 3
        num_caida = q_unitario**2 / (gravedad * altura_verte**3)
        y1 = 0.54 * altura_verte * num_caida**0.425
        y2 = 1.66 * altura_verte * num_caida**0.27
        long_d = 4.30 * altura_verte * num_caida**0.27
        long_resalto = 5 * (y2 - y1)
        long_colchon = long_d + long_resalto
        cota_3 = cota_A - espesor
        array_return['espesor'] = round(espesor, 3)
        array_return['long_colchon'] = round(long_colchon, 3)
        array_return['cota_3'] = round(cota_3, 3)

    #Perdias en canales pasante y saliente
    area_pasante = (bp + zp*yp)*yp
    vel_pasante = Qp / area_pasante
    carga_pasante = yp + (vel_pasante**2)/(2*gravedad)
    total_pasante =  carga_hidrau / carga_pasante
    
    area_saliente = (bs + zs*ys)*ys
    vel_saliente = Qs / area_saliente
    carga_saliente = ys + (vel_saliente**2)/(2*gravedad)
    total_saliente =  carga_hidrau / carga_saliente

    #Cotas
    cota_1 = cota_A + altura_verte + carga_hidrau
    cota_2 = cota_A + altura_verte + tirante_critico
    cota_4 = cota_B + carga_pasante
    cota_5 = cota_C + carga_saliente

    #Longitudes de la estructura
    long_hoja = 10 * tirante_critico
    long_estructura = 37 * tirante_critico

    #Calculo transición de canal rectangular a canal trapezoidal
    if es_trapezoidal:
        espejo_qpasante = long_pasante
        espejo_qsaliente = long_saliente

        espejo_pasante = bp + 2*zp*yp
        espejo_saliente = bs + 2*zs*ys
        grados = angulo*math.pi / 180
        long_transpa = (espejo_pasante - espejo_qpasante) / (math.tan(grados)*2)
        long_transsa = (espejo_saliente - espejo_qsaliente) / (math.tan(grados)*2)
        array_return['long_transpa'] = round(long_transpa, 3)
        array_return['long_transsa'] = round(long_transsa, 3)


    array_return['velocidad'] = round(velocidad, 3)
    array_return['numero_froude'] = round(numero_froude, 3)
    array_return['tirante_critico'] = round(tirante_critico, 3)
    array_return['energia_critica'] = round(energia_critica, 3)
    array_return['energia_especifica'] = round(energia_especifica, 3)
    array_return['altura_verte'] = round(altura_verte, 3)
    array_return['carga_hidrau'] = round(carga_hidrau, 3)
    array_return['ancho_verte'] = round(ancho_verte, 3)
    array_return['max_vertedero'] = round(long_vertedero, 3)
    array_return['long_pasante'] = round(long_pasante, 3)
    array_return['long_saliente'] = round(long_saliente, 3)
    array_return['total_pasante'] = round(total_pasante, 3)
    array_return['total_saliente'] = round(total_saliente, 3)
    array_return['carga_pasante'] = round(carga_pasante, 3)
    array_return['carga_saliente'] = round(carga_saliente, 3)
    array_return['cota_1'] = round(cota_1, 3)
    array_return['cota_2'] = round(cota_2, 3)
    array_return['cota_4'] = round(cota_4, 3)
    array_return['cota_5'] = round(cota_5, 3)
    array_return['long_hoja'] = round(long_hoja, 3)
    array_return['long_estructura'] = round(long_estructura, 3)


    return array_return

def partidor_movil(Q, y, b, z, ancho, n, cota_A, s, Qp, yp, bp, zp, Qs, ys, bs, zs, angulo, cota_B, cota_C):
    array_return1 = {}
    partidor_fijo = calculo_partidor(Q, y, b, z, ancho, n, cota_A, s, Qp, yp, bp, zp, Qs, ys, bs, zs, angulo, cota_B, cota_C)
    ancho_pasante = partidor_fijo['long_pasante']
    hipotenusa = partidor_fijo['long_hoja']
    localizacion_hoja = b/2

    if ancho_pasante > localizacion_hoja:
        faltante = ancho_pasante - localizacion_hoja
    else:
        faltante = localizacion_hoja - ancho_pasante
    
    angulo_alfa = math.asin(faltante/hipotenusa)
    grados_alfa = angulo_alfa* 180 / math.pi
    angulo_final = 90 - grados_alfa
    carga_movil = (Q / (1.235*hipotenusa))**(2/3)
    
    array_return1['angulo_final'] = round(angulo_final, 3)
    array_return1['carga_movil'] = round(carga_movil, 3)
    

    return array_return1