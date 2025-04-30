// Ask the user to input a sentence. 
// Count how many times each word appears and display the frequency of each word.
using System;
using System.Text.RegularExpressions;

public class countingWords
{
    public static void run()
    {
        while (true)
        {
            Console.Clear();

            Console.WriteLine("Input: ");
            string? input = Console.ReadLine();

            input = input?.ToLower();
            input = Regex.Replace(input, "[^a-z0-9 ]", "");

            List<string> sentence = new List<string>();

            if (input != null)
            {
                sentence.AddRange(input.Split(' ', StringSplitOptions.RemoveEmptyEntries));
            }

            Dictionary<string, int> wordCount = new Dictionary<string, int>();
            foreach (var word in sentence)
            {
                if (wordCount.ContainsKey(word))
                {
                    wordCount[word]++;
                }
                else
                {
                    wordCount[word] = 1;
                }
            }

            Console.WriteLine("Word frequency");
            foreach (var pair in wordCount)
            {
                Console.WriteLine($"{pair.Key}: {pair.Value}");
            }
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
