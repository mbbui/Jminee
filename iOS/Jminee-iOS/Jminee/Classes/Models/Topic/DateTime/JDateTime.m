//
//  JDateTime.m
//  Jminee
//
//  Created by Robert Pieta on 1/1/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import "JDateTime.h"

@implementation JDateTime

-(id)initDateTimeWithString:(NSString*)string {
    if(self = [super init]) {
        [NSDateFormatter setDefaultFormatterBehavior:NSDateFormatterBehavior10_4];
        NSDateFormatter *formatter = [[NSDateFormatter alloc] init];
        [formatter setDateFormat:@"yyyy-MM-dd HH:mm:ss"];
        NSDate *date = [formatter dateFromString:string];
        
        NSDateComponents *components = [[NSCalendar currentCalendar] components:NSYearCalendarUnit|NSMonthCalendarUnit|NSDayCalendarUnit|NSHourCalendarUnit|NSMinuteCalendarUnit|NSSecondCalendarUnit fromDate:date];
        
        _year = [components year];
        _months = [components month];
        _days = [components day];
        _hours = [components hour];
        _minutes = [components minute];
        _seconds = [components second];
    }
    return self;
}

#pragma mark -
#pragma mark Compare Methods

-(BOOL)isEqual:(id)object {
    if([object class] == [self class]) {
        JDateTime *comparison = (JDateTime*)object;
        if(_year == [comparison year] && _months == [comparison months] && _days == [comparison days] && _hours == [comparison hours] && _minutes == [comparison minutes] && _seconds == [comparison seconds]) return YES;
        else return NO;
    }
    else return NO;
}

-(NSComparisonResult)compare:(JDateTime*)datetime {
    if(_year > [datetime year]) return NSOrderedAscending;
    else if(_year < [datetime year]) return NSOrderedDescending;
    
    else if(_months > [datetime months]) return NSOrderedAscending;
    else if(_months < [datetime months]) return NSOrderedDescending;
    
    else if(_days > [datetime days]) return NSOrderedAscending;
    else if(_days < [datetime days]) return NSOrderedDescending;
    
    else if(_hours > [datetime hours]) return NSOrderedAscending;
    else if(_hours < [datetime hours]) return NSOrderedDescending;
    
    else if(_minutes > [datetime minutes]) return NSOrderedAscending;
    else if(_minutes < [datetime minutes]) return NSOrderedDescending;
    
    else if(_seconds > [datetime seconds]) return NSOrderedAscending;
    else if(_seconds < [datetime seconds]) return NSOrderedDescending;
    
    return NSOrderedSame;
}

#pragma mark -
#pragma mark Current Date Constructor

-(id)initDateTimeFromCurrentDate {
    if(self = [super init]) {
        NSDate *date = [NSDate date];
        
        NSDateComponents *components = [[NSCalendar currentCalendar] components:NSYearCalendarUnit|NSMonthCalendarUnit|NSDayCalendarUnit|NSHourCalendarUnit|NSMinuteCalendarUnit|NSSecondCalendarUnit fromDate:date];
        
        _year = [components year];
        _months = [components month];
        _days = [components day];
        _hours = [components hour];
        _minutes = [components minute];
        _seconds = [components second];
    }
    return self;
}

#pragma mark -
#pragma mark NSCodying Methods

#define Coder_Year @"year"
#define Coder_Month @"month"
#define Coder_Day @"day"
#define Coder_Hour @"hour"
#define Coder_Minute @"minute"
#define Coder_Second @"second"

-(id)initWithCoder:(NSCoder *)aDecoder {
    if(self = [super init]) {
        _year = [aDecoder decodeIntForKey:Coder_Year];
        _months = [aDecoder decodeIntForKey:Coder_Month];
        _days = [aDecoder decodeIntForKey:Coder_Day];
        _hours = [aDecoder decodeIntForKey:Coder_Hour];
        _minutes = [aDecoder decodeIntForKey:Coder_Minute];
        _seconds = [aDecoder decodeIntForKey:Coder_Second];
    }
    return self;
}

-(void)encodeWithCoder:(NSCoder *)aCoder {
    [aCoder encodeInt:_year forKey:Coder_Year];
    [aCoder encodeInt:_months forKey:Coder_Month];
    [aCoder encodeInt:_days forKey:Coder_Day];
    [aCoder encodeInt:_hours forKey:Coder_Hour];
    [aCoder encodeInt:_minutes forKey:Coder_Minute];
    [aCoder encodeInt:_seconds forKey:Coder_Second];
}

#pragma mark -
#pragma mark Description

-(NSString*)description {
    //return [NSString stringWithFormat:@"%4i-%02i-%02i %02i:%02i:%02i",_year,_months,_days,_hours,_minutes,_seconds];
    return [NSString stringWithFormat:@"%02i-%02i-%4i",_months,_days,_year];
}

@end
