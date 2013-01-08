//
//  JMessageDetailViewController~iphone.m
//  Jminee
//
//  Created by Robert Pieta on 1/1/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import "JMessageDetailViewController~iphone.h"

#import "JMessageModel.h"
#import "JDateTime.h"
#import "JSubjectModel.h"
#import <QuartzCore/QuartzCore.h>

@interface JMessageDetailViewController_iphone() {
@private
}
@end

@implementation JMessageDetailViewController_iphone

-(void)viewDidLoad
{
    [super viewDidLoad];
	// Do any additional setup after loading the view.
    [contentTextView.layer setCornerRadius:5.0f];
    [backgroundTextView.layer setCornerRadius:5.0f];
}

-(void)viewWillAppear:(BOOL)animated {
    [super viewWillAppear:animated];
    
    subjectLabel.text = [_subject title];
    creatorNameLabel.text = [_message creator_name];
    timeLabel.text = [[_message datetime] description];
    
    contentTextView.text = [_message content];
    
}

#pragma mark -
#pragma mark IBAction Methods

-(IBAction)backPushed:(id)sender {
    [self.navigationController popViewControllerAnimated:YES];
}

@end
