//
//  JResetPasswordRequest.h
//  Jminee
//
//  Created by Robert Pieta on 1/1/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import "JAbstractRequest.h"

@interface JResetPasswordRequest : JAbstractRequest

#pragma mark -
#pragma mark Reset Password Methods

-(void)setResetEmail:(NSString*)email;

@end
