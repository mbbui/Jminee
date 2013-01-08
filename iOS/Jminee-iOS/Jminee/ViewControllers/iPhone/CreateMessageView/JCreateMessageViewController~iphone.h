//
//  JCreateMessageViewController~iphone.h
//  Jminee
//
//  Created by Robert Pieta on 1/1/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import "JAbstractViewController~iphone.h"

@class JTopicModel;
@class JSubjectModel;
@interface JCreateMessageViewController_iphone : JAbstractViewController_iphone <UITextViewDelegate> {
    IBOutlet UITextView *contentTextView;
}
@property(nonatomic, strong) JTopicModel *topic;
@property(nonatomic, strong) JSubjectModel *subject;

#pragma mark -
#pragma mark IBAction Methods

-(IBAction)backPushed:(id)sender;
-(IBAction)submitPushed:(id)sender;

@end
