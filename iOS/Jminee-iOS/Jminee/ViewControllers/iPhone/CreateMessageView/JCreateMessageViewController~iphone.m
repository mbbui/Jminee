//
//  JCreateMessageViewController~iphone.m
//  Jminee
//
//  Created by Robert Pieta on 1/1/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import "JCreateMessageViewController~iphone.h"

#import "JTopicModel.h"
#import "JSubjectModel.h"
#import "JMessagesViewController~iphone.h"
#import "JCreateMessageRequest.h"
#import <QuartzCore/QuartzCore.h>

@interface JCreateMessageViewController_iphone() {
@private
}
@end

@implementation JCreateMessageViewController_iphone

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
    NSString *content = contentTextView.text;
    
    if([content isEqualToString:@""] || content == NULL) {
        [self displayError:Error_NoContent];
        return;
    }
    
    if(jrequest) {
        //Should be showing a download indicator.
        return;
    }
    
    content = [content stringByAddingPercentEscapesUsingEncoding:NSASCIIStringEncoding];
    
    jrequest = [[JCreateMessageRequest alloc] initRequest];
    [jrequest setDelegate:self];
    JCreateMessageRequest *createMessageRequest = (JCreateMessageRequest*)jrequest;
    [createMessageRequest setTopicId:[[_topic uid] intValue] andSubjecId:[[_subject uid] intValue] withContent:content];
    [createMessageRequest startRequest];
}

#pragma mark -
#pragma mark Keyboard Methods

-(BOOL)textViewShouldEndEditing:(UITextView *)textView {
    [self.view endEditing:YES];
    return YES;
}

-(void)textViewDidBeginEditing:(UITextView *)textView {
    [self textViewDidChange:nil];
}

-(void)touchesEnded:(NSSet *)touches withEvent:(UIEvent *)event {
    UITouch *touch = [touches anyObject];
    CGPoint touchLocation = [touch locationInView:self.view];
    
    if(touchLocation.y > 10) {
        [contentTextView resignFirstResponder];
    }
    
    [self.view endEditing:YES];
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
    if(![[request type] isEqualToString:RequestType_CreateMessage]) {
        jrequest = NULL;
        return;
    }
    
    NSLog(@"Login finished");
    
    if([request successful]) {
        int viewsCount = [[self.navigationController viewControllers] count];
        JMessagesViewController_iphone *messages = [[self.navigationController viewControllers] objectAtIndex:viewsCount-2];
        [messages setRefresh:YES];
        
        NSLog(@"Successful! Login complete!");
        [self backPushed:nil];
    }
    else [self displayError:[request error_code]];
    
    jrequest = NULL;
}

@end
