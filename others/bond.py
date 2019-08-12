# !/user/bin/env python
# -*- coding:utf-8 -*-
# author：mlh

import requests
import json

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
	"Referer": "http://www.sse.com.cn/assortment/bonds/list/",
	"Host": "query.sse.com.cn"
}


def bond(urls):
	res = requests.get(urls, headers=headers)
	n0 = len(res.text) - 1
	n1 = len("jsonpCallback44098(")
	# print(n0, n1)
	t = res.text
	r = t[n1:n0]
	# print(type(res.text))
	# print(json.loads(r))
	for j in range(20):
		bond_shortname = json.loads(r)["pageHelp"]["data"][j]["BOND_ABBR"]  # 证券简称
		bond_code = json.loads(r)["pageHelp"]["data"][j]["BOND_CODE"]  # 证券代码
		bond_fullname = json.loads(r)["pageHelp"]["data"][j]["BOND_FULL"]  # 证券全称
		print(bond_shortname, bond_code, bond_fullname)


for i in range(3, 37):
	url = "http://query.sse.com.cn/commonQuery.do?" \
		"jsonCallBack=jsonpCallback44098&" \
		"isPagination=true&" \
		"sqlId=COMMON_BOND_XXPL_ZQXX_L&" \
		"pageHelp.pageSize=20&" \
		"pageHelp.cacheSize=1&" \
		"pageHelp.pageNo={}&" \
		"pageHelp.beginPage={}&" \
		"pagecache=false&" \
		"BONDTYPE=%E8%AE%B0%E8%B4%A6%E5%BC%8F%E5%9B%BD%E5%80%BA&" \
		"pageHelp.endPage=11&_=1562124438109".format(i, i)
	bond(url)

