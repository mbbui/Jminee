//
//  JSetTopicImageURLRequest.h
//  Jminee
//
//  Created by Robert Pieta on 1/1/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import "JAbstractRequest.h"

@interface JSetTopicImageURLRequest : JAbstractRequest

#pragma mark -
#pragma mark Set Topic Image URL Methods

-(void)setImageURL:(NSString*)url forTopicId:(int)uid;

@end
