# -*- coding: utf-8 -*-
# @Author : suyuheng
# @file : Douyin_spider
# @Email : 2111686221@qq.com
# @Time : 2024/7/12 12:40

"""
    抖音首页 视频信息爬取
    获取抖音首页的前300条视频的标题、发布者、发布时间、点赞量
    title、nickname、、diggcount
"""
import time

from utils.common_utils import CommonUtils
import copy
import json

import urllib3
from urllib3.exceptions import InsecureRequestWarning

import requests
from urllib.parse import urlparse, parse_qs

urllib3.disable_warnings(InsecureRequestWarning)# 禁用安全请求警告，没证书。。。

class DyComment:

    def __init__(self):

        self.common_utils = CommonUtils()
        self.comment_list_headers = {
            'sec-ch-ua':'"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
            'Accept':'application/json, text/plain, */*',
            'sec-ch-ua-mobile':'?0',
            'User-Agent':self.common_utils.user_agent,
            'sec-ch-ua-platform':'"Windows"',
            'Sec-Fetch-Site':'same-origin',
            'Sec-Fetch-Mode':'cors',
            'Sec-Fetch-Dest':'empty',
            'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8',
        }

    def get_comment_list(self, req_url,refresh_index):
        referer_url = req_url
        ms_token = self.common_utils.get_ms_token()
        ttwid_str, webid = self.common_utils.get_ttwid_webid(referer_url)
        comment_lsit_req_url = f"https://www.douyin.com/aweme/v1/web/module/feed/?device_platform=webapp&aid=6383&channel=channel_pc_web&module_id=3003101&count=20&filterGids=&presented_ids=&refresh_index={refresh_index}&refer_id=&refer_type=10&awemePcRecRawData=%7B%22is_client%22%3Afalse%7D&Seo-Flag=0&install_time=1720843949&update_version_code=170400&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=123.0.0.0&browser_online=true&engine_name=Blink&engine_version=123.0.0.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid={webid}&verifyFp=verify_lwg2oa43_Ga6DRjOO_v2cd_4NL7_AHTp_qMKyKlDdoqra&fp=verify_lwg2oa43_Ga6DRjOO_v2cd_4NL7_AHTp_qMKyKlDdoqra&msToken={ms_token}"
        comment_list_headers1 = copy.deepcopy(self.comment_list_headers)
        comment_list_headers1['Referer'] = referer_url
        comment_list_headers1['Cookie'] = f'ttwid={ttwid_str};'
        abogus = self.common_utils.get_abogus(comment_lsit_req_url, self.common_utils.user_agent)
        url = comment_lsit_req_url + "&a_bogus=" + abogus
        response = requests.request("POST", url, headers=comment_list_headers1,verify=False, timeout=3)

        time.sleep(1)
        if refresh_index==3:
            response1 = requests.request("GET", 'https://www.douyin.com/discover', headers=comment_list_headers1, verify=False, timeout=3)
            path = f"discover.txt"
            with open(path, 'w', encoding='utf-8') as f:
                f.write(response1.text)

        if (response.text):
            req_txt = response.text
            path=f"{refresh_index}.txt"
            with open(path, 'w',encoding='utf-8') as f:
                f.write(req_txt)
        else:
            print(f"爬取失败或没有评论")




if __name__ == '__main__':
    req_url = "https://www.douyin.com/discover"
    dy_comment = DyComment()

    for refresh_index in range(2,15):
        print(refresh_index)
        dy_comment.get_comment_list(req_url,refresh_index)
        break
