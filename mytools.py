import pandas as pd

def 读取ssps数据():
    result, metadata = pyreadstat.read_sav(R'identity.sav',
apply_value_formats=True,formats_as_ordered_category=True)

def 有序变量描述统计函数(表名, 变量名):
    result = 表名[变量名].value_counts(sort=False)
    描述统计表 = pd.DataFrame(result)
    描述统计表['比例'] = 描述统计表['count'] / 描述统计表['count'].sum()
    描述统计表['累计比例'] = 描述统计表['比例'].cumsum()
    return 描述统计表

  def 数值变量描述统计(数据表，变量名):
    result = 数据表[变量名].describe()

   

def 相关系数强弱判断(相关系数值):
    if 相关系数值 >= 0.8:


def 制作交叉表(数据表,自变量,因变量):
    return pd.crosstab()

