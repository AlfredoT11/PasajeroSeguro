''' Reconocimiento facial '''
import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from skimage.color import rgb2gray
from skimage.transform import resize
import os

persona=1 #leer con serie
fotos=5
#total=persona
#muestras=fotos
def cargar_imagen(total,muestras):
#for i in range (1):
    Base=np.zeros([12000,muestras*total])
    for personas in range (total):
        Direccion=os.getcwd()+'/Photos'+str(personas)
        for fotos in range (muestras):
            Foto='/P'+str(fotos)+'.jpg'
            a=rgb2gray(io.imread(Direccion+Foto))
            a=resize(a, (120, 100), anti_aliasing=True)
            Base[:,(personas-1)*muestras+fotos]=a.flatten()
    w=np.uint8(Base*255)
    return w

bd=cargar_imagen(persona,fotos)

unos=np.ones([1,bd.shape[1]]);

media=np.matrix(np.mean(bd,axis=1))

BDP=bd-(media.T*unos)

#%% -----------Eigen faces & eigen values-------------- 

MC=(BDP.T).dot(BDP) #Matriz cuadrada compresa

Eval,Evec=np.linalg.eig(MC)

RE=BDP.dot(Evec)

car=10
[fil,col]=RE.shape

#MR=RE[:,RE[:,-1]:-1:RE[:,-1]-(car-1)]
Porciento=100

numcol=np.int(RE.shape[1]*Porciento/100)

eval=Eval

componente=[]
for i in range (numcol):
	pos=np.argmax(eval)
	componente.append(Evec[:,pos])
	eval[pos]=0
MR=np.array(componente)

patron=np.zeros([bd.shape[1],car])

for i in range(bd.shape[1]):
    patron[i,:]=(BDP[:,i].T).dot(MR)
    




#k=1; #%4 personas

#m=5; #%1 foto de cada persona (para pruebas)

#bd2=cargar_imagen(k,m);

#num=round((k*m)*rand(1,1));

#FA=bd2(:,num)