def words_count(filename):
    try:
        with open (filename,"r") as f:
            text=f.read()
        num_chars=len(text)
        num_words=len(text.split())
        with open (filename,"r") as f:
            num_lines=len(f.readlines())
        print("Number of characters:",num_chars)
        print("Number of words:",num_words)
        print("Number of lines:",num_lines)
    except FileNotFoundError:
        print("Error:file not found")
if __name__=="__main__":
    file_name=input("Enter the file name:")
    words_count(file_name)