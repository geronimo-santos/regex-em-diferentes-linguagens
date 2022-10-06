$regexp = '~(\d\d)(\w)~';

$alvo = '12a34b56c';
$achou = preg_match($regexp, $alvo, $match);

> echo $match[0];
12a
> echo $match[1];
12
> echo $match[2];
a

$achou = preg_match($regexp, $alvo, $match, PREG_OFFSET_CAPTURE);

print_r($match);
Array
(
[0] => Array
(

[0] => 12a

[1] => 0

)

[1] => Array

(

[0] => 12

[1] => 0

)

[2] => Array

(

[0] => a

[1] => 2

)
)

> echo $match[2][1]; //inicio do segundo grupo a
2

$achou = preg_match_all($regexp, $alvo, $matches);

> echo $matches[0][0];
12a
> echo $matches[0][1];
34b
> echo $matches[0][2];
56c

> echo $matches[1][0];
12
> echo $matches[2][0];
a


<!-- Na função preg_match_all, também existe o parâmetro PREG_OFFSET_CAPTURE, para receber os índices. Nesse caso será criado um array de 3 dimensões. -->





$string = '2007-12-31';



$string = 'Setembro 21';
$regex = '~(\w+)\s(\d+)~';
$novoTexto = '$2 de $1';

$resultado = preg_replace($regex, $novoTexto, $string);
echo $resultado; // 21 de Setembro

$string = '2007-12-31';
$regex = '~(\d{4})-(\d{2})-(\d{2})~';

$novoTexto = '$3-$2-$1';

$resultado =  preg_replace($regex, $novoTexto, $string);


$string = '2007-12-31';
$regex = '~(\d{4})-(\d{2})-(\d{2})~';
$novoTexto = '$3-$2-$1';
$resultado =  preg_replace($regex, $novoTexto, $string);

echo $resultado;


<!-- trocando / -->

$string = '31-12-2007';
$regex = '~-~';
$novoTexto = '/';
$resultado =  preg_replace($regex, $novoTexto, $string);
echo $resultado; // 31/12/2007