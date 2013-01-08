//
//  JGetMessagesRequest.h
//  Jminee
//
//  Created by Robert Pieta on 1/1/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import "JAbstractRequest.h"

@interface JGetMessagesRequest : JAbstractRequest

#pragma mark -
#pragma mark Get Messages Methods

-(void)setTopicId:(int)uid andSubjectId:(int)uid;

#pragma mark -
#pragma mark Get Topics Array

-(NSMutableArray*)getMessagesArray;

@end
