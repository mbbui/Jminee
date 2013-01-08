//
//  JWhatsJmineeViewController~iphone.m
//  Jminee
//
//  Created by Robert Pieta on 1/4/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import "JWhatsJmineeViewController~iphone.h"

#import "JWhatsJmineeCell.h"

@interface JWhatsJmineeViewController_iphone() {
@private
    NSMutableArray *textDataSource;
    NSMutableArray *imageDataSource;
}

@end

@implementation JWhatsJmineeViewController_iphone

-(void)viewDidLoad
{
    [super viewDidLoad];
	// Do any additional setup after loading the view.
    textDataSource = [NSMutableArray array];
    imageDataSource = [NSMutableArray array];
    
    [textDataSource addObject:@"Automatically organize all your notifications!"];
    [imageDataSource addObject:[NSNull null]];
    
    [textDataSource addObject:@"Automatically organize all your notifications!"];
    [imageDataSource addObject:[NSNull null]];
    
    [textDataSource addObject:@"Automatically organize all your notifications!"];
    [imageDataSource addObject:[NSNull null]];
    
    [textDataSource addObject:@"Automatically organize all your notifications!"];
    [imageDataSource addObject:[NSNull null]];
    
    [textDataSource addObject:@"Automatically organize all your notifications!"];
    [imageDataSource addObject:[NSNull null]];
    
    [textDataSource addObject:@"Automatically organize all your notifications!"];
    [imageDataSource addObject:[NSNull null]];
}

#pragma mark -
#pragma mark IBAction Methods

-(IBAction)backPushed:(id)sender {
    [self.navigationController popViewControllerAnimated:YES];
}

#pragma mark -
#pragma mark UICollection View Methods

-(NSInteger)numberOfSectionsInCollectionView:(UICollectionView *)collectionView
{
    return 1;
}

-(NSInteger)collectionView:(UICollectionView *)collectionView numberOfItemsInSection:(NSInteger)section
{
    return [textDataSource count];
}

-(UICollectionViewCell*)collectionView:(UICollectionView *)collectionView cellForItemAtIndexPath:(NSIndexPath *)indexPath {
    static NSString *CellIdentifier = CellIdentifier_JmineeInfoCell;
    
    JWhatsJmineeCell *cell = [collectionView dequeueReusableCellWithReuseIdentifier:CellIdentifier forIndexPath:indexPath];
    
    [cell infoTextView].text = [textDataSource objectAtIndex:indexPath.row];
    
    UIImage *image = [imageDataSource objectAtIndex:indexPath.row];
    if(image && ![image isEqual:[NSNull null]]) {
        [cell imageView].image = image;
    }
    
    return cell;
}

#pragma mark -
#pragma mark UICollectionViewFlowLayoutDelegate

-(CGSize)collectionView:(UICollectionView *)collectionView layout:(UICollectionViewLayout *)collectionViewLayout sizeForItemAtIndexPath:(NSIndexPath *)indexPath
{
    return CGSizeMake(145, 145);
}

#pragma mark -
#pragma mark UICollectionViewDelegate

-(void)collectionView:(UICollectionView *)collectionView didSelectItemAtIndexPath:(NSIndexPath *)indexPath {
    [collectionView deselectItemAtIndexPath:indexPath animated:YES];
}

@end
