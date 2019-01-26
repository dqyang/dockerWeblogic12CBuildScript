#Copyright (c) 2014-2018 Oracle and/or its affiliates. All rights reserved.
#
#Licensed under the Universal Permissive License v 1.0 as shown at http://oss.oracle.com/licenses/upl.
#
# WebLogic on Docker Default Domain
#
# Domain, as defined in DOMAIN_NAME, will be created in this script. Name defaults to 'base_domain'.
#
# Since : October, 2014
# Author: monica.riccelli@oracle.com
# ==============================================
# Display the variable values.
print 'dsDriver', dsDriver
print 'dsURL', dsURL
print 'dsTargetName', dsTargetName
print 'dsTargetType', dsTargetType
print 'vidadsname', vidadsname
print 'vidauser', vidauser
print 'vidapassword', vidapassword
print 'vidadsjndi', vidadsjndi
print 'letterdsname', letterdsname
print 'lettersuser', lettersuser
print 'letterspassword', letterspassword
print 'letterdsjndi', letterdsjndi
print 'taskdsname', taskdsname
print 'taskuser', taskuser
print 'taskpassword', taskpassword
print 'taskdsjndi', taskdsjndi

admin_listen_port= int(os.environ.get("ADMIN_LISTEN_PORT", "7001"))
adminURL='t3://72.17.0.2:7001'
print 'adminURL', adminURL

# Connect to the AdminServer.
connect(username, password, adminURL)

edit()
startEdit()

# Create data source.
cd('/')
cmo.createJDBCSystemResource(vidadsname)

cd('/JDBCSystemResources/' + vidadsname + '/JDBCResource/' + vidadsname)
cmo.setName(vidadsname)

cd('/JDBCSystemResources/' + vidadsname + '/JDBCResource/' + vidadsname + '/JDBCDataSourceParams/' + vidadsname)
set('JNDINames',jarray.array([String(vidadsjndi)], String))

cd('/JDBCSystemResources/' + vidadsname + '/JDBCResource/' + vidadsname + '/JDBCDriverParams/' + vidadsname)
cmo.setUrl(dsURL)
cmo.setDriverName(dsDriver)
set('Password', vidapassword)

cd('/JDBCSystemResources/' + vidadsname + '/JDBCResource/' + vidadsname + '/JDBCConnectionPoolParams/' + vidadsname)
cmo.setTestTableName('SQL SELECT 1 FROM DUAL\r\n\r\n')

cd('/JDBCSystemResources/' + vidadsname + '/JDBCResource/' + vidadsname + '/JDBCDriverParams/' + vidadsname + '/Properties/' + vidadsname)
cmo.createProperty('user')

cd('/JDBCSystemResources/' + vidadsname + '/JDBCResource/' + vidadsname + '/JDBCDriverParams/' + vidadsname + '/Properties/' + vidadsname + '/Properties/user')
cmo.setValue(vidauser)

cd('/JDBCSystemResources/' + vidadsname + '/JDBCResource/' + vidadsname + '/JDBCDataSourceParams/' + vidadsname)
cmo.setGlobalTransactionsProtocol('TwoPhaseCommit')

cd('/SystemResources/' + vidadsname)
set('Targets',jarray.array([ObjectName('com.bea:Name=' + dsTargetName + ',Type=' + dsTargetType)], ObjectName))

save()
activate()

disconnect()
# Exit WLST
# =========
exit()


