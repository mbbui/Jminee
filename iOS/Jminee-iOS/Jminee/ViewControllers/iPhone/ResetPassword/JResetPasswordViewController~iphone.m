//
//  JResetPasswordViewController~iphone.m
//  Jminee
//
//  Created by Robert Pieta on 1/1/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import "JResetPasswordViewController~iphone.h"

#import "JResetPasswordRequest.h"
#import <QuartzCore/QuartzCore.h>

@interface JResetPasswordViewController_iphone() {
@private
}
@end

@implementation JResetPasswordViewController_iphone

-(void)viewDidLoad
{
    [super viewDidLoad];
	// Do any additional setup after loading the view.
    [infoTextView.layer setCornerRadius:5.0f];
}

-(void)viewWillAppear:(BOOL)animated {
    [super viewWillAppear:animated];
    
    [emailTextField setEnabled:YES];
}

#pragma mark -
#pragma mark IBAction Methods

-(IBAction)backPushed:(id)sender {
    [self.navigationController popToRootViewControllerAnimated:YES];
}

-(IBAction)sendPushed:(id)sender {
    NSString *email = emailTextField.text;
    
    if([email isEqualToString:@""]) {
        [self displayError:Error_NoEmail];
        return;
    }
    if(![self isValidEmail:email]) {
        [self displayError:Error_InvalidEmail];
        return;
    }
    
    if(jrequest) {
        //Should be showing a download indicator.
        return;
    }
    
    jrequest = [[JResetPasswordRequest alloc] initRequest];
    [jrequest setDelegate:self];
    JResetPasswordRequest *resetPasswordRequest = (JResetPasswordRequest*)jrequest;
    [resetPasswordRequest setResetEmail:email];
    [resetPasswordRequest startRequest];

}

#pragma mark -
#pragma mark Request Methods

-(void)requestStartedLoading:(JAbstractRequest *)request {
    [emailTextField setEnabled:NO];
    
    [UIView animateWithDuration:0.1f animations:^{
        emailTextField.alpha = 0.3f;
    }];
}

-(void)requestFinished:(JAbstractRequest *)request {
    [emailTextField setEnabled:YES];
    
    [UIView animateWithDuration:0.1f animations:^{
        emailTextField.alpha = 1.0f;
    }];
    
    if(![[request type] isEqualToString:RequestType_PasswordReset]) {
        jrequest = NULL;
        return;
    }
    
    if([request successful]) {
        NSLog(@"Successful! Email sent to reset password!");
    }
    else [self displayError:[request error_code]];
    
    jrequest = NULL;
}

#pragma mark -
#pragma mark Keyboard Methods

-(BOOL)textFieldShouldReturn:(UITextField *)textField {
    [self textFieldDidEndEditing:textField];
    
    return YES;
}

-(void)textFieldDidEndEditing:(UITextField *)textField {
    [self.view endEditing:YES];
}

-(void)touchesEnded:(NSSet *)touches withEvent:(UIEvent *)event {
    UITouch *touch = [touches anyObject];
    CGPoint touchLocation = [touch locationInView:self.view];
    
    if(touchLocation.y > 10) {
        [emailTextField resignFirstResponder];
    }
    
    [self.view endEditing:YES];
}

-(void)didShowKeyboard {
    [UIView animateWithDuration:0.4f animations:^{
        infoTextView.alpha = 0.0f;
    }];
}

-(void)didHideKeyboard {
    [UIView animateWithDuration:0.4f animations:^{
        infoTextView.alpha = 1.0f;
    }];
}

@end
