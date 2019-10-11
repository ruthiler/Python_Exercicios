'''import math'''
from math import radians, sin, cos, tan

ang = float(input('Digite o Angulo: '))

'''print('O Seno do ângulo {:.1f}° é {:.2f}'.format(ang, math.sin(math.radians(ang))))
print('O Cosseno do ângulo {:.1f}° é {:.2f}'.format(ang, math.cos(math.radians(ang))))
print('A Tangente do ângulo {:.1f}° é {:.2f}'.format(ang, math.tan(math.radians(ang))))'''

print('O Seno do ângulo {:.1f}° é {:.2f}'.format(ang, sin(radians(ang))))
print('O Cosseno do ângulo {:.1f}° é {:.2f}'.format(ang, cos(radians(ang))))
print('A Tangente do ângulo {:.1f}° é {:.2f}'.format(ang, tan(radians(ang))))