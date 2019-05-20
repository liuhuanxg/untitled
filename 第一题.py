import os
import sys

def dump_file(input_dir):
    if not os.path.exists(input_dir):
        print('dir {} not exists'.format(input_dir))
        return
    path_list = [os.path.join(input_dir, f).strip('\n') for f in os.listdir(input_dir)]
    file_path_list = filter(lambda file_path: os.path.isfile(file_path), path_list)
    for file_path in file_path_list:
        print('{}:{} size:{}'.format(os.getpid(), file_path, os.path.getsize(file_path)))
if __name__ == '__main__':
    if len(sys.argv) > 1:
        dump_file(sys.argv[1])
    else:
        dump_file(os.getcwd())