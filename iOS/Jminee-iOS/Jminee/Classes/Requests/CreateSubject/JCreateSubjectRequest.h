//
//  JCreateSubjectRequest.h
//  Jminee
//
//  Created by Robert Pieta on 1/4/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import "JAbstractRequest.h"

@interface JCreateSubjectRequest : JAbstractRequest

#pragma mark -
#pragma mark Create Message Request

-(void)setTopicId:(int)uid andTitle:(NSString*)title withContent:(NSString*)content;

@end
