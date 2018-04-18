一个python工程结构的范例，包括如下内容：

- 在python根目录内安装包
- 依赖包安装
- 单元测试

在服务器端下载好代码之后执行

    $ cd PythonSkeleton
    $ python setup.py test
    $ python setup.py install
    $ python
---
    >>> from PythonSkeleton.MathDemo import MathDemo
    >>> MathDemo.add(1,2)
    
测试完成之后执行

    $ pip uninstall PythonSkeleton



