//Como podemos fazer para trocar o separador - por /?
"Caelum".replaceAll("[Cm]", "*") //*aelu* ---Ex:---

//Se queremos trocar o separador - por /, podemos fazer:

novaData.replaceAll("-", "/");
//Mas como String é imutável, precisamos atribuir o resultado do replaceAll (que é uma nova string) para a novaData:

novaData = novaData.replaceAll("-", "/");
//Com isso, a String ficará: 31/12/2007.

 

