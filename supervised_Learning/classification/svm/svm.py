# IMPLEMENTATION SVM


import numpy as np 
import pandas as pd 
from  sklearn.model_selection import train_test_split
from sklearn import svm
import matplotlib.pyplot as plt

class SVM:
    
    def __init__(self,epoch,alpha,batch_size,num_classes_,num_feactures,svm_c): 
        
        """
        parametros
        ---------

        
        alpha(float) : tasa de aprendizaje 
        batch_size(int) : Numero de muestras para el uso de training y testing
        svm_c(float): penalizacion del parametro 
        num_class(int) : numero de clases que tiene el dataset
        num_feactures(int) : numero de feactures que tiene el dataset.
        """
        self.epoch = epoch
        self.alpha = alpha
        self.batch_size = batch_size 
        self.num_class = num_classes_ 
        self.num_feactures = num_feactures 
        self.svm_c = svm_c

        self.time_stamp = [] #Guarda cada opoca, sirve para poder graficar
        self.time_loss = []   #Guarda funcion de perdida en cada epoca


    def hipotesis(self):
        pass


    def fun(self):
        pass

    def loss(self):
        pass

    def derivates(self):
        pass

    def update_parameters(self):
        pass
    
    def train(self,x,y):
        pass

    def plot_loss(self):
        pass

    
    def plot3d(self):
        pass