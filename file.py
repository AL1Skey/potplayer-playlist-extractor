import os
import shutil

# Class that copy file from file with dpl extension
class DPLextract:
    
    __filedata= None
    __filepaths = []

    # get list contain string each line from data
    def __init__(self):
        
        sourcedir = os.path.join(os.getcwd(),'input')

        if not os.path.isdir(sourcedir):
            os.makedirs('input')

        sourcefile = os.listdir(sourcedir)

        if sourcefile == []:
            raise ValueError('There is no file in input folder')
            safeExit()
        source = os.path.join(sourcedir,sourcefile[0])

        with open(source, 'r') as path:
            self.__filedata = path.readlines()
            print('File has being readed \n')
        
    
    # get path of file
    def getpath(self):
        #Data start at one
        counter = 1

        for pathFile in self.__filedata:
            if '*file*' in pathFile:
                splitter = str(counter)+'*file*'

                loc = pathFile.replace(splitter,"")
                loc = loc.replace("\n", '')

                self.__filepaths.append(loc)
                counter +=1
    
    # Copy the files
    def extract(self):

        workingdir = os.path.join(os.getcwd(),'DPLextract')

        # make output folder if not exist
        if not os.path.isdir(workingdir):
            os.makedirs('DPLextract')

        for filepath in self.__filepaths:
            filename = os.path.basename(filepath)
            fileExist = os.path.join(workingdir,filename)

            # if file is exist
            if os.path.isfile(filepath):

                # if file is exist on output folder
                if os.path.isfile(fileExist):
                    print(f"'{filename}' already exist")
                    continue
                
                shutil.copy2(filepath, workingdir)
                print(f"'{filename}' successfully copied to DPLextract")
            
            # if not
            else:
                print(f"{filename} doesn't exist")
