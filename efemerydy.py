import numpy as np

"""Wyznaczenie efemeryd (pozycji  obiektu) na podstawie znanych elementow orbitalnych
   Dla parametrow orbity dla epoki 2000.0 podaje wspolrzednie RA DEC w 2000.0 """


def inter_M(M, e):
	""" Iteracyjne rozwiazanie rownan na E  - anomalie mimosrodowa"""
	eps = 1.e-6
	E0 = np.radians(M) + e*np.sin(np.radians(M))
	E1 = np.radians(M) + e*np.sin(E0)
	En = E1
	En_1 = E0
	while np.degrees(En) - np.degrees(En_1) > eps :
		En_1 = En
		En = np.radians(M) + e*np.sin(En_1)
	return En


######Jowisz #########

#Parametry orbity
a = 5.203363       # wielka polosc [AU]
e = 0.048393       # mimosrod
i = 1.30530        # inklinacja [deg] 
Omega = 100.55615  # wezel wstepujacy [deg]
PI = 14.75385      # dlugosc peryhelium [deg] ( omega + Omega)
L = 34.40438       # srednia dlugosc orbitalna L = anomalia srednia + dlugosc peryhelium
omega = PI - Omega # odleglosc perycentrum od wezla wstepujacego
#Inne paramerty
Pzwrot = 365.2422  # dlugosc roku zwrotnikowego
dT = 5918          # od 1 stycznia 2000 [d]
G = 6.67e-11       # SI stala grawitacji
Msol = 2.e30	   # masa slonca [kg]
MJ = 1.8986e27	   # masa planety (Jupiter) [kg]
eps = 23.439       # nachylenie osi Ziemi wzgl ekliptyki

#P = np.sqrt(4.*np.pi**2 * (a*1.496e11)**3/G/(MJ+Msol))  # period in seconds
P = (a) **(3./2.) * Pzwrot  # Period in days

""" mozna uwzgledniac precesje aby podac wspolrzedne w dowolnej epoce 
precesja = 0.2215
P = 365.2569/1.000025*(a)**(3./2.)
"""
########## Polozenie obiektu na orbicie ##############

l = L + dT/P * 360.   #prawdziwa dlugosc orbitalna
if l > 360. :
	l -=360.

M = l - PI            # anomalia srednia
E = inter_M(M,e)      # anomalia mimosrodowa
print np.degrees(E), M,l

#wspolrzednie (x,y) w plaszczyznie orbity w AU
x = a*(np.cos(E) - e)
y = a* np.sqrt(1.-e*e)*np.sin(E)

#obrot ukladu o -PI (os X wycelowana w punkt Barana) - wspolrzedne (X,Y) [AU] 
Pi = np.radians(PI)
M_PI = np.array([[np.cos(Pi), -np.sin(Pi)],[np.sin(Pi), np.cos(Pi)]])  #macierz obrotu o PI
X,Y = np.dot(M_PI,[x,y])  # wspolrzedne heliocentryczne w plaszczyznie ciala
print X,Y

######### Przejscie do ukladu heliocentrcznego rownikowego ############

#Macierz przejscia [[Px,Qx,Rx],[Py,Qy,Ry],[Pz,Qz,Rz]]
#zamiana parametrow orbity na radiany
omega_r = np.radians(omega)
Omega_r = np.radians(Omega)
i_r = np.radians(i)
eps_r = np.radians(eps)
#wspolczynniki macierzy przejscia

Px = np.cos()
