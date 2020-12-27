import os
from datetime import datetime

# print(dir(os))
# print(os.getcwd())

# print(os.listdir('.'))

# os.mkdir('OS-Demo')
# cannot make multiple folders
# os.makedirs(r'OS-Demo-2/Sub-Dir-1')

# removing directories recursively can be dangerous
# os.removedirs('OS-Demo-2/Sub-Dir-1')
# os.rmdir(r'./OS-Demo-2/Sub-Dir-1')
# os.rmdir(r'OS-Demo-2')

# os.rename(r'hello.txt', r'hello-demo.txt')

# print(os.stat('hello-demo.txt'))
# st_mtime=1606856384
# print(datetime.fromtimestamp(st_mtime))

# generator that yields a tuple of the three values seen below; it traverses top-down starting from the directory passed as argument
# os.walk(r'..')

# useful to look for a file or collect file information
# for dirpath, dirnames, filenames in os.walk(r'.'): 
#     print('Current Path: ', dirpath)
#     print('Dirrectories: ',dirnames)
#     print('Files: ', filenames)
#     print()

# print(os.environ.get('HOME'))

# avoid this
# file_path = os.environ.get('HOME') + 'test.txt'

# file_path = os.path.join(os.environ.get('HOME'),'test.txt')
# print(file_path)

# file creation and working with files can be found in another video

# os.path.basename('some_path')
# os.path.dirname('some_path')
# os.path.split('some_path')
# os.path.exists('some_path')
# os.path.isdir('some_path')
# os.path.isfile('some_path')
# os.path.splitext('some_path')

