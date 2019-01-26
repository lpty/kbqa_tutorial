## 引言
在调研KBQA过程中的一些记录和简单实现，更多细节可以在我的博客上找到：https://blog.csdn.net/sinat_33741547/article/category/8636625

## 历史
* 2019-01-25

    增加d2rq和jean
    
* 2019-01-26

    增加rules
    基于规则的kbqa，预先定义规则模板，后基于正则进行匹配得到结果。匹配成功则该输入问题语义可知，返回对应SPARQL查询语句；
    本处代码来自： https://github.com/SimmerChan/KG-demo-for-movie ，在此基础上进行相应修改。

