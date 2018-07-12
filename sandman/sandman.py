from datetime import *
import os
import platform
from pyfiglet import figlet_format

#-*- coding:utf-8 -*-

def convSeg(seg):
    timelist = [str((seg//3600)%24),str((seg//60)%60),str(seg%60),str((seg//86400))]
    for i in range(len(timelist)):
        if len(timelist[i]) < 2:
            timelist[i] = "0"+str(timelist[i])
    print("Seu computador ira desligar as: %s:%s:%s" %(timelist[0],timelist[1],timelist[2]))

print(figlet_format('SANDMAN', font='big')+"Você quer? (Insira o número)\n1. Desligar   |   2. Reiniciar   |   3. Deslogar   |   4. Cancelar")
modo = input().upper()

if modo == "1" or modo == "DESLIGAR":
    print("\n"+"=+"*29+"\nEntre em quanto tempo quer que o computador desligue,\nno seguinte formato: (horas:minutos:segundos) (03:45:00)\n")
    if platform.system() == "Linux":
        modo = ""
    elif platform.system() == "Windows":
        modo = "-s"
elif modo == "2" or modo == "REINICIAR":
    print("\n"+"=+"*29+"\nEntre em quanto tempo quer que o computador reinicie,\nno seguinte formato: (horas:minutos:segundos) (03:45:00)\n")
    if platform.system() == "Linux":
        modo = "-r"
    elif platform.system() == "Windows":
        modo = "-r"
elif modo == "3" or modo == "DESLOGAR":
    print("\n"+"=+"*29+"\nEntre em quanto tempo quer que o computador deslogue,\nno seguinte formato: (horas:minutos:segundos) (03:45:00)\n")
    if platform.system() == "Linux":
        os.system('exit')
        quit()
    elif platform.system() == "Windows":
        modo = "-l"
elif modo == "4" or modo == "CANCELAR":
    print("\n"+"=+"*29+"\nCancelado\n")
    if platform.system() == "Linux":
        os.system('shutdown -c')
    elif platform.system() == "Windows":
        os.system('shutdown -a')
    quit()

itempo = input().split(":")

segundos = (int(itempo[2]))+(int(itempo[1])*60)+(int(itempo[0])*3600)

agora = datetime.now().strftime('%H:%M:%S').split(":")
agora = (int(agora[2]))+(int(agora[1])*60)+(int(agora[0])*3600)

convSeg(agora+segundos)

comando = str('shutdown '+modo+" "+str(segundos))

os.system(comando)