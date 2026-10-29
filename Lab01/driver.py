from executive import Executive

def main():
  file_name = input("Enter the name of the input file: ")
  my_exec = Executive(file_name)
  my_exec.user_interaction()
  my_exec.section_extractor()

if __name__ == "__main__":
  main()
