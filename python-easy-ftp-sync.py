def sincronizaFTP(miServidorFTP, miUsuario, miContraseña, miCarpetaRemota, miCarpetaLocal, subir=False, bajar=True):

  print("\n-- Conectando y comparando carpetas ----\n")

  import os
  from ftplib import FTP

  ftp = FTP(miServidorFTP)
  ftp.login(miUsuario, miContraseña)
  ftp.cwd(miCarpetaRemota)
  miListaRemota = set(ftp.nlst())
  miListaLocal = set(os.listdir(miCarpetaLocal))

  paraBajar= miListaRemota - miListaLocal
  paraSubir = miListaLocal - miListaRemota
  vacio = set()

  print("\nPor descargar:\n ")
  if ( paraBajar == vacio ):
    print("Todos los archivos han sido descargados.\n")
  else:
    print(paraBajar)

  print("\nPor cargar:\n")
  if ( paraSubir == vacio ):
    print("Todos los archivos han sido cargados.\n")
  else:
    print(paraSubir)

  ftp.close()
  ftp = None

if __name__ == '__main__':
  ServidorFTP = "192.168.1.47"
  Usuario = "usuario"
  Contraseña = "contraseña"
  CarpetaRemota = "/home/jimmy/Descargas/BCV"
  CarpetaLocal = "/home/kevin/Descargas/BCV"
  Cargar = False
  Descargar = True
  sincronizaFTP(ServidorFTP, Usuario, Contraseña, CarpetaRemota, CarpetaLocal, Cargar, Descargar)
