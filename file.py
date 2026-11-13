def sort_words_file(input_file,output_fle):
    try:
        with open(input_file,"r") as f:
          text=f.read()
        words=text.split()
        words=[word.lower() for word in words]
        words.sort()
        with open(output_fle,"w") as f:
          for word in words:
            f.write(word)
        print("Words sorted and written succesfully to ",output_file)
    except FileNotFoundError:
       print("Error :input file not found")
if __name__=="__main__": 
    input_file=input("Enter the source file path")
    output_file=input("Enter the output file path:")
    sort_words_file(input_file,output_file)      

        