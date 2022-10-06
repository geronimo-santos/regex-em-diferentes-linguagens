regex = /(\d\d)(\w)/

alvo = "11a22b33c"
resultado = regex.match(alvo)

puts resultado[0]
"11a"

puts resultado[1]
"11"
puts resultado[2]
"a"

puts resultado.begin 2 #inicio do grupo a
2
puts resultado.end 2 #fim do grupo a
3

> resultado.begin 0 #inicio do match inteiro 11a
0
> resultado.begin 1 #inicio do grupo 11
0
> resultado.end 0 #fim do match inteiro 11a
3
> resultado.end 1 #fim do grupo 11
2





> regex = /(\d\d)(\w)/ #dois grupos
> alvo = "12a34b56c"
> resultados = alvo.scan regex
=> [["12", "a"], ["34", "b"], ["56", "c"]]

> resultados[2][1]
=> "c"