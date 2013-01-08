//
//  JSubjectsViewController~iphone.m
//  Jminee
//
//  Created by Robert Pieta on 1/4/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import "JSubjectsViewController~iphone.h"

#import "JMessagesViewController~iphone.h"
#import "JCreateSubjectViewController~iphone.h"
#import "JGetSubjectsRequest.h"
#import "JSubjectModel.h"
#import "JDateTime.h"
#import "JTopicModel.h"

@interface JSubjectsViewController_iphone() {
@private
    NSMutableArray *subjectDataSource;
    JSubjectModel *selectedSubjectModel;
}
@end

@implementation JSubjectsViewController_iphone

-(void)viewDidLoad
{
    [super viewDidLoad];
	// Do any additional setup after loading the view.
    
    subjectDataSource = [NSMutableArray array];
    
    _refresh = YES;
    
}

-(void)viewWillAppear:(BOOL)animated {
    [super viewWillAppear:animated];
    
    if(_refresh) {
        jrequest = [[JGetSubjectsRequest alloc] initRequest];
        [jrequest setDelegate:self];
        JGetSubjectsRequest *getSubjectsRequest = (JGetSubjectsRequest*)jrequest;
        [getSubjectsRequest setTopicId:[[_topic uid] intValue]];
        [getSubjectsRequest startRequest];
        
        _refresh = NO;
    }
}

#pragma mark -
#pragma mark IBAction Methods

-(IBAction)backPushed:(id)sender {
    [self.navigationController popViewControllerAnimated:YES];
}

-(IBAction)newSubjectPushed:(id)sender {
    [self performSegueWithIdentifier:Segue_ToCreateSubjectView sender:self];
}

#pragma mark -
#pragma mark Request Methods

-(void)requestFinished:(JAbstractRequest *)request {
    if(![[request type] isEqualToString:RequestType_GetSubjects]) {
        jrequest = NULL;
        return;
    }
    
    if([request successful]) {
        JGetSubjectsRequest *getSubjectsRequest = (JGetSubjectsRequest*)jrequest;
        subjectDataSource = [getSubjectsRequest getSubjectArray];
        
        NSLog(@"Successful! Get subjects was successful! Data source array: %i",[subjectDataSource count]);
        [subjectsTableView reloadData];
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
    return [subjectDataSource count];
}

- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath
{
    static NSString *CellIdentifier = CellIdentifier_SubjectCell;
    
    UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:CellIdentifier];
    
    if (cell == nil) {
        cell = [[UITableViewCell alloc] initWithStyle:UITableViewCellStyleDefault reuseIdentifier:CellIdentifier];
        
        cell.accessoryType = UITableViewCellAccessoryNone;
        
    }
    
    JSubjectModel *subject = [subjectDataSource objectAtIndex:indexPath.row];
    
    UILabel *subjectTitleLabel = (UILabel*)[cell.contentView viewWithTag:1];
    UILabel *subjectTimeLabel = (UILabel*)[cell.contentView viewWithTag:2];
    
    subjectTitleLabel.text = [subject title];
    subjectTimeLabel.text = [[subject datetime] description];
    
    return cell;
}
- (CGFloat)tableView:(UITableView *)tableView heightForRowAtIndexPath:(NSIndexPath *)indexPath {
    return 51.0;
}


#pragma mark - Table view delegate

- (void)tableView:(UITableView *)tableView didSelectRowAtIndexPath:(NSIndexPath *)indexPath
{
    selectedSubjectModel = [subjectDataSource objectAtIndex:indexPath.row];
    [tableView deselectRowAtIndexPath:indexPath animated:YES];
    [self performSegueWithIdentifier:Segue_ToMessagesView sender:self];
}

#pragma mark - Segue Methods
-(void)prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender {
    if([[segue identifier] isEqualToString:Segue_ToMessagesView]) {
        JMessagesViewController_iphone *destination = [segue destinationViewController];
        [destination setSubject:selectedSubjectModel];
        [destination setTopic:_topic];
    }
    if([[segue identifier] isEqualToString:Segue_ToCreateSubjectView]) {
        JCreateSubjectViewController_iphone *destination = [segue destinationViewController];
        [destination setTopic:_topic];
    }
}

@end
