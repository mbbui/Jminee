//
//  JConstants.h
//  Jminee
//
//  Created by Robert Pieta on 1/1/13.
//  Copyright (c) 2013 Robert Pieta. All rights reserved.
//

//Constants
#define KeychainKey @"Com_ZealousAmoeba_Jminee"

//Segues
#define Segue_ToResetPasswordView @"toResetPasswordView"
#define Segue_ToRegistrationView @"toRegistrationView"
#define Segue_ToTopicsView @"toTopicsView"
#define Segue_ToMessagesView @"toMessagesView"
#define Segue_ToMessageDetailView @"toMessageDetailView"
#define Segue_ToCreateTopicView @"toCreateTopicView"
#define Segue_ToCreateMessageView @"toCreateMessageView"
#define Segue_ToSubjectsView @"toSubjectsView"
#define Segue_ToCreateSubjectView @"toCreateSubjectView"
#define Segue_ToWhatsJmineeView @"toWhatsJmineeView"

//Enums
typedef enum Error_Codes {
    Error_Unauthenticated = 1,
    Error_Unautorized = 2,
    Error_InvalidInputParameter = 3,
    Error_WrongUserPassword = 4,
    Error_FailedActivation = 5,
    Error_NoResetRecord = 6,
    Error_NonExistedUser = 7,
    Error_Other = 100,
    Error_None = 1000,
    Error_ConnectionError = 1001,
    Error_NoInternet = 1002,
    Error_NoEmail = 1003,
    Error_InvalidEmail = 1004,
    Error_NoPassword = 1005,
    Error_NoUsername = 1005,
    Error_ConnectionTimeout = 1006,
    Error_NoTitle = 1007,
    Error_InvalidMembersForm = 1008,
    Error_NoContent = 1009,
} Error_Code;

typedef enum Loading_Codes {
    Loading_Login,
    Loading_Registration,
    Loading_PasswordReset,
} Loading_Code;

typedef enum Animation_Codes {
    Animation_FadeIn_Bottom,
    //FadeIn_Top,
    //SwipeIn_FromBottom,
    //SwipeIn_FromTop,
} Animation_Code;

//Url Strings
#define URLStr_Base @"http://www.jminee.com:8080"
#define URLStr_CreateMessage @"/topic/create_comment?topic_id=%i&subject_id=%i&content=%@"

//Will include more parameters soon
#define URLStr_GetMessages @"/topic/get_comments?topic_id=%i&subject_id=%i"
#define URLStr_GetSubjects @"/topic/get_subjects?topic_id=%i"

#define URLStr_CreateTopic @"/topic/create_topic?title=%@"
#define URLStr_CreateTopic_Member @"&member=%@"
#define URLStr_GetTopics @"/topic/get_topics"
#define URLStr_GetTopics_Parameters @"?title=%@&nums=%i&max_time=%i&min_time=%i"
#define URLStr_SetTopicImageUrl @"/topic/set_topic_image_url?topic_id=%i&imge_url=%@"
#define URLStr_Login @"/login_handler?login=%@&password=%@"
#define URLStr_Registration @"/registration?email_address=%@&password=%@"
#define URLStr_PasswordReset @"/registration/forget_password?email_address=%@"
#define URLStr_CreateSubject @"/topic/create_subject?topic_id=%i&title=%@"
#define URLStr_CreateSubject_Content @"&content=%@"

//Download Codes
#define DownloadCode_UserInfo @"userInfo"
#define DownloadCode_UserInfoName @"name"
#define DownloadCode_UserInfoId @"id"
#define DownloadCode_UserInfoEmail @"email"

#define DownloadCode_TopicTime @"time"
#define DownloadCode_TopicUid @"uid"
#define DownloadCode_TopicCreatorName @"creator_name"
#define DownloadCode_TopicUpdateTime @"update_time"
#define DownloadCode_TopicNewMsg @"new_msg"
#define DownloadCode_TopicTitle @"title"
#define DownloadCode_TopicImageUrl @"logourl"

#define DownloadCode_MessageUid @"uid"
#define DownloadCode_MessageCreatorName @"creator_name"
#define DownloadCode_MessageTime @"time"
#define DownloadCode_MessageTopicId @"topic_id"
#define DownloadCode_MessageSubjectUid @"subject_id"
#define DownloadCode_MessageContent @"content"
#define DownloadCode_MessageDeleted @"deleted"

#define DownloadCode_EmailAddress @"email_address"
#define DownloadCode_Password @"password"
#define DownloadCode_Success @"success"
#define DownloadCode_ErrorCode @"error_code"
#define DownloadCode_More @"more"
#define DownloadCode_Topics @"topics"
#define DownloadCode_Messages @"comments"
#define DownloadCode_Logins @"__logins"
#define DownloadCode_Subjects @"subjects"

#define DownloadCode_SubjectCreatorId @"creator_id"
#define DownloadCode_SubjectTime @"time"
#define DownloadCode_SubjectUid @"uid"
#define DownloadCode_SubjectTitle @"title"
#define DownloadCode_SubjectTopicUid @"topic_id"

//Request Types
#define RequestType_Abstract @"abstract"
#define RequestType_Login @"login"
#define RequestType_Registration @"registration"
#define RequestType_PasswordReset @"password_reset"
#define RequestType_GetTopics @"get_topics"
#define RequestType_CreateTopic @"create_topic"
#define RequestType_SetTopicImage @"set_topic_image"
#define RequestType_GetMessages @"get_messages"
#define RequestType_CreateMessage @"create_message"
#define RequestType_GetSubjects @"get_subjects"
#define RequestType_CreateSubject @"create_subject"

//Cell Indentifiers
#define CellIdentifier_TopicCell @"TopicCell"
#define CellIdentifier_MessageCell @"MessageCell"
#define CellIdentifier_SubjectCell @"SubjectCell"
#define CellIdentifier_CreateTopicCell @"CreateTopicCell"
#define CellIdentifier_JmineeInfoCell @"JmineeInfoCell"

