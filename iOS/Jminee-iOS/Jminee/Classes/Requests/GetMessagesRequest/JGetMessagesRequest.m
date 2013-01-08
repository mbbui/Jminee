//
//  JGetMessagesRequest.m
//  Jminee
//
//  Created by Robert Pieta on 1/1/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import "JGetMessagesRequest.h"

#import "JMessageModel.h"

@implementation JGetMessagesRequest

-(id)initRequest {
    if(self = [super initRequest]) {
        _type = RequestType_GetMessages;
    }
    return self;
}

#pragma mark -
#pragma mark Get Messages Methods

-(void)setTopicId:(int)t_uid andSubjectId:(int)s_uid {
    _URLext = [NSString stringWithFormat:URLStr_GetMessages,t_uid,s_uid];
}

#pragma mark -
#pragma mark Get Topics Array

-(NSMutableArray*)getMessagesArray {
    if([super completed] && [super successful] && requestData != NULL) {
        NSDictionary *jsonDict = [NSJSONSerialization JSONObjectWithData:requestData options:NSJSONWritingPrettyPrinted error:nil];
        NSArray *jsonArray = [[jsonDict objectForKey:DownloadCode_Messages] copy];
        NSMutableArray *messagesArray = [NSMutableArray array];
        
        for(NSDictionary *messageDict in jsonArray) {
            JMessageModel *message = [[JMessageModel alloc] initMessageModelWithJSONDictionary:messageDict];
            [messagesArray addObject:message];
        }
        return messagesArray;
        
    }
    else return [NSArray array];
}

@end
