# Copyright (c) 2018 Oracle and/or its affiliates. All rights reserved.
#
# WLST Offline for deploying an application under APP_NAME packaged in APP_PKG_FILE located in APP_PKG_LOCATION
# It will read the domain under DOMAIN_HOME by default
#
# author: Bruno Borges <bruno.borges@oracle.com>
# since: December, 2015
#
import os

# Deployment Information
domainname = os.environ.get('DOMAIN_NAME', 'base_domain')
admin_server_name = os.environ.get('ADMIN_NAME', 'AdminServer')
domainhome = os.environ.get('DOMAIN_HOME', '/u01/oracle/user_projects/domains/' + domainname)

print('admin_server_name  : [%s]' % admin_server_name);

# Read Domain in Offline Mode
# ===========================
readDomain(domainhome)


#Create a Persistent Store
#================================================
cd('/')
jmsDBStore=create('VidaServiceJMSDBStore', 'JDBCStore')
#jmsDBStore.setDataSource('jmsDBStore')
#jmsDBStore.setPrefixName(domainname + admin_server_name)
cd('/JDBCStores/VidaServiceJMSDBStore')
set('DataSource', jmsdsname)
set('PrefixName', domainname + admin_server_name)
#jmsDBStore.setDataSource(getMBean('/SystemResources/'+jmsdsname))
#jmsDBStore.setPrefixName(domainname + admin_server_name)
#cmo.setDataSource(getMBean('/SystemResources/'+jmsdsname))
#cmo.setPrefixName(domainname + admin_server_name)
cd('/')

assign('JDBCStore', 'VidaServiceJMSDBStore', 'Target', admin_server_name)


# Create a JMS Server
# ===================
cd('/')
jmsserver=create('VidaServiceJMSServer', 'JMSServer')
print('Create JMSServer : [%s]' % 'VidaServiceJMSServer')

cd('/JMSServers/VidaServiceJMSServer')
set('PersistentStore', 'VidaServiceJMSDBStore')
print('FileStore_name     : [%s]' % getMBean('/JDBCStores/VidaServiceJMSDBStore'))

cd('/')
assign('JMSServer', 'VidaServiceJMSServer', 'Target', admin_server_name)

# Create a JMS System resource
# ============================
cd('/')
create('VidaServiceJMSSystemResource', 'JMSSystemResource')
cd('JMSSystemResource/VidaServiceJMSSystemResource/JmsResource/NO_NAME_0')

# Create a JMS Queue and its subdeployment
# ========================================
activityQueue = create('ActivityQueue','Queue')
activityQueue.setJNDIName('jms/ActivityQueue')
activityQueue.setSubDeploymentName('VidaServiceQueueSubDeployment')

activityErrorQueue = create('ActivityErrorQueue','Queue')
activityErrorQueue.setJNDIName('jms/ActivityErrorQueue')
activityErrorQueue.setSubDeploymentName('VidaServiceQueueSubDeployment')

chunkQueue = create('ChunkQueue','Queue')
chunkQueue.setJNDIName('jms/ChunkQueue')
chunkQueue.setSubDeploymentName('VidaServiceQueueSubDeployment')

chunkErrorQueue = create('ChunkErrorQueue','Queue')
chunkErrorQueue.setJNDIName('jms/ChunkErrorQueue')
chunkErrorQueue.setSubDeploymentName('VidaServiceQueueSubDeployment')

domainEventTopic = create('DomainEventTopic','Topic')
domainEventTopic.setJNDIName('jms/DomainEventTopic')
domainEventTopic.setSubDeploymentName('VidaServiceQueueSubDeployment')

changeCaptureTopic = create('ChangeCaptureTopic','Topic')
changeCaptureTopic.setJNDIName('jms/ChangeCaptureTopic')
changeCaptureTopic.setSubDeploymentName('VidaServiceQueueSubDeployment')

changeCaptureErrorQueue = create('ChangeCaptureErrorQueue','Queue')
changeCaptureErrorQueue.setJNDIName('jms/ChangeCaptureErrorQueue')
changeCaptureErrorQueue.setSubDeploymentName('VidaServiceQueueSubDeployment')


cd('/JMSSystemResource/VidaServiceJMSSystemResource')
create('VidaServiceQueueSubDeployment', 'SubDeployment')

# Target resources to the servers
# ===============================
cd('/')
assign('JMSSystemResource.SubDeployment', 'VidaServiceJMSSystemResource.VidaServiceQueueSubDeployment', 'Target', 'VidaServiceJMSServer')

# Update Domain, Close It, Exit
# ==========================
updateDomain()
closeDomain()
exit()
