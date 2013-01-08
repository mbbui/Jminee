//
//  JAbstractViewController~iphone.h
//  Jminee
//
//  Created by Robert Pieta on 1/1/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import <UIKit/UIKit.h>

#import "JConstants.h"
#import "JProtocols.h"

@class JUserModel;
@interface JAbstractViewController_iphone : UIViewController <JErrorDisplayProtocol,JRequestProtocol> {
    JAbstractRequest *jrequest;
    JUserModel *sharedUserModel;
}

#pragma mark -
#pragma mark Error Methods

-(void)displayError:(Error_Code)error;

#pragma mark -
#pragma mark Loading Methods

//** NEXT TO IMPLEMENT **//
-(void)displayLoading:(Loading_Code)loading;
-(void)dismissLoading;

#pragma mark -
#pragma mark Keyboard Methods

-(void)didShowKeyboard;
-(void)didHideKeyboard;

#pragma mark -
#pragma mark Check Methods

-(BOOL)isValidEmail:(NSString*)email;

@end
