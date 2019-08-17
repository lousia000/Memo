# LF will be replaced by CRLF in README.md.

> 我们都知道，在Windows中使用CRLF标识一行的结束，而在Linux/UNIX系统中只使用LF标识一行的结束。CRLF即Carriage-Return Line-Feed的缩写。
> 通常情况下，Git库不会自动修改文件内容，但是默认会将入库的文件的行尾符设置为LF，会将检出的文件的行尾符设置为CRLF。但是在执行如下操作时出现如下警告：
> - C:\Sam\works\bba-master>git add mywebdav.conf
> - warning: LF will be replaced by CRLF in mywebdav.conf.
> - The file will have its original line endings in your working directory.
> 
> 说明：工作目录中的mywebdav.conf文件的行尾是LF，但是这里在即将入Git库之前，却将LF转换为CRLF。所以给出警告。该警告无伤大雅，因为在Git库中的该文件仍然以LF为行尾。
> 
> 但是如何去除该警告呢？Git的CRLF相关特性与gitattributes文件中的设置相关
> 
> 在工作目录中，我们可以通过设置eol属性控制一个文件的行尾为CRLF或LF。我们也可以通过设置core.eol属性控制当前Git库中的所有文件的行尾为CRLF或LF。我们还可以设置core.autocrlf属性以覆盖core.eol属性的设置。如果要设置工作目录中的文件的行尾总是CRLF，而Git库中的文件的行尾总是LF，可以core.autocrlf=true。

> 1. 查看core.autocrlf属性
> 默认core.autocrlf属性设置如下。
> - C:\Sam\works\bba-master>git config --global --get core.autocrlf
> - C:\Sam\works\bba-master>git config --get core.autocrlf
> - true

> 2. 设置core.autocrlf属性
> 设置core.autocrlf属性为false，去除警告如下（只是眼不见心不烦罢了）。
> - C:\Sam\works\bba-master>git config core.autocrlf false
> - C:\Sam\works\bba-master>git config --get core.autocrlf
> - false
> - C:\Sam\works\bba-master>git add mywebdav.conf
