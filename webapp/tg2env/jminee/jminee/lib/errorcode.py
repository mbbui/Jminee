'''
Created on Jun 21, 2012

@author: bachbui
'''

class ErrorCode(object):
    '''
    classdocs
    '''

    UNAUTHENTICATED = 1
    UNAUTHORIZED = 2
    INVALIDATEDINPUT = 3
    WRONGUSERPASSWORD = 4
    FAILEDACTIVATION = 5
    NORESETRECORD = 6   
    NONEXISTEDUSER = 7
    CREATSUBJECTFAILED = 8
    OTHERS = 100 
    
class ExceptionProcessing(object):
    @classmethod
    def gotException(cls, e, log):
        #TODO: send email notification to the right person
        log.exception('Got exception: %s'%e)