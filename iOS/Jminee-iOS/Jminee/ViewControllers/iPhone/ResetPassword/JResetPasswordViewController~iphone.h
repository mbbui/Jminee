//
//  JResetPasswordViewController~iphone.h
//  Jminee
//
//  Created by Robert Pieta on 1/1/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import "JAbstractViewController~iphone.h"

@interface JResetPasswordViewController_iphone : JAbstractViewController_iphone <UITextFieldDelegate> {
    IBOutlet UITextField *emailTextField;
    
    IBOutlet UITextView *infoTextView;
}

#pragma mark -
#pragma mark IBAction Methods

-(IBAction)backPushed:(id)sender;
-(IBAction)sendPushed:(id)sender;

@end
