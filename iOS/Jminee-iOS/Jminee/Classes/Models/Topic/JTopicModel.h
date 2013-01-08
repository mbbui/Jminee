//
//  JTopicModel.h
//  Jminee
//
//  Created by Robert Pieta on 1/1/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import <Foundation/Foundation.h>

@class JDateTime;
@interface JTopicModel : NSObject <NSCoding>
@property(nonatomic, strong, readonly) JDateTime *datetime;
@property(nonatomic, strong, readonly) NSString *uid;
@property(nonatomic, strong, readonly) NSString *creator_name;
@property(nonatomic, strong) JDateTime *update_time;
@property(nonatomic, assign) int new_msg;
@property(nonatomic, strong, readonly) NSString *title;
@property(nonatomic, strong) NSString *image_url;

-(id)initTopicModelWithJSONDictionary:(NSDictionary*)dict;

@end
