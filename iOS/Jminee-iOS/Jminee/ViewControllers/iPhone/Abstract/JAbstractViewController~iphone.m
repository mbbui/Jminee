//
//  JAbstractViewController~iphone.m
//  Jminee
//
//  Created by Robert Pieta on 1/1/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import "JAbstractViewController~iphone.h"

#import "JErrorDisplay.h"
#import "JUserModel.h"
#import "JAbstractRequest.h"

@interface JAbstractViewController_iphone() {
@private
    JErrorDisplay *errorDisplay;
    NSMutableArray *errorQueue;
}
@end

@implementation JAbstractViewController_iphone

-(void)viewDidLoad
{
    [super viewDidLoad];
    
    errorDisplay = [[JErrorDisplay alloc] init];
    [errorDisplay setDelegate:self];
    errorQueue = [NSMutableArray array];
    
    sharedUserModel = [JUserModel initializeUserModel];
    
    NSNotificationCenter *center = [NSNotificationCenter defaultCenter];
    [center addObserver:self selector:@selector(didShowKeyboard) name:UIKeyboardWillShowNotification object:nil];
    [center addObserver:self selector:@selector(didHideKeyboard) name:UIKeyboardWillHideNotification object:nil];
}

-(void)viewWillDisappear:(BOOL)animated {
    [super viewWillDisappear:animated];
    if(jrequest) {
        [jrequest cancelRequest];
        jrequest = NULL;
    }
}

#pragma mark -
#pragma mark Error Methods

-(void)displayError:(Error_Code)error {
    if([errorQueue count] == 0 && ![errorDisplay animating]) {
        [errorDisplay displayErrorCode:error inView:self.view withAnimation:Animation_FadeIn_Bottom];
    }
    else {
        NSNumber *number = [NSNumber numberWithInt:error];
        BOOL insert = YES;
        
        for(NSNumber *num in errorQueue) {
            if([num intValue] == error) insert = NO;
        }
        
        if(insert) [errorQueue addObject:number];
    }
}

-(void)errorDisplayDidFinishCurrentError {
    if([errorQueue count] > 0) {
        NSNumber *number = [errorQueue objectAtIndex:0];
        [errorQueue removeObjectAtIndex:0];
        
        Error_Code error = [number intValue];
        
        [errorDisplay displayErrorCode:error inView:self.view withAnimation:Animation_FadeIn_Bottom];
    }
}

#pragma mark -
#pragma mark Loading Methods

-(void)displayLoading:(Loading_Code)loading {
    
}

-(void)dismissLoading {
    
}

#pragma mark -
#pragma mark Request Methods

-(void)requestCannotConnectToTheInternet:(JAbstractRequest *)request {
    [self displayError:Error_NoInternet];
}

-(void)requestFinished:(JAbstractRequest *)request {
    
}

-(void)requestTerminatedFromTimeout:(JAbstractRequest *)request {
    [self displayError:Error_ConnectionTimeout];
}

-(void)requestStartedLoading:(JAbstractRequest *)request {
    
}

#pragma mark -
#pragma mark Keyboard Methods

-(void)didShowKeyboard {
    
}

-(void)didHideKeyboard {
    
}

#pragma mark -
#pragma mark Check Methods

-(BOOL)isValidEmail:(NSString*)email {
    NSString *emailRegex = @"[A-Z0-9a-z._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,6}";
    NSPredicate *emailTest = [NSPredicate predicateWithFormat:@"SELF MATCHES %@", emailRegex];

    if (![emailTest evaluateWithObject:email]){
        return NO;
    }
    return YES;
}
    
@end
