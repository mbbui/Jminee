//
//  JCreateTopicViewController~iphone.h
//  Jminee
//
//  Created by Robert Pieta on 1/1/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import "JAbstractViewController~iphone.h"

@interface JCreateTopicViewController_iphone : JAbstractViewController_iphone <UITextFieldDelegate,UITableViewDataSource,UITableViewDelegate> {
    IBOutlet UITextField *titleTextField;
    IBOutlet UITextField *membersTextView;
    
    IBOutlet UITableView *membersTableView;
}

#pragma mark -
#pragma mark IBAction Methods

-(IBAction)backPushed:(id)sender;
-(IBAction)submitPushed:(id)sender;
-(IBAction)addMemberPushed:(id)sender;

@end
