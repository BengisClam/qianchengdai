# - * - coding：utf-8 -*-
# @Time       ：2019/7/14 16:57
# @Author     ：BeginsCalm
# @Email      ：13631693461@163.com
# @File       ：summary.py


# PO： PageObject   页面=>对象映射模型，思想
# 页面 ==> HTML --> DOM, ==> 各种各样的方法，定位元素修改元素，各种属性


# 等待，发送，点击，测试范畴之内
# 本质上：类封装，复用，很好理解
# Excel 封装成一个方法，属性


# PO 模式的优点：
# 1、提高代码的复用性，不同的测试用例只需要调用PageObject  有限的几个重复的方法
# 2、可维护性提高。 页面发生变化，只需要修改 PageObject 页面的的逻辑
# 3、可读性提高
