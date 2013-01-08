//
//  JCreateTopicRequest.h
//  Jminee
//
//  Created by Robert Pieta on 1/1/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import "JAbstractRequest.h"

@interface JCreateTopicRequest : JAbstractRequest

#pragma mark -
#pragma mark Create Topic Methods

-(void)setTitle:(NSString*)title andMembers:(NSArray*)members;

@end
