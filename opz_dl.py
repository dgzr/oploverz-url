#!/data/data/com.termux/files/usr/bin/python
# Update : (2020-09-03 23:04:09)
# Finish : Now!
# © Copyright 2020 | Ezz-Kun | kyun-kyunnn
from bs4 import BeautifulSoup as bs_
from os import system as _Auth
from string import ascii_letters as _ascii
from time import sleep
from random import randint
import requests as req_
import sys

b = '\033[1;34m'
h = '\033[1;32m'
p = '\033[1;37m'
m = '\033[1;31m'

class _print(object):
	def __init__(self,string):
		for i in string +'\n':
			sys.stdout.write(str(i))
			sys.stdout.flush()
			sleep(0.00050)

__banner__ = (f""" {b}╔═╗{p}┌─┐{b}╦  {p}┌─┐┬  ┬┌─┐┬─┐{b}╔═╗   ╦ ╦{p}┬─┐{b}╦
 {b}║ ║{p}├─┘{b}║  {p}│ │└┐┌┘├┤ ├┬┘{b}╔═╝{p}───{b}║ ║{p}├┬┘{b}║
 ╚═╝{p}┴  {b}╩═╝{p}└─┘ └┘ └─┘┴└─{b}╚═╝   ╚═╝{p}┴└─{b}╩═╝
 ┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈{b}≻
 {b}[{h}≈{b}]{p} Author {b}:{p} Ezz-Kun {b}|{h} (´•ω•`๑)
 {b}[{h}≈{b}]{p} Tools  {b}:{p} Oploverz {m}~{p} Url
 {b}[{h}≈{b}]{p} Versi  {b}:{p} {randint(10,999)}.{randint(10,100)} Update{m} !
 
 {h}► {b}[{p}Oploverz{b}]{h} ◄
""")

class _OpLoverz(object):
	def __init__(self,url):
		if 'https://' not in url:
			self.url = (f"https://www.oploverz.in/?s={url.replace(' ','+')}&post_type=post")
		else:
			self.url = url
		self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.83 Safari/537.1"}
		self.judul = []
		self.href_ = []
		self.info = []
		self.links = []
		self.server = []
		self.sorattl = []
		self._GetInformation(self.url)
	def _GetInformation(self,url_):
		try:
			_shogi = req_.get(url_,headers=self.headers).text
			_bes = bs_(_shogi,'html.parser')
			_data = _bes.findAll('div',class_='dtl')
			next_ = _bes.find('a',class_='nextpostslink',rel='next')
			prev_ = _bes.find('a',class_='previouspostslink',rel='prev')
			if len(_data) != 0:
				for cek_ in _data:
					self.judul.append(cek_.find('a')["title"])
					self.href_.append(cek_.find('a')["href"])
					self.info.append(cek_.find('span').text)
				_Auth('clear')
				_print(__banner__)
				for yui, yui_ in enumerate(self.judul):
					_print(f' {b}[{p}{yui+1}{b}].{p}{yui_}')
				if next_ != None:
					_print(f"""
	                {b}[{h}» {p}{_bes.find('span',class_='pages').text} {h}«{b}]{p}
	     {b}[{p} Type {b}[{p}N{b}]{p} For Next Type {b}[{p}P{b}]{p} For Prev {b}]{p}""")
				_cos = input(f'\n {b}[{h}»{p}Opz{h}«{b}]{p} Choice {b}≽{p} ')
				if _cos == '':
					exit(f' {b}[{h}»{p}Opz{h}«{b}]{p} Choice Is None !')
				elif str(_cos) in _ascii:
					if str(_cos).lower() == 'n':
						_OpLoverz(next_["href"])
					elif str(_cos).lower() == 'p':
						if prev_ != None:
							_OpLoverz(prev_["href"])
						else:
							exit(f' {b}[{h}»{p}Opz{h}«{b}]{p} Can Not Previous First Pages!')
				elif str(_cos) not in _ascii:
					if int(_cos)-1 < len(self.href_):
