//
//  JWhatsJmineeCell.m
//  Jminee
//
//  Created by Robert Pieta on 1/5/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import "JWhatsJmineeCell.h"

#import <QuartzCore/QuartzCore.h>

@implementation JWhatsJmineeCell

- (id)initWithFrame:(CGRect)frame
{
    self = [super initWithFrame:frame];
    if (self) {
        // Initialization code
    }
    return self;
}

#pragma mark -
#pragma mark Draw Methods

-(void)drawRect:(CGRect)rect
{
	[_infoTextView.layer setCornerRadius:5.0f];
    [_imageView.layer setCornerRadius:5.0f];
    
	[super drawRect:rect];
}

@end
