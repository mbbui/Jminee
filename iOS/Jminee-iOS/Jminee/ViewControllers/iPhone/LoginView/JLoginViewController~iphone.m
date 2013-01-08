//
//  JLoginViewController~iphone.m
//  Jminee
//
//  Created by Robert Pieta on 1/1/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import "JLoginViewController~iphone.h"

#import "JLoginRequest.h"
#import "JUserModel.h"
#import <QuartzCore/QuartzCore.h>

@interface JLoginViewController_iphone() {
@private
}
@end

@implementation JLoginViewController_iphone

-(void)viewDidLoad
{
    [super viewDidLoad];
	// Do any additional setup after loading the view.
    
    [signInButton.layer setCornerRadius:10.0f];
    [signInButton.layer setShadowOffset:CGSizeMake(0, 1)];
    [signInButton.layer setShadowColor:[[UIColor darkGrayColor] CGColor]];
    [signInButton.layer setShadowRadius:2.0];
    [signInButton.layer setShadowOpacity:0.8];
    
    [forgotPasswordButton.layer setCornerRadius:10.0f];
    [forgotPasswordButton.layer setShadowOffset:CGSizeMake(0, 1)];
    [forgotPasswordButton.layer setShadowColor:[[UIColor darkGrayColor] CGColor]];
    [forgotPasswordButton.layer setShadowRadius:2.0];
    [forgotPasswordButton.layer setShadowOpacity:0.8];
    
    [whatsJmineeButton.layer setCornerRadius:10.0f];
    [whatsJmineeButton.layer setShadowOffset:CGSizeMake(0, 1)];
    [whatsJmineeButton.layer setShadowColor:[[UIColor darkGrayColor] CGColor]];
    [whatsJmineeButton.layer setShadowRadius:2.0];
    [whatsJmineeButton.layer setShadowOpacity:0.8];
    
    [registerButton.layer setCornerRadius:10.0f];
    [registerButton.layer setShadowOffset:CGSizeMake(0, 1)];
    [registerButton.layer setShadowColor:[[UIColor darkGrayColor] CGColor]];
    [registerButton.layer setShadowRadius:2.0];
    [registerButton.layer setShadowOpacity:0.8];
}

-(void)viewWillAppear:(BOOL)animated {
    [super viewWillAppear:animated];
    
    usernameTextField.text = [sharedUserModel getSavedUsername];
    passwordTextField.text = [sharedUserModel getSavedPassword];
    
    [usernameTextField setEnabled:YES];
    [passwordTextField setEnabled:YES];
}

#pragma mark -
#pragma mark IBAction Methods

-(IBAction)forgotPasswordPushed:(id)sender {
    [self performSegueWithIdentifier:Segue_ToResetPasswordView sender:self];
}

-(IBAction)createAccountPushed:(id)sender {
    [self performSegueWithIdentifier:Segue_ToRegistrationView sender:self];
}

-(IBAction)signInPushed:(id)sender {
    NSString *username = usernameTextField.text;
    NSString *password = passwordTextField.text;
    
    if([username isEqualToString:@""]) {
        [self displayError:Error_NoUsername];
        return;
    }
    if([password isEqualToString:@""]) {
        [self displayError:Error_NoPassword];
        return;
    }

    if(jrequest) {
        //Should be showing a download indicator.
        return;
    }

    jrequest = [[JLoginRequest alloc] initRequest];
    [jrequest setDelegate:self];
    JLoginRequest *loginRequest = (JLoginRequest*)jrequest;
    [loginRequest setUsername:username andPassword:password];
    [loginRequest startRequest];
}

-(IBAction)whatsJmineePushed:(id)sender {
    [self performSegueWithIdentifier:Segue_ToWhatsJmineeView sender:self];
}

#pragma mark -
#pragma mark Request Methods

-(void)requestStartedLoading:(JAbstractRequest *)request {
    [usernameTextField setEnabled:NO];
    [passwordTextField setEnabled:NO];
    
    [UIView animateWithDuration:0.1f animations:^{
        usernameTextField.alpha = 0.3f;
        passwordTextField.alpha = 0.3f;
    }];
}

-(void)requestFinished:(JAbstractRequest *)request {
    [usernameTextField setEnabled:YES];
    [passwordTextField setEnabled:YES];
    
    [UIView animateWithDuration:0.1f animations:^{
        usernameTextField.alpha = 1.0f;
        passwordTextField.alpha = 1.0f;
    }];
    
    if(![[request type] isEqualToString:RequestType_Login]) {
        jrequest = NULL;
        return;
    }
    
    NSLog(@"Login finished");
    
    if([request successful]) {
        JLoginRequest *loginRequest = (JLoginRequest*)request;
        [loginRequest updateUserWithLoginInfo:sharedUserModel];
        
        NSLog(@"Successful! Login complete!");
        [self performSegueWithIdentifier:Segue_ToTopicsView sender:self];
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
    if([textField isEqual:usernameTextField]) {
        [passwordTextField becomeFirstResponder];
    }
    else [self.view endEditing:YES];
}

-(void)touchesEnded:(NSSet *)touches withEvent:(UIEvent *)event {
    UITouch *touch = [touches anyObject];
    CGPoint touchLocation = [touch locationInView:self.view];
    
    if(touchLocation.y > 10) {
        [usernameTextField resignFirstResponder];
        [passwordTextField resignFirstResponder];
    }
    
    [self.view endEditing:YES];
}

-(void)didShowKeyboard {
    [UIView animateWithDuration:0.3f animations:^{
        signInButton.alpha = 0.0f;
        forgotPasswordButton.alpha = 0.0f;
        whatsJmineeButton.alpha = 0.0f;
    }];
}

-(void)didHideKeyboard {
    [UIView animateWithDuration:0.3f animations:^{
        signInButton.alpha = 1.0f;
        forgotPasswordButton.alpha = 1.0f;
        whatsJmineeButton.alpha = 1.0f;
    }];
}

@end
