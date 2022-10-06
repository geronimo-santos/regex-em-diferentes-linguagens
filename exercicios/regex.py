import re

>>> resultado = re.search(r'\d\d\w','11a22b33c')
`

>>> resultado = re.search(r'(\d\d)\w','11a22b33c')
>>> resultado.group()
11a
>>> resultado.group(1)
11
>>>resultado.start()
0 
>>>resultado.end()
3

>>> resultados = re.finditer(r'(\d\d)\w','11a22b33c')
>>> for resultado in resultados:
...     print "%s com grupo %s [%s,%s]" % (resultado.group(), resultado.group(1),resultado.start(), resultado.end())
... 
11a com grupo 11 [0,3]
22b com grupo 22 [3,6]
33c com grupo 33 [6,9]

regex = re.compile(r'(\d\d)\w')
resultados = regex.finditer('11a22b33c')




# ============================================================================================
							# método findall

>>> import re

>>> regex = re.compile(r'(\d\d)(\w)')
>>> alvo = '11a22b33c'


>>> resultado = re.findall(regex, alvo)

>>> print resultado
[('11', 'a'), ('22', 'b'), ('33', 'c')]

>>> resultado[0]
('11', 'a')
>>> resultado[1]
('22', 'b')
>>> resultado[2]
('33', 'c')


>>> for grupo in resultado:
...     print grupo
... 
('11', 'a')
('22', 'b')
('33', 'c')



>>> for grupo in resultado:
...     print grupo[0] + grupo[1]
... 
11a
22b
33c

# ======================================================================================

					 	# Alterando o separador de uma data

>>> alvo = '2007-12-31'

>>> import re
>>> regex = '\s-\s'
>>> novotexto = ': '
>>> alura = 'Alura - Regex'
>>> resultado = re.sub(regex, novotexto, alura)



>>> print resultado
Alura: Regex


# Se queremos trocar todos os hífens por uma /, podemos fazer:

>>> import re
>>> regex = '-'
>>> novotexto = '/'
>>> alvo = '2007-12-31'
>>> resultado = re.sub(regex, novotexto, alvo)


>>> print resultado
2007/12/31

