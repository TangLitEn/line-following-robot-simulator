def printAndWrite(output,file_path='output.txt',mode='a',newline=True):
     """
     Write the given output to a text file.
     Parameters:
     - output: The content to be written to the file.
     - mode: 'w' for write and 'a' for append
     - file_path: The path to the text file. Default is 'output.txt'.

     By fefault, the file will be in new line, unless otherwise stated
     """ 
     print(output)
     if newline:
        print("\n")
     writeToFile(output,file_path,mode)
    

def writeToFile(output,file_path='output.txt',mode='a'):
    """
    Write the given output to a text file.

    Parameters:
    - output: The content to be written to the file.
    - mode: 'w' for write and 'a' for append
    - file_path: The path to the text file. Default is 'output.txt'.
    """
    try:
        with open(file_path, mode) as file:
            file.write(output)
    except Exception as e:
        print(f"An error occurred: {e}")
