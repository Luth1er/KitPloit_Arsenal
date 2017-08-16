#/usr/bin/python
# -*- coding:utf-8 -*-
'''
                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007
 Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.
                            Preamble
  The GNU General Public License is a free, copyleft license for
software and other kinds of works.
  The licenses for most software and other practical works are designed
to take away your freedom to share and change the works.  By contrast,
the GNU General Public License is intended to guarantee your freedom to
share and change all versions of a program--to make sure it remains free
software for all its users.  We, the Free Software Foundation, use the
GNU General Public License for most of our software; it applies also to
any other work released this way by its authors.  You can apply it to
your programs, too.
  When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
them if you wish), that you receive source code or can get it if you
want it, that you can change the software or use pieces of it in new
free programs, and that you know you can do these things.
  To protect your rights, we need to prevent others from denying you
these rights or asking you to surrender the rights.  Therefore, you have
certain responsibilities if you distribute copies of the software, or if
you modify it: responsibilities to respect the freedom of others.
  For example, if you distribute copies of such a program, whether
gratis or for a fee, you must pass on to the recipients the same
freedoms that you received.  You must make sure that they, too, receive
or can get the source code.  And you must show them these terms so they
know their rights.
  Developers that use the GNU GPL protect your rights with two steps:
(1) assert copyright on the software, and (2) offer you this License
giving you legal permission to copy, distribute and/or modify it.
  For the developers' and authors' protection, the GPL clearly explains
that there is no warranty for this free software.  For both users' and
authors' sake, the GPL requires that modified versions be marked as
changed, so that their problems will not be attributed erroneously to
authors of previous versions.
  Some devices are designed to deny users access to install or run
modified versions of the software inside them, although the manufacturer
can do so.  This is fundamentally incompatible with the aim of
protecting users' freedom to change the software.  The systematic
pattern of such abuse occurs in the area of products for individuals to
use, which is precisely where it is most unacceptable.  Therefore, we
have designed this version of the GPL to prohibit the practice for those
products.  If such problems arise substantially in other domains, we
stand ready to extend this provision to those domains in future versions
of the GPL, as needed to protect the freedom of users.
  Finally, every program is threatened constantly by software patents.
States should not allow patents to restrict development and use of
software on general-purpose computers, but in those that do, we wish to
avoid the special danger that patents applied to a free program could
make it effectively proprietary.  To prevent this, the GPL assures that
patents cannot be used to render the program non-free.
  The precise terms and conditions for copying, distribution and
modification follow.
'''
import requests
from bs4 import BeautifulSoup
import sys,os,time
global main_option, page
page = 1

os.system('clear')
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush() # defeat buffering
        time.sleep(8./90)
#time.sleep(10./90)

def fastprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush() # defeat buffering
        time.sleep(1./50)

def Animation(String, color):
    animation = "|/-\\"
    for i in range(15):
        time.sleep(0.1)
        sys.stdout.write("\r" + "[" + animation[i % len(animation)] + "]" + color + String)
        sys.stdout.flush()
    print('')

class Lab_Collors():
    vermelho = '\033[31m'
    verde = '\033[32m'
    azul = '\033[34m'
    ciano = '\033[36m'
    purple = '\033[35m'
    amarelo = '\033[33m'
    preto = '\033[30m'
    branco = '\033[37m'
    Verde_claro = '\033[39m'
    original = '\033[0;0m'

