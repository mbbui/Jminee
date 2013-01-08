//
//  JRegistrationViewController~iphone.m
//  Jminee
//
//  Created by Robert Pieta on 1/1/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import "JRegistrationViewController~iphone.h"

#import "JRegistrationRequest.h"
#import <QuartzCore/QuartzCore.h>

@interface JRegistrationViewController_iphone() {
@private
}
@end

@implementation JRegistrationViewController_iphone

-(void)viewDidLoad
{
    [super viewDidLoad];
	// Do any additional setup after loading the view.
    [infoTextView.layer setCornerRadius:5.0f];
}

-(void)viewWillAppear:(BOOL)animated {
    [super viewWillAppear:animated];
    
    [emailTextField setEnabled:YES];
    [passwordTextField setEnabled:YES];
}

#pragma mark -
#pragma mark IBAction Methods

-(IBAction)backPushed:(id)sender {
    [self.navigationController popToRootViewControllerAnimated:YES];
}

-(IBAction)submitPushed:(id)sender {
    NSString *email = emailTextField.text;
    NSString *password = passwordTextField.text;
    
    if([email isEqualToString:@""]) {
        [self displayError:Error_NoEmail];
        return;
    }
    if([password isEqualToString:@""]) {
        [self displayError:Error_NoPassword];
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
    
    jrequest = [[JRegistrationRequest alloc] initRequest];
    [jrequest setDelegate:self];
    JRegistrationRequest *registrationRequest = (JRegistrationRequest*)jrequest;
    [registrationRequest setEmail:email andPassword:password];
    [registrationRequest startRequest];
}

#pragma mark -
#pragma mark Request Methods

-(void)requestStartedLoading:(JAbstractRequest *)request {
    [emailTextField setEnabled:NO];
    [passwordTextField setEnabled:NO];
    
    [UIView animateWithDuration:0.1f animations:^{
        emailTextField.alpha = 0.3f;
        passwordTextField.alpha = 0.3f;
    }];
}

-(void)requestFinished:(JAbstractRequest *)request {
    [emailTextField setEnabled:YES];
    [passwordTextField setEnabled:YES];
    
    [UIView animateWithDuration:0.1f animations:^{
        emailTextField.alpha = 1.0f;
        passwordTextField.alpha = 1.0f;
    }];
    
    if(![[request type] isEqualToString:RequestType_Registration]) {
        jrequest = NULL;
        return;
    }
    
    if([request successful]) {
        NSLog(@"Successful! Registration complete!");
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
    if([textField isEqual:emailTextField]) {
        [passwordTextField becomeFirstResponder];
    }
    else [self.view endEditing:YES];
}

-(void)touchesEnded:(NSSet *)touches withEvent:(UIEvent *)event {
    UITouch *touch = [touches anyObject];
    CGPoint touchLocation = [touch locationInView:self.view];
    
    if(touchLocation.y > 10) {
        [emailTextField resignFirstResponder];
        [passwordTextField resignFirstResponder];
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
