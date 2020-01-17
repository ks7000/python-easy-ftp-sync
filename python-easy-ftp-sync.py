import os
from ftplib import FTP

miServidorFTP = "192.168.1.47"
miUsuario = "usuario"
miContraseña = "contraseña"
miCarpetaRemota = "/home/jimmy/Descargas/BCV"
miCarpetaLocal = "/home/kevin/Descargas/BCV"

ftp = FTP(miServidorFTP)
ftp.login(miUsuario, miContraseña)
ftp.cwd(miCarpetaRemota)
miListaRemota = ftp.nlst()
print(miListaRemota)

miListaLocal = set(os.listdir(miCarpetaLocal))
print(miListaLocal)

ftp.close()
ftp = None
