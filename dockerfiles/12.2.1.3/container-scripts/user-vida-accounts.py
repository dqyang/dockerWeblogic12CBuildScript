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

domainname = os.environ.get('DOMAIN_NAME', 'base_domain')
admin_listen_port= int(os.environ.get("ADMIN_LISTEN_PORT", "7001"))
adminURL='t3://' + wladminhost + ':7001'
print 'adminURL', adminURL

# Connect to the AdminServer.
connect(username, password, adminURL)

edit()
serverConfig()

cd('/SecurityConfiguration/'+domainname+'/Realms/myrealm/AuthenticationProviders/DefaultAuthenticator')

cmo.createGroup('VIDA_ADMIN', 'VIDA_ADMIN')
cmo.createGroup('VIDA_CLIENT_SVCS', 'VIDA_CLIENT_SVCS')

cmo.createUser('dev_manager','P@55w0rd','dev_manager')

cmo.addMemberToGroup('VIDA_ADMIN', 'dev_manager')
cmo.addMemberToGroup('VIDA_CLIENT_SVCS', 'dev_manager')

disconnect()
# Exit WLST
# =========
exit()


