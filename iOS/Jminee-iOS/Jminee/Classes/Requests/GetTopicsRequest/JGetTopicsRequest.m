//
//  JGetTopicRequest.m
//  Jminee
//
//  Created by Robert Pieta on 1/1/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import "JGetTopicsRequest.h"

#import "JTopicModel.h"

@implementation JGetTopicsRequest

-(id)initRequest {
    if(self = [super initRequest]) {
        _URLext = URLStr_GetTopics;
        _type = RequestType_GetTopics;
    }
    return self;
}

#pragma mark -
#pragma mark Get Topics Methods

-(void)setTitle:(NSString*)title nums:(int)num withMaxTime:(int)max_time andMinTime:(int)min_time {
    NSString *parameters = [NSString stringWithFormat:URLStr_GetTopics_Parameters,title,num,max_time,min_time];
    _URLext = [NSString stringWithFormat:@"%@%@",URLStr_GetTopics,parameters];
}

#pragma mark -
#pragma mark Get Topics Array

-(NSMutableArray*)getTopicsArray {
    if([super completed] && [super successful] && requestData != NULL) {
        NSDictionary *jsonDict = [NSJSONSerialization JSONObjectWithData:requestData options:NSJSONWritingPrettyPrinted error:nil];
        NSArray *jsonArray = [[jsonDict objectForKey:DownloadCode_Topics] copy];
        NSMutableArray *topicsArray = [NSMutableArray array];
        
        for(NSDictionary *topicDict in jsonArray) {
            JTopicModel *topic = [[JTopicModel alloc] initTopicModelWithJSONDictionary:topicDict];
            [topicsArray addObject:topic];
        }
        return topicsArray;
        
    }
    else return [NSArray array];
}

@end
