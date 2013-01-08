//
//  JCacheManager.m
//  Jminee
//
//  Created by Robert Pieta on 1/1/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import "JCacheManager.h"

#import "JTopicModel.h"
#import "JMessageModel.h"

#define FileName_SavedTopics @"savedTopics"
#define FileName_SavedMessages @"savedMessages"

@interface JCacheManager() {
@private
    NSMutableDictionary *topicDict;
    NSMutableDictionary *messageDict;
    NSMutableDictionary *imageDict;
}
-(id)init;
@end;

static JCacheManager *sharedCacheManager = nil;

@implementation JCacheManager

+(id)initializeCacheManager {
    @synchronized(self) {
        if(sharedCacheManager == nil)
            sharedCacheManager = [[JCacheManager alloc] init];
    }
    return sharedCacheManager;
}

-(id)init {
    if(self = [super init]) {
        topicDict = [NSMutableDictionary dictionary];
        messageDict = [NSMutableDictionary dictionary];
        imageDict = [NSMutableDictionary dictionary];
        
        if([self fileInDocumentsDirectoryExistsWithName:FileName_SavedTopics]) {
            NSData *data = [self returnDataInFileWithinDocumentsDirectoryWithName:FileName_SavedTopics];
            topicDict = [NSKeyedUnarchiver unarchiveObjectWithData:data];
        }
        else {
            NSData *data = [NSKeyedArchiver archivedDataWithRootObject:topicDict];
            [self writeDataToFileInDocumentsDirectoryWithName:FileName_SavedTopics data:data];
        }
        
        if([self fileInDocumentsDirectoryExistsWithName:FileName_SavedMessages]) {
            NSData *data = [self returnDataInFileWithinDocumentsDirectoryWithName:FileName_SavedMessages];
            messageDict = [NSKeyedUnarchiver unarchiveObjectWithData:data];
        }
        else {
            NSData *data = [NSKeyedArchiver archivedDataWithRootObject:messageDict];
            [self writeDataToFileInDocumentsDirectoryWithName:FileName_SavedMessages data:data];
        }
        
    }
    return self;
}

#pragma mark -
#pragma mark Cache Methods

-(void)saveTopicModel:(JTopicModel*)topic {
    [topicDict setObject:topicDict forKey:[topic uid]];
}

-(void)saveMessageModel:(JMessageModel*)message {
    if([messageDict objectForKey:[message topic_id]]) {
        NSMutableDictionary *dict = [messageDict objectForKey:[message topic_id]];
        [dict setObject:message forKey:[message uid]];
        [messageDict setObject:dict forKey:[message topic_id]];
    }
    else {
        NSMutableDictionary *dict = [NSMutableDictionary dictionary];
        [dict setObject:message forKey:[message uid]];
        [messageDict setObject:dict forKey:[message topic_id]];
    }
}

-(JTopicModel*)getTopicModelForTopicId:(int)topic_id {
    NSString *key = [NSString stringWithFormat:@"%i",topic_id];
    return [topicDict objectForKey:key];
}

-(JMessageModel*)getMessageModelForTopic:(JTopicModel*)topic andMessageId:(int)message_id {
    NSString *key = [NSString stringWithFormat:@"%i",message_id];
    if([messageDict objectForKey:[topic uid]]) {
        return [[messageDict objectForKey:[topic uid]] objectForKey:key];
    }
    else return NULL;
}

-(void)clearCache {
    topicDict = [NSMutableDictionary dictionary];
    messageDict = [NSMutableDictionary dictionary];
    
    [self saveData];
}

#pragma mark -
#pragma mark Data Methods

-(void)saveData {
    NSData *topic_data = [NSKeyedArchiver archivedDataWithRootObject:topicDict];
    [self writeDataToFileInDocumentsDirectoryWithName:FileName_SavedTopics data:topic_data];

    NSData *message_data = [NSKeyedArchiver archivedDataWithRootObject:messageDict];
    [self writeDataToFileInDocumentsDirectoryWithName:FileName_SavedMessages data:message_data];
}

#pragma mark -
#pragma mark Local Storage Methods

-(void)writeDataToFileInDocumentsDirectoryWithName:(NSString*)fileName data:(NSData*)data {
    NSArray *paths = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES);
    NSString *fullFilePath = [NSString stringWithFormat:@"%@/%@",[paths objectAtIndex:0],fileName];
    if(![self fileInDocumentsDirectoryExistsWithName:fileName]) {
        [[NSFileManager defaultManager] createFileAtPath:fullFilePath contents:data attributes:nil];
    }
    else {
        [data writeToFile:fullFilePath atomically:YES];
    }
}

-(NSData*)returnDataInFileWithinDocumentsDirectoryWithName:(NSString*)fileName {
    NSArray *paths = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES);
    NSString *fullFilePath = [NSString stringWithFormat:@"%@/%@",[paths objectAtIndex:0],fileName];
    return [NSData dataWithContentsOfFile:fullFilePath];
}

-(BOOL)fileInDocumentsDirectoryExistsWithName:(NSString*)fileName {
    NSArray *paths = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES);
    NSString *fullFilePath = [NSString stringWithFormat:@"%@/%@",[paths objectAtIndex:0],fileName];
    return [[NSFileManager defaultManager] fileExistsAtPath:fullFilePath];
}

-(void)deleteFileInDocumentsDirectoryWithName:(NSString*)fileName {
    NSArray *paths = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES);
    NSString *fullFilePath = [NSString stringWithFormat:@"%@/%@",[paths objectAtIndex:0],fileName];
    [[NSFileManager defaultManager] removeItemAtPath:fullFilePath error:nil];
}

#pragma mark -
#pragma mark Image Methods

-(void)cacheImage:(UIImage*)image forURL:(NSString*)url {
    if(image == NULL || url == NULL) return;
    
    if([url length] > 15) {
        url = [url substringFromIndex:[url length] - 15];
    }
    
    [imageDict setObject:image forKey:url];
}

-(UIImage*)imageForURL:(NSString*)url {
    if(url == NULL) return NULL;
    
    if([url length] > 15) {
        url = [url substringFromIndex:[url length] - 15];
    }
    
    return [imageDict objectForKey:url];
}

@end
