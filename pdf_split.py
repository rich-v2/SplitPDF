"""
Module to split pdf documents

Functions
pdf_split(filename, first, last, keep_pieces)
# This function is to be supplied with four input arguments:
#   a filename (relative to the source file location)
#   the first page to be read in
#   the last page to be read in
#   a boolean indicating whether all pieces are to be kept
"""
# Import Modules
import PyPDF2

def pdf_split(filename,first,last,keep_pieces):
    """ This function splits the file filename into up to 3 pieces."""
    if filename.find(".pdf") == -1:
        filename += ".pdf"
    # Open file
    with open(filename, 'rb') as f:
        # Create file reader object
        fileReader = PyPDF2.PdfFileReader(f)
        # Create file writer object
        fileWriter = PyPDF2.PdfFileWriter()

        # Fill writer with necessary pages
        for pageNum in range(first,last):
            pageObj = fileReader.getPage(pageNum)
            fileWriter.addPage(pageObj)

        # Save file with a meaningful name
        pdfOutputFile = open("pdf_split_" + filename, 'wb')
        fileWriter.write(pdfOutputFile)
        pdfOutputFile.close()

        # Save other parts
        if keep_pieces:
            # Only save previous part if first page is not equal to first page of the document
            if first > 0:
                fileWriter = PyPDF2.PdfFileWriter()
                for pageNum in range(first):
                    pageObj = fileReader.getPage(pageNum)
                    fileWriter.addPage(pageObj)
                
                 # Save file with a meaningful name
                pdfOutputFile = open("pdf_split_prev_" + filename, 'wb')
                fileWriter.write(pdfOutputFile)
                pdfOutputFile.close()

            # Only save following part if last page is not equal to last page of the document
            if last < fileReader.numPages:
                fileWriter = PyPDF2.PdfFileWriter()
                for pageNum in range(last,fileReader.numPages):
                    pageObj = fileReader.getPage(pageNum)
                    fileWriter.addPage(pageObj)
                
                 # Save file with a meaningful name
                pdfOutputFile = open("pdf_split_aftr_" + filename, 'wb')
                fileWriter.write(pdfOutputFile)
                pdfOutputFile.close()



# Decorator for pdf_split
def user_interaction(func):
    """ This function asks for user input to run pdf_split()."""
    # ask user for filename
    filename = input("Please enter the filename (Make sure it's located in the same directory as the module)\n>>> ")
    # ask user for first page
    first = int(input("First Page\n>>>")) - 1
    # ask user for last page
    last = int(input("Last Page\n>>>"))
    # ask user to keep all pieces
    keep_pieces = bool(int(input("Do you want to keep all pieces? [Y=1,N=0]\n>>>")))
    # Call pdf_split function
    func(filename,first,last,keep_pieces)


if __name__ == "__main__":
    try:
        user_interaction(pdf_split)
    except FileNotFoundError:
        print("File is not located in the directory")
    except ValueError:
        print("Wrong data type supplied. Please check your input")
    except IndexError:
        print("Supplied page number is not in range.")
    finally:
        input("An error occured.\nPress Enter to exit")
