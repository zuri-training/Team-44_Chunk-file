from multiprocessing import context
from django.shortcuts import redirect, render
import csv, io, os, zipfile    
from pathlib import Path
from media import writeToCsv


# from I4G003513VED.I4G003513VED.settings import MEDIA_URL
# from .csvSplitter import csvSplitter
# from .writeToCsv import csvSplitter
from django.core.files.storage import FileSystemStorage

# Create your views here.
def upload(request):
    if request.method == 'POST' and request.FILES:
        uploaded_file = request.FILES['doc']
        fs = FileSystemStorage()
        context = dict()
        username = 'abdolyom'
        newFileName = username +'_'+uploaded_file.name     
        name = fs.save(newFileName, uploaded_file)
                #!python3 - a csv splitter

        def csvSplitter(fileName,lineThreshold):
            media_folder = Path.cwd()/'media'
            # os.chdir(media_folder)
            fileName = os.path.join(media_folder, fileName)
            print(fileName)
            path = Path(fileName)
            if not path.exists():
                print('The file name specified does not exist')
                return 'error'
            elif path.is_dir():
                    print('The path specified is a folder')
                    print('Indicate the path to the file, Please.')
                    return 'error'
            elif not path.name.endswith('.csv'):
                print('Not a CSV file, please')
                return 'error'
            else:
                baseName = Path(fileName).stem
                suffix  = Path(fileName).suffix
                # os.makedirs(baseName,exist_ok=True)
                with open(fileName) as file:
                    fileReader = csv.reader(file)        
                    counter = 1
                    zipFileName = baseName+'.zip'
                    zipFileName = media_folder/zipFileName
                    zipFileObj = zipfile.ZipFile(zipFileName,'a')
                    for row in fileReader:
                        currentFileName = str(media_folder)+os.sep+baseName+str(counter)+suffix
                        currentSplitFile = open(currentFileName,'a',newline='')
                        outputWriter = csv.writer(currentSplitFile)
                        outputWriter.writerow(row)
                        if fileReader.line_num % lineThreshold == 0:
                            currentSplitFile.close()
                            counter+=1
                for file in media_folder.glob(f'{baseName}*.csv'):
                    zipFileObj.write(currentFileName,compress_type=zipfile.ZIP_DEFLATED)
                        # os.unlink(currentFileName)
        csvSplitter(name,10000)
        fs.delete(name)
        #     context[Path(file).stem] = fs.url(Path(file).name)
        return redirect('split')
    else: return render(request, 'upload.html')
                    

#csvSplitter('Sample-Spreadsheet-500000-rows.csv',1000)
# csvSplitter('./example.csv',2)



        
        #  (media_folder/name,3)
        # # url = fs.url(name)
        # # print(os.listdir(media_folder))
        # # print(list(media_folder.glob("*.csv")))
        # # context = {'url' : fs.url(name)}
        # # print(context)
        # urls = []

        # # for file in os.listdir(media_folder):
        # for file in Path(media_folder).glob('username*.csv'):
def split(request):
    # return render(request,'split.html')
       
        fs = FileSystemStorage()
        context = dict()
        media_folder = Path.cwd()/'media'
        # print(os.listdir(media_folder))
        # print(list(media_folder.glob("*.csv")))
        # context = {'url' : fs.url(name)}
        # print(context)
        urls = []

        # for file in os.listdir(media_folder):
        def returnMB(byte):
            return str(round(byte * 0.000001,1))+'MB'
        for file in Path(media_folder).glob('abdolyom*.zip'):
            context[Path(file).stem] = [fs.url(Path(file).name),returnMB(os.path.getsize(file))]
        print(context)
        return render(request,'split.html',{'context':context.items()})

def  home(request):
   return render(request, 'home.html')

            # urls.append({Path(file).stem: fs.url(Path(file).name)})
            # print(context[file])
        # print(context.items())
            # context[Path(file).stem] = fs.url(file)
        # print(url)
        # print(Path.cwd())
        # media = fs.url(Path.cwd()/'media'/'teblig.csv')
        # print(media)
        # f = open(Path.cwd()/'media'/'teblig.csv')
        # fr = csv.reader(f)
        # for i in fr:
        #     print(i)
        # print(MEDIA_URL)
        # return render(request,'upload.html',context)
        # user = request.user
        # file = request.POST.get('doc',None)
        # print(file)
        # print(uploaded_file.name, " ", uploaded_file.size)
        # # print(uploaded_file.read())
        # # with open(uploaded_file.read()) as fileObj:
        # file = uploaded_file.read().decode('utf-8')
        # reader = csv.reader(io.StringIO(file))
        # from pathlib import Path