//
//  JRegistrationViewController~iphone.h
//  Jminee
//
//  Created by Robert Pieta on 1/1/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import "JAbstractViewController~iphone.h"

@interface JRegistrationViewController_iphone : JAbstractViewController_iphone <UITextFieldDelegate> {
    IBOutlet UITextField *emailTextField;
    IBOutlet UITextField *passwordTextField;
    
    IBOutlet UITextView *infoTextView;
}

#pragma mark -
#pragma mark IBAction Methods

-(IBAction)backPushed:(id)sender;
-(IBAction)submitPushed:(id)sender;

@end
