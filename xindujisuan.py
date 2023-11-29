import numpy as np

import krippendorff

print("Example from https://en.wikipedia.org/wiki/Krippendorff's_Alpha")
print()
reliability_data_str = (
    "*  2  *  *  *  *  3  4  1  2  1", # 编码员A
    "1  *  2  1  3  3  4  3  *  *  *", # 编码员B
    "3  0  2  1  3  4  4  *  2  1  1",) # 编码员C
print("\n".join(reliability_data_str))
print()

reliability_data = [
    [np.nan if v == "*" else int(v) for v in coder.split()] for coder in reliability_data_str]

print("Krippendorff's alpha for 类别变量: ", krippendorff.alpha(reliability_data=reliability_data, level_of_measurement="nominal"))
print("Krippendorff's alpha for 数值变量: ", krippendorff.alpha(reliability_data=reliability_data))
