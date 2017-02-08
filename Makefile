PY=python
PELICAN=pelican
PELICAN_CACHE=/tmp/pelican-cache/hnc
PELICANOPTS=--cache-path $(PELICAN_CACHE)

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

VENV=$(HOME)/venv/pelican-3.4/bin/activate
PRDOUTPUTDIR=/var/www/hackncast/site
TMPDIR=/tmp/build/hackncast

DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

VERB ?= 0
ifeq ($(VERB), 1)
	PELICANOPTS += -v
endif

PRD ?= 0
ifeq ($(PRD), 0)
	CONF=$(BASEDIR)/pelicanconf.py
else
	CONF=$(BASEDIR)/publishconf.py
endif

help:
	@echo 'Makefile for a pelican Web site                                                 '
	@echo '                                                                                '
	@echo 'Usage:                                                                          '
	@echo '   make html                        (re)generate the web site                   '
	@echo '   make clean                       remove the generated files                  '
	@echo '   make regenerate                  regenerate files upon modification          '
	@echo '   make publish                     generate using production settings          '
	@echo '   make serve [PORT=8000]           serve site at http://localhost:8000         '
	@echo '   make devserver [PORT=8000]       start/restart develop_server.sh             '
	@echo '   make stopserver                  stop local server                           '
	@echo '                                                                                '
	@echo 'Custom targets (Virtual Environment):                                           '
	@echo '   make all [PRD=1]                 (re)generate the whole site                 '
	@echo '   make update [PRD=1]              update the .theme folder                    '
	@echo '   make build [PRD=1]               regenerate files from site                  '
	@echo '   make envserve [PORT=8000]        serve site at http://localhost:8000         '
	@echo '   make envdevserver [PORT=8000]    start/restart develop_server.sh             '
	@echo '   make move                        move files from $(TMPDIR) to $(PRDOUTPUTDIR)'
	@echo '   make ping                        ping search engines                         '
	@echo '                                                                                '
	@echo '   make clean                       remove the whole site                       '
	@echo '   make clean-out                   remove files from $(TMPDIR)                 '
	@echo '   make clean-tmp                   remove files from $(PRDOUTPUTDIR)           '
	@echo 'Set the PRD variable to 1 to build for production, e.g. PRD=1 make all          '
	@echo 'Set the DEBUG variable to 1 to enable debugging, e.g. DEBUG=1 make all          '
	@echo 'Set the VERB variable to 1 to enable VERBOSE, e.g. VERB=1 make all              '
	@echo '                                                                                '

html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

clean:
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)/*

regenerate:
	$(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

serve:
ifdef PORT
	cd $(OUTPUTDIR) && $(PY) -m pelican.server $(PORT)
else
	cd $(OUTPUTDIR) && $(PY) -m pelican.server
endif

devserver:
ifdef PORT
	$(BASEDIR)/develop_server.sh restart $(PORT)
else
	$(BASEDIR)/develop_server.sh restart
endif

stopserver:
	kill -9 `cat pelican.pid`
	kill -9 `cat srv.pid`
	@echo 'Stopped Pelican and SimpleHTTPServer processes running in background.'

publish:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)

#################################
#    Custom Makefile targets    #
#################################
all: update build prd-clean-out move ping
update:
ifeq ($(PRD), 1)
	@if [ "$$(ls -A .theme)" ]; then \
		cd .theme; \
		git pull http://github.com/hackncast/hackncast_theme && git clean -f; \
		cd -; \
	else \
		git clone http://github.com/hackncast/hackncast_theme .theme; \
	fi
endif

build:
	. $(VENV); LC_ALL="pt_BR.UTF-8" pelican $(BASEDIR)/content -o $(TMPDIR) -s $(CONF) $(PELICANOPTS)

envserve:
ifdef PORT
	cd $(TMPDIR) && $(PY) -m pelican.server $(PORT)
else
	cd $(TMPDIR) && $(PY) -m pelican.server
endif

envdevserver:
ifdef PORT
	$(BASEDIR)/env_develop_server.sh restart $(PORT)
else
	$(BASEDIR)/env_develop_server.sh restart
endif

move:
	mv $(TMPDIR)/* $(PRDOUTPUTDIR)/

ping:
ifeq ($(PRD), 1)
	echo "Pinging Google!"
	curl -Is http://www.google.com/webmasters/tools/ping?sitemap=http://hackncast.org/sitemap.xml | grep "200 OK" || echo "Erro pinging Google"
	echo "Pinging Bing!"
	curl -Is http://www.bing.com/webmaster/ping.aspx?siteMap=http://hackncast.org/sitemap.xml | grep "200 OK" || echo "Erro pinging Bing"
endif

prd-clean: prd-clean-tmp prd-clean-out prd-clean-cache
prd-clean-out:
	rm -rf $(PRDOUTPUTDIR)/*
prd-clean-tmp:
	rm -rf $(TMPDIR)
prd-clean-cache:
	rm -rf $(PELICAN_CACHE)/*


.PHONY: help html clean regenerate serve devserver stopserver publish all update build move ping
