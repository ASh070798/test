using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] Bags = new int[] { 4, 9, 3, 1, 6, 2, 5, 7, 8 }; // номера пакетов
            int max = Bags[0];
            int min = Bags[0];
            bool exist = false;
            max = Bags.Max();
            min = Bags.Min();
            for (int i = min+1; i < max; i++)
            {
                for (int j = 0; j < Bags.Length; j++)
                {
                    if (i == Bags[j])
                    {
                        exist = true;
                        break;
                    }
                    else
                        exist = false;
                }
                if (exist == false)
                {
                    Console.WriteLine("False!"); // не все пакеты дошли
                    return;
                }     
            }
            Console.WriteLine("Successfuly!"); // дошли все пакеты
        }
    }
}
