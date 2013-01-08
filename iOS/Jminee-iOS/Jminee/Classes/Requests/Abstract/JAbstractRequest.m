//
//  JAbstractRequest.m
//  Jminee
//
//  Created by Robert Pieta on 1/1/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import "JAbstractRequest.h"

#import "JErrorDisplay.h"
#import "Reachability.h"

@implementation JAbstractRequest

-(id)initRequest {
    if(self = [super init]) {
        _error_code = Error_None;
        
        _delegate = nil;
        _baseURL = URLStr_Base;
        _URLext = @"";
        
        _completed = NO;
        _successful = NO;
        
    }
    return self;
}

#pragma mark -
#pragma mark Request Methods

-(void)startRequest {
    _completed = NO;
    _successful = NO;
    
    Reachability *reachability = [Reachability reachabilityForInternetConnection];
    NetworkStatus internetStatus = [reachability currentReachabilityStatus];
    if (internetStatus == NotReachable) {
        if([self delegate]) [[self delegate] requestCannotConnectToTheInternet:self];
        _error_code = Error_NoInternet;
        return;
    }
    
    NSMutableURLRequest *request = [[NSMutableURLRequest alloc] init];
    
    NSString *urlString = [NSString stringWithFormat:@"%@%@",_baseURL,_URLext];
    NSLog(@"Created url with extension: %@",urlString);
    
    NSURL *URL = [NSURL URLWithString:urlString];
    [request setURL:URL];
    
    [request setHTTPMethod:@"GET"];
    [request setCachePolicy:NSURLRequestReloadIgnoringCacheData];
    [request setTimeoutInterval:60];
    
    requestData = [NSMutableData data];
    
    [UIApplication sharedApplication].networkActivityIndicatorVisible = YES;
    bool connect = [[NSURLConnection alloc] initWithRequest:request delegate:self];
    if (!connect) {
        _error_code = Error_ConnectionError;
        _successful = NO;
        _completed = YES;
        if([self delegate]) [[self delegate] requestFinished:self];
        return;
    }
    if([self delegate]) [[self delegate] requestStartedLoading:self];
}

-(void)cancelRequest {
    if(currentConnection) {
        [currentConnection cancel];
        currentConnection = NULL;
    }
    
    _completed = NO;
    _successful = NO;
    [UIApplication sharedApplication].networkActivityIndicatorVisible = NO;
    [NSURLConnection cancelPreviousPerformRequestsWithTarget:self];
}

#pragma mark -
#pragma mark NSURLConnection Delegate Methods

-(void)connection:(NSURLConnection *)connection didReceiveResponse:(NSURLResponse *)response{
    NSHTTPURLResponse *httpResponse = (NSHTTPURLResponse*)response;
	
    int statusCode = [httpResponse statusCode];
    NSLog(@"URL: %@, with status code: %i",[httpResponse URL],statusCode);
    
    [requestData setLength:0];
}

-(void)connection:(NSURLConnection *)connection didReceiveData:(NSData *)data {
    [requestData appendData:data];
}

-(void)connection:(NSURLConnection *)connection didFailWithError:(NSError *)error {
    _completed = YES;
    _successful = NO;
    
    _error_code = Error_ConnectionError;
    
    //Add connection timeout!
    if([error code] == 1001) {
        _error_code = Error_ConnectionTimeout;
        if([self delegate]) [[self delegate] requestTerminatedFromTimeout:self];
        return;
    }
    
    _error_code = Error_ConnectionError;
    if([self delegate]) [[self delegate] requestFinished:self];
    [UIApplication sharedApplication].networkActivityIndicatorVisible = NO;
}

-(void)connectionDidFinishLoading:(NSURLConnection *)connection {
    NSString *responseString = [[NSString alloc] initWithData:requestData encoding:NSUTF8StringEncoding];
    NSLog(@"Response string: %@",responseString);
    
    _completed = YES;
    
    NSDictionary *dict = [NSJSONSerialization JSONObjectWithData:requestData options:NSJSONWritingPrettyPrinted error:nil];
    if([[dict objectForKey:DownloadCode_Success] boolValue]) {
        _successful = true;
    }
    else {
        _successful = false;
        _error_code = [[dict objectForKey:DownloadCode_ErrorCode] intValue];
    }
    
    if([self delegate]) [[self delegate] requestFinished:self];
    [UIApplication sharedApplication].networkActivityIndicatorVisible = NO;
}

@end
