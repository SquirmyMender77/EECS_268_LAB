from executive import Executive
def main():
    """Ask for an input filename and run
    the executive."""
    file_name = input("Enter file name: ")
    Executive(file_name)

if __name__ == "__main__":
    main()
