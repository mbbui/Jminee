'''
Created on Jan 7, 2013

@author: bachbui
'''

from jminee.tests import TestController
from jminee.controllers.notification import UserNotification, NotificationController

class TestEmailNotification(TestController):
    def testSendEmail(self):
        notif = UserNotification(**dict(type='new_topic', user_name='friends@jminee.com',
                                        topic='Testing email notification',
                                      registered_users=['bduybach@yahoo.com']))
        NotificationController().send_newtopic_notif(notif)