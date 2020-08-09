'''
@Author: RyanHuang
@Github: DrRyanHuang
@Brife : 
    下载给定的数据集 `zip` 文件
    若预下载过, 请注释 `wget.download(url, zip_file_str)` 
@Notice:
    原程序是个 `shell` 脚本, 不能直接在 `windows` 运行, 笔者改为了 `Py` 文件
    以下为原 `shell` 脚本

# ---------------------------- shell ----------------------------

#!/bin/bash

FILE=$1

if [[ $FILE != "ae_photos" && $FILE != "apple2orange" && $FILE != "summer2winter_yosemite" &&  $FILE != "horse2zebra" && $FILE != "monet2photo" && $FILE != "cezanne2photo" && $FILE != "ukiyoe2photo" && $FILE != "vangogh2photo" && $FILE != "maps" && $FILE != "cityscapes" && $FILE != "facades" && $FILE != "iphone2dslr_flower" && $FILE != "ae_photos" ]]; then
    echo "Available datasets are: apple2orange, summer2winter_yosemite, horse2zebra, monet2photo, cezanne2photo, ukiyoe2photo, vangogh2photo, maps, cityscapes, facades, iphone2dslr_flower, ae_photos"
    exit 1
fi

URL=https://people.eecs.berkeley.edu/~taesung_park/CycleGAN/datasets/$FILE.zip
ZIP_FILE=./datasets/$FILE.zip
TARGET_DIR=./datasets/$FILE
mkdir -p ./datasets
wget -N $URL -O $ZIP_FILE
unzip $ZIP_FILE -d ./datasets/
rm $ZIP_FILE

# Adapt to project expected directory heriarchy
mkdir -p "$TARGET_DIR/train" "$TARGET_DIR/test"
mv "$TARGET_DIR/trainA" "$TARGET_DIR/train/A"
mv "$TARGET_DIR/trainB" "$TARGET_DIR/train/B"
mv "$TARGET_DIR/testA" "$TARGET_DIR/test/A"
mv "$TARGET_DIR/testB" "$TARGET_DIR/test/B"

# ---------------------------- shell ----------------------------
'''

import os
import shutil
import argparse
from pprint import pprint

import wget
import zipfile


# 用于解析命令行传回来的参数
def param_parse():

    # 创建一个参数解析对象
    parser = argparse.ArgumentParser()
    # 添加需要解析的参数
    parser.add_argument("-ds", 
                        "--dataset", 
                        help="请选择 `dataset` ",
                        type=str)
    
    # 参数解析
    args = parser.parse_args()
    param_dic = vars(args)
    
    return param_dic



# 数据集下载、解压等前置操作
def pre_dateset(user_dataset_str):
    # user_dataset_str ：用户需要的数据集字符串
    
    url = 'https://people.eecs.berkeley.edu/~taesung_park/CycleGAN/datasets/{}.zip'.format(user_dataset_str)
    zip_file_str = './datasets/{}.zip'.format(user_dataset_str)
    target_dir = './datasets/{}'.format(user_dataset_str)
    
    if not os.path.exists('./datasets'):
        os.mkdir('./datasets')
    
    # 下载数据集文件 `x.zip`
    # 若已经自行下载了数据集文件, 请将本行代码注释即可
    wget.download(url, zip_file_str)
    
    zip_file = zipfile.ZipFile(zip_file_str)
    # 将 `zip` 打包的内容直接仍到目标文件夹中 
    zip_file.extractall('./datasets')
    zip_file.close()
    
    # 删除掉下载的数据文件
    os.remove(zip_file_str)
    
    # 将数据目录改为预期的格式
    os.makedirs(os.path.join(target_dir, 'train'))
    os.makedirs(os.path.join(target_dir, 'test'))
    
    shutil.move(os.path.join(target_dir, 'trainA'), os.path.join(target_dir, 'train', 'A'))
    shutil.move(os.path.join(target_dir, 'trainB'), os.path.join(target_dir, 'train', 'B'))
    shutil.move(os.path.join(target_dir, 'testA'), os.path.join(target_dir, 'test', 'A'))
    shutil.move(os.path.join(target_dir, 'testB'), os.path.join(target_dir, 'test', 'B'))
    
    
if __name__ == '__main__':
    
    # 数据集名字列表
    dataset_list = ['apple2orange', 'summer2winter_yosemite', 'horse2zebra', 
                    'monet2photo', 'cezanne2photo', 'ukiyoe2photo', 
                    'vangogh2photo', 'maps', 'cityscapes', 'facades', 
                    'iphone2dslr_flower', 'ae_photos']
    
    param_dic = param_parse()
    
    # 选择用户的数据集
    user_dataset = param_dic['dataset']
    
    
    if user_dataset is not None:
        
        if user_dataset not in dataset_list:
            print('数据集 `{}` 不存在或者不支持'.format(user_dataset))
            print("请选择需要下载的数据集,", "当前支持的数据集有:")
            pprint(dataset_list)
            
        else:
            print('开始下载, 推荐手动下载 hhh')
            pre_dateset(user_dataset)
    else:
        print("请选择需要下载的数据集,", "当前支持的数据集有:")
        pprint(dataset_list)
        
    
    
    
    
    
    