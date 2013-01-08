'''
Created on Jan 7, 2013

@author: bachbui
'''

from jminee.tests import TestController
from jminee.controllers.notification import UserNotification, NotificationController

class TestEmailNotification(TestController):
    def testSendEmail(self):
#        notif = UserNotification(**dict(type='new_topic', user_name='friends@jminee.com',
#                                        topic='Testing email notification', new_topic=True,
#                                      registered_users=['bduybach@yahoo.com', 'bachbui@gmail.com']))
        
        notif = dict(type='new_topic', user_name='friends@jminee.com',
                        topic='Testing email notification',
                        registered_users=['bduybach@yahoo.com', 'bachbui@gmail.com'])
        NotificationController().send_topic_notif(notif)
        
        notif = dict(type='new_subject', user_name='friends@jminee.com',
                        topic='Testing email notification', subject='First subject',
                        registered_users=['bduybach@yahoo.com', 'bachbui@gmail.com'])
        NotificationController().send_topic_notif(notif)
        
        notif = dict(type='new_comment', user_name='friends@jminee.com',
                        topic='Testing email notification', subject='First subject',
                        comment='Perform a string formatting operation. The string on which this method is called can contain literal text or replacement fields delimited by braces {}. Each replacement field contains either the numeric index of a positional argument, or the name of a keyword argument. Returns a copy of the string where each replacement field is replaced with the string value of the corresponding argument.',
                        registered_users=['bduybach@yahoo.com', 'bachbui@gmail.com'])
        
        NotificationController().send_topic_notif(notif)