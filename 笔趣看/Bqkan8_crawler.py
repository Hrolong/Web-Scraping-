{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from bs4 import BeautifulSoup\n",
    "import requests, sys\n",
    "from time import sleep\n",
    "from fake_useragent import UserAgent\n",
    "from requests.adapters import HTTPAdapter\n",
    "from requests.packages.urllib3.util.retry import Retry\n",
    "import urllib3.contrib.pyopenssl"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "class downloader(object):\n",
    "\n",
    "    def __init__(self):\n",
    "        self.server = 'http://www.biqukan.com/'\n",
    "        self.target = 'http://www.biqukan.com/34658_34658426/'\n",
    "        #存放章节名\n",
    "        self.names = []\n",
    "        #存放章节链接\n",
    "        self.urls = []\n",
    "        #章节数\n",
    "        self.nums = 0\n",
    "\n",
    "    \"\"\"\n",
    "    函数说明:获取下载链接\n",
    "    \"\"\"\n",
    "    def get_download_url(self): \n",
    "        urllib3.contrib.pyopenssl.inject_into_urllib3()\n",
    "        req = requests.get(url=self.target, headers={'Connection':'close'},stream=True, verify=False)\n",
    "        requests.adapters.DEFAULT_RETRIES = 5 \n",
    "        sleep(5)\n",
    "        html = req.text\n",
    "        requests.adapters.DEFAULT_RETRIES = 5 \n",
    "        div_bf = BeautifulSoup(html, 'lxml')\n",
    "        div = div_bf.find_all('div', class_ = 'listmain')\n",
    "        a_bf = BeautifulSoup(str(div[0]))\n",
    "        a = a_bf.find_all('a')\n",
    "        #剔除不必要的章节，并统计章节数\n",
    "        self.nums = len(a[12:])\n",
    "        for each in a[12:]:\n",
    "            self.names.append(each.string)\n",
    "            self.urls.append(self.server + each.get('href'))\n",
    "\n",
    "    \"\"\"\n",
    "    函数说明:获取章节内容\n",
    "    \"\"\"\n",
    "    def get_contents(self, target):\n",
    "        urllib3.contrib.pyopenssl.inject_into_urllib3()\n",
    "        req = requests.get(url=self.target, headers={'Connection':'close'},stream=True, verify=False)\n",
    "        sleep(5)\n",
    "        html = req.text\n",
    "        requests.adapters.DEFAULT_RETRIES = 5 \n",
    "        bf = BeautifulSoup(html)\n",
    "        texts = bf.find_all('div', class_ = 'showtxt')\n",
    "        #texts = texts[0].text.replace('\\xa0'*8,'\\n\\n')\n",
    "        return texts\n",
    "\n",
    "    \"\"\"\n",
    "    函数说明:将爬取的文章内容写入文件\n",
    "    \"\"\"\n",
    "    def writer(self, name, path, text):\n",
    "        write_flag = True\n",
    "        with open(path, 'a', encoding='utf-8') as f:\n",
    "            f.write(name + '\\n')\n",
    "            f.writelines(text)\n",
    "            f.write('\\n\\n')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "《雪中悍刀行》开始下载：\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:0.000%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:0.099%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:0.198%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:0.298%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:0.397%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:0.496%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:0.595%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:0.694%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:0.794%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:0.893%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:0.992%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:1.091%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:1.190%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:1.290%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:1.389%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:1.488%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:1.587%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:1.687%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:1.786%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:1.885%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:1.984%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:2.083%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:2.183%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:2.282%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:2.381%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:2.480%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:2.579%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:2.679%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:2.778%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:2.877%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:2.976%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:3.075%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:3.175%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:3.274%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:3.373%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:3.472%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:3.571%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:3.671%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:3.770%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:3.869%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:3.968%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:4.067%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:4.167%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:4.266%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:4.365%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:4.464%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:4.563%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:4.663%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:4.762%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:4.861%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:4.960%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:5.060%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:5.159%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:5.258%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:5.357%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:5.456%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:5.556%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:5.655%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:5.754%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:5.853%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:5.952%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:6.052%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:6.151%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:6.250%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:6.349%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:6.448%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:6.548%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:6.647%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:6.746%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:6.845%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:6.944%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:7.044%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:7.143%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:7.242%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:7.341%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:7.440%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:7.540%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:7.639%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:7.738%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:7.837%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:7.937%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:8.036%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:8.135%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:8.234%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:8.333%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:8.433%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:8.532%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:8.631%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:8.730%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:8.829%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:8.929%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:9.028%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:9.127%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:9.226%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:9.325%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:9.425%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:9.524%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:9.623%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:9.722%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:9.821%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:9.921%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:10.020%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:10.119%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:10.218%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:10.317%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:10.417%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:10.516%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:10.615%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:10.714%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:10.813%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:10.913%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:11.012%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:11.111%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:11.210%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:11.310%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:11.409%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:11.508%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:11.607%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:11.706%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:11.806%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:11.905%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:12.004%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:12.103%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:12.202%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:12.302%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:12.401%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:12.500%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:12.599%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:12.698%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:12.798%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:12.897%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:12.996%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:13.095%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:13.194%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:13.294%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:13.393%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:13.492%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:13.591%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:13.690%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:13.790%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:13.889%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:13.988%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:14.087%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:14.187%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:14.286%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:14.385%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:14.484%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:14.583%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:14.683%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:14.782%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:14.881%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:14.980%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:15.079%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:15.179%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:15.278%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:15.377%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:15.476%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:15.575%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:15.675%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:15.774%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:15.873%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:15.972%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:16.071%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:16.171%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:16.270%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:16.369%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:16.468%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:16.567%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:16.667%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:16.766%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:16.865%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:16.964%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:17.063%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:17.163%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:17.262%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:17.361%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:17.460%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:17.560%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:17.659%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:17.758%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:17.857%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:17.956%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:18.056%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:18.155%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:18.254%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:18.353%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:18.452%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:18.552%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:18.651%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:18.750%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:18.849%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:18.948%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:19.048%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:19.147%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:19.246%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:19.345%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:19.444%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:19.544%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:19.643%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:19.742%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:19.841%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:19.940%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:20.040%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:20.139%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n",
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  已下载:20.238%\r"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings\n",
      "  InsecureRequestWarning,\n"
     ]
    },
    {
     "ename": "SSLError",
     "evalue": "HTTPSConnectionPool(host='www.bqkan.com', port=443): Max retries exceeded with url: /34658_34658426/ (Caused by SSLError(SSLError(\"bad handshake: SysCallError(-1, 'Unexpected EOF')\",),))",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mSysCallError\u001b[0m                              Traceback (most recent call last)",
      "\u001b[1;32mc:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\contrib\\pyopenssl.py\u001b[0m in \u001b[0;36mwrap_socket\u001b[1;34m(self, sock, server_side, do_handshake_on_connect, suppress_ragged_eofs, server_hostname)\u001b[0m\n\u001b[0;32m    484\u001b[0m             \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 485\u001b[1;33m                 \u001b[0mcnx\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdo_handshake\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    486\u001b[0m             \u001b[1;32mexcept\u001b[0m \u001b[0mOpenSSL\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mSSL\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mWantReadError\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\OpenSSL\\SSL.py\u001b[0m in \u001b[0;36mdo_handshake\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m   1827\u001b[0m         \u001b[0mresult\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0m_lib\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mSSL_do_handshake\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_ssl\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1828\u001b[1;33m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_raise_ssl_error\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_ssl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mresult\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1829\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\OpenSSL\\SSL.py\u001b[0m in \u001b[0;36m_raise_ssl_error\u001b[1;34m(self, ssl, result)\u001b[0m\n\u001b[0;32m   1558\u001b[0m                         \u001b[1;32mraise\u001b[0m \u001b[0mSysCallError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0merrno\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0merrorcode\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0merrno\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1559\u001b[1;33m                 \u001b[1;32mraise\u001b[0m \u001b[0mSysCallError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m-\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m\"Unexpected EOF\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1560\u001b[0m             \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mSysCallError\u001b[0m: (-1, 'Unexpected EOF')",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[1;31mSSLError\u001b[0m                                  Traceback (most recent call last)",
      "\u001b[1;32mc:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py\u001b[0m in \u001b[0;36murlopen\u001b[1;34m(self, method, url, body, headers, retries, redirect, assert_same_host, timeout, pool_timeout, release_conn, chunked, body_pos, **response_kw)\u001b[0m\n\u001b[0;32m    671\u001b[0m                 \u001b[0mheaders\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mheaders\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 672\u001b[1;33m                 \u001b[0mchunked\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mchunked\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    673\u001b[0m             )\n",
      "\u001b[1;32mc:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py\u001b[0m in \u001b[0;36m_make_request\u001b[1;34m(self, conn, method, url, timeout, chunked, **httplib_request_kw)\u001b[0m\n\u001b[0;32m    375\u001b[0m         \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 376\u001b[1;33m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_validate_conn\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mconn\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    377\u001b[0m         \u001b[1;32mexcept\u001b[0m \u001b[1;33m(\u001b[0m\u001b[0mSocketTimeout\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mBaseSSLError\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py\u001b[0m in \u001b[0;36m_validate_conn\u001b[1;34m(self, conn)\u001b[0m\n\u001b[0;32m    993\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[0mgetattr\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mconn\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m\"sock\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m  \u001b[1;31m# AppEngine might not have  `.sock`\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 994\u001b[1;33m             \u001b[0mconn\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mconnect\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    995\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connection.py\u001b[0m in \u001b[0;36mconnect\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    393\u001b[0m             \u001b[0mserver_hostname\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mserver_hostname\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 394\u001b[1;33m             \u001b[0mssl_context\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mcontext\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    395\u001b[0m         )\n",
      "\u001b[1;32mc:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\util\\ssl_.py\u001b[0m in \u001b[0;36mssl_wrap_socket\u001b[1;34m(sock, keyfile, certfile, cert_reqs, ca_certs, server_hostname, ssl_version, ciphers, ssl_context, ca_cert_dir, key_password)\u001b[0m\n\u001b[0;32m    369\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mHAS_SNI\u001b[0m \u001b[1;32mand\u001b[0m \u001b[0mserver_hostname\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 370\u001b[1;33m             \u001b[1;32mreturn\u001b[0m \u001b[0mcontext\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mwrap_socket\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0msock\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mserver_hostname\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mserver_hostname\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    371\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\contrib\\pyopenssl.py\u001b[0m in \u001b[0;36mwrap_socket\u001b[1;34m(self, sock, server_side, do_handshake_on_connect, suppress_ragged_eofs, server_hostname)\u001b[0m\n\u001b[0;32m    490\u001b[0m             \u001b[1;32mexcept\u001b[0m \u001b[0mOpenSSL\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mSSL\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mError\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 491\u001b[1;33m                 \u001b[1;32mraise\u001b[0m \u001b[0mssl\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mSSLError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"bad handshake: %r\"\u001b[0m \u001b[1;33m%\u001b[0m \u001b[0me\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    492\u001b[0m             \u001b[1;32mbreak\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mSSLError\u001b[0m: (\"bad handshake: SysCallError(-1, 'Unexpected EOF')\",)",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[1;31mMaxRetryError\u001b[0m                             Traceback (most recent call last)",
      "\u001b[1;32mc:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\requests\\adapters.py\u001b[0m in \u001b[0;36msend\u001b[1;34m(self, request, stream, timeout, verify, cert, proxies)\u001b[0m\n\u001b[0;32m    448\u001b[0m                     \u001b[0mretries\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmax_retries\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 449\u001b[1;33m                     \u001b[0mtimeout\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mtimeout\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    450\u001b[0m                 )\n",
      "\u001b[1;32mc:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\connectionpool.py\u001b[0m in \u001b[0;36murlopen\u001b[1;34m(self, method, url, body, headers, retries, redirect, assert_same_host, timeout, pool_timeout, release_conn, chunked, body_pos, **response_kw)\u001b[0m\n\u001b[0;32m    719\u001b[0m             retries = retries.increment(\n\u001b[1;32m--> 720\u001b[1;33m                 \u001b[0mmethod\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0merror\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0me\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0m_pool\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0m_stacktrace\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0msys\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mexc_info\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    721\u001b[0m             )\n",
      "\u001b[1;32mc:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\urllib3\\util\\retry.py\u001b[0m in \u001b[0;36mincrement\u001b[1;34m(self, method, url, response, error, _pool, _stacktrace)\u001b[0m\n\u001b[0;32m    435\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mnew_retry\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mis_exhausted\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 436\u001b[1;33m             \u001b[1;32mraise\u001b[0m \u001b[0mMaxRetryError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0m_pool\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0merror\u001b[0m \u001b[1;32mor\u001b[0m \u001b[0mResponseError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mcause\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    437\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mMaxRetryError\u001b[0m: HTTPSConnectionPool(host='www.bqkan.com', port=443): Max retries exceeded with url: /34658_34658426/ (Caused by SSLError(SSLError(\"bad handshake: SysCallError(-1, 'Unexpected EOF')\",),))",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[1;31mSSLError\u001b[0m                                  Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-3-5c9e5b1118ad>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      4\u001b[0m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'《雪中悍刀行》开始下载：'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m     \u001b[1;32mfor\u001b[0m \u001b[0mi\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdl\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mnums\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 6\u001b[1;33m         \u001b[0mdl\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mwriter\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdl\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mnames\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mi\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'雪中悍刀行.txt'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mdl\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget_contents\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdl\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0murls\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mi\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      7\u001b[0m         \u001b[0msys\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mstdout\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mwrite\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"  已下载:%.3f%%\"\u001b[0m \u001b[1;33m%\u001b[0m  \u001b[0mfloat\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mi\u001b[0m\u001b[1;33m/\u001b[0m\u001b[0mdl\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mnums\u001b[0m\u001b[1;33m*\u001b[0m\u001b[1;36m100\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;33m+\u001b[0m \u001b[1;34m'\\r'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      8\u001b[0m         \u001b[0msys\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mstdout\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mflush\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m<ipython-input-2-a61deddf2115>\u001b[0m in \u001b[0;36mget_contents\u001b[1;34m(self, target)\u001b[0m\n\u001b[0;32m     36\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mget_contents\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mtarget\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     37\u001b[0m         \u001b[0murllib3\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcontrib\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpyopenssl\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0minject_into_urllib3\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 38\u001b[1;33m         \u001b[0mreq\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mrequests\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0murl\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mtarget\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mheaders\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;33m{\u001b[0m\u001b[1;34m'Connection'\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;34m'close'\u001b[0m\u001b[1;33m}\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mstream\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mTrue\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mverify\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mFalse\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     39\u001b[0m         \u001b[0msleep\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m5\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     40\u001b[0m         \u001b[0mhtml\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mreq\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mtext\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\requests\\api.py\u001b[0m in \u001b[0;36mget\u001b[1;34m(url, params, **kwargs)\u001b[0m\n\u001b[0;32m     73\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     74\u001b[0m     \u001b[0mkwargs\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msetdefault\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'allow_redirects'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;32mTrue\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 75\u001b[1;33m     \u001b[1;32mreturn\u001b[0m \u001b[0mrequest\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'get'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mparams\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     76\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     77\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\requests\\api.py\u001b[0m in \u001b[0;36mrequest\u001b[1;34m(method, url, **kwargs)\u001b[0m\n\u001b[0;32m     58\u001b[0m     \u001b[1;31m# cases, and look like a memory leak in others.\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     59\u001b[0m     \u001b[1;32mwith\u001b[0m \u001b[0msessions\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mSession\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0msession\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 60\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0msession\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mrequest\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmethod\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mmethod\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0murl\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     61\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     62\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\requests\\sessions.py\u001b[0m in \u001b[0;36mrequest\u001b[1;34m(self, method, url, params, data, headers, cookies, files, auth, timeout, allow_redirects, proxies, hooks, stream, verify, cert, json)\u001b[0m\n\u001b[0;32m    531\u001b[0m         }\n\u001b[0;32m    532\u001b[0m         \u001b[0msend_kwargs\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mupdate\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0msettings\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 533\u001b[1;33m         \u001b[0mresp\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msend\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mprep\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0msend_kwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    534\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    535\u001b[0m         \u001b[1;32mreturn\u001b[0m \u001b[0mresp\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\requests\\sessions.py\u001b[0m in \u001b[0;36msend\u001b[1;34m(self, request, **kwargs)\u001b[0m\n\u001b[0;32m    666\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    667\u001b[0m         \u001b[1;31m# Resolve redirects if allowed.\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 668\u001b[1;33m         \u001b[0mhistory\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m[\u001b[0m\u001b[0mresp\u001b[0m \u001b[1;32mfor\u001b[0m \u001b[0mresp\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mgen\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;32mif\u001b[0m \u001b[0mallow_redirects\u001b[0m \u001b[1;32melse\u001b[0m \u001b[1;33m[\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    669\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    670\u001b[0m         \u001b[1;31m# Shuffle things around if there's history.\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\requests\\sessions.py\u001b[0m in \u001b[0;36m<listcomp>\u001b[1;34m(.0)\u001b[0m\n\u001b[0;32m    666\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    667\u001b[0m         \u001b[1;31m# Resolve redirects if allowed.\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 668\u001b[1;33m         \u001b[0mhistory\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m[\u001b[0m\u001b[0mresp\u001b[0m \u001b[1;32mfor\u001b[0m \u001b[0mresp\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mgen\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;32mif\u001b[0m \u001b[0mallow_redirects\u001b[0m \u001b[1;32melse\u001b[0m \u001b[1;33m[\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    669\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    670\u001b[0m         \u001b[1;31m# Shuffle things around if there's history.\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\requests\\sessions.py\u001b[0m in \u001b[0;36mresolve_redirects\u001b[1;34m(self, resp, req, stream, timeout, verify, cert, proxies, yield_requests, **adapter_kwargs)\u001b[0m\n\u001b[0;32m    245\u001b[0m                     \u001b[0mproxies\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mproxies\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    246\u001b[0m                     \u001b[0mallow_redirects\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mFalse\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 247\u001b[1;33m                     \u001b[1;33m**\u001b[0m\u001b[0madapter_kwargs\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    248\u001b[0m                 )\n\u001b[0;32m    249\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\requests\\sessions.py\u001b[0m in \u001b[0;36msend\u001b[1;34m(self, request, **kwargs)\u001b[0m\n\u001b[0;32m    644\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    645\u001b[0m         \u001b[1;31m# Send the request\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 646\u001b[1;33m         \u001b[0mr\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0madapter\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msend\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mrequest\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    647\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    648\u001b[0m         \u001b[1;31m# Total elapsed time of the request (approximately)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\users\\llong\\appdata\\local\\programs\\python\\python36\\lib\\site-packages\\requests\\adapters.py\u001b[0m in \u001b[0;36msend\u001b[1;34m(self, request, stream, timeout, verify, cert, proxies)\u001b[0m\n\u001b[0;32m    512\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[0misinstance\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0me\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mreason\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0m_SSLError\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    513\u001b[0m                 \u001b[1;31m# This branch is for urllib3 v1.22 and later.\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 514\u001b[1;33m                 \u001b[1;32mraise\u001b[0m \u001b[0mSSLError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0me\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mrequest\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mrequest\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    515\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    516\u001b[0m             \u001b[1;32mraise\u001b[0m \u001b[0mConnectionError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0me\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mrequest\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mrequest\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mSSLError\u001b[0m: HTTPSConnectionPool(host='www.bqkan.com', port=443): Max retries exceeded with url: /34658_34658426/ (Caused by SSLError(SSLError(\"bad handshake: SysCallError(-1, 'Unexpected EOF')\",),))"
     ]
    }
   ],
   "source": [
    "if __name__ == \"__main__\":\n",
    "    dl = downloader()\n",
    "    dl.get_download_url()\n",
    "    print('《雪中悍刀行》开始下载：')\n",
    "    for i in range(dl.nums):\n",
    "        dl.writer(dl.names[i], '雪中悍刀行.txt', dl.get_contents(dl.urls[i]))\n",
    "        sys.stdout.write(\"  已下载:%.3f%%\" %  float(i/dl.nums*100) + '\\r')\n",
    "        sys.stdout.flush()\n",
    "    print('《雪中悍刀行》下载完成')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
