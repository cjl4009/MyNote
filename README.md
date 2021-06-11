# MyNote
我的学习笔记
content_1: 词云生成，对于中文文本，可以找出所需要的词性的词语（使用jieba.posseg,返回flag和word二元组），然后把所有需要的词的列表使用：" ".join()连接成一个string送入wordcloud（对词云对象调用.generate()方法），即可生成词云对象，接着使用matplotlib显示即可。