//
//  JMessagesViewController~iphone.m
//  Jminee
//
//  Created by Robert Pieta on 1/1/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import "JMessagesViewController~iphone.h"

#import "JMessageDetailViewController~iphone.h"
#import "JCreateMessageViewController~iphone.h"
#import "JGetMessagesRequest.h"
#import "JMessageModel.h"
#import "JTopicModel.h"
#import "JDateTime.h"
#import "JSubjectModel.h"

@interface JMessagesViewController_iphone() {
@private
    NSMutableArray *messagesDataSource;
    JMessageModel *selectedMessageModel;
}
@end

@implementation JMessagesViewController_iphone

-(void)viewDidLoad
{
    [super viewDidLoad];
	// Do any additional setup after loading the view.
    
    messagesDataSource = [NSMutableArray array];
    
    _refresh = YES;
}

-(void)viewWillAppear:(BOOL)animated {
    [super viewDidAppear:animated];
    
    if(_refresh) {
        jrequest = [[JGetMessagesRequest alloc] initRequest];
        [jrequest setDelegate:self];
        JGetMessagesRequest *getMessagesRequest = (JGetMessagesRequest*)jrequest;
        [getMessagesRequest setTopicId:[[_topic uid] intValue] andSubjectId:[[_subject uid] intValue]];
        [getMessagesRequest startRequest];
        
        _refresh = NO;
    }
}

#pragma mark -
#pragma mark IBAction

-(IBAction)backPushed:(id)sender {
    [self.navigationController popViewControllerAnimated:YES];
}

-(IBAction)newMessagePushed:(id)sender {
    [self performSegueWithIdentifier:Segue_ToCreateMessageView sender:self];
}

#pragma mark -
#pragma mark Request Methods

-(void)requestFinished:(JAbstractRequest *)request {
    if(![[request type] isEqualToString:RequestType_GetMessages]) {
        jrequest = NULL;
        return;
    }
    
    if([request successful]) {
        JGetMessagesRequest *getMessagesRequest = (JGetMessagesRequest*)jrequest;
        messagesDataSource = [getMessagesRequest getMessagesArray];
        
        NSLog(@"Successful! Get messages was successful! Data source array: %i",[messagesDataSource count]);
        [messagesTableView reloadData];
    }
    else [self displayError:[request error_code]];
    
    jrequest = NULL;
}

#pragma mark -
#pragma mark Table View Methods

-(NSInteger)numberOfSectionsInTableView:(UITableView *)tableView
{
    //#warning Potentially incomplete method implementation.
    // Return the number of sections.
    return 1;
}

-(NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section
{
    //#warning Incomplete method implementation.
    // Return the number of rows in the section.
    return [messagesDataSource count];
}

- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath
{
    static NSString *CellIdentifier = CellIdentifier_MessageCell;
    
    UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:CellIdentifier];
    
    if (cell == nil) {
        cell = [[UITableViewCell alloc] initWithStyle:UITableViewCellStyleDefault reuseIdentifier:CellIdentifier];
        
        cell.accessoryType = UITableViewCellAccessoryNone;
        
    }
    
    JMessageModel *message = [messagesDataSource objectAtIndex:indexPath.row];
    
    UILabel *messageContentLabel = (UILabel*)[cell.contentView viewWithTag:1];
    UILabel *messageCreatorLabel = (UILabel*)[cell.contentView viewWithTag:2];
    UILabel *messageDateLabel = (UILabel*)[cell.contentView viewWithTag:3];
    
    messageContentLabel.text = [message content];
    messageCreatorLabel.text = [message creator_name];
    messageDateLabel.text = [[message datetime] description];
    
    return cell;
}
- (CGFloat)tableView:(UITableView *)tableView heightForRowAtIndexPath:(NSIndexPath *)indexPath {
    return 51.0;
}


#pragma mark - Table view delegate

- (void)tableView:(UITableView *)tableView didSelectRowAtIndexPath:(NSIndexPath *)indexPath
{
    selectedMessageModel = [messagesDataSource objectAtIndex:indexPath.row];
    [tableView deselectRowAtIndexPath:indexPath animated:YES];
    [self performSegueWithIdentifier:Segue_ToMessageDetailView sender:self];
}

#pragma mark - Segue Methods
-(void)prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender {
    if([[segue identifier] isEqualToString:Segue_ToMessageDetailView]) {
        JMessageDetailViewController_iphone *destination = [segue destinationViewController];
        [destination setMessage:selectedMessageModel];
        [destination setSubject:_subject];
    }
    if([[segue identifier] isEqualToString:Segue_ToCreateMessageView]) {
        JCreateMessageViewController_iphone *destination = [segue destinationViewController];
        [destination setSubject:_subject];
        [destination setTopic:_topic];
    }
}

@end
