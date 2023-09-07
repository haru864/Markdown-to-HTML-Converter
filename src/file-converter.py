import os
import sys
import markdown


def convertMarkdownToHtml(inputfile: str, outputfile: str) -> None:
    with open(inputfile, "r") as readFile:
        markdownContents = readFile.read()
    htmlContents = markdown.markdown(text=markdownContents)
    print(markdownContents)
    print(htmlContents)
    with open(outputfile, "w") as writeFile:
        writeFile.write(htmlContents)


def isSpecifiedFileFormat(filePath: str, extension: str) -> bool:
    fileName: str = os.path.basename(filePath)
    fileExtension = os.path.splitext(fileName)[1]
    return fileExtension == extension


def displayUsage() -> None:
    print("usage: python3 file-converter.py markdown <inputfile> <outputfile>")


if __name__ == "__main__":
    try:
        if len(sys.argv) < 4:
            raise Exception(f"[Error] Given argument is not enough")
        command: str = sys.argv[1]
        if command != "markdown":
            raise Exception(f"[Error] Given commend '{command}' is not allowed")
        inputfile: str = sys.argv[2]
        if os.path.exists(path=inputfile) == False:
            raise Exception(f"[Error] Given inputfile does not exist")
        if isSpecifiedFileFormat(filePath=inputfile, extension=".md") == False:
            raise Exception(f"[Error] Inputfile must be markdown")
        outputfile: str = sys.argv[3]
        if os.path.exists(path=outputfile) == True:
            if isSpecifiedFileFormat(filePath=outputfile, extension=".html") == True:
                isOverwrittenAllowed: str = input(
                    "outputfile already exists.\nDo you want to overwrite?(y/n) >"
                )
                if isOverwrittenAllowed != "y":
                    exit()
            else:
                raise Exception(f"[Error] Outputfile must be html")
        convertMarkdownToHtml(inputfile=inputfile, outputfile=outputfile)
    except Exception as e:
        print(str(e))
        displayUsage()

exit()
