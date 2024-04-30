# 释放文件夹(release_folder)

本程序的目的是在Windows中添加类似Android的文件夹释放操作。

## 演示

demo文件夹用于演示，其中包含若干文件及文件夹，在当前程序的目录下打开命令行，输入：

```
python folder_release.py -p ./demo/test
```

原本的文件结构为：

- demo
  -  test
     1.  101
     2. 102
        -  003.py
     3. 001.py
     4. 002.py

变更后的结构为：

- demo
  1. test
  2. 101
  3. 102
  4. 001.py
      -  003.py
  5. 002.py

不删除原初文件夹是为了防止误操作。

当将打包后文件添加至环境变量后，命令行指令变为：

```
folder_release -p ./demo/test
```

## 添加至右键菜单

若命令行操作不够方便，可将该操作添加至右键菜单。

1. 键盘按住win + R，输入regedit，回车，打开注册表，定位到

   ```
   计算机\HKEY_CLASSES_ROOT\Directory\shell
   ```

   

2. 右键shell，新建项，重命名为“释放”，这就是右键菜单显示的名称；

3. 右键“释放”，新建项，重命名为‘command’

4. 点击command，在窗口右侧修改其数据为

   ```
   "***" -p "%1"
   ```

   其中，***替换为release_folder.exe在Windows中的绝对路径，例如：

   ```
   "F:\tools\folder_release.exe" -p "%1"
   ```


完成所有操作后，右键文件夹时菜单会多出一栏“释放”。
