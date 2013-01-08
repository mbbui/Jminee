//
//  JCreateTopicViewController~iphone.m
//  Jminee
//
//  Created by Robert Pieta on 1/1/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import "JCreateTopicViewController~iphone.h"

#import "JCreateTopicRequest.h"
#import "JTopicsViewController~iphone.h"
#import <QuartzCore/QuartzCore.h>

@interface JCreateTopicViewController_iphone() {
@private
    NSMutableArray *membersDataSource;
}
@end

@implementation JCreateTopicViewController_iphone

-(void)viewDidLoad
{
    [super viewDidLoad];
	// Do any additional setup after loading the view.
    membersDataSource = nil;
    [membersTableView.layer setCornerRadius:5.0f];
}

#pragma mark -
#pragma mark IBAction Methods

-(IBAction)backPushed:(id)sender {
    [self.navigationController popViewControllerAnimated:YES];
}

-(IBAction)submitPushed:(id)sender {
    NSString *title = titleTextField.text;
    
    if([title isEqualToString:@""]) {
        [self displayError:Error_NoTitle];
        return;
    }
    
    title = [title stringByAddingPercentEscapesUsingEncoding:NSASCIIStringEncoding];
    
    
    if(jrequest) {
        //Should be showing a download indicator.
        return;
    }
    
    jrequest = [[JCreateTopicRequest alloc] initRequest];
    [jrequest setDelegate:self];
    JCreateTopicRequest *createTopicRequest = (JCreateTopicRequest*)jrequest;
    [createTopicRequest setTitle:title andMembers:membersDataSource];
    [createTopicRequest startRequest];
}

-(IBAction)addMemberPushed:(id)sender {
    NSString *member = membersTextView.text;
    if([self isValidEmail:member]) {
        if(membersDataSource == NULL) membersDataSource = [NSMutableArray array];
        
        [membersDataSource addObject:member];
        
        NSArray *sortedArray = [membersDataSource sortedArrayUsingComparator:^NSComparisonResult(id obj1, id obj2) {
            NSString *str1 = obj1;
            NSString *str2 = obj2;
            return [str1 compare:str2];
        }];
        membersDataSource = [NSMutableArray arrayWithArray:sortedArray];
        
        [membersTableView reloadData];
        membersTextView.text = @"";
    }
    else [self displayError:Error_InvalidMembersForm];
}

#pragma mark -
#pragma mark Keyboard Methods

-(BOOL)textFieldShouldReturn:(UITextField *)textField {
    [self textFieldDidEndEditing:textField];
    return YES;
}

-(void)textFieldDidEndEditing:(UITextField *)textField {
    if([textField isEqual:titleTextField]) {
        [membersTextView becomeFirstResponder];
    }
    else [self.view endEditing:YES];
}

-(void)touchesEnded:(NSSet *)touches withEvent:(UIEvent *)event {
    UITouch *touch = [touches anyObject];
    CGPoint touchLocation = [touch locationInView:self.view];
    
    if(touchLocation.y > 10) {
        [titleTextField resignFirstResponder];
        [membersTextView resignFirstResponder];
    }
    
    [self.view endEditing:YES];
}

-(void)didShowKeyboard {

}

-(void)didHideKeyboard {

}

#pragma mark -
#pragma mark Request Methods

-(void)requestFinished:(JAbstractRequest *)request {
    if(![[request type] isEqualToString:RequestType_CreateTopic]) {
        jrequest = NULL;
        return;
    }
    
    NSLog(@"Login finished");
    
    if([request successful]) {
        int viewsCount = [[self.navigationController viewControllers] count];
        JTopicsViewController_iphone *topics = [[self.navigationController viewControllers] objectAtIndex:viewsCount-2];
        [topics setRefresh:YES];
        
        NSLog(@"Successful! Login complete!");
        [self backPushed:nil];
    }
    else [self displayError:[request error_code]];
    
    jrequest = NULL;
}


#pragma mark -
#pragma mark Table View Methods

- (NSInteger)numberOfSectionsInTableView:(UITableView *)tableView
{
    //#warning Potentially incomplete method implementation.
    // Return the number of sections.
    return 1;
}

- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section
{
    //#warning Incomplete method implementation.
    // Return the number of rows in the section.
    return [membersDataSource count];
}

- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath
{
    static NSString *CellIdentifier = CellIdentifier_CreateTopicCell;
    
    UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:CellIdentifier];
    
    if (cell == nil) {
        cell = [[UITableViewCell alloc] initWithStyle:UITableViewCellStyleDefault reuseIdentifier:CellIdentifier];
        
        cell.accessoryType = UITableViewCellAccessoryNone;
        
    }
    
    UILabel *memberEmailLabel = (UILabel*)[cell.contentView viewWithTag:1];
    memberEmailLabel.text = [membersDataSource objectAtIndex:indexPath.row];
    
    return cell;
}
- (CGFloat)tableView:(UITableView *)tableView heightForRowAtIndexPath:(NSIndexPath *)indexPath {
    return 44.0;
}


#pragma mark - Table view delegate

- (void)tableView:(UITableView *)tableView didSelectRowAtIndexPath:(NSIndexPath *)indexPath
{
    [membersDataSource removeObjectAtIndex:indexPath.row];
    [tableView deselectRowAtIndexPath:indexPath animated:YES];
    [membersTableView reloadData];
}

@end
