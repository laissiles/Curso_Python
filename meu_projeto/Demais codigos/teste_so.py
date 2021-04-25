import platform
import getpass
from datetime import datetime



print ("nome da maquina...", platform.node())
print ("Arquitetura", platform.architecture())
print ("Versão SO",platform.release())
print ("Data", datetime.now())

print(getpass.getuser())
print(getpass.getpass("Diigte sua senha: "))