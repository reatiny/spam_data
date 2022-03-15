# train/val/test = 6/2/2

# encoding: utf-8
import os
import random


def ran_split(full_list, shuffle=False, ratio1=0.6, ratio2=0.2):
        sublists = []
        n_total = len(full_list)
        offset1 = int(n_total * ratio1)
        offset2 = int(n_total * ratio2) + offset1
        if n_total == 0 or offset1 < 1:
                return [], full_list
        if shuffle:
                random.shuffle(full_list)  # 打乱排序
        sublist_1 = full_list[:offset1]
        sublist_2 = full_list[offset1:offset2]
        sublist_3 = full_list[offset2:]
        sublists.append(sublist_1)
        sublists.append(sublist_2)
        sublists.append(sublist_3)
        return sublists  # sublists=[sublist_1,sublist_2,sublist_3]


def read_file(filepath):
        file_list = []
        with open(filepath, 'r', encoding='utf-8') as fr:
                data = fr.readlines()
                data = ''.join(data).strip('\n').splitlines()
        # ''.join() list转为str
        # s.strip(rm) 删除s中开头结尾处的rm字符
        # .splitlines() 将字符串返回列表
        file_list = data
        return file_list


def write_file(dst1, txt):
        fo = open(dst1, 'w', encoding='utf-8')
        for item in txt:
                fo.write(str(item) + '\n')


if __name__ == "__main__":
        root_path = r'/Users/wangchenrui/Desktop/data'
        from_txt = 'all.txt'
        txts = ['train.txt', 'test.txt', 'val.txt']
        from_path = os.path.join(root_path, from_txt)

        txt_list = read_file(from_path)

        sublists = ran_split(txt_list, shuffle=True, ratio1=0.6, ratio2=0.2)
        # 注：生成的sublist数量与txts数量相同

        for txt_name, i in zip(txts, range(len(txts))):
                to_path = os.path.join(root_path, txt_name)
                write_file(to_path, sublists[i])



