# Create context manager for working with files
# Open single file 1000 times using your context manager in ‘append mode’
# Add some info into file


class contextmanager:

    def __init__(self, original):
        self.original = original

    def __enter__(self):
        print("Entering stuff")
        with open("file.txt", "a") as file:
            file.write(str(self.original) + ", ")
        return "Hiiiiiiii"

    
    def __exit__(self, exc_type, exc_value, exc_tb):
        print("Leaving context bye")
        print(exc_type, exc_value, exc_tb, sep="\n")

the_list = 0

for x in range(0, 1000):
    the_list += 1
    with contextmanager(the_list) as the_copy:
        
        print("doing ")

print(f'the list: {the_list}')

        




