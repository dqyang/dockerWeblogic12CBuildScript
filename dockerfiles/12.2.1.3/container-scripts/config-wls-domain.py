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
startEdit()
cmo.getSecurityConfiguration().setAnonymousAdminLookupEnabled(true)
save()
activate()

edit()
startEdit()
serverRuntime()
atnr=cmo.getSecurityConfiguration().getDefaultRealm().lookupAuthenticationProvider("DefaultAuthenticator")
atnr.createGroup('resAdministrators', 'resAdministrators')
atnr.createGroup('resDeployers', 'resDeployers')
atnr.createGroup('resMonitors', 'resMonitors')

atnr.createUser('resAdmin','resAdmin1','resAdmin')
atnr.createUser('resMonitor','resMonitor1','resMonitor')
atnr.createUser('resDeployer','resDeployer1','resDeployer')

atnr.addMemberToGroup('resAdministrators', 'resAdmin')
atnr.addMemberToGroup('Administrators', 'resAdmin')
atnr.addMemberToGroup('resDeployers', 'resDeployer')
atnr.addMemberToGroup('resMonitors', 'resMonitor')
save()

activate()
disconnect()
# Exit WLST
# =========
exit()


