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

作为生产的QE程序，对性能要求比较高，为了保证高性能的运行，mkl、ifort的安装应该先进行，包括intel优化的数学库和fortran编译器，然后安装并行计算库openmpi，安装openmpi的步骤和一般linux安装源程序的方式相同，分为配置，编译，安装三步：
```
./configure --prefix=$HOME/local
make
make install
```
。在openmpi的安装目录下面应该有mpirun，mpif90等可执行文件。

1. 从官网找到安装包，下载完成，得到源程序的压缩文件qe-6.5.tar.gz
解压```tar -xzvf qe-6.5.tar.gz```

2. 解压完成，会生成一个新目录q-e-qe-6.5, cd q-e-qe-6.5 进入，生成的目录 应该这样子

3. 接下来首先应该保证系统安装有fortran（推荐ifort）和mkl库（推荐Intel MKL）
./configure

注意这里提示并行环境配置成功，并且找到了mkl库。

这是为了配置编译环境变量的脚本，make.sys里面有几行要根据实际情况修改如下，是本机器的编译器，必要时写出完整路径名
```
MPIF90 = mpif90
F90 = ifort
CC = icc
F77 = ifort
```

4. 编译QE的各个模块

```
make pw pp
```

这时要选择要编译的包，作为基本使用（其他可以以后装，ph等要在安装过程中下载，或手动下载复制到archive目录）

这样编译完成后，如果没有出错 ，在bin下面会有可执行文件，大部分是以.x 为后缀。

## References

1. www.quantum-espresso.org

