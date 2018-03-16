import os
import time
rootdir='b\\'

t1 = time.time() * 1000

import string

print('ascii_lowercase:{}',string.ascii_lowercase)
print('digits:{}',string.digits)
# CHRS = string.ascii_lowercase + string.digits  # 字符列表
# for parent, dirnames, filenames in os.walk(rootdir):
#     if parent=='b/':
#         continue
#     else:
#         i=0
#         for files in filenames:
#             files = os.path.join(parent,files)
#             newfiles = parent[-1:] + '_' + str(i) + '.png'
#             # print('newfiles:{}'.format(newfiles))
#             os.rename(files,'all/' + newfiles)
#             print('rename:{}-->{}'.format(files, 'all/' + newfiles))
#             i += 1


t2 = time.time() * 1000
print('take time:' + str(t2 - t1) + 'ms')