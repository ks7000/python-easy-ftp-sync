#    <python-easy-ftp-sync: synchronize two directories over FTP with Python.>
#    Copyright (C) <2020>  <Jimmy Olano🇻🇪>

#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

def sincronizaFTP(miServidorFTP, miUsuario, miContraseña, miCarpetaRemota, miCarpetaLocal, subir=False, bajar=True):

  print("\n-- Conectando y comparando carpetas ----\n")

  import os
  from ftplib import FTP

  if miCarpetaRemota[-1] != "/":
    miCarpetaRemota += "/"
  if miCarpetaLocal[-1] != "/":
    miCarpetaLocal += "/"
  if not os.path.exists(miCarpetaLocal):
    os.makedirs(miCarpetaLocal)

  ftp = FTP(miServidorFTP)
  ftp.login(miUsuario, miContraseña)
  ftp.cwd(miCarpetaRemota)
  miListaRemota = set(ftp.nlst())
  miListaLocal = set(os.listdir(miCarpetaLocal))

  paraSubir = miListaLocal - miListaRemota
  paraBajar = miListaRemota - miListaLocal
  vacio = set()

  if subir:
    print("\nPor cargar:\n ")
    if ( paraSubir == vacio ):
      print("Todos los archivos han sido cargados.\n")
    else:
      subidos = 0
      for fichero in paraSubir:
        print("  * Subiendo fichero:" + fichero)
        ftp.storbinary('STOR ' + fichero)
        subidos += 1

  if bajar:
    print("\nPor descargar:\n")
    if ( paraBajar == vacio ):
      print("Todos los archivos han sido descargados.\n")
    else:
      descargados = 0
      for fichero in paraBajar:
        print("  * Descargando fichero:" + fichero)
        archivo = open( miCarpetaLocal + fichero, 'wb')
        ftp.retrbinary('RETR ' + fichero, archivo.write)
        archivo.close()
        descargados += 1

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
