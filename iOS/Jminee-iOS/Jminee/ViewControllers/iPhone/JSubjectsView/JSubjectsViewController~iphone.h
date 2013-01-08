//
//  JSubjectsViewController~iphone.h
//  Jminee
//
//  Created by Robert Pieta on 1/4/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import "JAbstractViewController~iphone.h"

@class JTopicModel;
@interface JSubjectsViewController_iphone : JAbstractViewController_iphone <UITableViewDataSource,UITableViewDelegate> {
    IBOutlet UITableView *subjectsTableView;
}
@property(nonatomic, strong) JTopicModel *topic;
@property(nonatomic, assign) BOOL refresh;

#pragma mark -
#pragma mark IBAction Methods

-(IBAction)backPushed:(id)sender;
-(IBAction)newSubjectPushed:(id)sender;

@end
