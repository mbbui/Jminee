//
//  JTopicCell.h
//  Jminee
//
//  Created by Robert Pieta on 1/5/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface JTopicCell : UICollectionViewCell <NSURLConnectionDelegate>
@property(nonatomic, strong) IBOutlet UIImageView *imageView;
@property(nonatomic, strong) IBOutlet UILabel *textLabel;
@property(nonatomic, strong) IBOutlet UILabel *subjectLabel;
@property(nonatomic, strong) NSString *imageURL;

#pragma mark -
#pragma mark Download Methods

-(void)downloadAndDisplayImage;

@end
