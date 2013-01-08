//
//  JErrorDisplay.h
//  Jminee
//
//  Created by Robert Pieta on 1/1/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import "JConstants.h"
#import "JProtocols.h"

@interface JErrorDisplay : UIView {
    IBOutlet UILabel *errorLabel;
    IBOutlet UIToolbar *toolbar;
}

@property(nonatomic, assign) int duration;
@property(nonatomic, assign, readonly) BOOL animating;
@property(nonatomic, assign, readonly) BOOL loading;
@property(nonatomic, assign) id <JErrorDisplayProtocol> delegate;

#pragma mark -
#pragma mark Error Display Methods

-(void)displayErrorCode:(Error_Code)error inView:(UIView*)view withAnimation:(Animation_Code)animation;

@end
