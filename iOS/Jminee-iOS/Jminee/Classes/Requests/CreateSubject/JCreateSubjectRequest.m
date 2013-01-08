//
//  JCreateSubjectRequest.m
//  Jminee
//
//  Created by Robert Pieta on 1/4/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import "JCreateSubjectRequest.h"

@implementation JCreateSubjectRequest

-(id)initRequest {
    if(self = [super initRequest]) {
        _type = RequestType_CreateSubject;
    }
    return self;
}

#pragma mark -
#pragma mark Create Message Request

-(void)setTopicId:(int)uid andTitle:(NSString*)title withContent:(NSString*)content {
    _URLext = [NSString stringWithFormat:URLStr_CreateSubject,uid,title];
    if(![content isEqualToString:@""]) {
        NSString *string = [NSString stringWithFormat:URLStr_CreateSubject_Content,content];
        _URLext = [_URLext stringByAppendingString:string];
    }
}

@end
