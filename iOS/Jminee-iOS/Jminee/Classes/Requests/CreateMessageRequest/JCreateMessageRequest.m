//
//  JCreateMessagesRequest.m
//  Jminee
//
//  Created by Robert Pieta on 1/1/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import "JCreateMessageRequest.h"

@implementation JCreateMessageRequest

-(id)initRequest {
    if(self = [super initRequest]) {
        _type = RequestType_CreateMessage;
    }
    return self;
}

#pragma mark -
#pragma mark Create Message Request

-(void)setTopicId:(int)t_uid andSubjecId:(int)s_uid withContent:(NSString*)content {
    _URLext = [NSString stringWithFormat:URLStr_CreateMessage,t_uid,s_uid,content];
}

@end
