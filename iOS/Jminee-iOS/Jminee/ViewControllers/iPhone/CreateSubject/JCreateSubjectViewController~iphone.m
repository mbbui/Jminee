//
//  JCreateSubjectViewController~iphone.m
//  Jminee
//
//  Created by Robert Pieta on 1/4/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import "JCreateSubjectViewController~iphone.h"

#import "JSubjectsViewController~iphone.h"
#import "JCreateSubjectRequest.h"
#import "JTopicModel.h"
#import <QuartzCore/QuartzCore.h>

@interface JCreateSubjectViewController_iphone ()

@end

@implementation JCreateSubjectViewController_iphone

-(void)viewDidLoad
{
    [super viewDidLoad];
	// Do any additional setup after loading the view.
    [contentTextView.layer setCornerRadius:5.0f];
}

#pragma mark -
#pragma mark IBAction Methods

-(IBAction)backPushed:(id)sender {
    [self.navigationController popViewControllerAnimated:YES];
}

-(IBAction)submitPushed:(id)sender {
    NSString *title = titleTextField.text;
    NSString *content = contentTextView.text;
    
    if([title isEqualToString:@""]) {
        [self displayError:Error_NoTitle];
        return;
    }
    
    title = [title stringByAddingPercentEscapesUsingEncoding:NSASCIIStringEncoding];
    content = [content stringByAddingPercentEscapesUsingEncoding:NSASCIIStringEncoding];
    
    if(jrequest) {
        //Should be showing a download indicator.
        return;
    }
    
    jrequest = [[JCreateSubjectRequest alloc] initRequest];
    [jrequest setDelegate:self];
    JCreateSubjectRequest *createSubjectRequest = (JCreateSubjectRequest*)jrequest;
    [createSubjectRequest setTopicId:[[_topic uid] intValue] andTitle:title withContent:content];
    [createSubjectRequest startRequest];

}

#pragma mark -
#pragma mark Keyboard Methods

-(void)textViewDidBeginEditing:(UITextView *)textView {
    [self textViewDidChange:nil];
}

-(BOOL)textFieldShouldReturn:(UITextField *)textField {
    [self textFieldDidEndEditing:textField];
    return YES;
}

-(void)textFieldDidEndEditing:(UITextField *)textField {
    if([textField isEqual:titleTextField]) {
        [contentTextView becomeFirstResponder];
    }
    else [self.view endEditing:YES];
}

-(BOOL)textViewShouldEndEditing:(UITextView *)textView {
    [self.view endEditing:YES];
    return YES;
}

-(void)textViewDidChange:(UITextView *)textView {
    UIFont *myFont = [UIFont systemFontOfSize:14.0];
    
    NSString *text = contentTextView.text;
    if(contentTextView.selectedRange.location < [contentTextView.text length])
        text = [text substringToIndex:contentTextView.selectedRange.location];
    
    CGSize size = [text sizeWithFont:myFont constrainedToSize:CGSizeMake(266, 1000) lineBreakMode:NSLineBreakByWordWrapping];
    
    int center = [[ UIScreen mainScreen] bounds].size.height == 568 ? 548/2 : 460/2;
    [UIView animateWithDuration:0.3f animations:^{
        if(size.height < center) self.view.center = CGPointMake(self.view.center.x, center-size.height);
        else self.view.center = CGPointMake(self.view.center.x, 0);
    }];
}

-(void)touchesEnded:(NSSet *)touches withEvent:(UIEvent *)event {
    UITouch *touch = [touches anyObject];
    CGPoint touchLocation = [touch locationInView:self.view];
    
    if(touchLocation.y > 10) {
        [titleTextField resignFirstResponder];
        [contentTextView resignFirstResponder];
    }
    
    [self.view endEditing:YES];
}

-(void)didShowKeyboard {
    
}

-(void)didHideKeyboard {
    int center = [[ UIScreen mainScreen] bounds].size.height == 568 ? 548/2 : 460/2;
    [UIView animateWithDuration:0.3f animations:^{
        self.view.center = CGPointMake(self.view.center.x, center);
    }];
}

#pragma mark -
#pragma mark Request Methods

-(void)requestFinished:(JAbstractRequest *)request {
    if(![[request type] isEqualToString:RequestType_CreateSubject]) {
        jrequest = NULL;
        return;
    }
    
    NSLog(@"Login finished");
    
    if([request successful]) {
        int viewsCount = [[self.navigationController viewControllers] count];
        JSubjectsViewController_iphone *subjects = [[self.navigationController viewControllers] objectAtIndex:viewsCount-2];
        [subjects setRefresh:YES];
        
        NSLog(@"Successful! Login complete!");
        [self backPushed:nil];
    }
    else [self displayError:[request error_code]];
    
    jrequest = NULL;
}


@end
