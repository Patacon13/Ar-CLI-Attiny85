import os
nombre = input("Ingrese nombre de archivo a compilar ")
nombreSalida = input("Ingrese el nombre del archivo compilar: ")
#cmd = 'md compilado & DEL .\compilado\\' + nombre+'.c /Q & DEL .\compilado\\'+nombre+'.ino /Q & copy .\\'+nombre+'.c .\compilado\\compilado.ino & cls & arduino-cli compile --fqbn arduino:avr:uno compilado & pause & exit'
cmd = 'md '+nombreSalida+' & DEL .\\'+nombreSalida+'\\' + nombreSalida+'.c /Q & DEL .\\'+nombreSalida+'\\'+nombreSalida+'.ino /Q & copy .\\'+nombre+'.c .\\'+nombreSalida+'\\'+nombreSalida+'.ino & cls & arduino-cli compile --fqbn attiny:avr:ATtinyX5 '+nombreSalida+' & pause & exit'
os.system(cmd)
