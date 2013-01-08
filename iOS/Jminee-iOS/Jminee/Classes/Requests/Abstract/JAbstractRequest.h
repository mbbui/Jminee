//
//  JAbstractRequest.h
//  Jminee
//
//  Created by Robert Pieta on 1/1/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "JProtocols.h"
#import "JConstants.h"

@interface JAbstractRequest : NSObject <NSURLConnectionDelegate> {
    Error_Code _error_code;
    
    NSMutableData *requestData;
    NSURLConnection *currentConnection;
    
    @protected
    NSString *_URLext;
    NSString *_type;
}

@property(nonatomic, assign) id <JRequestProtocol> delegate;
@property(nonatomic, strong, readonly) NSString *baseURL;
@property(nonatomic, strong, readonly) NSString *URLext;
@property(nonatomic, strong, readonly) NSString *type;

@property(nonatomic, assign) BOOL completed;
@property(nonatomic, assign) BOOL successful;
@property(nonatomic, assign, readonly) Error_Code error_code;

-(id)initRequest;

#pragma mark -
#pragma mark Request Methods

-(void)startRequest;
-(void)cancelRequest;

@end
