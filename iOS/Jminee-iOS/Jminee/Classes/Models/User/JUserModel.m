//
//  JUserModel.m
//  Jminee
//
//  Created by Robert Pieta on 1/1/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import "JUserModel.h"

#import "JConstants.h"
#import "KeychainItemWrapper.h"

@interface JUserModel() {
@private
}
-(id)init;
@end;

static JUserModel *sharedUserModel = nil;

@implementation JUserModel

+(id)initializeUserModel {
    @synchronized(self) {
        if(sharedUserModel == nil)
            sharedUserModel = [[JUserModel alloc] init];
    }
    return sharedUserModel;
}

-(id)init {
    if(self = [super init]) {
        
    }
    return self;
}

#pragma mark -
#pragma mark Update Methods

-(void)updateUserInfoWithJSONDict:(NSDictionary*)dict {
    _email = [[dict objectForKey:DownloadCode_UserInfoEmail] copy];
    _name = [[dict objectForKey:DownloadCode_UserInfoName] copy];
    _uid = [[dict objectForKey:DownloadCode_UserInfoId] intValue];
}

#pragma mark -
#pragma mark KeyChain Methods

-(NSString*)getSavedUsername {
    return [self getUsernameFromKeychain];
}

-(NSString*)getSavedPassword {
    return [self getPasswordFromKeychain];
}

-(void)removeKeychainInfo {
    [self clearKeychain];
}

#pragma mark -
#pragma mark Keychain Data Methods

-(void)setUsernameInKeychain:(NSString*)username {
    NSLog(@"Store username: %@ in keychain",username);
    KeychainItemWrapper *keychain = [[KeychainItemWrapper alloc] initWithIdentifier:KeychainKey accessGroup:nil];
    [keychain setObject:@"Jminee" forKey: (__bridge id)kSecAttrService];
    [keychain setObject:username forKey:(__bridge id)(kSecAttrAccount)];
}

-(void)setPasswordInKeychain:(NSString*)password {
    KeychainItemWrapper *keychain = [[KeychainItemWrapper alloc] initWithIdentifier:KeychainKey accessGroup:nil];
    [keychain setObject:@"Jminee" forKey: (__bridge id)kSecAttrService];
    [keychain setObject:password forKey:(__bridge id)(kSecValueData)];
}

-(void)clearKeychain {
    KeychainItemWrapper *keychain = [[KeychainItemWrapper alloc] initWithIdentifier:KeychainKey accessGroup:nil];
    
    [keychain setObject:@"Jminee" forKey: (__bridge id)kSecAttrService];
    [keychain setObject:@"" forKey:(__bridge id)(kSecValueData)];
    //[keychain resetKeychainItem];
}

-(NSString*)getUsernameFromKeychain {
    KeychainItemWrapper *keychain = [[KeychainItemWrapper alloc] initWithIdentifier:KeychainKey accessGroup:nil];
    NSString *username = [keychain objectForKey:(__bridge id)(kSecAttrAccount)];
    if([username isEqual:NULL]) username = @"";
    
    return [username copy];
}

-(NSString*)getPasswordFromKeychain {
    KeychainItemWrapper *keychain = [[KeychainItemWrapper alloc] initWithIdentifier:KeychainKey accessGroup:nil];
    NSString *password = [keychain objectForKey:(__bridge id)(kSecValueData)];
    if([password isEqual:NULL]) password = @"";
    
    return [password copy];
}

@end
