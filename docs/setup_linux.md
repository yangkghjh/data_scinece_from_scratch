# Python 开发环境（Linux）

---------------------

```shell
➜ cat /etc/redhat-release
CentOS release 6.8 (Final)
```

## 安装 Python 2.7

下载 Python 安装包

```shell
wget http://www.python.org/ftp/python/2.7.13/Python-2.7.13.tgz
tar zxvf Python-2.7.13.tgz
cd Python-2.7.13
```

安装依赖（包括 matplotlib 需要的 tcl/tk）

```shell
yum install tcl
yum intstall tcl-devel
yum install tk
yum install tk-devel
```

配置 & 编译

```shell
./configure
make all
make & make install
```

添加软连接

```shell
ln -s /usr/local/bin/python2.7 /usr/bin/python
```

## 安装 PIP

下载并运行安装脚本

```shell
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py
```

使用国内源

```shell
mkdir ~/.pip/
vim ~/.pip/pip.conf
```

添加以下内容

```
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```