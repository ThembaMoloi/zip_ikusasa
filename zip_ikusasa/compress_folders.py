import zipfile
import os

#create a zip directory
def zip_directory(directory_path, zip_path):
    try:
        with zipfile.ZipFile(zip_path, 'w') as zipf: #create zipped folder
            if os.path.exists(directory_path):  #check if folder we want to zip does exist
                for root, dirs, files, in os.walk(directory_path):
                    for file in files:
                        zipf.write(
                                    os.path.join(root, file),
                                    os.path.relpath(
                                        os.path.join(root, file),
                                        os.path.join(directory_path, '..')
                                    )
                                ) #add each file in the folder to the compressed folder
                print(f' Successfully zipped {directory_path} into {zip_path} ')
                return True
            else:
                print(f'Compression falied, could not find {directory_path}') #in case the file does not exist in the specified directory
                return False
    except Exception as e:
        print(f'An unxpected error occured: {e}')

if __name__ == "__main__":    #run the program
    directory_path = input('Enter directory path:') #get file path
    zip_path = directory_path+'.zip' #specify zipped file destination

    if zip_directory(directory_path, zip_path):
        print('Compression complete') #upon success communicate message
    else:
        print('Compression failed') #upon failure communicate message
