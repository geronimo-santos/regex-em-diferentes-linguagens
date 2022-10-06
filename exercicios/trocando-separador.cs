//Se queremos trocar o separador - por /, podemos fazer:

string.Format("{0}{1}{2}{3}{4}", dia, separador1, mes, separador2, ano).Replace("-", "/");

//Com isso, a String ficará: 31/12/2007.

//O código completo:

using System.Text.RegularExpressions;

namespace Rextester
{
    public class Program
    {
        public static void Main(string[] args)
        {
           string alvo = "2007-12-31";
           Regex regexp = new Regex(@"(\d{4})(-)(\d{2})(-)(\d{2})");

            MatchCollection resultados = regexp.Matches(alvo);
            foreach(Match resultado in resultados)
            {

                string ano = resultado.Groups[1].Value;
                string mes = resultado.Groups[3].Value;
                string dia = resultado.Groups[5].Value;

                string separador1 = resultado.Groups[2].Value;
                string separador2 = resultado.Groups[4].Value;

                string novaData = string.Format("{0}{1}{2}{3}{4}", dia, separador1, mes, separador2, ano).Replace("-", "/");
                Console.WriteLine(novaData);
            }
        }
    }
}