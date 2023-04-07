# zhihu-hot-qa-crawler
Crawl two years hot question answer on zhihu.com  
爬取知乎过往两年的热搜问题和回答。  
multiple code conjunction, shit codes, sorry.  
本质是多个仓库的结合体，垃圾代码，请见谅。
  
**Requirements**:  
pip install beautifulsoup4  
pip install lxml  
需要安装beautifulsoup4库和lxml。  
**Usage**:  
Download .md from https://github.com/justjavac/zhihu-trending-hot-questions  
put uv.py into all .md files directory.  
python uv.py  
*default only download the first question, remove the break to download all.*  
用法是先下载存有问题链接的所有md文件，然后把uv.py放到同一目录下，再运行即可，默认只下载第一个问题的五条回答，可通过break语句控制。
