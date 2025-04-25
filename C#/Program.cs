using System;
using System.Runtime.InteropServices;

class Program
{
    static void Main(string[] args)
    {
        Console.Clear();

        Console.WriteLine("---Programs---");

        Console.WriteLine("1 - Even or odd counter");
        Console.WriteLine("2 - Word reverser");

        Console.WriteLine("Select one: ");
        string cho = Console.ReadLine()!;

        int choice = int.Parse(cho);

        switch (choice)
        {
            case 1:
                Console.Clear();
                EvenOrOddCounter.Run();
                break;
            case 2:
                Console.Clear();
                wordReverser.Run();
                break;
            default:
                break;
        }
    }
}