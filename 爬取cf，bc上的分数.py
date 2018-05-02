# coding:utf8
import sys
import urllib2, re


# 爬取codeforces的分数
def GetCfRating(name):
    url = 'http://codeforces.com/profile/' + name
    html = urllib2.urlopen(url).read()
    content = html.decode('utf-8')
    pattern = re.compile('Contest rating.*?">(.*?)</span>', re.S)
    items = re.findall(pattern, content)
    for item in items:
        print item


# 爬取bestcoder的分数
def GetBcRating(name):
    url = 'http://bestcoder.hdu.edu.cn/rating.php?user=' + name
    html = urllib2.urlopen(url).read()
    content = html
    pattern = re.compile('RATING.*?">(.*?)</span>', re.S)
    items = re.findall(pattern, content)
    for item in items:
        print item


print "请输入你想在Codeforces上查找的ID分数:"
s = raw_input()
GetCfRating(s)

GetCfRating("palayutm")
print "跪烂Orz"
GetCfRating("tourist")
print "跪烂Orz"
GetCfRating("quailty")
print "再次跪烂Orz"

GetCfRating("biGinNer")

GetCfRating("doubility")

"""
2343
跪烂Orz
3235
跪烂Orz
2491
再次跪烂Orz
2159
"""

