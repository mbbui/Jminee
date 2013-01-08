//
//  JTopicsViewController~iphone.m
//  Jminee
//
//  Created by Robert Pieta on 1/1/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import "JTopicsViewController~iphone.h"
#import "JSubjectsViewController~iphone.h"

#import "JGetTopicsRequest.h"
#import "JUserModel.h"
#import "JTopicModel.h"
#import "JDateTime.h"

#import "JTopicCell.h"

@interface JTopicsViewController_iphone() {
@private
    NSMutableArray *topicsDataSource;
    JTopicModel *selectedTopicModel;
}
@end

@implementation JTopicsViewController_iphone

-(void)viewDidLoad
{
    [super viewDidLoad];
	// Do any additional setup after loading the view.
    
    topicsDataSource = [NSMutableArray array];
    
    _refresh = YES;
    selectedTopicModel = NULL;
    //[topicsCollectionView registerClass:[JTopicCell class] forCellWithReuseIdentifier:CellIdentifier_TopicCell];
}

-(void)viewWillAppear:(BOOL)animated {
    [super viewWillAppear:animated];
    
    if(_refresh) {
        _refresh = NO;
        
        jrequest = [[JGetTopicsRequest alloc] initRequest];
        [jrequest setDelegate:self];
        JGetTopicsRequest *getTopicsRequest = (JGetTopicsRequest*)jrequest;
        [getTopicsRequest startRequest];
    }
}

#pragma mark -
#pragma mark IBAction

-(IBAction)logoutPushed:(id)sender {
    [sharedUserModel removeKeychainInfo];
    [self.navigationController popViewControllerAnimated:YES];
}

-(IBAction)newTopicPushed:(id)sender {
    [self performSegueWithIdentifier:Segue_ToCreateTopicView sender:self];
}

#pragma mark -
#pragma mark Request Methods

-(void)requestFinished:(JAbstractRequest *)request {
    if(![[request type] isEqualToString:RequestType_GetTopics]) {
        jrequest = NULL;
        return;
    }
    
    if([request successful]) {
        JGetTopicsRequest *getTopicsRequest = (JGetTopicsRequest*)jrequest;
        topicsDataSource = [getTopicsRequest getTopicsArray];
        
        NSLog(@"Successful! Get topics was successful! Data source array: %i",[topicsDataSource count]);
        [topicsCollectionView reloadData];
    }
    else [self displayError:[request error_code]];
    
    jrequest = NULL;
}

#pragma mark - Segue Methods
-(void)prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender {
    if([[segue identifier] isEqualToString:Segue_ToSubjectsView]) {
        JSubjectsViewController_iphone *destination = [segue destinationViewController];
        [destination setTopic:selectedTopicModel];
    }
}

#pragma mark -
#pragma mark UICollection View Methods

-(NSInteger)numberOfSectionsInCollectionView:(UICollectionView *)collectionView
{
    return 1;
}

-(NSInteger)collectionView:(UICollectionView *)collectionView numberOfItemsInSection:(NSInteger)section
{
    return [topicsDataSource count];
}

-(UICollectionViewCell*)collectionView:(UICollectionView *)collectionView cellForItemAtIndexPath:(NSIndexPath *)indexPath {
    static NSString *CellIdentifier = CellIdentifier_TopicCell;
    
    JTopicCell *cell = [collectionView dequeueReusableCellWithReuseIdentifier:CellIdentifier forIndexPath:indexPath];
    
    JTopicModel *topic = [topicsDataSource objectAtIndex:indexPath.row];
    
    [cell textLabel].text = [topic title];
    [cell setImageURL:[topic image_url]];
    [cell subjectLabel].text = [NSString stringWithFormat:@"%i",[topic new_msg]];
    
    [cell downloadAndDisplayImage];
    
    return cell;
}

#pragma mark -
#pragma mark UICollectionViewFlowLayoutDelegate

-(CGSize)collectionView:(UICollectionView *)collectionView layout:(UICollectionViewLayout *)collectionViewLayout sizeForItemAtIndexPath:(NSIndexPath *)indexPath
{
    return CGSizeMake(144, 118);
}

#pragma mark -
#pragma mark UIScrollViewDelegate Methods

-(void)scrollViewDidEndDragging:(UIScrollView *)scrollView willDecelerate:(BOOL)decelerate
{
    if(!decelerate) {
        [self loadImages];
    }
}

-(void)scrollViewDidEndDecelerating:(UIScrollView *)scrollView {
    [self loadImages];
}

#pragma mark -
#pragma mark Image Download Methods

-(void)loadImages {
    if([topicsDataSource count] > 0) {
        NSArray *visiblePaths = [topicsCollectionView indexPathsForVisibleItems];
        for (NSIndexPath *indexPath in visiblePaths) {
            JTopicCell *cell = (JTopicCell*)[topicsCollectionView cellForItemAtIndexPath:indexPath];
            [cell downloadAndDisplayImage];
        }
    }
}

#pragma mark -
#pragma mark UICollectionViewDelegate

-(void)collectionView:(UICollectionView *)collectionView didSelectItemAtIndexPath:(NSIndexPath *)indexPath {
    selectedTopicModel = [topicsDataSource objectAtIndex:indexPath.row];
    [self performSegueWithIdentifier:Segue_ToSubjectsView sender:self];
    [collectionView deselectItemAtIndexPath:indexPath animated:YES];
}

@end
