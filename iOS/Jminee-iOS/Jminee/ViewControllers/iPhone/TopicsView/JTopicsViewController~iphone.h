//
//  JTopicsViewController~iphone.h
//  Jminee
//
//  Created by Robert Pieta on 1/1/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import "JAbstractViewController~iphone.h"

@interface JTopicsViewController_iphone : JAbstractViewController_iphone <UICollectionViewDelegate,UICollectionViewDataSource,UIScrollViewDelegate> {
    IBOutlet UICollectionView *topicsCollectionView;
}
@property(nonatomic, assign) BOOL refresh;

-(IBAction)logoutPushed:(id)sender;
-(IBAction)newTopicPushed:(id)sender;

@end
