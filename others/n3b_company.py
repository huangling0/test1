# !/user/bin/env python
# -*- coding:utf-8 -*-
# author：mlh

import requests
import json



headers = {
	"Cookie": "BIGipServerNEEQ_8000-NEW=100729780.16415.0000; "
			"Hm_lvt_b58fe8237d8d72ce286e1dbd2fc8308c=1561683007,1561942702,1562028923,1562053050;"
			"Hm_lpvt_b58fe8237d8d72ce286e1dbd2fc8308c=1562053055",
	"Referer": "http://www.neeq.com.cn/nq/listedcompany.html",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
	"Host": "www.neeq.com.cn"
}


def company(urls):
	res = requests.get(urls, headers=headers)
	n0 = len(res.text)-2
	n1 = len("jQuery183013081803994728336_1562060752485([")
	# print(n0, n1)
	t = res.text
	r = t[n1:n0]
	# print(type(res.text))
	# print(json.loads(r))
	for j in range(20):
		company_code = json.loads(r)["content"][j]["xxzqdm"]  # 公司代码

		company_Sname = json.loads(r)["content"][j]["xxzqjc"]  # 公司简称
		company_name = json.loads(r)["content"][j]["xxzbqs"]  # 公司名称
		company_local = json.loads(r)["content"][j]["xxssdq"]  # 公司地区
		company_zhengquan = json.loads(r)["content"][j]["xxzbqs"]  # 证券公司
		company_hangye = json.loads(r)["content"][j]["xxhyzl"]  # 行业
		print(company_code, company_Sname, company_name, company_local, company_zhengquan, company_hangye)


for i in range(0, 496):
	url = "http://www.neeq.com.cn/nqxxController/nqxx.do?" \
		"callback=jQuery183013081803994728336_1562060752485" \
		"&page={}&typejb=T&xxzqdm=&xxzrlx=&xxhyzl=&xxssdq=&sortfield=xxzqdm&" \
		"sorttype=asc&dicXxzbqs=&xxfcbj=&_=1562060760464".format(i)
	company(url)







