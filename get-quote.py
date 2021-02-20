#function for reading
def main():

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(*quotes,sep = "\n")

if __name__== "__main__":
  main()

# for writing new quote
text_file.write('\nI made a balls of it');
text_file.close()

main()

#n = text_file.write('Welcome to pythonexamples.org')
#text_file.close()


