#!/../usr/bin/python3
# Mulai : Senin, 10 Agustus 2020,-19:22:18 WIB
# Done  : Senin, 10 Agustus 2020,-20:40:29 WIB
# WSite : https://www.oploverz.in
# Github: https://github.com/Ezz-Kun
# Copyright © 2020 Ezz-Kun 

from bs4 import BeautifulSoup as bs
from time import sleep
from os import system
from string import ascii_letters
import requests as req
import sys

m = '\033[1;31m'
k = '\033[1;33m'
h = '\033[1;32m'
b = '\033[1;34m'
p = '\033[1;37m'
bgb = '\033[1;44m'
cl = '\033[0m'

__banner__ = (
f'\t {b}╔═╗{p}┌─┐{b}╦ {p} ┌─┐┬  ┬┌─┐┬─┐{b}╔═╗   ╦ ╦{p}┬─┐{b}╦  \n'
f'\t ║ ║{p}├─┘{b}║  {p}│ │└┐┌┘├┤ ├┬┘{b}╔═╝{p}───{b}║ ║{p}├┬┘{b}║  \n'
f'\t ╚═╝{p}┴  {b}╩═╝{p}└─┘ └┘ └─┘┴└─{b}╚═╝   ╚═╝{p}┴└─{b}╩═╝\n'
f'{p}     {b}≼{p}──────────────────────────────────────────{b}≽\n'
f'\t    ↔ {p}Author {b}:{p} Ezz-Kun {h}(。-`ω´-) {b}↔\n'
f'\t{b}↔ {p}Tools {b}: {p}OpLoverZ.in Url Generator {b}↔\n\n'
f'{b}【 »{p}Ezz-Kun{b}« 】{m}~{b}!{p}\n'
)

__Argument__ = (
f'{b}【{h}→{p}01{h}←{b}】{p}Start \n{b}【{h}→{p}02{h}←{b}】{p}Help \n{b}【{h}→{p}03{h}←{b}】{p}Exit\n'
)

def clean():
	system('clear')

class Print(object):
	def __init__(self,string):
		for i in string +'\n':
			sys.stdout.write(str(i))
			sys.stdout.flush()
			sleep(0.00050)

class OpeLoverz(object):
	def __init__(self,judul):
		self.judul = judul
		self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.83 Safari/537.1"}
		self.komtol = (f"https://www.oploverz.in/?s={self.judul.replace(' ','+')}&post_type=post")
		self.Opz_Title(self.komtol)

	def Opz_Title(self,url):
		right = 1
		titl = ['']
		tit_url = ['']
		next_ = ['']
		info = ['']
		sux = req.get(url,headers=self.headers).text
		so = bs(sux,'html.parser')
		pages = so.find('a',class_="nextpostslink")
		prev = so.find('a',class_="previouspostslink")
		x = so.findAll('div',class_="dtl")
		if len(x) != 0:
			for joke in x:
				titl.append(joke.find('a')["title"])
				tit_url.append(joke.find('a')["href"])
				info.append(joke.find('span').get_text())
			var = 1
			clean()
			Print(__banner__)
			for c in range(len(titl)-1):
				print(f'{b}[{p}{var}{b}]{h}» {p}{titl[var]}')
				var +=1
			if pages is not None:
				print(f'\n\t {b}【 {p}Type {b}[{p}N{b}]{p} For Next {b}[{p}P{b}]{p} For Prev{b} 】')
			fuc = input(f'\n{b}[{h}→{p}Opz{h}←{b}]{h} »{p} Choice {h}⌲{b} :{p} ')
			if fuc == '':
				print(f'{b}[{h}→{p}Opz{h}←{b}]{h} »{p} Nothing Choice!')
				sleep(0.5)
				_Main()
			elif str(fuc) in ascii_letters:
				if str(fuc).lower() == 'n':
					self.Opz_Title(pages["href"])
				elif str(fuc).lower() == 'p':
					if prev is not None:
						self.Opz_Title(prev["href"])
					else:
						exit(f'{b}[{h}→{p}Opz{h}←{b}]{h} »{p}Goblok Banget Sumpah!! Page Pertama mana bisa prev amjir!')
			elif str(fuc) not in ascii_letters:
				if int(fuc) < len(titl):
					clean()
					Print(__banner__)
					Print(f'{b}[{h}→{p}Opz{h}←{b}]{h} »{p} {info[int(fuc)]}\n')
					self.Opz_Link(tit_url[int(fuc)])
				else:
					exit(f'{b}[{h}→{m}Opz{h}←{b}]{h} »{p}Maximum Out Of Range Index')
			else:
				exit(f'{b}[{h}→{m}Opz{h}←{b}]{h} »{p}Exit Tuul')
		else:
			exit(f'{b}[{h}→{m}Opz{h}←{b}]{p}Error : Tittle ``{self.judul}`` Cannot Be Found')
	def Opz_Link(self,Url):
		jo = 1
		data = ['']
		urel = ['']
		server = ['']
		poko = ['']
		infoz = ['']
		xof = req.get(Url,headers=self.headers).text
		su = bs(xof,'html.parser')
		dof = su.findAll('div',class_="sorattl title-download")
		inf = su.findAll('div',class_="dtl")
		for deku in inf:
			infoz.append(deku.find('span').get_text())
		for tamper in dof:
			data.append(tamper.get_text())
