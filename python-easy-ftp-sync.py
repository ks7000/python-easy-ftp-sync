from ftplib import FTP
ftp = FTP('192.168.1.47')
ftp.login('usuario','contraseña')
ftp.cwd('/home/jimmy/Descargas/BCV')

miLista = ftp.nlst()
archivo = open(miLista[0], 'wb')
ftp.retrbinary('RETR ' + miLista[0], archivo.write)
archivo.close()

ftp.close()
ftp = None
