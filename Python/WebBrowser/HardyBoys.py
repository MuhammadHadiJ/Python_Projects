import webbrowser as wb

bookName = input("Enter the book name: ")
bookNum = input("The book number in the serial: ")

bookName = bookName.replace(" ","_")
bookName = bookName.lower()

bookNum = "0"+ bookNum

wb.open("http://thecreativearchive.weebly.com/uploads/2/4/9/2/24925026/"+bookNum+"_"+bookName+".pdf")