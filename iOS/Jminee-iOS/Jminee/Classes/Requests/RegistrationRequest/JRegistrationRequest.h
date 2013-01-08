//
//  JRegistrationRequest.h
//  Jminee
//
//  Created by Robert Pieta on 1/1/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import "JAbstractRequest.h"

@interface JRegistrationRequest : JAbstractRequest

#pragma mark -
#pragma mark Registration Methods

-(void)setEmail:(NSString*)email andPassword:(NSString*)password;

@end
