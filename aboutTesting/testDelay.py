import os,sys
import time
import pycurl
#接收需要处理网站地址
#URL = sys.argv[1]
URL = "http://localhost:5001/chainDetail"

c=pycurl.Curl() #创建一个Curl的对象
c.setopt(pycurl.URL,URL)  #定义请求的URL常量
c.setopt(pycurl.CONNECTTIMEOUT,5) # 定义请求连接的等待时间
c.setopt(pycurl.TIMEOUT,5)  #定义请求超时时间
c.setopt(pycurl.NOPROGRESS,0) #屏蔽下载进度条
c.setopt(pycurl.FORBID_REUSE,1) #完成交互后强制断开连接，不重用
c.setopt(pycurl.MAXREDIRS,1)  #指定HTTP重定向的最大数为1
c.setopt(pycurl.DNS_CACHE_TIMEOUT,30)  #设置保存DNS信息的时间为30秒
#创建一个文件对象，以"wb"方式打开，用来存储返回的http头部及页面内容
indexfile = open('content.txt','wb')
c.setopt(pycurl.WRITEHEADER,indexfile) #讲返回的HTTP HEADER 定向到indexfile文件
c.setopt(pycurl.WRITEDATA,indexfile)  #将返回的 HTTP 内容定向到indexfile文件对象
try:
    c.perform()   #提交请求
    print("")
except Exception as e:
    print('connection error:'+str(e))
    indexfile.close()
    c.close()
    sys.exit()

namelookup_time = c.getinfo(c.NAMELOOKUP_TIME)  #获取DNS解析时间
connect_time = c.getinfo(c.CONNECT_TIME)  #获取建立连接时间
pretransfer_time = c.getinfo(c.PRETRANSFER_TIME)  #获取从建立连接到准备传输所消耗的时间
starttransfer_time = c.getinfo(c.STARTTRANSFER_TIME) #获取从建立链接到传输开始消耗的时间
total_time = c.getinfo(c.TOTAL_TIME)  # 获取传输的总时间
http_code = c.getinfo(c.HTTP_CODE)  #获取HTTP 状态吗
size_download = c.getinfo(c.SIZE_DOWNLOAD)  #获取下载数据包大小
header_size = c.getinfo(c.HEADER_SIZE)   #获取HTTP头部大小
speed_download = c.getinfo(c.SPEED_DOWNLOAD)  #获取平均下载速度
#打印输出相关数据
print('HTTP状态码：%s' % http_code)
print('DNS解析时间: %.2f ms' % (namelookup_time*1000))
print('建立连接时间: %.2f ms' % (connect_time*1000))
print('准备传输时间: %.2f ms' % (pretransfer_time*1000))
print('传输开始时间: %.2f ms' % (starttransfer_time*1000))
print('传输结束总时间: %.2f ms' % (total_time*1000))
print('下载数据包大小: %d bytes ' % size_download)
print('HTTP头部大小: %d bytes' % header_size)
print('平均下载速度: %d bytes/s' % speed_download)
#关闭文件和Curl对象

indexfile.close()
c.close()