//
//  JGetTopicRequest.h
//  Jminee
//
//  Created by Robert Pieta on 1/1/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import "JAbstractRequest.h"

@interface JGetTopicsRequest : JAbstractRequest

#pragma mark -
#pragma mark Get Topics Methods

-(void)setTitle:(NSString*)title nums:(int)num withMaxTime:(int)max_time andMinTime:(int)min_time;

#pragma mark -
#pragma mark Get Topics Array

-(NSMutableArray*)getTopicsArray;

@end
