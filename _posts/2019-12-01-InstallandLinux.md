---
slideinit: "<section markdown=\"1\" data-background=\"../../../../../img/slidebackground.png\"><section markdown=\"1\">"
vertical: "</section><section markdown=\"1\">"
horizontal: "</section></section><section markdown=\"1\" data-background=\"../../../../../img/slidebackground.png\"><section markdown=\"1\">"
layout: post
title: QE安装与Linux操作系统使用
author: yyyu200
tags: DFT
subtitle: ""
category: Blogs
notebookfilename: intro
visualworkflow: true
published: true
theme: beige
trans: cube
---


* TOC
{:toc}

# QE安装与Linux操作系统使用

作为生产的QE程序，对性能要求比较高，为了保证高性能的运行，mkl、ifort的安装应该先进行，包括intel优化的数学库和fortran编译器，然后安装并行计算库openmpi，安装openmpi的步骤和一般linux安装源程序的方式相同，分为配置、编译、安装三步：

```
./configure --prefix=$HOME/local
make
make install
```
。在openmpi的安装目录下面应该有mpirun，mpif90等可执行文件。

(1) 从官网找到安装包，下载完成，得到源程序的压缩文件qe-6.5.tar.gz
解压```tar -xzvf qe-6.5.tar.gz```
解压完成，会生成一个新目录q-e-qe-6.5, ```cd q-e-qe-6.5``` 进入

(2) 配置编译环境变量，在QE目录运行```./configure```。
注意结果提示并行环境配置成功，有如下内容：
```
Parallel environment detected successfully.\
Configured for compilation of parallel executables.
```
并且找到了mkl库。

<p align="left">
    <img src="https://raw.githubusercontent.com/yyyu200/DFTbook/master/img/confs.png" width="1000"/>
</p>

make.inc里面有几行要根据实际情况修改如下，是本机器的编译器，必要时写出完整路径名
```
MPIF90 = mpif90
F90 = ifort
CC = icc
F77 = ifort
```

(3) 编译QE的各个模块

```
make pw pp
```

这时要选择要编译的包，作为基本使用（其他可以以后装，ph等要在安装过程中下载，或手动下载复制到archive目录）

这样编译完成后，如果没有出错 ，在bin下面会有可执行文件，大部分是以.x 为后缀。

## References

1. www.quantum-espresso.org

