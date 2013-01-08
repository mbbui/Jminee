//
//  JRegistrationRequest.m
//  Jminee
//
//  Created by Robert Pieta on 1/1/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import "JRegistrationRequest.h"

@implementation JRegistrationRequest

-(id)initRequest {
    if(self = [super initRequest]) {
        _type = RequestType_Registration;
    }
    return self;
}

#pragma mark -
#pragma mark Registration Methods

-(void)setEmail:(NSString*)email andPassword:(NSString*)password {
    _URLext = [NSString stringWithFormat:URLStr_Registration,email,password];
}

@end
