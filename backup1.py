import os
import time
source=r"d:\工作\文博相关技术资料\67个文博行业规范（国家文物局2017年公布）"
target_dir=r"d:\工作\资源库\行业\行业标准"
target=target_dir+time.strftime("%Y%m%d%H%M%S")+".zip"
zip_command="zip -qr'%s'%s"%(target,''.join(source))
if os.system(zip_command)==0:
    print("successful backup to",target)
else:
        print('backup FAILED')
