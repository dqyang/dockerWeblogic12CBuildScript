# Copyright (c) 2018 Oracle and/or its affiliates. All rights reserved.
#
# WLST Offline for deploying an application under APP_NAME packaged in APP_PKG_FILE located in APP_PKG_LOCATION
# It will read the domain under DOMAIN_HOME by default
#
# author: Bruno Borges <bruno.borges@oracle.com>
# since: December, 2015
#
import java.lang
import os
import string

# Deployment Information
domainname = os.environ.get('DOMAIN_NAME', 'base_domain')
domainhome = os.environ.get('DOMAIN_HOME', '/u01/oracle/user_projects/domains/' + domainname)
admin_name = os.environ.get("ADMIN_NAME", "AdminServer")
xuName    = 'jrules-res-xu-WL12'
xupkg     = 'jrules-res-xu-WL12.rar'
resName    = 'jrules-res-management-WL12'
respkg     = 'jrules-res-management-WL12.ear'
appdir     = os.environ.get('APP_PKG_LOCATION', '/u01/oracle/deploy')

connect(username,password,'t3://172.17.0.2:7001')

# Deplloy Application
# ==================

deploy(appName=xuName, path=appdir + '/' + xupkg, upload="false")
deploy(appName=resName, path=appdir + '/' + respkg, upload="false")


# Disconnect
# ==========================
disconnect()
exit()
