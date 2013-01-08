//
//  JErrorDisplay.m
//  Jminee
//
//  Created by Robert Pieta on 1/1/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import "JErrorDisplay.h"

#define RGBA(r, g, b, a) [UIColor colorWithRed:r/255.0 green:g/255.0 blue:b/255.0 alpha:a]

@interface JErrorDisplay() {
@private
}
@end;

@implementation JErrorDisplay

-(id)initWithFrame:(CGRect)frame {
    if (self = [super initWithFrame:frame]) {
        _duration = 1.5;
        
        UIColor *orange = RGBA(100.0, 6.0, 0.0, 1.0);
        
        toolbar = [[UIToolbar alloc] initWithFrame:CGRectMake(0, 0, 320, 44)];
        [toolbar setTintColor:orange];
        [self addSubview:toolbar];
        
        errorLabel = [[UILabel alloc] initWithFrame:CGRectMake(0, 0, 320, 44)];
        [errorLabel setTextColor:[UIColor whiteColor]];
        [errorLabel setFont:[UIFont fontWithName:@"System" size:19]];
        [errorLabel setTextAlignment:NSTextAlignmentCenter];
        [errorLabel setText:@""];
        [errorLabel setBackgroundColor:[UIColor clearColor]];
        [errorLabel setLineBreakMode:NSLineBreakByWordWrapping];
        
        [self addSubview:errorLabel];
        
        _loading = NO;
        _animating = NO;
    }
    return self;
}


#pragma mark -
#pragma mark Error Display Methods

-(void)displayErrorCode:(Error_Code)error inView:(UIView*)view withAnimation:(Animation_Code)animation {
    NSLog(@"Display Error: %i",error);
    
    self.alpha = 0.0f;
    
    [view addSubview:self];
    
    if(error == Error_None) {
        return;
    }
    else if(error == Error_Unauthenticated) [errorLabel setText:@"Please Login In"];
    else if(error == Error_Unautorized) [errorLabel setText:@"Unauthorized Request"];
    else if(error == Error_InvalidInputParameter) [errorLabel setText:@"Invalid Input"];
    else if(error == Error_WrongUserPassword) [errorLabel setText:@"Incorrect Username or Password"];
    else if(error == Error_FailedActivation) [errorLabel setText:@"Activation Failed"];
    else if(error == Error_NoResetRecord) [errorLabel setText:@"No password reset request"];
    else if(error == Error_NonExistedUser) [errorLabel setText:@"No such user exists"];
    else if(error == Error_Other) [errorLabel setText:@"Unknown Error"];
    else if(error == Error_ConnectionError) [errorLabel setText:@"Unknown Download Error"];
    else if(error == Error_NoInternet) [errorLabel setText:@"No Internet Connection"];
    else if(error == Error_NoEmail) [errorLabel setText:@"Email cannot be blank"];
    else if(error == Error_InvalidEmail) [errorLabel setText:@"Email is not valid"];
    else if(error == Error_NoPassword) [errorLabel setText:@"Password cannot be blank"];
    else if(error == Error_NoUsername) [errorLabel setText:@"Username cannot be blank"];
    else if(error == Error_ConnectionTimeout) [errorLabel setText:@"Internet connection too slow"];
    else if(error == Error_NoTitle) [errorLabel setText:@"Title cannot be blank"];
    else if(error == Error_InvalidMembersForm) [errorLabel setText:@"Members must be valid emails"];
    else if(error == Error_NoContent) [errorLabel setText:@"Content cannot be blank"];
    
    _loading = NO;
    _animating = YES;
    
    //Change to add more animations if necessary
    [self fadeInBottom];
}

#pragma mark -
#pragma mark Animation Methods

-(void)fadeInBottom {
    //if ([[UIScreen mainScreen] bounds].size.height == 568) self.center = CGPointMake(0, 568-70);
    //else self.center = CGPointMake(0, 480-70);
    
    self.alpha = 0.0f;
    
    [UIView animateWithDuration:0.5f delay:0.0f options:UIViewAnimationCurveEaseIn animations:^{
        self.alpha = 1.0f;
    } completion:^(BOOL finished){
        [UIView animateWithDuration:0.5f delay:_duration options:UIViewAnimationCurveEaseOut animations:^{
            self.alpha = 0.0f;
        } completion:^(BOOL finished) {
            [self removeFromSuperview];
            _animating = NO;
            if([self delegate]) [[self delegate] errorDisplayDidFinishCurrentError];
        }];
    }];
    
}

@end
