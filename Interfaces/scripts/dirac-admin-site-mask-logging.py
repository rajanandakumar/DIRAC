#!/usr/bin/env python
"""
  Retrieves site mask logging information.
"""

########################################################################
# File :    dirac-admin-site-mask-logging
# Author :  Stuart Paterson
########################################################################

from __future__ import print_function
__RCSID__ = "$Id$"

import DIRAC
from DIRAC.Core.Base import Script

Script.setUsageMessage( '\n'.join( [ __doc__.split( '\n' )[1],
                                     'Usage:',
                                     '  %s [option|cfgfile] ... Site ...' % Script.scriptName,
                                     'Arguments:',
                                     '  Site:     Name of the Site' ] ) )

Script.parseCommandLine( ignoreErrors = True )
args = Script.getPositionalArgs()

if len( args ) < 1:
  Script.showHelp()

from DIRAC.Interfaces.API.DiracAdmin import DiracAdmin
diracAdmin = DiracAdmin()
exitCode = 0
errorList = []

for site in args:
  result = diracAdmin.getSiteMaskLogging( site, printOutput = True )
  if not result['OK']:
    errorList.append( ( site, result['Message'] ) )
    exitCode = 2

for error in errorList:
  print("ERROR %s: %s" % error)

DIRAC.exit( exitCode )
