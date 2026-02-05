def countVowels(seq):
    count = 0

    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    for i in range(len(seq)):
        if seq[i] in vowels:
            count += 1

    print("Number of vowels in the given string is: ", count)

countVowels('abcA')
countVowels(['a','ab','A','I'])

def Check_Vow(string, vowels):
	final = [i for i in string if i in vowels]
	print(len(final))
	print(final)

string = "so cool"
vowels = "AaEeIiOoUu"
Check_Vow(string, vowels);