#		clean()
#		Print(__banner__)
		for neko in range(len(data)-1):
			Print(f"{b}[{p}{jo}{b}]{h}»{p}{data[jo].replace('oploverz','')}")
			jo +=1
		sun = int(input(f'\n{b}[{h}→{p}Opz{h}←{b}]{h} »{p} Choice {h}⌲{b} :{p} '))
		poko.extend(dof)
		try:
			fox = poko[sun].findNextSiblings()[1].findAll('a')
		except IndexError:
			fox = poko[sun].findNext().findAll('a')
		for ozi in fox:
			server.append(ozi.get_text())
			urel.append(ozi["href"])
		jo -= (jo - 1)
		for y in range(len(urel)-1):
			Print(f'{b}[{p}{jo}{b}]{h} » {p}{server[jo]} {b}:{p} {urel[jo]}')
			jo +=1
		shin = int(input(f'\n{b}[{h}→{p}Opz{h}←{b}]{h} »{p} Open To Browser? {h}⌲{b} :{p} '))
		if shin == '':
			_Main()
		elif shin < len(urel) - 1:
			system(f'termux-open {urel[shin]}')
			self.Opz_Title(self.komtol)
		else:
			print(f'{b}[{h}→{m}Opz{h}←{b}]{h} »{p}Nothing Choice!')
			sleep(0.4)
			_Main()

def _Main():
	clean()
	Print(__banner__)
	Toki = input(f'{b}[{h}→{p}Opz{h}←{b}]{p}Title{h} ⌲{p} : ')
	if Toki == '':
		print(f'{b}[{h}→{m}Opz{h}←{b}]{h} »{p}Nothing Choice!')
		sleep(0.4)
		_Main()
	else:
		OpeLoverz(Toki)

if __name__=="__main__":
	try:
		clean()
		Print(__banner__)
		Print(__Argument__)
		nimek = int(input(f'{b}【{h}→{p}Opz{h}←{b}】{p}Set{h} ⌲{p} : '))
		if nimek == 1:
			_Main()
		elif nimek == 2:
			clean()
			Print(__banner__)
			Print(f'{p}Jika Yang Sebelum nya adalah Versi Batch Yaitu\n{k}Kusonime.com{p} Namun Yang sekarang Adalah Versi Ketengan :v\nYaitu {k}Oploverz.in{p}, \nHampir sama kek yg sblm nya ... \nudah, gitu doang asw ..males jelasin nya :v\n\n{h}●{p} Contact Wa : 085325463021')
		elif nimek == 3:
			exit(f'{b}【{h}→{m}Opz{h}←{b}】{p} Exit Tuul !')
		else:
			exit(f'{b}【{h}→{m}Opz{h}←{b}】{p} Nothing Choice!')
	except req.exceptions.ConnectionError:
		exit(f'{b}[{m}Kuso{b}]{p} No Internet Connection! ')
	except (EOFError,ValueError,KeyboardInterrupt):
		exit('\n')
