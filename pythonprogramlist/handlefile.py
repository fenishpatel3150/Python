def read_file(path):
    try:
        with open(path,'w') as f:
            print("File content:")
            f.write('hello bro')
    except FileNotFoundError:
        print(f"File '{path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

path = input('Enter file name: ')
read_file(path)