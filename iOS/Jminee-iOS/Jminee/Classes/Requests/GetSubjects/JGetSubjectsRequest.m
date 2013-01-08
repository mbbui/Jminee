//
//  JGetSubjectsRequest.m
//  Jminee
//
//  Created by Robert Pieta on 1/4/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import "JGetSubjectsRequest.h"

#import "JSubjectModel.h"

@implementation JGetSubjectsRequest

-(id)initRequest {
    if(self = [super initRequest]) {
        _type = RequestType_GetSubjects;
    }
    return self;
}

#pragma mark -
#pragma mark Get Subjects Methods

-(void)setTopicId:(int)uid {
    _URLext = [NSString stringWithFormat:URLStr_GetSubjects,uid];
}

#pragma mark -
#pragma mark Get Subjects Array

-(NSMutableArray*)getSubjectArray {
    if([super completed] && [super successful] && requestData != NULL) {
        NSDictionary *jsonDict = [NSJSONSerialization JSONObjectWithData:requestData options:NSJSONWritingPrettyPrinted error:nil];
        NSArray *jsonArray = [[jsonDict objectForKey:DownloadCode_Subjects] copy];
        NSMutableArray *subjectsArray = [NSMutableArray array];
        
        for(NSDictionary *subjectDict in jsonArray) {
            JSubjectModel *subject = [[JSubjectModel alloc] initSubjectModelWithJSONDictionary:subjectDict];
            [subjectsArray addObject:subject];
        }
        return subjectsArray;
        
    }
    else return [NSArray array];
}

@end
