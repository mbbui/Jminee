//
//  JGetSubjectsRequest.h
//  Jminee
//
//  Created by Robert Pieta on 1/4/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import "JAbstractRequest.h"

@interface JGetSubjectsRequest : JAbstractRequest

#pragma mark -
#pragma mark Get Subjects Methods

-(void)setTopicId:(int)uid;

#pragma mark -
#pragma mark Get Subjects Array

-(NSMutableArray*)getSubjectArray;

@end
