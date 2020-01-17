from ftplib import FTP
ftp = FTP('192.168.1.47')
ftp.login('usuario','contraseña')
ftp.cwd('/home/jimmy/Descargas')
ftp.dir()
ftp.quit()
