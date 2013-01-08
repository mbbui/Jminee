//
//  JSubjectModel.h
//  Jminee
//
//  Created by Robert Pieta on 1/4/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import <Foundation/Foundation.h>

@class JDateTime;
@interface JSubjectModel : NSObject <NSCoding>
@property(nonatomic, assign, readonly) int creator_id;
@property(nonatomic, strong, readonly) NSString *title;
@property(nonatomic, strong, readonly) NSString *uid;
@property(nonatomic, assign, readonly) int topic_id;
@property(nonatomic, strong, readonly) JDateTime *datetime;

-(id)initSubjectModelWithJSONDictionary:(NSDictionary*)dict;

#pragma mark -
#pragma mark Data Methods

-(NSDictionary*)topicModelDictionary;

@end
