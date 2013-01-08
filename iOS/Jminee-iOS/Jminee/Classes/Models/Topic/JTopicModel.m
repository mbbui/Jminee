//
//  JTopicModel.m
//  Jminee
//
//  Created by Robert Pieta on 1/1/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import "JTopicModel.h"

#import "JDateTime.h"
#import "JConstants.h"

@interface JTopicModel() {
@private
    NSDictionary *jsonDict;
}
@end;

@implementation JTopicModel

-(id)initTopicModelWithJSONDictionary:(NSDictionary*)dict {
    if(self = [super init]) {
        jsonDict = dict;
        
        _datetime = [[JDateTime alloc] initDateTimeWithString:[dict objectForKey:DownloadCode_TopicTime]];
        _uid = [dict objectForKey:DownloadCode_TopicUid];
        _creator_name = [dict objectForKey:DownloadCode_TopicCreatorName];
        _update_time = [[JDateTime alloc] initDateTimeWithString:[dict objectForKey:DownloadCode_TopicUpdateTime]];
        _new_msg = [[dict objectForKey:DownloadCode_TopicNewMsg] intValue];
        _title = [dict objectForKey:DownloadCode_TopicTitle];
        
        _image_url = [dict objectForKey:DownloadCode_TopicImageUrl];
        if(_image_url == NULL || [_image_url isEqual:[NSNull null]]) _image_url = @"";
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
        _datetime = [aDecoder decodeObjectForKey:DownloadCode_TopicTime];
        _uid = [aDecoder decodeObjectForKey:DownloadCode_TopicUid];
        _creator_name = [aDecoder decodeObjectForKey:DownloadCode_TopicCreatorName];
        _update_time = [aDecoder decodeObjectForKey:DownloadCode_TopicUpdateTime];
        _new_msg = [aDecoder decodeIntForKey:DownloadCode_TopicNewMsg];
        _title = [aDecoder decodeObjectForKey:DownloadCode_TopicTitle];
        _image_url = [aDecoder decodeObjectForKey:DownloadCode_TopicImageUrl];
    }
    return self;
}

-(void)encodeWithCoder:(NSCoder *)aCoder {
    [aCoder encodeObject:_datetime forKey:DownloadCode_TopicTime];
    [aCoder encodeObject:_uid forKey:DownloadCode_TopicUid];
    [aCoder encodeObject:_creator_name forKey:DownloadCode_TopicCreatorName];
    [aCoder encodeObject:_update_time forKey:DownloadCode_TopicUpdateTime];
    [aCoder encodeInt:_new_msg forKey:DownloadCode_TopicNewMsg];
    [aCoder encodeObject:_title forKey:DownloadCode_TopicTitle];
    [aCoder encodeObject:_image_url forKey:DownloadCode_TopicImageUrl];
}

@end
