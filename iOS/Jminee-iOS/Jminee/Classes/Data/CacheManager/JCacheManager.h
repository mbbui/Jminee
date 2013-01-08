//
//  JCacheManager.h
//  Jminee
//
//  Created by Robert Pieta on 1/1/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import <Foundation/Foundation.h>

@class JTopicModel;
@class JMessageModel;
@interface JCacheManager : NSObject

+(id)initializeCacheManager;

#pragma mark -
#pragma mark Cache Methods

-(void)saveTopicModel:(JTopicModel*)topic;
-(void)saveMessageModel:(JMessageModel*)message;

-(JTopicModel*)getTopicModelForTopicId:(int)topic_id;
-(JMessageModel*)getMessageModelForTopic:(JTopicModel*)topic andMessageId:(int)message_id;

-(void)clearCache;

#pragma mark -
#pragma mark Image Methods

-(void)cacheImage:(UIImage*)image forURL:(NSString*)url;
-(UIImage*)imageForURL:(NSString*)url;

@end
