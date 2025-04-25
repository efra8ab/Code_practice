//Write a program that asks the user to input 10 integers. 
//Your program should count and display:

//How many of the integers are even
//How many of the integers are odd

using System;
using System.Runtime.InteropServices;

public class EvenOrOddCounter
{
    public static void Run()
    {
        while (true)
        {
            Console.Clear();

            Console.WriteLine("Welcome to the Even or odd counter");

            int evenCount = 0;
            int oddCount = 0;
            List<int> numbers = new List<int>();

            for (int i = 0; i < 10; i++)
            {
                Console.Write($"Enter number {i + 1}: ");
                int number = int.Parse(Console.ReadLine()!);
                numbers.Add(number);

                if (number % 2 == 0)
                {
                    evenCount += 1;
                }
                else
                    oddCount += 1;
            }

            Console.WriteLine($"You entered {oddCount} odd numbers and {evenCount} even numbers");
            Console.Write("Do you wish to play again? y/n :");

            string choice;
            choice = Console.ReadLine()!;

            if (choice != "y")
            {
                break;
            }
        }        
    }
}