class Banner():
	ban = '''                         .s$$$Ss.                         _......
             .8,         $$$. _. .              ..sS$$$$$"  ...,.;
  o.   ,@..  88        =.$"$'  '          ..sS$$$$$$$$$$$s. _;"'
   @@@.@@@. .88.   `  ` ""l. .sS$$.._.sS$$$$$$$$$$$S'"'
    .@@@q@@.8888o.         .s$$$$$$$$$$$$$$$$$$$$'
      .:`@@@@33333.       .>$$$$$$$$$$$$$$$$$$'                                                   ⓀⓘⓣⓅⓛⓞⓘⓣ
   ☣  .: `@@@@333'       ..>$$$$$$$$$$$$$$$$$$'                   COPYRIGHT © 2017 KITPLOIT - PENTEST TOOLS FOR YOUR SECURITY ARSENAL ☣
 ☣     :  `@@333.     `.,   s$$$$$$${}$$$'
       :   `@33       $$ S.s$$$$$$$$$$$$$$$$$'                                     MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
  ☣ ☣  .S   `Y      ..`  ,"$' `$$$$$$$$$$$$$$                                      MMMMMMMMMMMMMMd/-          ``-odMMMMMMMMMMMMMM
       $s  .       ..S$s,    . .`$$$$$$$$$$$$.                                     MMMMMMMMMMMMd/`               `.sMMMMMMMMMMMMM
  ☣    $s .,      ,s ,$$$$,,sS$s.$$$$$$$$$$$$$.                                    MMMMMMMMMMMh                     -hMMMMMMMMMMM
       / /$$SsS.s. ..s$$$$$$$$$$$$$$$$$$$$$$$$$.                                   MMMMMMMMMMN.                     `oNMMMMMMMMMM
 ☣    /`.`$$$$$dN.ssS$$'`$$$$$$$$$$$$$$$$$$$$$$$.           {}        MMMMMMMMMMm`                      :+ooMMMMMMMM
     ///   `$$$$$$$$$'    `$$$$$$$$$$$$$$$$$$$$$$.                                 MMMMMMMMMMy`   `-///:.               -NMMMMMMM
  ☣ ///|     `S$$S$'       `$$$$$$$$$$$$$$$$$$$$$$.         {}             MMMMMMMMMh`    .+:-:/:               .dMMMMMMM
 ☣ / /                      $$$$$$$$$$$$$$$$$$$$$.                                 MMMMMMMMM-     `/s/s+.               .hhymMMMM
                            `$$$$$$$$$$$$$$$$$$$$$s.        {}              MMMdhhhmMo`    `.``.`.              .:-``+NMMM
   ☣                         $$$"'        .?T$$$$$$$                               My:.` `.oNy+.`                     :dy` `+mMMM
 ☣    ☣                     .$'        ...      ?$$#        {}  myos/`  `omNdy-                ./`-hMN.  `-hMM
                            !       -=S$$$$$s                                      /...-`   `:yNMo.              ./.-yNd+     /NM
   ☣                      .!       -=s$$'  `$=-_      :     {}     Nh/.    .` `:oyh+-`        ``.-:/ys:```.`  -dM
☣      ☣                 ,        .$$$'     `$,       .|                           MMN+..---..`  `--:++/-..-:oyyo++:-.:+ydh:  -mM
    ☣                   ,       .$$$'          .        ,   {}                MMMdhmmmmmdy+-`   `-/ohhyo/-```.+ydNMMMy` `sMM
                       ,     ..$$$'                                                MMMMNNNMMMMMMNs/.`    ``   `./smMMMMMMm-``+NMM
     ☣                     .s$$$'                 `s     .                         MMho--sMMMMMMMmmh/.       `/ymNMMMMMMMm/shNMMM
  ☣    ☣            .   .s$$$$'                    $s. ..$s                        Mh. `+mMMMMMMy.``  `.//.`   `.:dmMMMMMNNNMMMMM
                   .  .s$$$$'                      `$s=s$$$                        Mo  .dMMNhy::.``-:ohmMMmy+-``  ``/:/s/:::oNMMM
    ☣                .$$$$'                         ,    $$s                       d.  -hy/-``.:oydmNMMMMMMMMmhys:.    `   .sdMMM
☣               `   " .$$'                               $$$                       d-   ` `-+hmNMMMMMMMMMMMMMMMMMNm+. `.   ``.yNM
   ☣            ,   s$$'                              .  $$$s                      Ms    -hNMMMMMMMMMMMMMMMMMMMMMMMNh:`   :yyoodM
 ☣           ` .s..s$'                                .s ,$$                       Mh-`  +NMMMMMMMMM ⓀⓘⓣⓅⓛⓞⓘⓣ MMMMMMMd/`  .:::hMM
     ☣        .s$$$'                                   "s$$$,                      MMNo` `+mMMMMMMMMMMMMMMMMMMMMMMMMMMNh+::/oymMM
    ☣      -   $$$'                                     .$$$$.                     MMMs.`.+mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
         ."  .s$$s                                     .$',',$.              
.........$s.s$$$$S..............   ................    $$....s$s............... .......................................................'''


	Exploit_ban = '''
                            ,-.^._                 _
                           .'      `-.            ,' ;
                /`-.  ,----'         `-.   _  ,-.,'  `                  {}
             _.'   `--'                 `-' '-'      ;                                          {}
            :                         *             ;    __,-.          {}
            ,'    *            Mazar-i-Sharif       ;_,-',.__'--.                               {}
           :    Herat                              ,--```    `--'       {}
           :                                      ;                                             {}
           :               *                       :                     {}                    
           ;          Coder X Coder                :                                             {}
          (                                       ;                                           
           `-.                           *      ,'
             ;      *                  Kabul   :                                             
           .'   Black Crow                 .-._,'
         .'                               `.
      _.'                                .__;
      `._                  *            ;                               
         `.             Kandahar       :    ,------------------------.  ==========> [Exiting Here!] 
           `.               ,..__,---._;    |        Moskov          |           
             `-.__         :                | Capital: Kabul         |                 {}
                  `.--.____;      Gr        | Pop: 28,150,000 (2009) |
                                            | Area: 251,772 sq.mi.   |
                                            |      (652,086 sq.km.)  |
                                            `------------------------'
'''

