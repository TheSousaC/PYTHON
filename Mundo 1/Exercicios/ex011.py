#Pintar a parede

Altura = float(input('Qual a altura da parede?' ))
Largura = float(input('Qual a largura da parede? '))

Area = Altura * Largura

Litros_Tinta = Area / 2

print('A sua parede tem {:.2f}m² e precisará de {:.2f}L de tinta para ser completamente pintada'.format(Area, Litros_Tinta))