import shutil
import os

srcRootPath = 'D:/WorkSpace_PlantForm/platform/'
dstRootPath = 'D:/WorkSpace_PlantForm/test/'
if os.path.exists(dstRootPath):
    shutil.rmtree(dstRootPath)
for filename in open("filelist.txt"):
    try :
        srcFile = srcRootPath + filename.replace('\n','').replace('\\','/')
        dstFile = dstRootPath + filename.replace('\n','').replace('\\','/')
        if os.path.isfile(srcFile):
            tmpdir = os.path.dirname(dstFile)
            if not os.path.exists(tmpdir):
                os.makedirs(tmpdir)
            shutil.copy(srcFile, dstFile)
        else :
            os.makedirs(dstFile)
        # os.system(r"xcopy /S " + srcFile + " " + dstFile)

    except Exception as e:
        if e.__getattribute__('strerror') == 'No such file or directory':
            try :
                if os.path.isfile(srcFile):
                    tmpdir = os.path.dirname(dstFile)
                    if not os.path.exists(tmpdir):
                        os.makedirs(os.path.dirname(dstFile))
                    shutil.copy(srcFile, dstFile)
                else:
                    os.makedirs(dstFile)
            except Exception as se:
                print(srcFile, e)
        else :
            print(srcFile, e)