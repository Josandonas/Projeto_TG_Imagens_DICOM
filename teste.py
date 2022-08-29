import pydicom
import matplotlib.pyplot as plt
import os
# pip install python-gdcm
# pip install matplotlib
# pip install pydicom
ds = pydicom.dcmread("1.2.392.200036.9116.2.6.1.44063.1805388139.1661100477.736601.mdt.DCM")
print(ds.SeriesDescription)
# plt.imshow(ds.pixel_array, cmap=plt.cm.bone)
# plt.show()
from pydicom import dcmread

pasta = 'muda aqui pro caminho'
for diretorio, subpastas, arquivos in os.walk(pasta, topdown=False):
    for arquivo in arquivos:         
        if arquivo.endswith('.DCM'):
            arqDicom = dcmread(arquivo)
            tag = arqDicom.SeriesDescription            
            if 'OSSO Bone ' in tag:
                print(arqDicom.SeriesDescription)
                #print('true')
                print('Excluindo arquivo', arquivo)
                os.remove(arquivo)
# teste 1 (célio)