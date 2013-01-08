//
//  JLoginRequest.m
//  Jminee
//
//  Created by Robert Pieta on 1/1/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import "JLoginRequest.h"

#import "JUserModel.h"

@interface JLoginRequest() {
@private
    NSString *lastUsername;
    NSString *lastPassword;
}
@end;

@implementation JLoginRequest

-(id)initRequest {
    if(self = [super initRequest]) {
        _type = RequestType_Login;
    }
    return self;
}

#pragma mark -
#pragma mark Login Methods

-(void)setUsername:(NSString*)username andPassword:(NSString*)password {
    lastUsername = [username copy];
    lastPassword = [password copy];
    
    _URLext = [NSString stringWithFormat:URLStr_Login,username,password];
}

#pragma mark -
#pragma mark Action Methods

-(BOOL)shouldRemindAboutPasswordReset {
    if([super completed] && [super successful] && requestData != NULL) {
        NSDictionary *dict = [NSJSONSerialization JSONObjectWithData:requestData options:NSJSONWritingPrettyPrinted error:nil];
        if([[dict objectForKey:DownloadCode_Logins] intValue] > 2) return YES;
    }
    return NO;
}

-(void)updateUserWithLoginInfo:(JUserModel*)user {
    if([super completed] && [super successful] && requestData != NULL) {
        [user setUsernameInKeychain:lastUsername];
        [user setPasswordInKeychain:lastPassword];
        
        NSDictionary *dict = [NSJSONSerialization JSONObjectWithData:requestData options:NSJSONWritingPrettyPrinted error:nil];
        [user updateUserInfoWithJSONDict:[dict objectForKey:DownloadCode_UserInfo]];
    }
}

@end
