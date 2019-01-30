# Copyright (c) 2018 Oracle and/or its affiliates. All rights reserved.
#
# WLST Offline for deploying an application under APP_NAME packaged in APP_PKG_FILE located in APP_PKG_LOCATION
# It will read the domain under DOMAIN_HOME by default
#
# author: Daniel Yang 
# since: Jan. 2019
#
import os

# Deployment Information
domainname = os.environ.get('DOMAIN_NAME', 'base_domain')
domainhome = os.environ.get('DOMAIN_HOME', '/u01/oracle/user_projects/domains/' + domainname)
admin_server_name = os.environ.get("ADMIN_NAME", "AdminServer")

# Read Domain in Offline Mode
# ===========================
readDomain(domainhome)

# Create Datasource
# ==================
create(resdsname, 'JDBCSystemResource')
cd('/JDBCSystemResource/' + resdsname + '/JdbcResource/' + resdsname)
cmo.setName(resdsname)

cd('/JDBCSystemResource/' + resdsname + '/JdbcResource/' + resdsname)
create('myJdbcDataSourceParams','JDBCDataSourceParams')
cd('JDBCDataSourceParams/NO_NAME_0')
set('JNDIName', java.lang.String(resdsjndiname))
set('GlobalTransactionsProtocol', java.lang.String('TwoPhaseCommit'))

cd('/JDBCSystemResource/' + resdsname + '/JdbcResource/' + resdsname)
create('myJdbcDriverParams','JDBCDriverParams')
cd('JDBCDriverParams/NO_NAME_0')
set('DriverName', xadriver)
set('URL', resdsurl)
set('PasswordEncrypted', resdspassword)
set('UseXADataSourceInterface', 'true')

print 'create JDBCDriverParams Properties'
create('myProperties','Properties')
cd('Properties/NO_NAME_0')
create('user','Property')
cd('Property/user')
set('Value', resdsusername)

cd('../../')
create('databaseName','Property')
cd('Property/databaseName')
set('Value', dsdbname)

print 'create JDBCConnectionPoolParams'
cd('/JDBCSystemResource/' + resdsname + '/JdbcResource/' + resdsname)
create('myJdbcConnectionPoolParams','JDBCConnectionPoolParams')
cd('JDBCConnectionPoolParams/NO_NAME_0')
set('TestTableName','SQL SELECT 1 FROM DUAL')

# Assign
# ======
assign('JDBCSystemResource', resdsname, 'Target', admin_server_name)

# Update Domain, Close It, Exit
# ==========================
updateDomain()
closeDomain()
exit()