#						print(self.href_)
						self._downloadPages(self.href_[int(_cos)-1])
					else:
						exit(f' {b}[{m}»{p}Err{m}«{b}]{p} Your Choice Out Of Index!')
				else:
					exit(f' {b}[{m}»{p}Err{m}«{b}]{p} Invalid Choice!')
			else:
				exit(f' {b}[{m}»{p}Err{m}«{b}]{p} Title ``url`` Not Found In Oploverz')		
		except req_.exceptions.ConnectionError:
			exit(f' {b}[{m}»{p}Err{m}«{b}]{p} No Internet Connection{m}!')
		except (EOFError,KeyboardInterrupt):
			exit(f' {b}[{m}»{p}Err{m}«{b}]{p} Passing{m}!{p}')
	def _downloadPages(self,_url):
		try:
			_shogi = req_.get(_url,headers=self.headers).text
			_bes = bs_(_shogi,'html.parser')
			sora_ttl = _bes.findAll('div',class_='sorattl title-download')
			sora_url = _bes.findAll('div',class_='soraurl list-download')
			list(self.sorattl.append(_.text.split(' – ')[-1]) for _ in sora_ttl)
			_Auth('clear')
			_print(__banner__)
			for ciu, ciu_ in enumerate(self.sorattl):
				_print(f' {b}[{p}{ciu+1}{b}].{p}{ciu_}')
			_sor = int(input(f'\n {b}[{h}»{p}Opz{h}«{b}]{p} Choice {b}≽{p} '))
			if (_sor-1) < len(sora_url):
				for cek in sora_url[_sor-1].findAll('a'):
					self.server.append(cek.text)
					self.links.append(cek["href"])
				for serv, serv_ in enumerate(self.server):
					_print(f' {b}[{p}{serv+1}{b}].{p}{serv_} {b}≽{p} {self.links[serv]}')
				_opz = int(input(f'\n {b}[{h}»{p}Opz{h}«{b}]{p} Open To Browser {b}≽{p} '))
				if (_opz-1) < len(self.links):
#					print(self.links[_opz-1])
					_Auth(f'termux-open {self.links[_opz-1]}')
					_OpLoverz(self.url)
				else:
					exit(' {b}[{m}»{p}Err{m}«{b}]{p} Your Choice Out Of Range{m}!{p}')
			else:
				exit(' {b}[{m}»{p}Err{m}«{b}]{p} Your Choice Out Of Range{m}!{p}')
		except req_.exceptions.ConnectionError:
			exit(f' {b}[{m}»{p}Err{m}«{b}]{p} No Internet Connection{m}!')
		except (EOFError,KeyboardInterrupt,ValueError):
			exit(f' {b}[{m}»{p}Err{m}«{b}]{p} Passing{m}!{p}')

def _MainOpz():
	_Auth('clear')
	_print(__banner__)
	print(f""" {b}[{p}01{b}].{p}Search Title
 {b}[{p}02{b}].{p}More Information
 {b}[{p}03{b}].{p}Exit""")
	try:
		_cus = int(input(f'\n {b}[{h}»{p}Opz{h}«{b}]{p} Choice {b}≽{p} '))
		if _cus == '':
			exit(f' {b}[{h}»{p}Opz{h}«{b}]{p} Choice Is Nothing!')
		elif _cus == 1:
			_Auth('clear')
			_print(__banner__)
			jdl_ = input(f' {b}[{h}»{p}Opz{h}«{b}]{p} Title {b}≽{p} ')
			if jdl_ == '':
				exit(f' {b}[{h}»{p}Opz{h}«{b}]{p} Title Is Nothing!')
			else:
				_OpLoverz(jdl_)
		elif _cus == 2:
			_print(f"""
 {m}▪{p} Gak Ada Yang Beda ,Cuman Fix Error Doang Gak Ada
   Function Auto Download Nya, Sengaja Lewat Open Browser
   Biar Bisa Ke UC Browser& Download Juga Jadi Wuzz.. Wuzz..
 {m}▪{p} Yang Nama Nya Web Anime Ya Pasti Gak Ada Yang
   Lengkap, Kalau Anime Yang Di Cari Gak Ada Di Oploverz
   Bisa Pake Yg Neonime, Kalau Batch Bisa Pake Yg Kusonime
 {b}▪{p} Versi KusoNime {b}≽{p} https://github.com/Ezz-Kun/kusonime-url
 {b}▪{p} Versi NeoNime {b}≽{p} https://github.com/Ezz-Kun/neonime-url
 {h}▪{p} Contact Wa : 085325463021
""")
			input(f' {b}[{h}»{p}Opz{h}«{b}]{p} Enter To Back!')
			_MainOpz()
		elif _cus == 3:
			exit(f' {b}[{m}»{p}Err{m}«{b}]{p} Exit Tools{m}!')
		else:
			exit(f' {b}[{h}»{p}Opz{h}«{b}]{p} Invalid Choice!')
	except (ValueError,KeyboardInterrupt,EOFError):
		exit(f' {b}[{m}»{p}Err{m}«{b}]{p} Something Error{m}!{p}')

if __name__=="__main__":
	_MainOpz()
