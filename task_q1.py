"""Task AI 4 Climate 

Q1/Write a method that will remove any given character from a String ? 
"""
def remove_charcater_from_string(string: str, char: str):

    #==+_+==># string.replace(char, "") 
    return "".join([c for c in string if c != char])


if __name__ == "__main__":
    
    test_string = "Hello Alaa in Computiq  *_*!!OMG!!*_*"
    new_string = remove_charcater_from_string(test_string, "q")

    print(new_string)

