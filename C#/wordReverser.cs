// Write a program that asks the user to input a sentence, 
// and then prints each word in reverse order, not reversed letters.

using System;

public class wordReverser
{
    public static void Run()
    {
        while (true)
        {
            Console.Clear();
            Console.Write("Write a sentence: ");
            string sentence = Console.ReadLine()!;

            List<string> words = new List<string>(sentence.Split(" ", StringSplitOptions.RemoveEmptyEntries));
            words.Reverse();

            Console.WriteLine("\nHere is your reversed sentence:");
            Console.WriteLine(string.Join(" ", words));

            Console.Write("\nDo you wish to play again? y/n :");

            string choice;
            choice = Console.ReadLine()!;

            if (choice != "y")
            {
                break;
            }
        }
    }
}