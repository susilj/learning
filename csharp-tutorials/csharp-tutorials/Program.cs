using System;

namespace csharp_tutorials_v8
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            nullable_string nullableString = new nullable_string();
            nullableString.NullableString = "test";

            Console.WriteLine(nullableString.NullableString);
        }
    }
}
