"""Task AI 4 Climate 

Q3/write a function that count how many the given character repeated in a given string?
"""

def get_count_of_char(string: str, char: str) -> int:
    """Get count how many the given character repeated in a given string"""
    return len([ i for i in string if i == char]) 



if __name__ == "__main__":

    test_string = "Hello Alaa in Computiq  *_*!!OMG!!*_*"
    repeated_char = get_count_of_char(test_string, "!")
    print(repeated_char)
