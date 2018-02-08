'''
Created on Dec 1, 2017

@author: NNA
'''

import cast.application
import logging
import ast
import re

class ExtensionApplication(cast.application.ApplicationLevelExtension):

    def end_application(self, application):
        logging.info("Running code at the end of an Application")
        