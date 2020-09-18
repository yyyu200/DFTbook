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

(0) 如果计算量大、对性能要求高，并行库、数学库、编译器的安装应该先进行，如果只是试用，可以不安装最优化的库，只安装fortran编译器即可，直接进入第(1)部分。安装先后顺序应该是(a)mkl,fortran编译器，(b)openmpi，因为openmpi依赖fortran编译器。

安装openmpi的步骤和一般linux安装源程序的方式相同，分为配置、编译、安装三步：

```
./configure --prefix=$HOME/local
make
make install
```
。在openmpi的安装目录下面应该有mpirun，mpif90等可执行文件。运行mpif90 -v可以查看openmpi依赖的fortran编译器版本。

mkl(Intel math kernel library)、ifort分别是intel优化的数学库、fortran编译器，可以在官网下载，申请免费试用版。安装是交互式的。

GCC中的fortran编译器gfortran可以在系统的软件仓库中安装，例如Ubuntu系统用命令安装：

```
sudo apt-get install gfortran
```


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
    <img src="../../../../../img/confs_results.png" width="1000"/>
</p>

编译选项在make.inc，正常是不用改动的，里面有几行可能根据实际情况修改如下，是本机器的编译器，必要时写出完整路径
名
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

这样编译完成后，如果没有出错 ，在bin下面会有可执行文件，大部分是以.x 为后缀，包括pw.x，pp.x等。

## Linux系统

查看各个命令的说明见（以ls为例）：
```
man ls
ls --help
info ls
```

常用命令：

ls 列出目录内容和文件信息

cat 查看文件内容

head和tail阅读文件的开头和结尾

head -n 20 显示文件的前20行

tail -n 20 显示文件后20行

less 更好的文本阅读工具

文件目录管理

mkdir:建立目录

rm:删除文件和目录(-r)

mv:移动和重命名目录

cp : 复制文件和目录(-r)

history 查看当前操作的命令历史

常用文本编辑、处理命令，以下几个工具实际上是非常强大，但也是十分复杂的，请参考相关说明文档：

vi/vim

grep

sed

awk

从linux拷贝到windows的文本文件打开时，推荐用[Notepad++](https://notepad-plus-plus.org/downloads/)，系统自带的"
写字板"也可以，但是用"记事本"由于操作系统换行符不兼容，效果不好。

## References

1. www.quantum-espresso.org

