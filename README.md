一个python工程结构的范例，包括如下内容：

- 在python根目录内安装包
- 依赖包安装
- 单元测试

在服务器端下载好代码之后执行

```bash  
$ cd PythonSkeleton  
$ python setup.py test      ## 8个测试案例，6个正确，2个错误
$ python setup.py install  
$ python  
```  
  
```python  
>>> from PythonSkeleton.MathDemo import MathDemo  
>>> MathDemo.add(1,2)  
```    
    
测试完成之后删除python根目录下的安装包

```bash
$ pip uninstall PythonSkeleton
```


