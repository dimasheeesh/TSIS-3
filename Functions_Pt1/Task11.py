def is_palindrome(word):
    # Remove spaces and convert to lowercase
    word = word.replace(" ", "").lower()
    return word == word[::-1]

def main():
    word = input("Enter a word or phrase: ")
    if is_palindrome(word):
        print("The word or phrase is a palindrome.")
    else:
        print("The word or phrase is not a palindrome.")

if __name__ == "__main__":
    main()
