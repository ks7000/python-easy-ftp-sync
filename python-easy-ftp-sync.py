from ftplib import FTP

miServidorFTP = "192.168.1.47"
miUsuario = "usuario"
miContraseña = "contraseña"
miCarpetaRemota = "/home/jimmy/Descargas/BCV"

ftp = FTP(miServidorFtp)
ftp.login(miUsuario, miContraseña')
ftp.cwd(miCarpetaRemota)

miLista = ftp.nlst()
archivo = open(miLista[1], 'wb')
ftp.retrbinary('RETR ' + miLista[1], archivo.write)
archivo.close()

ftp.close()
ftp = None
