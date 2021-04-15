#
## 1.创建一个data文件夹（名字自己可以定）
进入data文件夹下，创建 Annotation、images、imageSets、JPEGImages、labels
```
cd data
mkdir  Annotations images ImageSets JPEGImages labels
```
## 2.移动已有的数据集
将需要的数据集图片放入images  原始标注xml文件放入Annotations  
并将images内文件复制到JPEGIamges中

## 3.在根目录下（与data一个目录）创建make_txt.py 文件
https://github.com/SuTn/Littro_model/blob/main/Yolov5/make_txt.py
可根据自己的名字修改data

## 4.在data目录下创建voc_label.py
将标签格式转换为yolo形式
其中classes = ['person','car'] 由自己数据集的定义实现

**注意** 生成的train.txt  中图片为绝对路径，相对路径时报错 建议使用绝对路径

https://github.com/SuTn/Littro_model/blob/main/Yolov5/voc_label.py

## 5.将数据集图片复制到images中

## 6.根据数据集创建自己的data.yaml文件
参考data中的yaml文件自行修改即可
