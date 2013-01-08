//
//  JTopicCell.m
//  Jminee
//
//  Created by Robert Pieta on 1/5/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import "JTopicCell.h"

#import <QuartzCore/QuartzCore.h>
#import "JCacheManager.h"

@interface JTopicCell() {
@private
    NSMutableData *requestData;
    
    BOOL downloading;
    BOOL downloaded;
    
    JCacheManager *sharedCache;
}
@end;

@implementation JTopicCell

-(id)initWithFrame:(CGRect)frame
{
    self = [super initWithFrame:frame];
    if (self) {
        // Initialization code
        _imageURL = @"";
        
        downloaded = NO;
        downloading = NO;
    }
    NSLog(@"asdad");
    
    return self;
}

-(void)prepareForReuse {
    downloaded = NO;
    downloading = NO;
    [_imageView setImage:NULL];
}

#pragma mark -
#pragma mark Download Methods

-(void)downloadAndDisplayImage {
    NSLog(@"Download for: %@",_textLabel.text);
    
    sharedCache = [JCacheManager initializeCacheManager];
    UIImage *image = [sharedCache imageForURL:_imageURL];
    if(image != NULL) {
        downloaded = YES;
        
        [_imageView setImage:image];
        NSLog(@"Found image for: %@",_textLabel.text);
    }
    
    if(downloading || downloaded) return;
    downloading = YES;
    
    requestData = [NSMutableData data];
    
    if([_imageURL isEqualToString:@""]) return;
    
    NSMutableURLRequest *request = [[NSMutableURLRequest alloc] init];
    
    NSURL *URL = [NSURL URLWithString:_imageURL];
    [request setURL:URL];
    
    [request setHTTPMethod:@"GET"];
    [request setCachePolicy:NSURLRequestReloadIgnoringCacheData];
    [request setTimeoutInterval:60];
    
    requestData = [NSMutableData data];
    
    bool connect = [[NSURLConnection alloc] initWithRequest:request delegate:self];
    if (!connect) {

    }
}


#pragma mark -
#pragma mark Draw Methods

-(void)drawRect:(CGRect)rect
{
    [_imageView.layer setMasksToBounds:YES];
	[_imageView.layer setCornerRadius:5.0f];
    
    [_subjectLabel.layer setCornerRadius:5.0f];
    [_textLabel.layer setCornerRadius:5.0f];
    
	[super drawRect:rect];
}

#pragma mark -
#pragma mark NSURLConnectionMethods

-(void)connection:(NSURLConnection *)connection didReceiveResponse:(NSURLResponse *)response{
    [requestData setLength:0];
}

-(void)connection:(NSURLConnection *)connection didReceiveData:(NSData *)data {
    [requestData appendData:data];
}

-(void)connection:(NSURLConnection *)connection didFailWithError:(NSError *)error {
    requestData = NULL;
    downloading = NO;
    NSLog(@"Download for url: %@, title: %@ failed with error: %@",_imageURL,_textLabel.text,[error description]);
}

-(void)connectionDidFinishLoading:(NSURLConnection *)connection {
    //NSString *responseString = [[NSString alloc] initWithData:requestData encoding:NSUTF8StringEncoding];
    //NSLog(@"Response string: %@",responseString);
    NSLog(@"Download for url: %@, title: %@ succeeded",_imageURL,_textLabel.text);
    
    UIImage *image = [[UIImage alloc] initWithData:requestData];
    sharedCache = [JCacheManager initializeCacheManager];
    [sharedCache cacheImage:image forURL:_imageURL];
    
    _imageView.alpha = 0.0f;
    [_imageView setImage:image];
    
    [UIView animateWithDuration:0.5f animations:^{
        _imageView.alpha = 1.0f;
    }];
    
    requestData = NULL;
    downloading = NO;
    downloaded = YES;
}

@end
