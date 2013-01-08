//
//  JResetPasswordRequest.m
//  Jminee
//
//  Created by Robert Pieta on 1/1/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import "JResetPasswordRequest.h"

@implementation JResetPasswordRequest

-(id)initRequest {
    if(self = [super initRequest]) {
        _type = RequestType_PasswordReset;
    }
    return self;
}

#pragma mark -
#pragma mark Reset Password Methods

-(void)setResetEmail:(NSString*)email {
    _URLext = [NSString stringWithFormat:URLStr_PasswordReset,email];
}

@end
