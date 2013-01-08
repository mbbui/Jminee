//
//  JDateTime.h
//  Jminee
//
//  Created by Robert Pieta on 1/1/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface JDateTime : NSObject <NSCoding>
@property(nonatomic, assign, readonly) int year;
@property(nonatomic, assign, readonly) int months;
@property(nonatomic, assign, readonly) int days;
@property(nonatomic, assign, readonly) int hours;
@property(nonatomic, assign, readonly) int minutes;
@property(nonatomic, assign, readonly) int seconds;
@property(nonatomic, strong, readonly) NSString *dateString;

-(id)initDateTimeWithString:(NSString*)string;

#pragma mark -
#pragma mark Compare Methods

-(BOOL)isEqual:(id)object;
-(NSComparisonResult)compare:(JDateTime*)datetime;

#pragma mark -
#pragma mark Current Date Constructor

-(id)initDateTimeFromCurrentDate;

#pragma mark -
#pragma mark Description

-(NSString*)description;

@end
