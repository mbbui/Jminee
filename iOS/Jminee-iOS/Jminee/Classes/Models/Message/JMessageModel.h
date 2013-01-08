//
//  JMessageModel.h
//  Jminee
//
//  Created by Robert Pieta on 1/1/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import <Foundation/Foundation.h>

@class JDateTime;
@interface JMessageModel : NSObject <NSCoding>
@property(nonatomic, strong, readonly) JDateTime *datetime;
@property(nonatomic, strong, readonly) NSString *uid;
@property(nonatomic, strong, readonly) NSString *creator_name;
@property(nonatomic, strong, readonly) NSString *topic_id;
@property(nonatomic, strong, readonly) NSString *subject_id;
@property(nonatomic, strong, readonly) NSString *content;
@property(nonatomic, assign, readonly) BOOL deleted;

-(id)initMessageModelWithJSONDictionary:(NSDictionary*)dict;

#pragma mark -
#pragma mark Data Methods

-(NSDictionary*)messageModelDictionary;

@end