class urls():
	Recents = [	'http://www.kitploit.com',
				'http://www.kitploit.com/search?updated-max=2017-07-20T19%3A46%3A00-04%3A00&max-results=9',
				'http://www.kitploit.com/search?updated-max=2017-07-15T10%3A30%3A00-04%3A00&max-results=9',
				'http://www.kitploit.com/search?updated-max=2017-07-09T11%3A02%3A00-04%3A00&max-results=9',
				'http://www.kitploit.com/search?updated-max=2017-07-03T11%3A30%3A00-04%3A00&max-results=9',
				'http://www.kitploit.com/search?updated-max=2017-06-25T10%3A30%3A00-04%3A00&max-results=9',
				'http://www.kitploit.com/search?updated-max=2017-06-17T11%3A25%3A00-04%3A00&max-results=9',
				'http://www.kitploit.com/search?updated-max=2017-06-09T11%3A38%3A00-04%3A00&max-results=9',
				'http://www.kitploit.com/search?updated-max=2017-06-01T11%3A12%3A00-04%3A00&max-results=9',
				'http://www.kitploit.com/search?updated-max=2017-05-23T11%3A01%3A00-04%3A00&max-results=9',
			]
	Android = ['http://www.kitploit.com/search/label/Android', 'http://www.kitploit.com/search/label/Android?updated-max=2016-06-01T19:13:00-04:00&max-results=20&start=20&by-date=false', 'http://www.kitploit.com/search/label/Android?updated-max=2016-12-27T11%3A30%3A00-03%3A00&max-results=9', 'http://www.kitploit.com/search/label/Android?updated-max=2016-07-09T15%3A31%3A00-04%3A00&max-results=9', 'http://www.kitploit.com/search/label/Android?updated-max=2015-10-24T20%3A07%3A00-03%3A00&max-results=9', 'http://www.kitploit.com/search/label/Android?updated-max=2015-01-31T12%3A31%3A00-03%3A00&max-results=9']
	Iphone  = 'http://www.kitploit.com/search/label/iPhone'


