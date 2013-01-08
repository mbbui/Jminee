//
//  JMessageModel.m
//  Jminee
//
//  Created by Robert Pieta on 1/1/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import "JMessageModel.h"

#import "JDateTime.h"
#import "JConstants.h"

@interface JMessageModel() {
@private
    NSDictionary *jsonDict;
}
@end;

@implementation JMessageModel

-(id)initMessageModelWithJSONDictionary:(NSDictionary*)dict {
    if(self = [super init]) {
        jsonDict = dict;
        
        _datetime = [[JDateTime alloc] initDateTimeWithString:[dict objectForKey:DownloadCode_MessageTime]];
        _uid = [dict objectForKey:DownloadCode_MessageUid];
        _creator_name = [dict objectForKey:DownloadCode_MessageCreatorName];
        _topic_id = [dict objectForKey:DownloadCode_MessageTopicId];
        _subject_id = [dict objectForKey:DownloadCode_MessageSubjectUid];
        _content = [dict objectForKey:DownloadCode_MessageContent];
        _deleted = [[dict objectForKey:DownloadCode_MessageDeleted] boolValue];
    }
    return self;
}

#pragma mark -
#pragma mark Data Methods

-(NSDictionary*)messageModelDictionary {
    return jsonDict;
}

#pragma mark -
#pragma mark NSCodying Methods

-(id)initWithCoder:(NSCoder *)aDecoder {
    if(self = [super init]) {
        _datetime = [aDecoder decodeObjectForKey:DownloadCode_MessageTime];
        _uid = [aDecoder decodeObjectForKey:DownloadCode_MessageUid];
        _creator_name = [aDecoder decodeObjectForKey:DownloadCode_MessageCreatorName];
        _topic_id = [aDecoder decodeObjectForKey:DownloadCode_MessageTopicId];
        _subject_id = [aDecoder decodeObjectForKey:DownloadCode_MessageSubjectUid];
        _content = [aDecoder decodeObjectForKey:DownloadCode_MessageContent];
        _deleted = [aDecoder decodeBoolForKey:DownloadCode_MessageDeleted];
    }
    return self;
}

-(void)encodeWithCoder:(NSCoder *)aCoder {
    [aCoder encodeObject:_datetime forKey:DownloadCode_MessageTime];
    [aCoder encodeObject:_uid forKey:DownloadCode_MessageUid];
    [aCoder encodeObject:_creator_name forKey:DownloadCode_MessageCreatorName];
    [aCoder encodeObject:_topic_id forKey:DownloadCode_MessageTopicId];
    [aCoder encodeObject:_subject_id forKey:DownloadCode_MessageSubjectUid];
    [aCoder encodeObject:_content forKey:DownloadCode_MessageContent];
    [aCoder encodeBool:_deleted forKey:DownloadCode_MessageDeleted];
}

@end
