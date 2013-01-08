//
//  JMessagesViewController~iphone.h
//  Jminee
//
//  Created by Robert Pieta on 1/1/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import "JAbstractViewController~iphone.h"

@class JTopicModel;
@class JSubjectModel;
@interface JMessagesViewController_iphone : JAbstractViewController_iphone {
    IBOutlet UITableView *messagesTableView;
}
@property(nonatomic, strong) JTopicModel *topic;
@property(nonatomic, strong) JSubjectModel *subject;
@property(nonatomic, assign) BOOL refresh;

#pragma mark -
#pragma mark IBAction Methods

-(IBAction)backPushed:(id)sender;
-(IBAction)newMessagePushed:(id)sender;

@end
