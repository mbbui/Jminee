//
//  JCreateMessagesRequest.h
//  Jminee
//
//  Created by Robert Pieta on 1/1/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import "JAbstractRequest.h"

@interface JCreateMessageRequest : JAbstractRequest

#pragma mark -
#pragma mark Create Message Request

-(void)setTopicId:(int)t_uid andSubjecId:(int)s_uid withContent:(NSString*)content;

@end
