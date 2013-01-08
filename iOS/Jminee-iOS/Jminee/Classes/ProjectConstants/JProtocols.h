//
//  JProtocols.h
//  Jminee
//
//  Created by Robert Pieta on 1/1/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

@class JAbstractRequest;
@protocol JRequestProtocol <NSObject>
@required
-(void)requestFinished:(JAbstractRequest*)request;
-(void)requestCannotConnectToTheInternet:(JAbstractRequest*)request;
-(void)requestTerminatedFromTimeout:(JAbstractRequest*)request;
-(void)requestStartedLoading:(JAbstractRequest*)request;
@end

@protocol JErrorDisplayProtocol <NSObject>
@required
-(void)errorDisplayDidFinishCurrentError;
@end