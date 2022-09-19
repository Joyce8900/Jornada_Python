from random import randint




class Celular:
  def __init__(self, fabricante, modelo, tela, armazenamento, camera, bateria, tela_ligada, memoria):
      self.fabricante = fabricante
      self.modelo = modelo
      self.tela = tela
      self.armazenamento = armazenamento
      self.camera = camera
      self.bateria = bateria
      self.tela_ligada = tela_ligada
      self.memoria = memoria

  def ligar_tela(self):
    self.tela_ligada = True
  def verificar_carga_bateria(self):
    self.bateria = int(randint (0,2651))

class CelularAndroid:
  pass

class CelularIphone:
  pass

celular_android = Celular("Xiaomi","Redmi 11",6.4,128,50,6400,False, 6) 


celular_Iphone = Celular (
  fabricante="Apple",modelo="Iphone 13 Pro Max",tela=5.75,
  armazenamento=128,memoria=3, camera=16,bateria=2650,tela_ligada=False)


celular_Iphone.ligar_tela()
celular_android.verificar_carga_bateria()
print (f"A carga da sua bateria é: {celular_android.bateria}mA restantes, sua porcetangem é de: {int((celular_android.bateria*100)/2650)}% ")



