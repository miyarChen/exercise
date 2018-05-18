# -*- coding:utf-8 -*-
"""
解析xml文件
取出Channels的所有子元素
"""
# Python3.3以上版本ElementTree会自动寻找可用的C库来加快速度，因此可以不用导入cElementTree
import xml.etree.ElementTree as ET
import json


tree = ET.parse('movies.xml')    # 载入数据
root = tree.getroot()    # 获取根节点
# 从字符串读取数据
# root = ET.fromstring(movies_as_string)
print(root)
print(root.tag)
# print(root.attrib)
# print(root.text)
# print(root.tail)

channels = root.findall('Channels')
# print(channels)
results = []
child_tag_list = []
child_tag_tup = ()
child_text_list = []
c = 0
for child in channels:  # child为根节点root下一级的元素
    # print(child.getchildren())  # 获取child下所有子节点
    c = c+1
    child_tag_list.append(child.tag+'_'+str(c))

    children_tag_tup = ()
    children_tag_list = []
    children_text_list = []
    for children in child:
        # print(children.tag, ":", children.text)   # 打印Channels所有子元素
        children_tag_list.append(children.tag)
        children_text_list.append(children.text)

    children_tag_tup = tuple(children_tag_list)     # 将列表转化成元组
    children_dict = dict.fromkeys(children_tag_tup)     # 新建一个Channels所有子元素的字典：key=Channels的子元素，value=元素文本
    child_text_list.append(children_dict)

    i = 0
    while i < len(children_text_list):
        children_dict[children_tag_list[i]] = children_text_list[i]
        i = i+1

child_tag_tup = tuple(child_tag_list)
child_dict = dict.fromkeys(child_tag_tup)     # 创建以Channels子元素为key的字典

# 将Channels下所有子元素赋值给以Channels为key的字典中的value
i = 0
while i < len(child_text_list):
    child_dict[child_tag_list[i]] = child_text_list[i]
    i = i + 1

results = json.dumps(child_dict, sort_keys=True, indent=2)     # 将字典转化成json数据格式，排序并且缩进两个字符输出
print(results)
