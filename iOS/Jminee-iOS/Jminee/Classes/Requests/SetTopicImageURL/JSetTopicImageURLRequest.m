//
//  JSetTopicImageURLRequest.m
//  Jminee
//
//  Created by Robert Pieta on 1/1/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

#import "JSetTopicImageURLRequest.h"

@implementation JSetTopicImageURLRequest

-(id)initRequest {
    if(self = [super initRequest]) {
        _type = RequestType_SetTopicImage;
    }
    return self;
}

#pragma mark -
#pragma mark Set Topic Image URL Methods

-(void)setImageURL:(NSString*)url forTopicId:(int)uid {
    _URLext = [NSString stringWithFormat:URLStr_SetTopicImageUrl,uid,url];
}

@end
