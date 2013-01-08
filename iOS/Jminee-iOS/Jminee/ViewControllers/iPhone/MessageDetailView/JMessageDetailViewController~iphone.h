//
//  JMessageDetailViewController~iphone.h
//  Jminee
//
//  Created by Robert Pieta on 1/1/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import "JAbstractViewController~iphone.h"

@class JMessageModel;
@class JSubjectModel;
@interface JMessageDetailViewController_iphone : JAbstractViewController_iphone {
    IBOutlet UILabel *subjectLabel;
    IBOutlet UILabel *creatorNameLabel;
    IBOutlet UILabel *timeLabel;
    
    IBOutlet UITextView *contentTextView;
    IBOutlet UITextView *backgroundTextView;
}
@property(nonatomic, strong) JMessageModel *message;
@property(nonatomic, strong) JSubjectModel *subject;

#pragma mark -
#pragma mark IBAction Methods

-(IBAction)backPushed:(id)sender;

@end
