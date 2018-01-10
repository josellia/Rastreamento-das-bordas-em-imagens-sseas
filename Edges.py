#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Imagens médicas em Python, uma aplicação por rastreamento das bordas em imagens ósseas


import cv2
from matplotlib import pyplot as plt


def imagem_ossea(x):
    pass

img_osso = cv2.imread('osso.jpg', 0)
img = cv2.GaussianBlur(img_osso,(5,5),0)#Aplicando filtro Gaussiano
canny_edge = cv2.Canny(img, 0, 0)

cv2.imshow('Osso', img)
cv2.imshow('canny_edge', canny_edge)
# Barra para o  rastreamento das bordas
cv2.createTrackbar('Var_minimo', 'canny_edge', 0, 500, imagem_ossea)
cv2.createTrackbar('Var_max', 'canny_edge', 0, 500, imagem_ossea)

while (True):
    cv2.imshow('Osso', img)
    cv2.imshow('canny_edge', canny_edge)

    valor_minimo = cv2.getTrackbarPos('Var_minimo', 'canny_edge')
    print("Mostrando valor min",valor_minimo)
    valor_max = cv2.getTrackbarPos('mVar_max', 'canny_edge')
    print("Mostrando valor max",valor_max)

    canny_edge = cv2.Canny(img, valor_minimo, valor_max)
    if cv2.waitKey(20) == ord('s'):  # Delay 20 milisegundos . Para sair aperte a letra s do teclado.
        break

