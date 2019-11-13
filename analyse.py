#读取数据
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
text=pd.read_excel（r"F:\python\实训报告项目题目\酒类销售数据分析项目\酒类销售数据.x1sx",sheet_name=’底表’,encoding='UIF-8'）
text

#处理空值
#①统计每一列非空个数
text.count()
#②删除多余的列
text.drop(columns=['商品ID'，'广告词'，'促销活动']，inplace=True)
text

#品牌总销售额统计
d={"价格（元）":"价格","近30天销量（件）":"近30天销量"}
text.rename(columns=d,inplace=True)
text
text['总销售额']=text['价格']*text['近30天销量']
text.groupby('品牌').agg('价格'：'mean','近30天销量':'mean','总销售额':'mean'})
text2=text.groupby('品牌').agg({'总销售额':'mean'})
text2
text2=text2.sort_values(by='总销售额',ascending=False)
text2.head()
top_text2=text2.iloc[:10,:]
print(top_text2)

#品牌评论数统计
text.groupby('品牌').agg({'评论数':'mean'})
text3=text.groupby('品牌').agg({'评论数':'mean'})
text3
text3=text3.sort_values('by评论数',ascending=False)
text3.head()
top_text3=text3.iloc[:10,:]
print(top_text3)

#清洗数据
text.to_excel('酒类数据清晰.x1sx',sheet_name='清洗数据')
text.corr()