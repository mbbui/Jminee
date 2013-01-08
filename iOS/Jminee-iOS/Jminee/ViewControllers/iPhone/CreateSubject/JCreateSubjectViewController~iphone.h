//
//  JCreateSubjectViewController~iphone.h
//  Jminee
//
//  Created by Robert Pieta on 1/4/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import "JAbstractViewController~iphone.h"

@class JTopicModel;
@interface JCreateSubjectViewController_iphone : JAbstractViewController_iphone <UITextFieldDelegate,UITextViewDelegate> {
    IBOutlet UITextField *titleTextField;
    IBOutlet UITextView *contentTextView;
}
@property(nonatomic, strong) JTopicModel *topic;

#pragma mark -
#pragma mark IBAction Methods

-(IBAction)backPushed:(id)sender;
-(IBAction)submitPushed:(id)sender;

@end
