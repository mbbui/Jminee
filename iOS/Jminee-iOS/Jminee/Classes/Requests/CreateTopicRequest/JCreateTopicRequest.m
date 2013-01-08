//
//  JCreateTopicRequest.m
//  Jminee
//
//  Created by Robert Pieta on 1/1/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import "JCreateTopicRequest.h"

@implementation JCreateTopicRequest

-(id)initRequest {
    if(self = [super initRequest]) {
        _type = RequestType_CreateTopic;
    }
    return self;
}

#pragma mark -
#pragma mark Create Topic Methods

-(void)setTitle:(NSString*)title andMembers:(NSArray*)members {
    NSString *string = [NSString stringWithFormat:URLStr_CreateTopic,title];
    for(NSString *member_name in members) {
        string = [string stringByAppendingFormat:URLStr_CreateTopic_Member,member_name];
    }

    _URLext = [NSString stringWithString:string];
}

@end
