# Copyright (c) 2018 Maximus
#
# WLST online script to deploy applicaitons.
#
# author: Daniel Yang
# since: January 2018
#
import java.lang
import os
import string

def deployapp(app, dirName):
    "deploys an app"	
    appName = app[0];
    warName = app[2];
	
    appPath = dirName+'/'+warName
    try:
        print 'Redeploying ',app[0]
        undeploy(appName)
    except Exception:
        print 'Deploying...'
    if appName == 'webApp':
       planPath=dirName+'/'+'Plan-gradle.xml'
       print 'planPath:'+planPath
       deploy(appName=appName,path=appPath,planPath=planPath,upload="false")
    else:
       deploy(appName=appName,path=appPath,upload="false")
    return

# Deployment Information
domainname = os.environ.get('DOMAIN_NAME', 'base_domain')
domainhome = os.environ.get('DOMAIN_HOME', '/u01/oracle/user_projects/domains/' + domainname)
admin_name = os.environ.get("ADMIN_NAME", "AdminServer")
deployDirName = os.environ.get('APP_PKG_LOCATION', '/u01/oracle/deploy')
adminURL='t3://' + wladminhost + ':7001'

connect(username,password,adminURL)

apps = [
        ['CommonServices','flSchipCommonServices', 'commonServices.war'],
        ['TaskManagement','flSchipTaskManagement', 'taskManagement.war'],
        ['LettersManagement','flSchipOutboundDocManagement', 'LettersManagement.war'],
        ['BatchProcessing','flSchipBatchProcessing', 'batchProcessing.war'],
        ['Finance','flSchipFinance', 'finance.war'],
        ['InboundDocManagment','flSchipInboundDocManagement', 'inboundDocManagement.war'],
        ['AccountManagement','flSchipAccountManagement', 'accountManagement.war'],
        ['Enrollment','flSchipEnrollment', 'enrollmentManagement.war'],
        ['eligibility','flSchipEligibility', 'eligibility.war'],
        ['ServiceClient','flSchipServiceClient', 'serviceClient.war'],
        ['LettersGeneration','flSchipLettersGeneration','LettersGeneration.war'],
        ['webApp','flSchipWebApp', 'webApp.war']
       ]
for app in apps:
  deployapp(app, deployDirName)


# Disconnect
# ==========================
disconnect()
exit()