class Exploit_KitPloit_Setup():
	Exploit_Colector       = "1) Exploit Collector"
	DDoS                   = "2) Denial Of Service (DDoS)"            
	Remote_code_execution  = "3) Remote Code Execution"               
	SQLI                   = "4) SQL Injection"
	Overflow               = "5) Overflow's"
	XSS                    = "6) XSS"
	File_Upload            = "7) File Upload"
	Search                 = "8) Advanced Search"
	Exit                   = "9) Exit"
class Setup_Menu_Options():
	PL_Symbol              = "> PL <"
	Recents_Posts          = "1) RECENT POSTS"
	Android                = "2) Android"
	IPHONE                 = "3) IPHONE"
	Exploits_Arsenal       = "4) Exploits Arsenal ☣"
	Advanced_search        = "5) Advanced Search"
	Exit                   = "6) Exit"


def get_http(url):
	url = '{}'.format(url)
	try:
		return requests.get(url)
	except (requests.exceptions.HTTPError, requests.exceptions.RequestsException, requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
		print(str(e))
		pass
	except Exception as e:
		raise

def parse_HomePage(content):

	soup = BeautifulSoup(content, 'lxml')

	Feed_Div = soup.find_all('div',{'class':'retitle'})

	for feed in Feed_Div:
		info_feed = [feed.a.get('href'), feed.a.string]
		title  = info_feed[1].encode("utf-8")
		title = title.replace('\n','')
		print "----------------------------------------------------------------------------------"
		print ''
		print Lab_Collors.verde+"[+] Title: {}".format(Lab_Collors.azul+title)
		r = get_http(str(info_feed[0]))
		if r:
			Parse_description(r.text)
		print Lab_Collors.amarelo+"[+] url: {}".format(Lab_Collors.ciano+str(info_feed[0]))
		print ''

def Parse_description(content):
	soup = BeautifulSoup(content, 'lxml')
	about_br_tags = soup.find_all('div',{'class':'post-body entry-content'})[0]
	try:
		Feed_Div = soup.find_all('div',{'style':'text-align: justify;'})[0].text
		Information_exploit = soup.find_all('div',{'class':'post-body entry-content'})[0].text
		st1pped = Feed_Div.strip()
		print ''
		print Lab_Collors.branco+"[+] Description: {}".format(Lab_Collors.purple+st1pped)
	except:
		limit = 0
		for br in about_br_tags:
			if limit == 2:
				break;
			br = br.string
			if br != None and br != '\n':
				br = br.strip()
				if limit == 0:
					print ''
					print Lab_Collors.branco+'Description:',br
				else:
					print br
				limit += 1
	print ''

def parse_links(content):

	soup = BeautifulSoup(content, 'lxml')

	Feed_Div = soup.find_all('div',{'class':'post-title-container'})
	Title_Exploits_Div = soup.find_all('div',{'class':'r-snippetized'})
	for feed in Feed_Div:
		info_feed = [feed.h3.a.get('href'), feed.a.string]
		link = str(info_feed[0])
		print ''
		r = get_http(link)
		if r:
			parse__Exploited(r.text, link)

def parse__Exploited(content, link):

	try:
		soup = BeautifulSoup(content, 'lxml')
		Title_Exploits_Div = soup.find_all('div',{'class':'post-title-container'})[0].text
		Title_Exploits_Div = Title_Exploits_Div.strip()
		print Lab_Collors.vermelho+'---------------------------------------------------------------------------------------------------------------------------------------'
		print Lab_Collors.verde+"[+] Title: {}".format(Lab_Collors.azul+Title_Exploits_Div)
		print ''
	except:
		pass

	try:
		Information_exploit = soup.find_all('div',{'id':'vulnerability'})[0].text
		Information_exploit = Information_exploit.strip()
		print Lab_Collors.branco+'[+] Description: '+Lab_Collors.amarelo+Information_exploit

		print Lab_Collors.vermelho+'---------------------------------------------------------------------------------------------------------------------------------------'
		print ''
	except:
		pass


	try:
		Information_exploit = soup.find_all('div',{'class':'post-body entry-content float-container'})
		Strong_Divs = soup.find_all("strong")
		for strong_string in Strong_Divs:
		    print Lab_Collors.vermelho+strong_string.text+Lab_Collors.vermelho+strong_string.next_sibling
	except:
		pass
	try:
		print Lab_Collors.amarelo+"[+] Exploit: {}".format(Lab_Collors.ciano+link)
		#time.sleep(2)
	except:
		pass


def loop_infinite(content):
	global page
	try:
		soup = BeautifulSoup(content, 'lxml')
		More_Posts = soup.find_all('div',{'class':'blog-pager container'})
		for a_tag in More_Posts:
			a_tag = [a_tag.a.get('href')]
		new_url  = str(a_tag[0])
		get_tag  = get_http(new_url)
		page += 1
		print ''
		Animation('Page {}'.format(page), Lab_Collors.branco)
		if get_tag:
			parse_links(get_tag.text)
			loop_infinite(get_tag.text)
	except Exception as e:
		print ''
		print Lab_Collors.vermelho+'_> D A N G E R <_ %s' % e
		print ''

def Exploit_Arsenal_Advanced_Scraping():
	os.system('clear')
	print Lab_Collors.azul+Banner.Exploit_ban.format(Lab_Collors.ciano+Exploit_KitPloit_Setup.Exploit_Colector+Lab_Collors.azul, 
												Lab_Collors.verde+Exploit_KitPloit_Setup.DDoS+Lab_Collors.azul, 
												Lab_Collors.amarelo+Exploit_KitPloit_Setup.Remote_code_execution+Lab_Collors.azul, 
												Lab_Collors.branco+Exploit_KitPloit_Setup.SQLI+Lab_Collors.azul,
												Lab_Collors.purple+Exploit_KitPloit_Setup.Overflow+Lab_Collors.azul,
												Lab_Collors.verde+Exploit_KitPloit_Setup.XSS+Lab_Collors.azul,
												Lab_Collors.ciano+Exploit_KitPloit_Setup.File_Upload+Lab_Collors.azul,
												Lab_Collors.amarelo+Exploit_KitPloit_Setup.Search+Lab_Collors.azul,
												Lab_Collors.vermelho+Exploit_KitPloit_Setup.Exit+Lab_Collors.azul
												)
	fastprint(Lab_Collors.amarelo+"   ☣ Telegram Channel: @Phantasm_Lab"+Lab_Collors.ciano+"               ☣ Telegram: @DreadPirateRobert"+Lab_Collors.vermelho+"           ☣ GitHub: github.com/Luth1er")
	print Lab_Collors.Verde_claro+'......................................................................................................................................'
	sair = False	
	while not sair:
		Choose_the_Option = raw_input(Lab_Collors.azul+'[+] Choose the option: ')
		if Choose_the_Option == '1':
			url = "http://exploit.kitploit.com/"
			get_request = get_http(url)
			if get_request:
				parse_links(get_request.text)
				print ''
				loop_infinite(get_request.text)

		if Choose_the_Option == '2':
			DOS = 'http://exploit.kitploit.com/search?q=Denial%20of%20Service'
			get_request = get_http(DOS)
			if get_request:
				parse_links(get_request.text)
				print ''
				loop_infinite(get_request.text)
		elif Choose_the_Option == '3':
			Remote = 'http://exploit.kitploit.com/search?q=Remote'
			get_request = get_http(Remote)
			if get_request:
				parse_links(get_request.text)
				print ''
				loop_infinite(get_request.text)
		elif Choose_the_Option == '4':
			SQLI = 'http://exploit.kitploit.com/search?q=SQL%20Injection'
			get_request = get_http(SQLI)
			if get_request:
				parse_links(get_request.text)
				print ''
				loop_infinite(get_request.text)
		elif Choose_the_Option == '5':
			Overflow = 'http://exploit.kitploit.com/search?q=Overflow'
			get_request = get_http(Overflow)
			if get_request:
				parse_links(get_request.text)
				print ''
				loop_infinite(get_request.text)
		elif Choose_the_Option == '6':
			XSS = 'http://exploit.kitploit.com/search?q=XSS'
			get_request = get_http(XSS)
			if get_request:
				parse_links(get_request.text)
				print ''
				loop_infinite(get_request.text)
		elif Choose_the_Option == '7':
			File_Upload = 'http://exploit.kitploit.com/search?q=File%20Upload'
			get_request = get_http(File_Upload)
			if get_request:
				parse_links(get_request.text)
				print ''
				loop_infinite(get_request.text)
		elif Choose_the_Option == '8':
			Search_exp9   = raw_input('[+] $earch_Vulnerability _> ')
			exp9_full_url = 'http://exploit.kitploit.com/search?q={}'.format(Search_exp9)
			exp9          = exp9_full_url.replace(' ', '%')
			exp9_request  = get_http(exp9)
			if exp9_request:
				parse_links(exp9_request.text)
				print ''
				loop_infinite(exp9_request.text)
		elif Choose_the_Option == '9':
			sair = True
			Animation("Exiting", Lab_Collors.vermelho)
			print ''
			sys.exit(1)
		elif Choose_the_Option == 'clear':
			os.system('clear')

def Kit_Ploit_Home():
	print Lab_Collors.Verde_claro+Banner.ban.format(
												Lab_Collors.amarelo+Setup_Menu_Options.PL_Symbol+Lab_Collors.Verde_claro,
												Lab_Collors.ciano+Setup_Menu_Options.Recents_Posts+Lab_Collors.Verde_claro, 
												Lab_Collors.azul+Setup_Menu_Options.Android+Lab_Collors.Verde_claro, 
												Lab_Collors.amarelo+Setup_Menu_Options.IPHONE+Lab_Collors.Verde_claro, 
												Lab_Collors.branco+Setup_Menu_Options.Exploits_Arsenal+Lab_Collors.Verde_claro,
												Lab_Collors.purple+Setup_Menu_Options.Advanced_search+Lab_Collors.Verde_claro,
												Lab_Collors.verde+Setup_Menu_Options.Exit+Lab_Collors.Verde_claro)
	fastprint(Lab_Collors.amarelo+"   ☣ Telegram Channel: @Phantasm_Lab"+Lab_Collors.ciano+"               ☣ Telegram: @DreadPirateRobert"+Lab_Collors.vermelho+"           ☣ GitHub: github.com/Luth1er")
	print Lab_Collors.Verde_claro+'......................................................................................................................................'
	sair = False
	while not sair:
		main_option = raw_input(Lab_Collors.vermelho+'[-] Enter an Option: ')
		if main_option == '1':
			for url in urls.Recents:
				r = get_http(url)
				if r:
					parse_HomePage(r.text)
					_next = raw_input('[+] You can next ? [n/Y] > ')
					if _next == 'y':
						pass
					else:
						break;

		elif main_option == '2':
			for url in urls.Android:
				r = get_http(url)
				if r:
					parse_HomePage(r.text)
					_next = raw_input('[+] You can next ? [n/Y] > ')
					if _next == 'y':
						pass
					else:
						break;
						os.system('clear')
						Banner()
		elif main_option == '3':
			r = get_http(urls.Iphone)
			if r:
				parse_HomePage(r.text)
		
		elif main_option == '4':
			Exploit_Arsenal_Advanced_Scraping()
				
		elif main_option == '5':
			_search    = raw_input('\n$earch _> ')
			_search    = _search.replace(' ', '%')
			url        = 'http://www.kitploit.com/search/max-results=7?q={}'.format(_search)
			Get_search = get_http(url) 
			if Get_search:
				parse_HomePage(Get_search.text)

		elif main_option == '6':
			sair = True
			Animation('Exiting')
			print ''
			sys.exit(1)

		elif main_option == 'clear':
			os.system('clear')

Kit_Ploit_Home()
