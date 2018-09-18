# -*- coding: utf-8 -*-
# import scrapy
from scrapy import FormRequest, Spider, Request
from example.js import encrypt_pwd, encode_email
from time import time
from example.config import acc, pwd
from json import dumps


class ExampleSpider(Spider):
    name = 'example'

    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/68.0.3440.106 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'Referer': 'https://account.talkingdata.com/?backurl=https://www.talkingdata.com&languagetype=zh_cn',
            'Host': 'account.talkingdata.com',
            'Connection': 'keep-alive'
        }
        return [Request('https://account.talkingdata.com/api/v1/preLogin?email={}&isMobilePhone=false&_={}'.format(
            encode_email(acc), str(int(time()) * 1000)), headers=headers, callback=self.first)]

    def first(self, response):
        formdata = {
            'email': encode_email(acc),
            'password': encrypt_pwd(pwd)
        }
        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                          ' Chrome/68.0.3440.106 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/json',
            'Referer': 'https://account.talkingdata.com/?backurl=https://www.talkingdata.com&languagetype=zh_cn',
            'Origin': 'https://account.talkingdata.com',
            'Connection': 'keep-alive',
            'Host': 'account.talkingdata.com'
        }
        return [Request('https://account.talkingdata.com/api/v1/login', method='POST', body=dumps(formdata),
                      headers=headers, callback=self.second)]

    def second(self, response):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/68.0.3440.106 Safari/537.36',
            'Referer': 'https://account.talkingdata.com/?backurl=https://www.talkingdata.com&languagetype=zh_cn',
            'Upgrade-Insecure-Requests': '1',
            'Connection': 'keep-alive',
            'Host': 'account.talkingdata.com'
        }
        return [Request('https://account.talkingdata.com/api/v1/center', headers=headers)]

    def parse(self, response):
        # a = 'https://www.talkingdata.com/tracking?languagetype=zh_cn'
        print(response.text)
