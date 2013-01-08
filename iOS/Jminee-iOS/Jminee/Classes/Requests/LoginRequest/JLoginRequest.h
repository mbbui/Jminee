//
//  JLoginRequest.h
//  Jminee
//
//  Created by Robert Pieta on 1/1/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import "JAbstractRequest.h"

@class JUserModel;
@interface JLoginRequest : JAbstractRequest

#pragma mark -
#pragma mark Login Methods

-(void)setUsername:(NSString*)username andPassword:(NSString*)password;

#pragma mark -
#pragma mark Action Methods

-(BOOL)shouldRemindAboutPasswordReset;
-(void)updateUserWithLoginInfo:(JUserModel*)user;

@end
