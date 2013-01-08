//
//  JUserModel.h
//  Jminee
//
//  Created by Robert Pieta on 1/1/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface JUserModel : NSObject
@property(nonatomic, strong, readonly) NSString *email;
@property(nonatomic, strong, readonly) NSString *name;
@property(nonatomic, assign, readonly) int uid;

+(id)initializeUserModel;

#pragma mark -
#pragma mark Update Methods

-(void)updateUserInfoWithJSONDict:(NSDictionary*)dict;

#pragma mark -
#pragma mark KeyChain Methods

-(void)setUsernameInKeychain:(NSString*)username;
-(void)setPasswordInKeychain:(NSString*)password;
-(NSString*)getSavedUsername;
-(NSString*)getSavedPassword;
-(void)removeKeychainInfo;

@end
