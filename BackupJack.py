import os,shutil
#import datetime, time

class Backup:

    File =["SF","dst"]

    def __init__(self,*File):
        self.root_src_dir =File[0]
        self.root_dst_dir =File[1]

    def CopyDirectory_TO_Backup(self):

        try:
            for src_dir, dirs, files in os.walk(self.root_src_dir):
                dst_dir = src_dir.replace(self.root_src_dir,self.root_dst_dir,1)
                if not os.path.exists(dst_dir):
                    os.makedirs(dst_dir)
                for file_ in files:
                    src_file = os.path.join(src_dir, file_)
                    dst_file = os.path.join(dst_dir, file_)
                    if os.path.exists(dst_file):
                        os.remove(dst_file)
                    shutil.copy(src_file, dst_dir)
            print("Data copied to destination")
        except:
            print("Data not copied")

def send_Data():
    sf1 = "C:\\Users\\Jackie\\Downloads\\Documents"
    sf2 = "C:\\Users\\Jackie\\Desktop"
    sf3 = "C:\\Users\\Jackie\\Documents"
    Dst = r"\\DLINK-1B4C79/Volume_1/JackieScripBackup"

    copy = Backup(sf1,Dst)
    copy2 = Backup(sf2,Dst)
    copy3 = Backup(sf3, Dst)
    copy.CopyDirectory_TO_Backup(),copy2.CopyDirectory_TO_Backup(),copy3.CopyDirectory_TO_Backup()
send_Data()