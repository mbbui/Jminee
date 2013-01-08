//
//  JSubjectModel.m
//  Jminee
//
//  Created by Robert Pieta on 1/4/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import "JSubjectModel.h"

#import "JConstants.h"
#import "JDateTime.h"

@interface JSubjectModel() {
@private
    NSDictionary *jsonDict;
}
@end;

@implementation JSubjectModel

-(id)initSubjectModelWithJSONDictionary:(NSDictionary*)dict {
    if(self = [super init]) {
        jsonDict = dict;
        
        _datetime = [[JDateTime alloc] initDateTimeWithString:[dict objectForKey:DownloadCode_SubjectTime]];
        _uid = [dict objectForKey:DownloadCode_SubjectUid];
        _topic_id = [[dict objectForKey:DownloadCode_SubjectTopicUid] intValue];
        _creator_id = [[dict objectForKey:DownloadCode_SubjectCreatorId] intValue];
        _title = [dict objectForKey:DownloadCode_SubjectTitle];
        
    }
    return self;
}

#pragma mark -
#pragma mark Data Methods

-(NSDictionary*)topicModelDictionary {
    return jsonDict;
}

#pragma mark -
#pragma mark NSCodying Methods

-(id)initWithCoder:(NSCoder *)aDecoder {
    if(self = [super init]) {
        _datetime = [aDecoder decodeObjectForKey:DownloadCode_SubjectTime];
        _uid = [aDecoder decodeObjectForKey:DownloadCode_SubjectUid];
        _creator_id = [aDecoder decodeIntForKey:DownloadCode_SubjectCreatorId];
        _title = [aDecoder decodeObjectForKey:DownloadCode_SubjectTitle];
        _topic_id = [aDecoder decodeIntForKey:DownloadCode_SubjectTopicUid];
    }
    return self;
}

-(void)encodeWithCoder:(NSCoder *)aCoder {
    [aCoder encodeObject:_datetime forKey:DownloadCode_SubjectTime];
    [aCoder encodeInt:_creator_id forKey:DownloadCode_SubjectCreatorId];
    [aCoder encodeObject:_uid forKey:DownloadCode_SubjectUid];
    [aCoder encodeObject:_title forKey:DownloadCode_SubjectTitle];
    [aCoder encodeInt:_topic_id forKey:DownloadCode_SubjectTopicUid];
}

@end
