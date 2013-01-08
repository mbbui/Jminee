//
//  JLoginViewController~iphone.h
//  Jminee
//
//  Created by Robert Pieta on 1/1/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import "JAbstractViewController~iphone.h"

@interface JLoginViewController_iphone : JAbstractViewController_iphone <UITextFieldDelegate> {
    IBOutlet UITextField *usernameTextField;
    IBOutlet UITextField *passwordTextField;
    
    IBOutlet UIButton *signInButton;
    IBOutlet UIButton *forgotPasswordButton;
    IBOutlet UIButton *whatsJmineeButton;
    IBOutlet UIButton *registerButton;
}

#pragma mark -
#pragma mark IBAction Methods

-(IBAction)forgotPasswordPushed:(id)sender;
-(IBAction)createAccountPushed:(id)sender;
-(IBAction)signInPushed:(id)sender;
-(IBAction)whatsJmineePushed:(id)sender;

@end
