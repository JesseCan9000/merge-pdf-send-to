import PyPDF4 
import time
from sys import argv
import os

def merge_pdfs(_pdfs,path):

    mergeFile = PyPDF4.PdfFileMerger()

    for _pdf in _pdfs:

        mergeFile.append(PyPDF4.PdfFileReader(_pdf, 'rb'))

    mergeFile.write(path + "Merged_File_" + timestr + ".pdf")

if __name__ == '__main__':

    timestr = time.strftime("%m_%d_%Y-%H;%M;%S")

    _pdfs = [argv[n] for n in range(1,len(sys.argv))]
    save_path = "\\".join(argv[1].split("\\")[0:-1]) + "\\"

    merge_pdfs(_pdfs,save_path)