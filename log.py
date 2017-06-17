# -*- coding: utf-8 -*-
import logging

class Logger():
   
    @staticmethod
    def debugLog(logcontent):
        logging.basicConfig(filename='loginfo.log', level=logging.DEBUG)
        logging.info(logcontent)
