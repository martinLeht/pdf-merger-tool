from PyPDF2 import PdfFileMerger
import argparse

def merge_pdfs(pdfs, merged_file):
    merger = PdfFileMerger()
    for pdf in pdfs:
        try:
            print("Merging file %s" % pdf)
            merger.append(pdf)
        except FileNotFoundError:
            print("Skipping file %s" % pdf)
    print("Writing result file")
    merger.write(merged_file)
    merger.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge multiple PDF:s into one PDF file.")
      
    parser.add_argument(
        "infiles",
        help="Input files to merge.",
        metavar='String...',
        nargs='*'
    )
    parser.add_argument(
        "--out",
        help="Merged output file. (default: result.pdf)",
        default="result.pdf",
        nargs='?'
    )
    
    args = parser.parse_args()
    
    print("Input files:", args.infiles) 
    print("Outpt file: ", args.out)
    
    merge_pdfs(args.infiles, args.out)

