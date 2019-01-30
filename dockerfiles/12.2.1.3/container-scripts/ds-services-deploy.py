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

# Create vida Datasource
# ==================
create(vidadsname, 'JDBCSystemResource')
cd('/JDBCSystemResource/' + vidadsname + '/JdbcResource/' + vidadsname)
cmo.setName(vidadsname)

cd('/JDBCSystemResource/' + vidadsname + '/JdbcResource/' + vidadsname)
create('myJdbcDataSourceParams','JDBCDataSourceParams')
cd('JDBCDataSourceParams/NO_NAME_0')
set('JNDIName', java.lang.String(vidadsjndiname))
set('GlobalTransactionsProtocol', java.lang.String('TwoPhaseCommit'))

cd('/JDBCSystemResource/' + vidadsname + '/JdbcResource/' + vidadsname)
create('myJdbcDriverParams','JDBCDriverParams')
cd('JDBCDriverParams/NO_NAME_0')
set('DriverName', xadriver)
set('URL', servicedsURL)
set('PasswordEncrypted', vidadspassword)
set('UseXADataSourceInterface', 'true')

print 'create JDBCDriverParams Properties'
create('myProperties','Properties')
cd('Properties/NO_NAME_0')
create('user','Property')
cd('Property/user')
set('Value', vidadsusername)

cd('../../')
create('databaseName','Property')
cd('Property/databaseName')
set('Value', dsdbname)

print 'create JDBCConnectionPoolParams'
cd('/JDBCSystemResource/' + vidadsname + '/JdbcResource/' + vidadsname)
create('myJdbcConnectionPoolParams','JDBCConnectionPoolParams')
cd('JDBCConnectionPoolParams/NO_NAME_0')
set('TestTableName','SQL SELECT 1 FROM DUAL')

# Create letters Datasource
# ==================
cd('/')
create(lettersdsname, 'JDBCSystemResource')
cd('/JDBCSystemResource/' + lettersdsname + '/JdbcResource/' + lettersdsname)
cmo.setName(lettersdsname)

cd('/JDBCSystemResource/' + lettersdsname + '/JdbcResource/' + lettersdsname)
create('myJdbcDataSourceParams','JDBCDataSourceParams')
cd('JDBCDataSourceParams/NO_NAME_0')
set('JNDIName', java.lang.String(lettersdsjndiname))
set('GlobalTransactionsProtocol', java.lang.String('TwoPhaseCommit'))

cd('/JDBCSystemResource/' + lettersdsname + '/JdbcResource/' + lettersdsname)
create('myJdbcDriverParams','JDBCDriverParams')
cd('JDBCDriverParams/NO_NAME_0')
set('DriverName', xadriver)
set('URL', servicedsURL)
set('PasswordEncrypted', lettersdspassword)
set('UseXADataSourceInterface', 'true')

print 'create JDBCDriverParams Properties'
create('myProperties','Properties')
cd('Properties/NO_NAME_0')
create('user','Property')
cd('Property/user')
set('Value', lettersdsusername)

cd('../../')
create('databaseName','Property')
cd('Property/databaseName')
set('Value', dsdbname)

print 'create JDBCConnectionPoolParams'
cd('/JDBCSystemResource/' + lettersdsname + '/JdbcResource/' + lettersdsname)
create('myJdbcConnectionPoolParams','JDBCConnectionPoolParams')
cd('JDBCConnectionPoolParams/NO_NAME_0')
set('TestTableName','SQL SELECT 1 FROM DUAL')


# Create task Datasource
# ==================
cd('/')
create(taskdsname, 'JDBCSystemResource')
cd('/JDBCSystemResource/' + taskdsname + '/JdbcResource/' + taskdsname)
cmo.setName(taskdsname)

cd('/JDBCSystemResource/' + taskdsname + '/JdbcResource/' + taskdsname)
create('myJdbcDataSourceParams','JDBCDataSourceParams')
cd('JDBCDataSourceParams/NO_NAME_0')
set('JNDIName', java.lang.String(taskdsjndiname))
set('GlobalTransactionsProtocol', java.lang.String('TwoPhaseCommit'))

cd('/JDBCSystemResource/' + taskdsname + '/JdbcResource/' + taskdsname)
create('myJdbcDriverParams','JDBCDriverParams')
cd('JDBCDriverParams/NO_NAME_0')
set('DriverName', xadriver)
set('URL', servicedsURL)
set('PasswordEncrypted', taskdspassword)
set('UseXADataSourceInterface', 'true')

print 'create JDBCDriverParams Properties'
create('myProperties','Properties')
cd('Properties/NO_NAME_0')
create('user','Property')
cd('Property/user')
set('Value', taskdsusername)

cd('../../')
create('databaseName','Property')
cd('Property/databaseName')
set('Value', dsdbname)

print 'create JDBCConnectionPoolParams'
cd('/JDBCSystemResource/' + taskdsname + '/JdbcResource/' + taskdsname)
create('myJdbcConnectionPoolParams','JDBCConnectionPoolParams')
cd('JDBCConnectionPoolParams/NO_NAME_0')
set('TestTableName','SQL SELECT 1 FROM DUAL')


# Create JMS NonXA Datasource
# ==================
cd('/')
create(jmsdsname, 'JDBCSystemResource')
cd('/JDBCSystemResource/' + jmsdsname + '/JdbcResource/' + jmsdsname)
cmo.setName(jmsdsname)

cd('/JDBCSystemResource/' + jmsdsname + '/JdbcResource/' + jmsdsname)
create('myJdbcDataSourceParams','JDBCDataSourceParams')
cd('JDBCDataSourceParams/NO_NAME_0')
set('JNDIName', java.lang.String(jmsdsjndiname))
set('GlobalTransactionsProtocol', java.lang.String('TwoPhaseCommit'))

cd('/JDBCSystemResource/' + jmsdsname + '/JdbcResource/' + jmsdsname)
create('myJdbcDriverParams','JDBCDriverParams')
cd('JDBCDriverParams/NO_NAME_0')
set('DriverName', nonXaDriver)
set('URL', servicedsURL)
set('PasswordEncrypted', jmsdspassword)
set('UseXADataSourceInterface', 'true')

print 'create JDBCDriverParams Properties'
create('myProperties','Properties')
cd('Properties/NO_NAME_0')
create('user','Property')
cd('Property/user')
set('Value', jmsdsusername)

cd('../../')
create('databaseName','Property')
cd('Property/databaseName')
set('Value', dsdbname)

print 'create JDBCConnectionPoolParams'
cd('/JDBCSystemResource/' + jmsdsname + '/JdbcResource/' + jmsdsname)
create('myJdbcConnectionPoolParams','JDBCConnectionPoolParams')
cd('JDBCConnectionPoolParams/NO_NAME_0')
set('TestTableName','SQL SELECT 1 FROM DUAL')


# Assign
# ======
assign('JDBCSystemResource', vidadsname, 'Target', admin_server_name)
assign('JDBCSystemResource', lettersdsname, 'Target', admin_server_name)
assign('JDBCSystemResource', taskdsname, 'Target', admin_server_name)
assign('JDBCSystemResource', jmsdsname, 'Target', admin_server_name)

# Update Domain, Close It, Exit
# ==========================
updateDomain()
closeDomain()
exit()
