**DOCUMENT STRUCTURE**
The requested document **is appended to this terms and conditions page** . This document
**contains supplementary attachments** . To access the supplementary attachments, you must open
[this document in an application that supports PDF attachments. See the AWS Artifact User Guide](https://docs.aws.amazon.com/artifact/latest/ug/downloading-documents.html#view-attachments-in-pdf)
for instructions on how to open attachments.


**TERMS AND CONDITIONS**

You hereby agree that you will not distribute, display, or otherwise make this document available
to an _individual or entity_, unless expressly permitted herein. This document is AWS Confidential
[Information (as defined in the AWS Customer Agreement), and you may not remove these terms](https://aws.amazon.com/agreement/)
and conditions from this document, nor take excerpts of this document, without Amazon’s
express written consent. You may not use this document for purposes competitive with Amazon.
You may distribute this document, in its complete form, upon the commercially reasonable
request by (1) an end user of your service, to the extent that your service functions on relevant
AWS offerings provided that such distribution is accompanied by documentation that details the
function of AWS offerings in your service, provided that you have entered into a confidentiality
agreement with the end user that includes terms not less restrictive than those provided herein
and have named Amazon as an intended beneficiary, or (2) a regulator, so long as you request
confidential treatment of this document (each (1) and (2) is deemed a “Permitted Recipient”).
You must keep comprehensive records of all Permitted Recipient requests, and make such records
available to Amazon and its auditors, upon request. You further (i) acknowledge and agree that
you do not acquire any rights against Amazon’s Service Auditors in connection with your receipt
or use of this document, and (ii) release Amazon’s Service Auditor from any and all claims or
causes of action that you have now or in the future against Amazon’s Service Auditor arising from
this document. The foregoing sentence is meant for the benefit of Amazon’s Service Auditors,
who are entitled to enforce it. “Service Auditor” means the party that created this document for
Amazon or assisted Amazon with creating this document.


## System and Organization Controls 2 (SOC 2) Type 2 Report Description of the Amazon Web Services System Relevant to Security, Availability, Confidentiality, and Privacy For the Period April 1, 2024 to March 31, 2025

Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


#### **Description of the Amazon Web Services System Relevant to Security,** **Availability, Confidentiality, and Privacy**

**Table of Contents**


SECTION I – Assertion of Amazon Web Services ........................................................................................... 3


SECTION II – Independent Service Auditor’s Assurance Report ................................................................. 11


SECTION III – Description of the Amazon Web Services System Relevant to Security, Availability,
Confidentiality, and Privacy ........................................................................................................................ 21


Amazon Web Services System Overview ............................................................................................... 22


Relevant Aspects of Internal Controls .................................................................................................... 28


A. Policies ........................................................................................................................................ 29


B. Communications .............................................................................................................................


C. Service Commitments and System Requirements ...................................................................... 33


D. Procedures .................................................................................................................................. 34


E. Monitoring .................................................................................................................................. 90


Complementary User Entity Controls ..................................................................................................... 91


SECTION IV – Description of Criteria, AWS Controls, Tests, and Results of Tests ...................................... 95


Testing Performed and Results of Entity-Level Controls ........................................................................ 96


Procedures for Assessing Completeness and Accuracy of Information Provided by the Entity (IPE) .... 96


Trust Services Criteria and Related Controls for Systems and Applications .......................................... 96


Information System Control Environment ............................................................................................. 97


AWS Controls Mapped to the Security, Availability, Confidentiality, and Privacy Criteria .................... 97


Security, Availability, Confidentiality and Privacy Criteria Mapped to AWS Controls & Service
Auditor’s Testing Performed and Results ............................................................................................. 111


SECTION V – Other Information Provided By Amazon Web Services ....................................................... 179


Modifications to existing controls ........................................................................................................ 180


Addition of new controls ...................................................................................................................... 181


APPENDIX – Glossary of Terms ................................................................................................................. 182


Appendix – Glossary of Terms .............................................................................................................. 183


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


2


### **SECTION I – Assertion of Amazon Web Services**

Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


3


**Amazon Web Services**

410 Terry Avenue North
Seattle, WA 98109-5210


**Amazon Web Services’ Management Assertion**

We have prepared the accompanying description titled “Description of the Amazon Web Services System
Relevant to Security, Availability, Confidentiality, and Privacy” (Description) of Amazon Web Services, Inc.
(“AWS” or “Service Organization”) in accordance with the criteria for a description of a service
organization’s system set forth in the Description Criteria DC section 200 _2018 Description Criteria for a_
_Description of a Service Organization’s System in a SOC 2 Report_ (Description Criteria). The Description is
intended to provide report users with information about the Amazon Web Services System (System) that
may be useful when assessing the risks arising from interactions with the System, particularly information
about system controls that the Service Organization has designed, implemented and operated to provide
reasonable assurance that its service commitments and system requirements were achieved based on the
trust services criteria relevant to security, availability, confidentiality, and privacy (applicable trust services
criteria) set forth in TSP section 100, _2017 Trust Services Criteria for Security, Availability, Processing_
_Integrity, Confidentiality, and Privacy,_ in _AICPA Trust Services Criteria_ .


The scope of this system description includes the following services:




- Amazon API Gateway

- Amazon AppFlow

- Amazon Application Recovery Controller

- Amazon AppStream 2.0

- Amazon Athena

- Amazon Augmented AI [excludes Public

Workforce and Vendor Workforce for all

features]

- Amazon Bedrock [excludes Amazon
Bedrock Marketplace]

- Amazon Braket

- Amazon Chime

- Amazon Chime SDK

- Amazon Cloud Directory

- Amazon CloudFront [excludes content
delivery through Amazon CloudFront
Embedded Point of Presences]

- Amazon CloudWatch

- Amazon CloudWatch Logs

- Amazon CodeWhisperer

- Amazon Cognito

- Amazon Comprehend

- Amazon Comprehend Medical

- Amazon Connect

- Amazon Data Firehose

- Amazon DataZone




- Amazon WorkSpaces

- Amazon WorkSpaces Secure Browser
(formerly known as Amazon Workspaces
Web)

- Amazon WorkSpaces Thin Client

- AWS Amplify

- AWS App Mesh

- AWS App Runner

- AWS AppFabric

- AWS Application Migration Service

- AWS AppSync

- AWS Artifact

- AWS Audit Manager

- AWS B2B Data Interchange

- AWS Backup

- AWS Batch

- AWS Certificate Manager (ACM)

- AWS Chatbot

- AWS Clean Rooms

- AWS Cloud Map

- AWS Cloud9

- AWS CloudFormation

- AWS CloudHSM

- AWS CloudShell

- AWS CloudTrail

- AWS CodeBuild



Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


4


- Amazon Detective

- Amazon DevOps Guru

- Amazon DocumentDB [with MongoDB
compatibility]

- Amazon DynamoDB

- Amazon DynamoDB Accelerator (DAX)

- Amazon EC2 Auto Scaling

- Amazon Elastic Block Store (EBS)

- Amazon Elastic Compute Cloud (EC2)

- Amazon Elastic Container Registry (ECR)

- Amazon Elastic Container Service [both
Fargate and EC2 launch types]

- Amazon Elastic File System (EFS)

- Amazon Elastic Kubernetes Service (EKS)

[both Fargate and EC2 launch types]

- Amazon Elastic MapReduce (EMR)

- Amazon ElastiCache

- Amazon EventBridge

- Amazon FinSpace

- Amazon Forecast

- Amazon Fraud Detector

- Amazon FSx

- Amazon GuardDuty

- Amazon Inspector

- Amazon Inspector Classic

- Amazon Kendra

- Amazon Keyspaces (for Apache Cassandra)

- Amazon Kinesis Data Streams

- Amazon Kinesis Video Streams

- Amazon Lex

- Amazon Location Service

- Amazon Macie

- Amazon Managed Grafana

- Amazon Managed Service for Apache Flink

- Amazon Managed Service for Prometheus

- Amazon Managed Streaming for Apache
Kafka

- Amazon Managed Workflows for Apache
Airflow (Amazon MWAA)

- Amazon MemoryDB (formerly known as
Amazon MemoryDB for Redis)

- Amazon MQ



**Amazon Web Services**

410 Terry Avenue North
Seattle, WA 98109-5210


- AWS CodeCommit

- AWS CodeDeploy

- AWS CodePipeline

- AWS Config

- AWS Control Tower

- AWS Data Exchange

- AWS Database Migration Service (DMS)

- AWS DataSync

- AWS Direct Connect

- AWS Directory Service [excludes Simple AD]

- AWS Elastic Beanstalk

- AWS Elastic Disaster Recovery

- AWS Elemental MediaConnect

- AWS Elemental MediaConvert

- AWS Elemental MediaLive

- AWS Entity Resolution

- AWS Fault Injection Service

- AWS Firewall Manager

- AWS Global Accelerator

- AWS Glue

- AWS Glue DataBrew

- AWS Health Dashboard

- AWS HealthImaging

- AWS HealthLake

- AWS HealthOmics

- AWS IAM Identity Center

- AWS Identity and Access Management
(IAM)

- AWS IoT Core

- AWS IoT Device Defender

- AWS IoT Device Management

- AWS IoT Events

- AWS IoT Greengrass

- AWS IoT SiteWise

- AWS IoT TwinMaker

- AWS Key Management Service (KMS)

- AWS Lake Formation

- AWS Lambda

- AWS License Manager

- AWS Mainframe Modernization

- AWS Managed Services

- AWS Network Firewall



Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


5


- Amazon Neptune

- Amazon OpenSearch Service

- Amazon Personalize

- Amazon Pinpoint and End User Messaging
(formerly Amazon Pinpoint)

- Amazon Polly

- Amazon Q Business

- Amazon Q Developer

- Amazon Quantum Ledger Database (QLDB)

- Amazon QuickSight

- Amazon Redshift

- Amazon Rekognition

- Amazon Relational Database Service (RDS)

- Amazon Route 53

- Amazon S3 Glacier

- Amazon SageMaker AI (formerly Amazon
SageMaker) [excludes Studio Lab, Public

Workforce and Vendor Workforce for all

features]

- Amazon Security Lake

- Amazon Simple Email Service (SES)

- Amazon Simple Notification Service (SNS)

- Amazon Simple Queue Service (SQS)

- Amazon Simple Storage Service (S3)

- Amazon Simple Workflow Service (SWF)

- Amazon SimpleDB

- Amazon Textract

- Amazon Timestream

- Amazon Transcribe

- Amazon Translate

- Amazon Verified Permissions

- Amazon Virtual Private Cloud (VPC)

- Amazon WorkDocs

- Amazon WorkMail



**Amazon Web Services**

410 Terry Avenue North
Seattle, WA 98109-5210


- AWS OpsWorks [includes Chef Automate,
Puppet Enterprise]

- AWS OpsWorks Stacks

- AWS Organizations

- AWS Outposts

- AWS Payment Cryptography

- AWS Private Certificate Authority

- AWS Resilience Hub

- AWS Resource Access Manager (RAM)

- AWS Resource Explorer

- AWS Resource Groups

- AWS RoboMaker

- AWS Secrets Manager

- AWS Security Hub

- AWS Serverless Application Repository

- AWS Service Catalog

- AWS Shield

- AWS Signer

- AWS Snowball

- AWS Snowball Edge

- AWS Step Functions

- AWS Storage Gateway

- AWS Systems Manager

- AWS Transfer Family

- AWS User Notifications

- AWS Verified Access

- AWS WAF

- AWS Wickr

- AWS X-Ray

- EC2 Image Builder

- Elastic Load Balancing (ELB)

- FreeRTOS

- VM Import/Export



More information about the in-scope services, can be found at the following web address:
[https://aws.amazon.com/compliance/services-in-scope/](https://aws.amazon.com/compliance/services-in-scope/)


The scope of locations covered in this report includes the supporting data centers located in the following
regions:


  - **Australia:** Asia Pacific (Sydney) (ap-southeast-2), Asia Pacific (Melbourne) (ap-southeast-4)


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


6


**Amazon Web Services**

410 Terry Avenue North
Seattle, WA 98109-5210


  - **Bahrain:** Middle East (Bahrain) (me-south-1)

  - **Brazil:** South America (São Paulo) (sa-east-1)

  - **Canada:** Canada (Central) (ca-central-1), Canada West (Calgary) (ca-west-1)

  - **England:** Europe (London) (eu-west-2)

  - **France:** Europe (Paris) (eu-west-3)

  - **Germany:** Europe (Frankfurt) (eu-central-1)

  - **Hong Kong:** Asia Pacific (ap-east-1)

  - **India:** Asia Pacific (Mumbai) (ap-south-1), Asia Pacific (Hyderabad) (ap-south-2)

  - **Indonesia:** Asia Pacific (Jakarta) (ap-southeast-3)

  - **Ireland:** Europe (Ireland) (eu-west-1)

  - **Israel:** Israel (Tel Aviv) (il-central-1)

  - **Italy:** Europe (Milan) (eu-south-1)

  - **Japan:** Asia Pacific (Tokyo) (ap-northeast-1), Asia Pacific (Osaka) (ap-northeast-3)

  - **Malaysia:** Asia Pacific (Malaysia) (ap-southeast-5)*

  - **Mexico:** Mexico (Central) (mx-central-1)*

  - **Singapore:** Asia Pacific (Singapore) (ap-southeast-1)

  - **South Africa:** Africa (Cape Town) (af-south-1)

  - **South Korea:** Asia Pacific (Seoul) (ap-northeast-2)

  - **Spain:** Europe (Spain) (eu-south-2)

  - **Sweden:** Europe (Stockholm) (eu-north-1)

  - **Switzerland:** Europe (Zurich) (eu-central-2)

  - **Thailand:** Asia Pacific (Thailand) (ap-southeast-7)*

  - **United Arab Emirates:** Middle East (UAE) (me-central-1)

  - **United States:** US East (Northern Virginia) (us-east-1), US East (Ohio) (us-east-2), US West
(Oregon) (us-west-2), US West (Northern California) (us-west-1), AWS GovCloud (US-East) (usgov-east-1), AWS GovCloud (US-West) (us-gov-west-1)


- Effective date for this region is February 15, 2025.

and the following AWS Edge locations in:




- Caba, Argentina

- General Pacheco,

Argentina

- Brisbane, Australia

- Canberra, Australia

- Melbourne, Australia

- Perth, Australia

- Vienna, Austria

- Brussels, Belgium

- Fortaleza, Brazil

- Rio de Janeiro, Brazil




- Milan, Italy

- Rome, Italy

- Inzai, Japan

- Nairobi, Kenya

- Kuala Lumpur, Malaysia

- Santiago de Querétaro,

Mexico

- Amsterdam, Netherlands

- Diemen, Netherlands

- Schiphol-Rijk, Netherlands

- Auckland, New Zealand




- Atlanta, United States

- Aurora, United States

- Bluffdale, United States

- Boston, United States

- Chandler, United States

- Chicago, United States

- Columbus, United States

- Dallas, United States

- Denver, United States

- El Segundo, United States



Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


7


- São Paulo, Brazil

- Sofia, Bulgaria

- Scarborough, Canada

- Toronto, Canada

- Vancouver, Canada

- Huechuraba, Chile

- Santiago, Chile

- Bogotá, Colombia

- Zagreb, Croatia

- Prague, Czech Republic

- Ballerup, Denmark

- Cairo, Egypt

- Tallinn, Estonia

- Helsinki, Finland

- Espoo, Finland

- Marseille, France

- Berlin, Germany

- Dusseldorf, Germany

- Frankfurt, Germany

- Hamburg, Germany

- Munich, Germany

- Koropi, Greece

- Kropia, Greece

- Budapest, Hungary

- Bangalore, India

- Chennai, India

- Kolkata, India

- Mumbai, India

- New Delhi, India

- Noida, India

- Pune, India

- Jakarta, Indonesia

- Clonshaugh, Ireland

- Dublin, Ireland

- Haifa, Israel




- Rosedale, New Zealand

- Lagos, Nigeria

- Oslo, Norway

- Barka, Oman

- Santiago de Surco, Peru

- Manila, Philippines

- Quezon, Philippines

- Warsaw, Poland

- Lisbon, Portugal

- Doha, Qatar

- Bucharest, Romania

- Jeddah, Saudi Arabia

- Singapore, Singapore

- Cape Town, South Africa

- Johannesburg, South Africa

- Anyang-si, South Korea

- Seoul, South Korea

- Barcelona, Spain

- Madrid, Spain

- Stockholm, Sweden

- Zurich, Switzerland

- New Taipei City, Taiwan

- Taipei, Taiwan

- Bangkok, Thailand

- Bang Chalong, Thailand

- Istanbul, Turkey

- Dubai, United Arab

Emirates

- Fujairah, United Arab

Emirates

- London, United Kingdom

- Manchester, United

Kingdom

- Swinton, United Kingdom

- Ashburn, United States



**Amazon Web Services**

410 Terry Avenue North
Seattle, WA 98109-5210


 - Elk Grove Village, United

States

 - Franklin, United States

 - Greenwood Village, United

States

 - Hillsboro, United States

 - Houston, United States

 - Irvine, United States

 - Kansas City, United States

 - Las Vegas, United States

 - Los Angeles, United States

 - Lynnwood, United States

 - Miami, United States

 - Milpitas, United States

 - Minneapolis, United States

 - New York City, United States

 - Newark, United States

 - North Las Vegas, United

States

 - Philadelphia, United States

 - Phoenix, United States

 - Piscataway, United States

 - Pittsburgh, United States

 - Portland, United States

 - Reston, United States

 - Richardson, United States

 - Seattle, United States

 - Secaucus, United States

 - Tampa, United States

 - Tempe, United States

 - West Valley City, United

States

 - Hanoi, Vietnam

 - Ho Chi Minh, Vietnam



Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


8


**Amazon Web Services**

410 Terry Avenue North
Seattle, WA 98109-5210



and the following Wavelength locations in:




  - Toronto, Canada   - Alpharetta, United States   - Minneapolis, United States

  - Berlin, Germany   - Annapolis Junction, United   - New Berlin, United States

  - Dortmund, Germany States   - Pembroke Pines, United States

  - Munich, Germany   - Aurora, United States   - Plant City, United States

  - Osaka, Japan   - Azusa, United States   - Redmond, United States

  - Tama, Japan   - Charlotte, United States   - Rocklin, United States

  - Daejeon, South Korea   - Euless, United States   - Southfield, United States

  - Seoul, South Korea   - Houston, United States   - Tempe, United States

  - London, United Kingdom   - Knoxville, United States   - Wall Township, United States

  - Salford, United Kingdom   - Las Vegas, United States   - Westborough, United States


as well as Local Zone locations in:




- Toronto, Canada

- Berlin, Germany

- Dortmund, Germany

- Munich, Germany

- Osaka, Japan

- Tama, Japan

- Daejeon, South Korea

- Seoul, South Korea

- London, United Kingdom

- Salford, United Kingdom




- Alpharetta, United States

- Annapolis Junction, United

States

- Aurora, United States

- Azusa, United States

- Charlotte, United States

- Euless, United States

- Houston, United States

- Knoxville, United States

- Las Vegas, United States




- Caba, Argentina

- Perth, Australia

- Santiago, Chile

- Ballerup, Denmark

- Espoo, Finland

- Hamburg, Germany

- Kolkata, India

- New Delhi, India

- Noida, India*

- Santiago de Queretaro,

Mexico

- Nouaceur, Morocco

- Rosedale, New Zealand

- Lagos, Nigeria

- Barka, Oman

- Santiago de Surco, Peru




- Manila, Philippines

- Warsaw, Poland

- Singapore, Singapore*

- New Taipei City, Taiwan

- Bang Chalong, Thailand

- Atlanta, United States

- Boston, United States

- Chicago, United States

- Doral, United States

- El Segundo, United States

- Garland, United States

- Greenwood Village,

United States

- Hillsboro, United States

- Houston, United States

- Irvine, United States




- Itasca, United States

- Kansas City, United States

- Kapolei, United States

- Las Vegas, United States

- Lee's Summit, United States*

- Lithia Springs, United States

- Mesa, United States

- Miami, United States

- Minneapolis, United States

- North Las Vegas, United

States

- Philadelphia, United States

- Phoenix, United States

- Piscataway, United States

- Richardson, United States

- Seattle, United States




- This location is a Dedicated Local Zone and may not be available to all customers.

The Description also indicates complementary user entity controls that are suitably designed and
operating effectively are necessary along with AWS’ controls to achieve the service commitments and
system requirements. The Description presents AWS’ controls and the complementary user entity
controls assumed in the design of AWS’ controls.

We confirm, to the best of our knowledge and belief, that:


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


9


**Amazon Web Services**

410 Terry Avenue North
Seattle, WA 98109-5210


a. The Description presents the System that was designed and implemented throughout the period

April 1, 2024 to March 31, 2025 in accordance with the Description Criteria.


b. The controls stated in the Description were suitably designed throughout the period April 1, 2024

to March 31, 2025 to provide reasonable assurance that AWS’ service commitments and system
requirements would be achieved based on the applicable trust services criteria, if its controls
operated throughout that period, and if user entities applied the complementary user entity
controls assumed in the design of AWS’ controls throughout the period April 1, 2024 to March 31,

2025.


c. The AWS controls stated in the Description operated effectively throughout the period April 1, 2024

to March 31, 2025 to provide reasonable assurance that AWS’ service commitments and system
requirements were achieved based on the applicable trust services criteria, if the complementary
user entity controls assumed in the design of AWS’ controls operated effectively throughout that
period.

Amazon Web Services Management


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


10


### **SECTION II – Independent Service Auditor’s Assurance Report**

Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


11


### **SECTION III – Description of the Amazon Web Services System** **Relevant to Security, Availability, Confidentiality, and Privacy**

Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


21


Section III – Description of the Amazon Web Services System


**Amazon Web Services System Overview**

Since 2006, Amazon Web Services (AWS) has provided flexible, scalable and secure IT infrastructure to
businesses of all sizes around the world. With AWS, customers can deploy solutions in a cloud computing
environment that provides compute power, storage, and other application services over the Internet as
their business needs demand. AWS affords businesses the flexibility to employ the operating systems,
application programs, and databases of their choice.


The scope of this system description includes the following services:




- Amazon API Gateway

- Amazon AppFlow

- Amazon Application Recovery Controller

- Amazon AppStream 2.0

- Amazon Athena

- Amazon Augmented AI [excludes Public

Workforce and Vendor Workforce for all

features]

- Amazon Bedrock [excludes Amazon Bedrock
Marketplace]

- Amazon Braket

- Amazon Chime

- Amazon Chime SDK

- Amazon Cloud Directory

- Amazon CloudFront [excludes content delivery
through Amazon CloudFront Embedded Point
of Presences]

- Amazon CloudWatch

- Amazon CloudWatch Logs

- Amazon CodeWhisperer

- Amazon Cognito

- Amazon Comprehend

- Amazon Comprehend Medical

- Amazon Connect

- Amazon Data Firehose

- Amazon DataZone

- Amazon Detective

- Amazon DevOps Guru

- Amazon DocumentDB [with MongoDB
compatibility]

- Amazon DynamoDB

- Amazon DynamoDB Accelerator (DAX)

- Amazon EC2 Auto Scaling

- Amazon Elastic Block Store (EBS)

- Amazon Elastic Compute Cloud (EC2)

- Amazon Elastic Container Registry (ECR)




- Amazon WorkSpaces

- Amazon WorkSpaces Secure Browser
(formerly known as Amazon Workspaces
Web)

- Amazon WorkSpaces Thin Client

- AWS Amplify

- AWS App Mesh

- AWS App Runner

- AWS AppFabric

- AWS Application Migration Service

- AWS AppSync

- AWS Artifact

- AWS Audit Manager

- AWS B2B Data Interchange

- AWS Backup

- AWS Batch

- AWS Certificate Manager (ACM)

- AWS Chatbot

- AWS Clean Rooms

- AWS Cloud Map

- AWS Cloud9

- AWS CloudFormation

- AWS CloudHSM

- AWS CloudShell

- AWS CloudTrail

- AWS CodeBuild

- AWS CodeCommit

- AWS CodeDeploy

- AWS CodePipeline

- AWS Config

- AWS Control Tower

- AWS Data Exchange

- AWS Database Migration Service (DMS)

- AWS DataSync

- AWS Direct Connect

- AWS Directory Service [excludes Simple AD]



Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


22


Section III – Description of the Amazon Web Services System




- Amazon Elastic Container Service [both Fargate
and EC2 launch types]

- Amazon Elastic File System (EFS)

- Amazon Elastic Kubernetes Service (EKS) [both
Fargate and EC2 launch types]

- Amazon Elastic MapReduce (EMR)

- Amazon ElastiCache

- Amazon EventBridge

- Amazon FinSpace

- Amazon Forecast

- Amazon Fraud Detector

- Amazon FSx

- Amazon GuardDuty

- Amazon Inspector

- Amazon Inspector Classic

- Amazon Kendra

- Amazon Keyspaces (for Apache Cassandra)

- Amazon Kinesis Data Streams

- Amazon Kinesis Video Streams

- Amazon Lex

- Amazon Location Service

- Amazon Macie

- Amazon Managed Grafana

- Amazon Managed Service for Apache Flink

- Amazon Managed Service for Prometheus

- Amazon Managed Streaming for Apache Kafka

- Amazon Managed Workflows for Apache
Airflow (Amazon MWAA)

- Amazon MemoryDB (formerly known as
Amazon MemoryDB for Redis)

- Amazon MQ

- Amazon Neptune

- Amazon OpenSearch Service

- Amazon Personalize

- Amazon Pinpoint and End User Messaging
(formerly Amazon Pinpoint)

- Amazon Polly

- Amazon Q Business

- Amazon Q Developer

- Amazon Quantum Ledger Database (QLDB)

- Amazon QuickSight

- Amazon Redshift

- Amazon Rekognition

- Amazon Relational Database Service (RDS)

- Amazon Route 53




- AWS Elastic Beanstalk

- AWS Elastic Disaster Recovery

- AWS Elemental MediaConnect

- AWS Elemental MediaConvert

- AWS Elemental MediaLive

- AWS Entity Resolution

- AWS Fault Injection Service

- AWS Firewall Manager

- AWS Global Accelerator

- AWS Glue

- AWS Glue DataBrew

- AWS Health Dashboard

- AWS HealthImaging

- AWS HealthLake

- AWS HealthOmics

- AWS IAM Identity Center

- AWS Identity and Access Management (IAM)

- AWS IoT Core

- AWS IoT Device Defender

- AWS IoT Device Management

- AWS IoT Events

- AWS IoT Greengrass

- AWS IoT SiteWise

- AWS IoT TwinMaker

- AWS Key Management Service (KMS)

- AWS Lake Formation

- AWS Lambda

- AWS License Manager

- AWS Mainframe Modernization

- AWS Managed Services

- AWS Network Firewall

- AWS OpsWorks [includes Chef Automate, Puppet
Enterprise]

- AWS OpsWorks Stacks

- AWS Organizations

- AWS Outposts

- AWS Payment Cryptography

- AWS Private Certificate Authority

- AWS Resilience Hub

- AWS Resource Access Manager (RAM)

- AWS Resource Explorer

- AWS Resource Groups

- AWS RoboMaker

- AWS Secrets Manager

- AWS Security Hub



Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


23


Section III – Description of the Amazon Web Services System




- Amazon S3 Glacier

- Amazon SageMaker AI (formerly Amazon
SageMaker) [excludes Studio Lab, Public

Workforce and Vendor Workforce for all

features]

- Amazon Security Lake

- Amazon Simple Email Service (SES)

- Amazon Simple Notification Service (SNS)

- Amazon Simple Queue Service (SQS)

- Amazon Simple Storage Service (S3)

- Amazon Simple Workflow Service (SWF)

- Amazon SimpleDB

- Amazon Textract

- Amazon Timestream

- Amazon Transcribe

- Amazon Translate

- Amazon Verified Permissions

- Amazon Virtual Private Cloud (VPC)

- Amazon WorkDocs

- Amazon WorkMail




- AWS Serverless Application Repository

- AWS Service Catalog

- AWS Shield

- AWS Signer

- AWS Snowball

- AWS Snowball Edge

- AWS Step Functions

- AWS Storage Gateway

- AWS Systems Manager

- AWS Transfer Family

- AWS User Notifications

- AWS Verified Access

- AWS WAF

- AWS Wickr

- AWS X-Ray

- EC2 Image Builder

- Elastic Load Balancing (ELB)

- FreeRTOS

- VM Import/Export



More information about the in-scope services, can be found at the following web address:
[https://aws.amazon.com/compliance/services-in-scope/](https://aws.amazon.com/compliance/services-in-scope/)


The scope of locations covered in this report includes the supporting data centers located in the following
regions:


  - **Australia:** Asia Pacific (Sydney) (ap-southeast-2), Asia Pacific (Melbourne) (ap-southeast-4)

  - **Bahrain:** Middle East (Bahrain) (me-south-1)

  - **Brazil:** South America (São Paulo) (sa-east-1)

  - **Canada:** Canada (Central) (ca-central-1), Canada West (Calgary) (ca-west-1)

  - **England:** Europe (London) (eu-west-2)

  - **France:** Europe (Paris) (eu-west-3)

  - **Germany:** Europe (Frankfurt) (eu-central-1)

  - **Hong Kong:** Asia Pacific (ap-east-1)

  - **India:** Asia Pacific (Mumbai) (ap-south-1), Asia Pacific (Hyderabad) (ap-south-2)

  - **Indonesia:** Asia Pacific (Jakarta) (ap-southeast-3)

  - **Ireland:** Europe (Ireland) (eu-west-1)

  - **Israel:** Israel (Tel Aviv) (il-central-1)

  - **Italy:** Europe (Milan) (eu-south-1)

  - **Japan:** Asia Pacific (Tokyo) (ap-northeast-1), Asia Pacific (Osaka) (ap-northeast-3)

  - **Malaysia:** Asia Pacific (Malaysia) (ap-southeast-5)*

  - **Mexico:** Mexico (Central) (mx-central-1)*

  - **Singapore:** Asia Pacific (Singapore) (ap-southeast-1)

  - **South Africa:** Africa (Cape Town) (af-south-1)


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


24


Section III – Description of the Amazon Web Services System


  - **South Korea:** Asia Pacific (Seoul) (ap-northeast-2)

  - **Spain:** Europe (Spain) (eu-south-2)

  - **Sweden:** Europe (Stockholm) (eu-north-1)

  - **Switzerland:** Europe (Zurich) (eu-central-2)

  - **Thailand:** Asia Pacific (Thailand) (ap-southeast-7)*

  - **United Arab Emirates:** Middle East (UAE) (me-central-1)

  - **United States:** US East (Northern Virginia) (us-east-1), US East (Ohio) (us-east-2), US West
(Oregon) (us-west-2), US West (Northern California) (us-west-1), AWS GovCloud (US-East) (usgov-east-1), AWS GovCloud (US-West) (us-gov-west-1)


- Effective date for this region is February 15, 2025.

and the following AWS Edge locations in:




- Caba, Argentina

- General Pacheco,

Argentina

- Brisbane, Australia

- Canberra, Australia

- Melbourne, Australia

- Perth, Australia

- Vienna, Austria

- Brussels, Belgium

- Fortaleza, Brazil

- Rio de Janeiro, Brazil

- São Paulo, Brazil

- Sofia, Bulgaria

- Scarborough, Canada

- Toronto, Canada

- Vancouver, Canada

- Huechuraba, Chile

- Santiago, Chile

- Bogotá, Colombia

- Zagreb, Croatia

- Prague, Czech Republic

- Ballerup, Denmark

- Cairo, Egypt

- Tallinn, Estonia

- Helsinki, Finland

- Espoo, Finland

- Marseille, France

- Berlin, Germany

- Dusseldorf, Germany




- Milan, Italy

- Rome, Italy

- Inzai, Japan

- Nairobi, Kenya

- Kuala Lumpur, Malaysia

- Santiago de Querétaro,

Mexico

- Amsterdam, Netherlands

- Diemen, Netherlands

- Schiphol-Rijk, Netherlands

- Auckland, New Zealand

- Rosedale, New Zealand

- Lagos, Nigeria

- Oslo, Norway

- Barka, Oman

- Santiago de Surco, Peru

- Manila, Philippines

- Quezon, Philippines

- Warsaw, Poland

- Lisbon, Portugal

- Doha, Qatar

- Bucharest, Romania

- Jeddah, Saudi Arabia

- Singapore, Singapore

- Cape Town, South Africa

- Johannesburg, South Africa

- Anyang-si, South Korea

- Seoul, South Korea

- Barcelona, Spain




- Atlanta, United States

- Aurora, United States

- Bluffdale, United States

- Boston, United States

- Chandler, United States

- Chicago, United States

- Columbus, United States

- Dallas, United States

- Denver, United States

- El Segundo, United States

- Elk Grove Village, United

States

- Franklin, United States

- Greenwood Village, United

States

- Hillsboro, United States

- Houston, United States

- Irvine, United States

- Kansas City, United States

- Las Vegas, United States

- Los Angeles, United States

- Lynnwood, United States

- Miami, United States

- Milpitas, United States

- Minneapolis, United States

- New York City, United States

- Newark, United States

- North Las Vegas, United

States



Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


25


Section III – Description of the Amazon Web Services System




- Frankfurt, Germany

- Hamburg, Germany

- Munich, Germany

- Koropi, Greece

- Kropia, Greece

- Budapest, Hungary

- Bangalore, India

- Chennai, India

- Kolkata, India

- Mumbai, India

- New Delhi, India

- Noida, India

- Pune, India

- Jakarta, Indonesia

- Clonshaugh, Ireland

- Dublin, Ireland

- Haifa, Israel




- Madrid, Spain

- Stockholm, Sweden

- Zurich, Switzerland

- New Taipei City, Taiwan

- Taipei, Taiwan

- Bangkok, Thailand

- Bang Chalong, Thailand

- Istanbul, Turkey

- Dubai, United Arab

Emirates

- Fujairah, United Arab

Emirates

- London, United Kingdom

- Manchester, United

Kingdom

- Swinton, United Kingdom

- Ashburn, United States



and the following Wavelength locations in:




 - Philadelphia, United States

 - Phoenix, United States

 - Piscataway, United States

 - Pittsburgh, United States

 - Portland, United States

 - Reston, United States

 - Richardson, United States

 - Seattle, United States

 - Secaucus, United States

 - Tampa, United States

 - Tempe, United States

 - West Valley City, United

States

 - Hanoi, Vietnam

 - Ho Chi Minh, Vietnam


- Minneapolis, United States

- New Berlin, United States

- Pembroke Pines, United States

- Plant City, United States

- Redmond, United States

- Rocklin, United States

- Southfield, United States

- Tempe, United States

- Wall Township, United States

- Westborough, United States


 - Kansas City, United States

 - Kapolei, United States

 - Las Vegas, United States

 - Lee's Summit, United States*

 - Lithia Springs, United States

 - Mesa, United States

 - Miami, United States

 - Minneapolis, United States




  - Toronto, Canada

  - Berlin, Germany

  - Dortmund, Germany

  - Munich, Germany

  - Osaka, Japan

  - Tama, Japan

  - Daejeon, South Korea

  - Seoul, South Korea

  - London, United Kingdom

  - Salford, United Kingdom


as well as Local Zone locations in:


   - Caba, Argentina

   - Perth, Australia

   - Santiago, Chile

   - Ballerup, Denmark

   - Espoo, Finland

   - Hamburg, Germany

   - Kolkata, India

   - New Delhi, India

   - Noida, India*




- Alpharetta, United States

- Annapolis Junction, United

States

- Aurora, United States

- Azusa, United States

- Charlotte, United States

- Euless, United States

- Houston, United States

- Knoxville, United States

- Las Vegas, United States


 - Warsaw, Poland

 - Singapore, Singapore*

 - New Taipei City, Taiwan

 - Bang Chalong, Thailand

 - Atlanta, United States

 - Boston, United States

 - Chicago, United States

 - Doral, United States

 - El Segundo, United States



Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


26


Section III – Description of the Amazon Web Services System




- North Las Vegas, United

States

- Philadelphia, United States

- Phoenix, United States

- Piscataway, United States

- Richardson, United States

- Seattle, United States




- Santiago de Queretaro,

Mexico

- Nouaceur, Morocco

- Rosedale, New Zealand

- Lagos, Nigeria

- Barka, Oman

- Santiago de Surco, Peru

- Manila, Philippines




- Garland, United States

- Greenwood Village,

United States

- Hillsboro, United States

- Houston, United States

- Irvine, United States

- Itasca, United States




- This location is a Dedicated Local Zone and may not be available to all customers.

**Shared Responsibility Environment**

Moving the customer’s IT infrastructure to AWS builds a shared responsibility model between customers
and AWS. AWS operates, manages, and controls the components from the host operating system and
virtualization layer down to the physical security of the facilities in which the services operate. In turn,
customers assume responsibility and management of the design, implementation and operation of their
AWS environment, which may include guest operating systems (including updates and security patches),
other associated application software, as well as the configuration of the AWS-provided security group
firewall. Customers should carefully consider the services they choose as customer responsibilities vary
depending on the services they use, the integration of those services into their IT environments, and
applicable laws and regulations. It is possible to enhance security and/or meet more stringent compliance
requirements by leveraging technology such as host-based firewalls, host-based intrusion
detection/prevention, and encryption. AWS provides tools and information to assist customers in their
efforts to account for and to validate that controls are operating effectively in their extended IT
environment. More information can be found on the AWS Compliance center at
[https://aws.amazon.com/compliance.](https://aws.amazon.com/compliance)

AWS offers a variety of different infrastructure and platform services. More information can be found on

                                                            -                                                            the AWS Shared Responsibility Model at [https://aws.amazon.com/compliance/shared](https://aws.amazon.com/compliance/shared-responsibility-model/) responsibility
[model/.](https://aws.amazon.com/compliance/shared-responsibility-model/) For the purpose of understanding security and shared responsibility for AWS’ services, AWS has
categorized its services into three main categories: infrastructure, container, and abstracted. Each
category comes with a slightly different security ownership model based on how customers interact and
access the functionality. Customer responsibility is determined by the AWS Cloud services that a customer
selects. This determines the amount of configuration work the customer must perform as part of their
security responsibilities.

Infrastructure Services: Services such as Amazon Elastic Compute Cloud (Amazon EC2) and Amazon
Virtual Private Cloud (Amazon VPC) are categorized as Infrastructure Services and, as such, require the
customer to perform the necessary security configuration and management tasks. If a customer deploys
an Amazon EC2 instance, that customer is responsible for management of the guest operating system
(including updates and security patches), any application software or utilities installed by the customer
on the instances, and the configuration of the AWS-provided firewall (called a security group) on each

instance.


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


27


Section III – Description of the Amazon Web Services System


Container Services: Services in this category typically run separately on Amazon EC2 or other
infrastructure instances, but sometimes customers are not required to manage the operating system or
the platform layer. AWS provides a managed service for these application “containers”. Customers are
responsible for setting up and managing network controls, such as firewall rules, and for managing
platform-level identity and access management separately from IAM. Examples of container services
include Amazon Relational Database Services (Amazon RDS), Amazon Elastic Map Reduce (Amazon EMR)

and AWS Elastic Beanstalk.

Abstracted Services: This category includes high-level storage, database, and messaging services, such as
Amazon Simple Storage Service (Amazon S3), Amazon Glacier, Amazon DynamoDB, Amazon Simple
Queuing Service (Amazon SQS), and Amazon Simple Email Service (Amazon SES). These services abstract
the platform or management layer on which the customers can build and operate cloud applications. The
customers access the endpoints of these abstracted services using AWS Application Programming
Interfaces (APIs), and AWS manages the underlying service components or the operating system on which
they reside.

As every customer deploys their environment differently in AWS, customers can take advantage of shifting
the management of certain IT controls to AWS, which results in a (new) distributed control environment.
Customers can then use the AWS control and compliance documentation available to them to perform
their control evaluation and verification procedures as required. Certain functions of services have been
identified as controls in the system description and are denoted as “service-specific” as they are unique
to the respective service.

More information and examples on the AWS Security Best Practices can be found at

                               -                                [https://aws.amazon.com/architecture/security](https://aws.amazon.com/architecture/security-identity-compliance/) identity compliance/.

Furthermore, AWS publishes security blogs that cover best practices around using AWS services at
[https://aws.amazon.com/blogs/security/tag/best-practices/.](https://aws.amazon.com/blogs/security/tag/best-practices/)

**Relevant Aspects of Internal Controls**

As defined by the American Institute of Certified Public Accountants (AICPA), internal control is a process
affected by an entity’s board of directors, management, and other personnel and consists of five
interrelated components:


  - Control Environment – Sets the tone of an organization, influencing the control consciousness of
its people. It is the foundation for all other components of internal control, providing discipline

and structure.


  - Risk Assessment – The entity’s identification and analysis of relevant risks to the achievement of
its objectives, forming a basis for determining how the risks should be managed.


  - Information and Communication – Surrounding these activities are information and
communication systems. These enable the entity’s people to capture and exchange information
needed to conduct and control its operations.


  - Monitoring – The entire process must be monitored, and modifications made as necessary. In this
way, the system can react dynamically, changing as conditions warrant.


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


28


Section III – Description of the Amazon Web Services System


  - Control Activities – Control policies and procedures must be established and executed to help
ensure that the actions identified by management as necessary to address risks to the
achievement of the entity’s objectives are effectively carried out.

This section briefly describes the essential characteristics and other interrelated components of internal
controls in achieving the service commitments and system requirements for the applicable trust services
criteria of security, availability, confidentiality, and privacy as they pertain to AWS that may be relevant

to customers in five broad areas:


  - Policies (Control Environment and Risk Management) – The entity has defined and documented
its policies relevant to the applicable trust services criteria.


  - Communications (Information and Communication) – The entity has communicated its defined
policies to responsible parties and authorized users of the system.


  - Service Commitments and System Requirements (Control Activities) – The entity has
communicated its service commitments and system requirements to customers in accordance
with customer agreements.


  - Procedures (Control Activities) – The entity has placed in operation procedures to achieve service
commitments and systems requirements in accordance with its defined policies.


  - Monitoring – The entity monitors the system and takes action to maintain compliance with its
defined policies.

**A.** **Policies**

**A.1 Control Environment**

AWS is a unit within Amazon.com (“Amazon” or “the Company”) that is aligned organizationally around
each of the web services, such as Amazon EC2, Amazon S3, Amazon VPC, Amazon EBS and Amazon RDS.
AWS leverages some aspects of Amazon’s overall control environment in the delivery of these web
services. The collective control environment encompasses management and employee efforts to establish
and maintain an environment that supports the effectiveness of specific controls. AWS maintains internal
informational websites describing the AWS environment, its boundaries, user responsibilities and services
**(Control AWSCA-9.1)** .

The control environment at Amazon begins at the highest level of the Company. Executive and senior
leadership play important roles in establishing the Company’s core values and tone at the top. The
Company’s Code of Business Conduct and Ethics, which sets guiding principles, is made available to every
employee.


Amazon is committed to having highly qualified members as a part of its Board of Directors (Board)
**(Control AWSCA-1.7)** . Annually, the Amazon Corporate Governance Committee provides each Board
member a questionnaire that establishes whether they are independent and qualified to serve on each
Board or Committee under the applicable rules. The Corporate Governance Committee periodically
reviews and assesses the composition of the Board and evaluates the overall Board performance during
the annual assessment of individual Board members. The Leadership Development and Compensation
Committee, with the full Board present, annually evaluates the succession plan for each member of the


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


29


Section III – Description of the Amazon Web Services System


Senior Management team **(Control AWSCA-1.8)** . This includes the annual Company and CEO performance
and succession plan.

AWS is committed to protecting its customers’ data and maintaining compliance with applicable
regulatory requirements. This is demonstrated by the consolidated annual operational plan that includes
regulatory and compliance requirements and objectives to enable the identification and assessment of
risks relating to those objectives **(Control AWSCA-1.9)** . AWS’ policies and procedures outline the required
guidance for operation and information security that supports AWS environments, acceptable use of
mobile devices, and access to data content and network devices **(Control AWSCA-3.16)** . Periodically, AWS
employees are required to review and comply with the most current versions of applicable policies and
procedures.

Amazon has setup an ethics hotline for the employees or third-party contractors to report misconduct or
violation of AWS policies, practices, rules, requirements or procedures **(Control AWSCA-9.6).** Material
violations of the Company Code of Business Conduct and Ethics or any other similar policies are
appropriately handled accordingly which may include disciplinary action or termination of employment.
Violations by vendors or third-party contractors are reported by Amazon to their employers for
disciplinary action, removal of assignment with Amazon, or termination **(Control AWSCA-9.7).**

AWS has implemented a formal audit program that monitors and audits controls that are designed to
protect against organizational risks and safeguard customer content. This includes external independent
assessments against regulatory, internal and external control frameworks **(Control AWSCA-9.8)** . The
internal and external audits are planned, performed and reported to the Audit Committee. The AWS
compliance team conducts audits according to a documented schedule. They review the audit plan and
communicate the audit requirements to the Audit Committee. These requirements are based on standard
criteria that verify AWS' compliance with relevant regulatory obligations and reported risk areas.

AWS Artifact is the primary resource for customers to obtain compliance-related information from AWS.
It provides access to AWS’ security and compliance reports and select online agreements. Reports
available in AWS Artifact include: AWS System and Organization Controls (SOC) reports, Payment Card
Industry (PCI) Attestation of Compliance, and certifications from accreditation bodies across geographies
and industry verticals that validate the implementation and operating effectiveness of AWS security
controls. Amongst other things, compliance reports are made available to customers to enable them to
evaluate AWS’ conformance with security controls and associated compliance obligations.

The AWS organizational structure provides a framework for planning, executing and controlling business
operations **(Control AWSCA-1.1).** AWS Leadership assigns roles and responsibilities based on the AWS
organizational structure to provide for adequate staffing, efficiency of operations and the segregation of
duties. Management has also established authority and appropriate lines of reporting for key personnel.
The Company follows a structured on-boarding process to assist new employees as they become familiar
with Amazon tools, processes, systems, policies and procedures.

AWS performs a formal evaluation of the appropriate resourcing and staffing to align employee
qualifications with the entity’s business objectives to support the achievement of the entity’s business
objectives. Appropriate feedback is given to the employee on strengths and growth areas during the
annual performance review process. Employee strength and growth evaluations are shared by the
employee’s manager with the employee **(Control AWSCA-9.3).**


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


30


Section III – Description of the Amazon Web Services System


The GovCloud (US East) and GovCloud (US West) environments are AWS regions located in the United
States (US) that are designed to maintain physical and logical access controls that limit access by AWS
personnel to the AWS Network for the GovCloud (US) regions to US citizens. The AWS control environment
described in this document is also applicable to the GovCloud (US) regions.

AWS has established an information security framework. As part of this framework, AWS periodically
reviews and updates the security policies, provides security training to its employees, which includes
instruction on data classification. Additionally, the AWS Application Security (AppSec) team performs
security reviews of AWS applications. These reviews assess the availability, confidentiality, and integrity
of data, as well as conformance to the security policies. Where necessary, AWS Security leverages the
security framework and security policies established and maintained by Amazon Corporate Information
Security.

AWS has a process in place to review environmental and geo-political risks before launching a new region
**(Control AWSCA-1.10)** . Risk assessments encompass reviews of natural catastrophe (e.g., extreme
weather events), technological (e.g., fire, nuclear radiation, industrial pollution) and man-made (e.g.,
vehicle impact, intentional acts, geo-political) hazards, including exposures presented by nearby entities;
as applicable. In addition to site-specific considerations, AWS evaluates scenarios potentially affecting
separate Availability Zones (AZs) within a region.

**A.2 Risk Management**

AWS maintains a formal risk management program to identify, analyze, treat, continuously monitor and
report on risks that affect AWS’ business objectives, regulatory requirements, and customers. The AWS
Enterprise Risk Management (ERM) team identifies enterprise risks, documents them in a risk register,
and reports results to leadership on a quarterly basis. The risk management program consists of the
following phases:


1) Identifying Risks


ERM has developed a tailored approach to identifying risks across the business. The approach is:


      - Bottom-up to identify existing risks and emerging risks, with a focus on internal
mechanisms and data to identify risks;


      - Top down to gather information from key leaders and external sources; and


      - Proactive outreach from risk owners to gather information from other internal teams,
external events, and industry trends.


2) Analyzing Risks


ERM reviews the identified risks with senior leaders, risk owners and risk subject matter experts
(SMEs) to calibrate, assess, and prioritize. This is accomplished by evaluating:


      - Probability (likelihood of occurrence in a defined time period);


      - Impact (degree of severity in terms of the domains in which it may impact); and


      - Current Risk Controls (existence of mechanisms or controls that address inherent risk).


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


31


Section III – Description of the Amazon Web Services System


3) Treating Risks


ERM’s approach is risk treatment, versus risk mitigation. ERM collaborates with business SMEs to
develop treatment plans after considering available options. It is the risk owner that determines
whether to accept or further mitigate the risk based on the residual risk rating once options are
considered. Options might include:


      - Eliminating or avoiding the risk (e.g., stopping the activity);


      - Reducing the risk (e.g., implementing controls);


      - Transferring the risk (e.g., to a third-party); or


      - Accepting the risk (when capacity and appetite exist).


4) Monitoring and Reporting Risks


ERM actively monitors material risks and their treatment plans and provides quarterly reports to
senior leadership. Reports may include important information about key risks and treatments, as
well as emerging trends and general program updates **(Control AWSCA-1.5)** .


In addition to the ERM Risk Assessment, Internal Audit performs a separate Risk Assessment to identify
and prioritize significant AWS risks and uses this information to define the audit plan. The Risk Assessment
incorporates input from multiple sources such as changes to the business, internal audits, operational
events, and emerging risks. The audit plan and changes to the plan during the year are presented to the
Audit Committee. Internal Audit also communicates significant audit findings and associated action plans

to the Audit Committee.

Additionally, at least on a monthly basis, AWS management reviews the AWS operational metrics and
Correction of Errors (COEs) to improve the overall availability of AWS services and to identify areas of
improvements while mitigating risks to AWS environments. The “COE” documents are used to perform
deep root cause analysis of certain incidents across AWS, document actions taken, and assign follow-up

action items and owners to track to resolution.


**B.** **Communications**

AWS has implemented various methods of internal communication at a global level to help employees
understand their individual roles and responsibilities and to communicate significant events in a timely
manner **.** These methods include orientation and training programs for newly hired employees; annual
training programs are tailored based on employee roles and responsibilities and may include Amazon
Security Awareness (ASA) **(Control AWSCA-1.4)**, Software Developer Engineer (SDE) Bootcamp,
International Traffic in Arms Regulations (ITAR) Secure Coding Training, Threat Modeling the Right Way
for Amazon Builders, Fraud/Bribery/Foreign corrupt practices training, Privacy Engineering Foundations
for AWS Service Teams training, Managing Third Parties Using the Third-Party Risk Management Lifecycle,
Export Compliance trainings; regular management meetings for updates on business performance and
other matters; and electronic means such as video conferencing, electronic mail messages, and the
posting of information via the Amazon intranet on topics such as reporting of information security
incidents and guidelines describing change management. The AWS Internal Privacy Policy informs AWS
employees and applicable vendors/contractors about AWS’ requirements regarding the privacy of
customers’ personal information in accordance with applicable legislation and other AWS obligations.


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


32


Section III – Description of the Amazon Web Services System


**C.** **Service Commitments and System Requirements**

**C.1 Service Commitments**

AWS communicates service commitments to user entities (AWS customers) in the form of Service Level
[Agreements (SLAs), customer agreements (https://aws.amazon.com/agreement/), contracts or through](https://aws.amazon.com/agreement/)
the description of the service offerings provided online through the AWS website. More information
regarding Service Level Agreements can be found at [https://aws.amazon.com/legal/service-level-](https://aws.amazon.com/legal/service-level-agreements/)
[agreements/.](https://aws.amazon.com/legal/service-level-agreements/)

AWS uses various methods of external communication to support its customers and the community.
Mechanisms are in place to allow the AWS Support Escalation and Event Management (E2M) team to be
notified and to notify customers of potential operational issues that could impact the customer
experience. AWS Health Dashboard is available to alert customers of “General Service Events” which show
the health of all AWS services and “Your Account Events” which show events specific to the account.
Current status information can be checked by the customer on this site or by leveraging Amazon
EventBridge Integrations or RSS feeds, which allow customers to be notified of interruptions to each
[individual service. Details related to security and compliance with AWS can also be obtained on the AWS](https://aws.amazon.com/security/)
[Security Center](https://aws.amazon.com/security/) [and AWS Compliance websites.](https://aws.amazon.com/compliance/)

[Customers have the ability to contact AWS through the ‘Contact us’ page for issues related to AWS](https://aws.amazon.com/contact-us/)
services. AWS provides publicly available mechanisms for external parties to contact AWS to report
security events and publishes information including a system description and security and compliance
information addressing AWS commitments and responsibilities **(Control AWSCA-9.5)** . Customers can also
subscribe to Premium Support offerings that include direct communication with the customer support
team and proactive alerts for any customer impacting issues. AWS also deploys monitoring and alarming
mechanisms which are configured by AWS Service Owners to identify and notify operational and
management personnel of incidents when early warning thresholds are crossed on key operational
metrics **(Control AWSCA-8.1)** . Additionally, incidents are logged within a ticketing system, assigned a
severity rating and tracked to resolution **(Control AWSCA-8.2)** .

**C.2 System Requirements**

The selection and use of services by AWS’ customers must be set up and operated under a shared
responsibility model so that the functionality of the services and the associated security is appropriately
managed. AWS is responsible for protecting the infrastructure that runs the service(s) offered in the AWS
Cloud. The customer’s responsibility is determined by the AWS Cloud service(s) that a customer selects
and the interdependencies of those services within the AWS Cloud and their own networked
environment. Customers should assess the objectives of their AWS cloud services network and identify
the risks and corresponding controls that need to be implemented to address those risks when using AWS
services, software, and operational controls. Customers should carefully consider the specific AWS
services they choose, as their security responsibilities can vary depending on the service(s) they select, as
well as the type of configurations and operational controls required for those services.

When designing and developing its services, AWS management has created internal policies that are
relevant to the services and systems available to customers. The development of these policies and
procedures helps to support management decision-making and provides the operational teams with clear


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


33


Section III – Description of the Amazon Web Services System


business requirements and guidance for managing each AWS service and system. As each AWS service is
unique, the system requirements to use different services vary depending on the service and each

customer’s environment.

As explained in the Availability section of the report, AWS has processes and infrastructure in place to
make AWS services available to customers to meet their needs. AWS communicates its system
requirements to customers and how to get started with using the AWS services in the form of user guides,
developer guides, API references, service specific tutorials, or SDK toolkits. More information regarding
AWS Documentation can be found at [https://docs.aws.amazon.com/. These resources help the customers](https://docs.aws.amazon.com/)
with architecting the AWS services to satisfy their business needs.

AWS has identified the following objectives to support the security, change, and operational processes
underlying their service commitments and business requirements. These objectives help ensure the
system operates and mitigates risks that threaten the achievement of the service commitments and
system requirements. The objectives below provide reasonable assurance that:


  - Data integrity is maintained through all phases, including transmission, storage and processing.


  - Policies and mechanisms are in place to appropriately restrict unauthorized access to systems and
data, and customer data is appropriately segregated from other customers.


  - _S_ ystem incidents are recorded and analyzed timely and tracked to resolution.


  - Changes (including emergency/non-routine and configuration) to existing IT resources are
documented, authorized, tested, approved and implemented by authorized personnel.


  - Critical system components are replicated across multiple AZs and authoritative backups are
maintained and monitored to ensure successful replication to meet the service commitments.


  - Controls are implemented to safeguard data from within and outside of the boundaries of

environments which store a customer’s content to meet the service commitments.


  - Procedures have been established so that the collection, use, retention, disclosure, and disposal
of customer content within AWS services is in accordance with the service commitments.

**D.** **Procedures**

**D.1 Security Organization**

AWS has an established information security organization that is managed by the AWS Security team and
is led by the AWS Chief Information Security Officer (CISO). AWS Security team responsibilities are defined
and allocated across the organization. The AWS Security team works with AWS service teams, other
internal security teams, and external parties striving to ensure that security risks are mitigated. AWS
Security establishes and maintains policies and procedures to delineate standards for logical access on
the AWS system and infrastructure hosts. The policies also identify functional responsibilities for the
administration of logical access, privacy, and security. Where applicable, AWS Security leverages the
information system framework and policies established and maintained by Amazon Corporate
Information Security. AWS and Amazon Corporate Information Security policies are reviewed and
approved on an annual basis by AWS Security Leadership and are used to support AWS in meeting the
service commitments made to the customers **(Control AWSCA-1.1**, **AWSCA -1.2**, and **AWSCA-1.3)** .


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


34


|Section III – De  As part of this annual assessment, the following policies the last year:|escription of the Amazon Web Services System s were inspected to verify approval occurred within kxwds|
|---|---|
|AWS Access Control Policy<br>|AWS Media Protection Policy<br>|
|AWS Configuration Management Policy<br>|AWS Password Policy<br>|
|AWS Contingency Planning Policy<br>|AWS Personnel Security Policy<br>|
|AWS Critical Permission Group Standard<br>|AWS Physical and Environmental Protection<br>Policy<br>**Ri**|
|Data Center Security Standard: Media Handling,<br>Storage and Destruction<br>|Secure Software Development Policy<br>**L**|
|AWS Data Classification and Handling Policy<br>|AWS Security Assessment and Certification<br>Standard<br>**Ik**|
|AWS Facility Badge Management and Use Standard<br>|AWS Security Awareness Training Policy<br>|
|AWS Identification and Authentication Policy<br>|AWS System and Communications Protection<br>Policy<br>**g**|
|AWS Incident Response Policy<br>|AWS System and Information Integrity Policy<br>|
|AWS Information Security Risk Management Policy<br>|AWS System Maintenance Policy<br>|
|AWS Internal Privacy Policy<br>|AWS Third Party Information Sharing Policy<br>|
|AWS Risk Management Policy<br>|<br>|


AWS has a security awareness and training policy that is disseminated via an internal Amazon
communication portal to all employees. This policy addresses purpose, scope, roles and responsibilities.
AWS maintains and provides security awareness training to all information system users on an annual
basis. The training also includes components such as privacy, data protection training, and data handling
leading practices **(Control AWSCA-1.4)** .

As a part of AWS’ responsibilities within the shared responsibility model, AWS implements the three lines
of defense model established by the Institute of Internal Auditors (IIA), discussed in the IIA’s Three Lines
[Model“https://www.theiia.org/en/content/position-papers/2020/the-iias-three-lines-model-an-update-](https://www.theiia.org/en/content/position-papers/2020/the-iias-three-lines-model-an-update-of-the-three-lines-of-defense/)
[of-the-three-lines-of-defense/” whitepaper. In this model, operational management is the first line of](https://www.theiia.org/en/content/position-papers/2020/the-iias-three-lines-model-an-update-of-the-three-lines-of-defense/)
defense, the various risk control and compliance oversight functions established by management are the
second line of defense **(Control AWSCA-1.5)**, and independent assurance is the third. As its third line of
defense, Amazon has an Internal Audit function to periodically evaluate risks and assess conformance to
AWS security processes with due professional care **(Control AWSCA-9.8)** .

Further, AWS Security Assurance works with third-party assessors to obtain an independent assessment
of risk management content/processes by performing periodic security assessments and compliance
audits or examinations (e.g., SOC, FedRAMP, ISO, PCI) to evaluate the security, integrity, confidentiality,
and availability of information and resources. AWS management also collaborates with Internal Audit to
determine the health of the AWS control environment and leverages this information to fairly present the
assertions made within the reports.


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


35


Section III – Description of the Amazon Web Services System


**D.2 Logical Security**

AWS has established policies and procedures to delineate standards for logical access to AWS systems
and infrastructure hosts. The policies also identify functional responsibilities for the administration of
logical access and security. Where permitted by law, AWS requires that employees undergo a background
screening, at the time of hiring commensurate with their position and level of access and in accordance
with the AWS Personnel Security Policy **(Control AWSCA-9.2)** .

AWS employees who have access to systems that could impact the confidentiality, integrity, or availability,
or privacy of customer content are required to complete a post-hire background screening within a year
from their last background check. Post-hire screening includes criminal screening requirements consistent
with the pre-hire background screening. Access to the systems that could impact the confidentiality,
integrity, or availability, or privacy of customer content is managed by membership in permission groups.
Employees who support internal services or have access to network resources are not required to
complete the post-hire background screening. Post-hire background screening is conducted where it is
legally permissible by local law and in accordance with the AWS Personnel Security Policy **(Control**
**AWSCA-9.9)** .

Account Provisioning
The responsibility for provisioning user access, which includes employee and contractor access, is shared
across Human Resources (HR), Corporate Operations, and Service Owners.

A standard employee or contractor account with minimum privileges is provisioned in a disabled state
when a hiring manager submits their new employee or contractor onboarding request in Amazon’s HR
system. The account is automatically enabled after the employee’s record is activated in Amazon’s HR
system. First time passwords are set to a unique value and are required to be changed on first use **(Control**
**AWSCA-2.1)** .

Access Management
AWS employs the concept of least privilege, allowing only the necessary access for users to accomplish
their job function. User accounts are created to have minimal access. Access above these least privileges
require appropriate and separate authorization.

Access to resources including Services, Hosts, Network devices, and Windows and UNIX groups is
approved in Amazon’s proprietary Permission management system by the appropriate owner or manager.
Requests for changes in access are captured in the Amazon permissions management tool audit log. When
changes in an employee’s job function occur, continued access must be approved to the resource, or it
will be automatically revoked **(Control AWSCA-2.2).**

Periodic Access Review

Access control lists or permission groups granting access to critical infrastructure are reviewed for
appropriateness on a periodic basis. On a quarterly basis, reviews are performed by appropriate AWS
management personnel of user access to AWS systems supporting the infrastructure and network; explicit
re-approval is required, or access to the resource is revoked. On a semi-annual basis, AWS reviews the
access to AWS accounts. When an internal user no longer has a required business need to access the


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


36


Section III – Description of the Amazon Web Services System


operational management system, the user’s privileges and access to the relevant systems are revoked
( **Control AWSCA-2.3** ).

Access Removal

Access is revoked when an employee’s record is terminated in Amazon’s HR system. Windows and UNIX
accounts are disabled, and Amazon’s permission management system removes the user from all systems
**(Control AWSCA-2.4).**

Password Policy
Access and administration of logical security for Amazon relies on user IDs, passwords and Kerberos to
authenticate users to services, resources and devices as well as to authorize the appropriate level of
access for the user. AWS Security has established a password policy with required configurations and
expiration intervals. AWS has a credential monitoring and response process to monitor compromised
credentials for Amazon employees. Impacted user credentials are identified, tracked and rotated in a
timely manner **(Control AWSCA-2.5).**

Remote Access

AWS requires two-factor authentication over an approved cryptographic channel for authentication to
the internal AWS network from remote locations **(Control AWSCA-2.6).**

AWS enables customers to select who has access to AWS services and resources (if resource-level
permissions are applicable to the service) that they own. AWS prevents customers from accessing AWS
resources that are not assigned to them via access permissions. User content is segregated by the service’s
software. Content is only returned to individuals authorized to access the specified AWS service or
resource (if resource-level permissions are applicable to the service) **(Control AWSCA-3.5)** .

AWS performs Application Security (AppSec) reviews when needed for externally launched products,
services, and significant feature additions prior to launch to identify security and privacy risks and
determine if they are mitigated. As a part of the AppSec review, the Application Security team collects
detailed information from service teams required for the review. The Application Security team tracks
reviews against an independently managed inventory of products and features to be released to ensure
that none are inadvertently launched before a completed review. As part of the security review, newly
created or modified IAM policies allowing end users to interact with launched updates are also reviewed.
The Application Security team then determines the granularity of review required based on the design,
threat model, and impact to AWS’ risk profile. During this process, they work with the service team to
identify, prioritize, and remediate security findings. The Application Security team provides their final
approval for launch only upon completion of the review **(Control AWSCA-3.6)** . Penetration testing is
performed as needed.

AWS Network Security

The AWS Network consists of the internal data center facilities, servers, networking equipment and host
software systems that are within AWS’ control and are used to provide AWS services.

The AWS network provides significant protection against traditional network security issues. The following
are a few examples:


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


37


Section III – Description of the Amazon Web Services System


  - **Distributed Denial of Service (DDoS) Attacks.** In order to defend against network attacks,
including DDoS attempts and suspicious traffic patterns, events from multiple sources are
collected, monitored and actioned through an integrated ticketing system, enabling rapid threat
detection and coordinated response measures. ( **Control AWSCA-8.2** ). Additionally, AWS’
networks are multi-homed across a number of providers to achieve Internet access diversity.


  - **Man in the Middle (MITM) Attacks.** All of the AWS APIs are available via TLS/SSL-protected
endpoints, which provide server authentication. Amazon EC2 Amazon Machine Images (AMIs)
automatically generate new SSH host certificates on first boot and log them to the instance’s

console. Customers can then use the secure APIs to call the console and access the host

certificates before logging into the instance for the first time. Customers can use TLS/SSL for all of
their interactions with AWS **(Control AWSCA-3.11).**


  - **IP Spoofing.** The AWS-controlled, host-based firewall infrastructure will not permit an instance to
send traffic with a source IP or MAC address other than its own **(Control AWSCA-3.10)** .


  - **Port Scanning.** Unauthorized port scans by Amazon EC2 customers are a violation of the AWS
Acceptable Use Policy. Violations of the AWS Acceptable Use Policy are taken seriously, and every
reported violation is investigated. Customers can report suspected abuse via the contacts
available on our website at: [https://aws.amazon.com/contact-us/report-abuse/. Port scans of](https://aws.amazon.com/contact-us/report-abuse/)
Amazon EC2 instances are generally ineffective because, by default, all inbound ports on Amazon
EC2 instances are closed and are only opened by the customer. Customers’ strict management of
security groups can further mitigate the threat of port scans. Customers may request permission
to conduct vulnerability scans as required to meet specific compliance requirements. These scans
must be limited to customers’ own instances and must not violate the AWS Acceptable Use Policy.
Advanced approval for these types of scans can be initiated by submitting a request via the AWS
website at: [https://aws.amazon.com/security/penetration-testing/.](https://aws.amazon.com/security/penetration-testing/)


  - **Packet sniffing by other tenants.** Virtual instances are designed to prevent other instances
running in promiscuous mode to receive or “sniff” traffic that is intended for a different virtual
instance. While customers can place instances into promiscuous mode, the hypervisor will not
deliver any traffic to them that is not addressed to them. Even two virtual instances that are
owned by the same customer located on the same physical host cannot listen to each other’s
traffic. While Amazon EC2 does provide protection against one customer inadvertently or
maliciously attempting to view another’s data, as standard practice customers can encrypt
sensitive traffic **(Control AWSCA-3.10).**


  - **Anti-virus software installed on workstations.** Anti-virus software is deployed and running on
Amazon corporate workstations. Client Engineering and Enterprise Engineering teams deploy
Anti-virus software at imaging to Amazon corporate workstations. AWS has implemented checks
to ensure that anti-virus software is installed, running, and capable of quarantining any noncompliant workstations. This quarantine functionality isolates those workstations from the
network until the necessary remediation actions have been taken **(Control AWSCA-3.18)** .

Firewall devices are configured to restrict access to production networks **(Control AWSCA-3.1).** The
configurations of these firewall policies are maintained via an automatic push from a parent server
**(Control AWSCA-3.2).** All changes to the firewall policies are reviewed and approved by appropriate AWS
management personnel **(Control AWSCA-3.3).**


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


38


Section III – Description of the Amazon Web Services System


AWS Security performs at least quarterly vulnerability scans on host operating systems, web applications,
and databases in the AWS environment using a variety of tools **(Control AWSCA-3.4).** AWS Security teams
also subscribe to newsfeeds for applicable vendor flaws and proactively monitor vendors’ websites and
other relevant outlets for new patches. AWS customers have the ability to report issues to AWS via the

                                                          AWS Vulnerability Reporting website at: [https://aws.amazon.com/security/vulnerability](https://aws.amazon.com/security/vulnerability-reporting/) reporting/.

AWS utilizes virtualization techniques to control and restrict traffic flow. This includes the use of virtual
networking devices, host-based firewalls, and Access Control Lists (ACLs) within EC2 and VPC. Additionally,
AWS offers a variety of operating systems for its EC2 instances. It is the responsibility of the customers to
appropriately configure server resources within the customer VPC.

External Access Control

External API access to services is configurable by customers via AWS Identity and Access Management
(IAM). IAM enables customers to securely control access to AWS services and resources for their users.
Using IAM, customers can create and manage AWS users, roles, groups, and create and attach policies to
those entities with granular permissions that allow or deny access to AWS resources. Security Groups act
as firewalls and may also be used to control access to some in-scope applications such as VPC, EFS,
ElastiCache, and DMS. These groups default to a “deny all” access mode and customers must specifically
authorize network connectivity. This can be achieved by authorizing a network IP range or authorizing an
existing Security Group **(Control AWSCA-3.5)** .

Interacting with the Services
AWS provides several methods of interacting with its services in the form of APIs, Software Development
Kits (SDKs), the AWS Management Console, and the AWS command line interface. All of the methods
ultimately rely on public APIs and follow standard AWS authentication and authorization practices.

Authenticated calls to AWS services are signed by an X.509 certificate and/or the customer's AWS Secret
Access Key. When using the AWS Command Line Interface (AWS CLI) or one of the AWS SDKs to make
requests to AWS, these tools automatically sign the requests with the access key specified by the customer
when the tools were configured. Manually created requests must be signed using Signature Version 4 or
Signature Version 2. All AWS services support Signature Version 4, except Amazon SimpleDB, which
requires Signature Version 2. For AWS services that support both versions, it is recommended to use
Signature Version 4.

Internal Logging
AWS maintains centralized repositories that provide core log archival functionality available for internal
use by AWS service teams. Leveraging S3 for high scalability, durability, and availability allows service
teams to collect, archive, and view service logs in a central log service.

Production hosts at AWS are deployed using master baseline images **(Control AWSCA-9.4)** . The baseline
images are equipped with a standard set of configurations and functions including logging and monitoring
for security purposes.

These logs are stored and accessible by AWS security teams for root cause analysis in the event of a
suspected security incident. Logs for a given host are also available to the team that owns that host in
case the team needs to search their logs for operational and security analysis.


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


39


Section III – Description of the Amazon Web Services System


Encryption
Amazon cryptographic policy defines the appropriate cryptography implementation through the Amazon
cryptographic standard. The cryptography standard is based on FIPS standards, NIST standards, and/or
the Commercial National Security Algorithm Suite (Suite B). Implementation guidance including
appropriate encryption key length and algorithm specific parameters are provided to service teams
through application security reviews. Additionally, AWS Security Engineers within the cryptography
review program review the appropriate use of cryptography within AWS. In addition, API calls can be
encrypted with TLS/SSL to maintain confidentiality. It is the customer’s responsibility to appropriately
configure and manage usage and implementation of available encryption options to meet compliance
requirements.

Each production firmware version release for the AWS Key Management Service HSM (Hardware Security
Module) either holds or is in the process of actively pursuing FIPS 140-3 level 3 certification from the
National Institute of Standards and Technology's (NIST) Cryptographic Module Validation Program (CMVP)
**(Control AWSCA-4.14)** . The certification process involves a coordinated effort between the AWS KMS
team and NVLAP-certified FIPS consulting laboratories which acts as authorized intermediary between
AWS KMS and NIST/CMVP. Before deployment, each new firmware version undergoes thorough
evaluation to ensure compliance with the FIPS 140-3 level 3 standards, as verified by the FIPS consulting
laboratory. Once compliance is confirmed, the laboratory submits a comprehensive report to NIST's
CMVP, initiating the formal FIPS 140-3 review and certification process for the firmware version.

All new objects uploaded to Amazon S3 are automatically encrypted with server-side encryption **(AWSCA-**
**3.19).** Amazon S3 automatically applies server-side encryption with Amazon S3 managed keys (SSE-S3) for
each new object uploaded to Amazon S3, unless a customer specifies a different encryption option.
Amazon S3 server- side encryption uses 256-bit Advanced Encryption Standard Galois/Counter Mode
(AES-GCM) to encrypt all uploaded objects. Customers can also alternatively choose to encrypt their
objects with server-side encryption with customer-provided encryption keys (SSE-C), server-side
encryption with AWS Key Management Service keys (SSE-KMS), server-side encryption with AWS Key
Management Service keys (SSE-KMS) with S3 Bucket Keys, or Dual-layer server-side encryption with AWS
Key Management Service keys (DSSE-KMS).

Deletion of Customer Content

AWS provides customers the ability to delete their content. Once successfully removed, the data is
rendered unreadable **(Control AWSCA-7.7).** For services that utilize ephemeral storage, such as EC2, the
ephemeral storage is deleted once the EC2 instance is deleted.

**D.3 AWS Service Descriptions**

The following section describes the AWS services within the scope of this report. These descriptions are
not exhaustive, and customers should review documentation provided online for additional information
on these services. Any AI functionality made available by services within the scope of this report are not

included in the controls described.

Amazon API Gateway
Amazon API Gateway is a service that makes it easy for developers to publish, maintain, monitor, and
secure APIs at any scale. With Amazon API Gateway, customers can create a custom API to code running


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


40


Section III – Description of the Amazon Web Services System


in AWS Lambda, and then call the Lambda code from customers' API. Amazon API Gateway can execute
AWS Lambda code in a customer’s account, start AWS Step Functions state machines, or make calls to
AWS Elastic Beanstalk, Amazon EC2, or web services outside of AWS with publicly accessible HTTP
endpoints. Using the Amazon API Gateway console, customers can define customers' REST API and its
associated resources and methods, manage customers' API lifecycle, generate customers' client SDKs, and

view API metrics.

Amazon AppFlow
Amazon AppFlow is an integration service that enables customers to securely transfer data between
Software-as-a-Service (SaaS) applications like Salesforce, SAP, Zendesk, Slack, and ServiceNow, and AWS
services like Amazon S3 and Amazon Redshift. With AppFlow, customers can run data flows at enterprise
scale at the frequency they choose - on a schedule, in response to a business event, or on demand.
Customers are able to configure data transformation capabilities like filtering and validation to generate
rich, ready-to-use data as part of the flow itself, without additional steps.

Amazon Application Recovery Controller (Effective August 15, 2024)
Amazon Application Recovery Controller gives insights into whether customers’ applications and
resources are ready for recovery. The Application Recovery Controller also helps manage and coordinate
recovery for customers’ applications across AWS Regions and Availability Zones (AZs). These capabilities
make it simpler and more reliable to recover applications by reducing the manual steps required by
traditional tools and processes.

Amazon AppStream 2.0
Amazon AppStream 2.0 is an application streaming service that provides customers instant access to their
desktop applications from anywhere. Amazon AppStream 2.0 simplifies application management,
improves security, and reduces costs by moving a customer’s applications from their users’ physical
devices to the AWS Cloud. The Amazon AppStream 2.0 streaming protocol provides customers a
responsive, fluid performance that is almost indistinguishable from a natively installed application. With
Amazon AppStream 2.0, customers can realize the agility to support a broad range of compute and storage
requirements for their applications.

Amazon Athena

Amazon Athena is an interactive query service that makes it easy to analyze data in Amazon S3 using
standard SQL. Athena is serverless, so there is no infrastructure for customers to manage. Athena is highly
available; and executes queries using compute resources across multiple facilities and multiple devices in
each facility. Amazon Athena uses Amazon S3 as its underlying data store, making customers’ data highly

available and durable.

Amazon Augmented AI (excludes Public Workforce and Vendor Workforce for all features)
Amazon Augmented AI (A2I) is a machine learning service which makes it easy to build the workflows
required for human review. Amazon A2I brings human review to all developers, removing the
undifferentiated heavy lifting associated with building human review systems or managing large numbers
of human reviewers whether it runs on AWS or not. The public and vendor workforce options of this
service are not in scope for purposes of this report.


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


41


Section III – Description of the Amazon Web Services System


Amazon Bedrock (excludes Amazon Bedrock Marketplace)
Amazon Bedrock is a fully managed service that makes foundation models (FMs) from Amazon and leading
Artificial Intelligence (AI) companies available through an API, so customers can choose from various FMs

to find the model that's best suited for their use case. With the Amazon Bedrock serverless experience,

customers can quickly get started, easily experiment with FMs, privately customize FMs with their own

data, and seamlessly integrate and deploy them into customer applications using AWS tools and

capabilities. Agents for Amazon Bedrock are fully managed and make it easier for developers to create

generative-AI applications that can deliver up-to-date answers based on proprietary knowledge sources
and complete tasks for a wide range of use cases. The Foundational Models (FMs) from Amazon and

leading AI companies, made available by Amazon Bedrock, and the FMs offered through Bedrock

Marketplace, are not included in the design of the controls described in this SOC report.

Amazon Braket

Amazon Braket, the quantum computing service of AWS, is designed to help accelerate scientific research
and software development for quantum computing. Amazon Braket provides everything customers need
to build, test, and run quantum programs on AWS, including access to different types of quantum
computers and classical circuit simulators and a unified development environment for building and
executing quantum circuits. Amazon Braket also manages the classical infrastructure required for the
execution of hybrid quantum-classical algorithms. When customers choose to interact with quantum
computers provided by third-parties, Amazon Braket anonymizes the content, so that only content
necessary to process the quantum task is sent to the quantum hardware provider. No AWS account

information is shared and customer data is not stored outside of AWS.

Amazon Chime

Amazon Chime is a communications service that lets customers meet, chat, and place business calls inside
and outside organizations, all using a single application. With Amazon Chime, customers can conduct and
attend online meetings with HD video, audio, screen sharing, meeting chat, dial—in numbers, and in-room
video conference support. Customer can use chat and chat rooms for persistent communications across
desktop and mobile devices. Customers are also able to administer enterprise users, manage policies, and
set up SSO or other advanced features in minutes using Amazon Chime management console.

Amazon Chime SDK

The Amazon Chime SDK is a set of real-time communications components that customers can use to
quickly add messaging, audio, video, and screen sharing capabilities to their web or mobile applications.
Customers can use the Amazon Chime SDK to build real-time media applications that can send and receive
audio and video and allow content sharing. The Amazon Chime SDK works independently of any Amazon
Chime administrator accounts and does not affect meetings hosted on Amazon Chime.

Amazon Cloud Directory
Amazon Cloud Directory enables customers to build flexible cloud-native directories for organizing
hierarchies of data along multiple dimensions. Customers also can create directories for a variety of use
cases, such as organizational charts, course catalogs, and device registries. For example, customers can
create an organizational chart that can be navigated through separate hierarchies for reporting structure,
location, and cost center.


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


42


Section III – Description of the Amazon Web Services System


Amazon CloudFront (excludes content delivery through Amazon CloudFront Embedded Point of
Presences)
Amazon CloudFront is a fast content delivery network (CDN) web service that securely delivers data,
videos, applications and APIs to customers globally with low latency and high-transfer speeds. CloudFront
offers the most advanced security capabilities, including field level encryption and HTTPS support,
seamlessly integrated with AWS Shield, AWS Web Application Firewall and Route 53 to protect against
multiple types of attacks including network and application layer DDoS attacks. These services co-reside
at edge networking locations – globally scaled and connected via the AWS network backbone – providing
a more secure, performant, and available experience for the users.

CloudFront delivers customers' content through a worldwide network of Edge locations. When an end
user requests content that customers serve with CloudFront, the user is routed to the Edge location that
provides the lowest latency, so content is delivered with the best possible performance. If the content is
already in that Edge location, CloudFront delivers it immediately.

Amazon CloudWatch

Amazon CloudWatch is a monitoring and management service built for developers, system operators, site
reliability engineers (SRE), and IT managers. CloudWatch provides the customers with data and actionable

insights to monitor their applications, understand and respond to system-wide performance changes,

optimize resource utilization, and get a unified view of operational health. CloudWatch collects

monitoring and operational data in the form of logs, metrics, and events, providing the customers with a

unified view of AWS resources, applications and services that run on AWS, and on-premises servers.


Amazon CloudWatch Logs

Amazon CloudWatch Logs is a service used to monitor, store, and access log files from Amazon Elastic
Compute Cloud (EC2) instances, AWS CloudTrail, Route 53 and other sources. CloudWatch Logs enables
customers to centralize the logs from systems, applications and AWS services used in a single, highly
scalable service. Customers can easily view them, search for patterns, filter on specific fields or archive
them securely for future analysis. CloudWatch Logs enables customers to view logs, regardless of their
source, as a single and consistent flow of events ordered by time, and to query them based on specific

criteria.

Amazon CodeWhisperer (Deprecated August 15, 2024)
Amazon CodeWhisperer is a productivity tool that generates real-time, single-line or full-function code
suggestions in the customers’ integrated development environment (IDE) and in the command line to help
quickly build software. Customers can quickly and easily accept the top suggestion, view more
suggestions, or continue writing their own code.

Amazon Cognito
Amazon Cognito lets customers add user sign-up, sign-in, and manage permissions for mobile and web
applications. Customers can create their own user directory within Amazon Cognito. Customers can also
choose to authenticate users through social identity providers such as Facebook, Twitter, or Amazon; with
SAML identity solutions; or by using customers' own identity system. In addition, Amazon Cognito enables
customers to save data locally on users' devices, allowing customers' applications to work even when the
devices are offline. Customers can then synchronize data across users' devices so that their app
experience remains consistent regardless of the device they use.


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


43


Section III – Description of the Amazon Web Services System


Amazon Comprehend
Amazon Comprehend is a natural language processing (NLP) service that uses machine learning to find
insights and relationships in text. Amazon Comprehend uses machine learning to help the customers
uncover insights and relationships in their unstructured data without machine learning experience. The
service identifies the language of the text; extracts key phrases, places, people, brands, or events;
understands how positive or negative the text is; analyzes text using tokenization and parts of speech;
and automatically organizes a collection of text files by topic.

Amazon Comprehend Medical
Amazon Comprehend Medical is a HIPAA-eligible natural language processing (NLP) service that facilitates
the use of machine learning to extract relevant medical information from unstructured text. Using
Amazon Comprehend Medical, customers can quickly and accurately gather information, such as medical
condition, medication, dosage, strength, and frequency from a variety of sources like doctors’ notes,
clinical trial reports, and patient health records. Amazon Comprehend Medical uses advanced machine
learning models to accurately and quickly identify medical information, such as medical conditions and
medications, and determines their relationship to each other, for instance, medicine dosage and strength.

Amazon Connect

Amazon Connect is a unified omnichannel solution built to empower personalized, efficient and proactive
experiences across customers’ preferred channels. Customer can ensure customer issues are quickly
resolved, and if multiple contacts are needed, seamlessly maintain context as customer needs change.
Amazon Connect also helps customers proactively engage their customers at scale with relevant
information, such as appointment reminders, product recommendations, and marketing promotions.

Amazon Data Firehose

Amazon Data Firehose is a reliable way to load streaming data into data stores and analytics tools. It can
capture, transform, and load streaming data into Amazon S3, Amazon Redshift, and Amazon OpenSearch
Service enabling near real-time analytics with existing business intelligence tools and dashboards
customers are already using today. The service automatically scales to match the throughput of the
customers’ data and requires no ongoing administration. It can also batch, compress, transform, and
encrypt the data before loading it, minimizing the amount of storage used at the destination and
increasing security.

Amazon DataZone

Amazon DataZone is a data management service that makes it faster and easier for customers to catalog,
discover, share, and govern data stored across AWS, on premises, and third-party sources. With Amazon
DataZone, engineers, data scientists, product managers, analysts, and business users can quickly access
data throughout an organization so that they can discover, use, and collaborate to derive data-driven
insights. Administrators and data owners who oversee an organization's data assets can easily manage
and govern access to data. Amazon DataZone provides built-in workflows for data consumers to request
access to data and for data owners to approve the access.

Amazon Detective

Amazon Detective allows customers to easily analyze, investigate, and quickly identify the root cause of
potential security issues or suspicious activity. Amazon Detective collects log data from customer’s AWS
resources and uses machine learning, statistical analysis, and graph theory to build a linked set of data


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


44


Section III – Description of the Amazon Web Services System


that enables customers to conduct faster and more efficient security investigations. AWS Security services
can be used to identify potential security issues or findings.

Amazon Detective can analyze trillions of events from multiple data sources and automatically creates a
unified, interactive view of the resources, users, and the interactions between them over time. With this
unified view, customers can visualize all the details and context in one place to identify the underlying
reasons for the findings, drill down into relevant historical activities, and quickly determine the root cause.

Amazon DevOps Guru
Amazon DevOps Guru is a service powered by machine learning (ML) that is designed to improve an
application’s operational performance and availability. DevOps Guru helps detect behaviors that deviate
from normal operating patterns so customers can identify operational issues before they impact them.

DevOps Guru uses ML models informed by years of Amazon.com and AWS operational excellence to
identify anomalous application behavior (for example, increased latency, error rates, resource constraints,
and others) and helps surface critical issues that could cause potential outages or service disruptions.
When DevOps Guru identifies a critical issue, it automatically sends an alert and provides a summary of
related anomalies, the likely root cause, and context for when and where the issue occurred. When
possible, DevOps Guru also helps provide recommendations on how to remediate the issue.

Amazon DocumentDB (with MongoDB compatibility)
Amazon DocumentDB (with MongoDB compatibility) is a fast, scalable, and highly available document
database service that supports MongoDB workloads. Amazon DocumentDB is designed from the groundup to give customers the performance, scalability, and availability customers need when operating
mission-critical MongoDB workloads at scale. Amazon DocumentDB implements the Apache 2.0 opensource MongoDB 3.6 API by emulating the responses that a MongoDB client expects from a MongoDB
server, allowing customers to use their existing MongoDB drivers and tools with Amazon DocumentDB.
Amazon DocumentDB uses a distributed, fault-tolerant, self-healing storage system that auto-scales up to
64 TB per database cluster.

Amazon DynamoDB
Amazon DynamoDB is a managed NoSQL database service. Amazon DynamoDB enables customers to
offload to AWS the administrative burdens of operating and scaling distributed databases such as
hardware provisioning, setup and configuration, replication, software patching, and cluster scaling.

Customers can create a database table that can store and retrieve data and serve any requested traffic.
Amazon DynamoDB automatically spreads the data and traffic for the table over a sufficient number of
servers to handle the request capacity specified and the amount of data stored, while maintaining
consistent, fast performance. All data items are stored on Solid State Drives (SSDs) and are automatically
replicated across multiple AZs in a region.

Amazon DynamoDB Accelerator (DAX)
Amazon DynamoDB Accelerator (DAX) is a fully managed, highly available caching service built for Amazon
DynamoDB. DAX delivers up to a 10 times performance improvement—from milliseconds to
microseconds—even at millions of requests per second. DAX does the heavy lifting required to add inmemory acceleration to your DynamoDB tables, without requiring developers to manage cache
invalidation, data population, or cluster management.


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


45


Section III – Description of the Amazon Web Services System


Amazon EC2 Auto Scaling
Amazon EC2 Auto Scaling launches/terminates instances on a customer's behalf according to conditions
customers define, such as schedule, changing metrics like average CPU utilization, or health of the
instance as determined by EC2 or ELB health checks. It allows customers to have balanced compute across
multiple AZs and scale their fleet based on usage.

Amazon Elastic Block Store (EBS)
Amazon Elastic Block Store (EBS) provides persistent block storage volumes for use with Amazon EC2
instances in the AWS Cloud. Each Amazon EBS volume is automatically replicated within its AZ to protect
customers from component failure. Amazon EBS allows customers to create storage volumes from 1 GB
to 16 TB that can be mounted as devices by Amazon EC2 instances. Storage volumes behave like raw,
unformatted block devices, with user supplied device names and a block device interface. Customers can
create a file system on top of Amazon EBS volumes or use them in any other way one would use a block
device (e.g., a hard drive).

Amazon EBS volumes are presented as raw unformatted block devices that have been wiped prior to being
made available for use. Wiping occurs before reuse. If customers have procedures requiring that all data
be wiped via a specific method, customers can conduct a wipe procedure prior to deleting the volume for
compliance with customer requirements. Amazon EBS includes Data Lifecycle Manager, which provides a
simple, automated way to back up data stored on Amazon EBS volumes.

Amazon Elastic Compute Cloud (EC2)
Amazon Elastic Compute Cloud (EC2) is Amazon’s Infrastructure as a Service (IaaS) offering, which
provides scalable computing capacity using server instances in AWS’ data centers. Amazon EC2 is designed
to make web-scale computing easier by enabling customers to obtain and configure capacity with minimal
friction. Customers create and launch instances, which are virtual machines that are available in a wide
variety of hardware and software configurations.

Security within Amazon EC2 is provided on multiple levels: the operating system (OS) of the host layer,
the virtual instance OS or guest OS, a firewall, and signed API calls. Each of these items builds on the
capabilities of the others. This helps prevent data contained within Amazon EC2 from being intercepted
by unauthorized systems or users and to provide Amazon EC2 instances themselves security without
sacrificing flexibility of configuration. The Amazon EC2 service utilizes a hypervisor to provide memory
and CPU isolation between virtual machines and controls access to network, storage, and other devices,
and maintains strong isolation between guest virtual machines. Independent auditors regularly assess the
security of Amazon EC2 and penetration teams regularly search for new and existing vulnerabilities and

attack vectors.

AWS prevents customers from accessing physical hosts or instances not assigned to them by filtering
through the virtualization software **(Control AWSCA-3.12).**

Amazon EC2 provides a complete firewall solution, referred to as a Security Group. This mandatory
inbound firewall is configured in a default deny-all mode to prevent unauthorized access and Amazon EC2
customers must explicitly open the ports needed to allow inbound traffic **(Control AWSCA-3.9).**


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


46


Section III – Description of the Amazon Web Services System


Amazon provides a Time Sync function for time synchronization in EC2 Linux instances with the
Coordinated Universal Time (UTC). It is delivered over the Network Time Protocol (NTP) and uses a fleet
of redundant satellite-connected and atomic clocks in each region to provide a highly accurate reference
clock via the local 169.254.169.123 IPv4 address or fd00:ec2::123 IPv6 address. Irregularities in the Earth’s
rate of rotation that cause UTC to drift with respect to the International Celestial Reference Frame (ICRF),
by an extra second, are called leap second. Time Sync addresses this clock drift by smoothing out leap
seconds over a period of time (commonly called leap smearing) which makes it easy for customer
applications to deal with leap seconds. The Amazon EC2 clock synchronization for the US East (Northern
Virginia), US East (Ohio), Asia Pacific (Tokyo), Asia Pacific (Thailand), Asia Pacific (Malaysia), and Europe
(Stockholm) regions have been uplifted to achieve accuracy within 100 microseconds versus 1 millisecond
for the other regions on supported EC2 instances. Instance types that do not support this will still have 1
millisecond accuracy **(Control AWSCA-7.10).**

Amazon Elastic Container Registry (ECR)
Amazon Elastic Container Registry is a Docker container image registry that makes it easy for developers
to store, manage, and deploy Docker container images. Amazon Elastic Container Registry is integrated
with Amazon Elastic Container Service (ECS) and Amazon Elastic Kubernetes Service (EKS).

Amazon Elastic Container Service (both Fargate and EC2 launch types)
Amazon Elastic Container Service is a highly scalable, high performance container management service
that supports Docker containers and allows customers to easily run applications on a managed cluster of
Amazon EC2 instances. Amazon Elastic Container Service eliminates the need for customers to install,
operate, and scale customers' own cluster management infrastructure. With simple API calls, customers
can launch and stop Docker-enabled applications, query the complete state of customers' clusters, and
access many familiar features like security groups, Elastic Load Balancing, EBS volumes, and IAM roles.
Customers can use Amazon Elastic Container Service to schedule the placement of containers across
customers' clusters based on customers' resource needs and availability requirements.

Amazon Elastic File System (EFS)
Amazon Elastic File System (EFS) provides file storage for Amazon EC2 instances. EFS presents a network
attached file system interface via the NFS v4 protocol. EFS file systems grow and shrink elastically as data
is added and deleted by users. Amazon EFS spreads data across multiple AZs; in the event that an AZ is
not reachable, the structure allows customers to still access their full set of data. The customer is
responsible for choosing which of their Virtual Private Clouds (VPCs) they want a file system to be accessed
from by creating resources called mount targets. One mount target exists for each AZ, which exposes an
IP address and DNS name for mounting the customer’s file system onto their EC2 instances. Customers
then log into their EC2 instance and issue a ‘mount’ command, pointing at their mount target’ IP address
or DNS name. A mount target is assigned one or more VPC security groups to which it belongs. The VPC
security groups define rules for what VPC traffic can reach the mount targets and in turn can reach the
file system.

Amazon Elastic Kubernetes Service (EKS) (both Fargate and EC2 launch types)
Amazon Elastic Kubernetes Service (EKS) makes it easy to deploy, manage, and scale containerized
applications using Kubernetes on AWS. Amazon EKS runs the Kubernetes management infrastructure for
the customer across multiple AWS AZs to eliminate a single point of failure. Amazon EKS is certified
Kubernetes conformant so the customers can use existing tooling and plugins from partners and the
Kubernetes community. Applications running on any standard Kubernetes environment are fully


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


47


Section III – Description of the Amazon Web Services System


compatible and can be easily migrated to Amazon EKS.

Amazon Elastic MapReduce (EMR)
Amazon Elastic MapReduce (EMR) is a web service that provides managed Hadoop clusters on Amazon
EC2 instances running a Linux operating system. Amazon EMR uses Hadoop processing combined with
several AWS products to do such tasks as web indexing, data mining, log file analysis, machine learning,
scientific simulation, and data warehousing. Amazon EMR actively manages clusters for customers,
replacing failed nodes and adjusting capacity as requested. Amazon EMR securely and reliably handles a
broad set of big data use cases, including log analysis, web indexing, data transformations (ETL), machine
learning, financial analysis, scientific simulation, and bioinformatics.

Amazon ElastiCache

Amazon ElastiCache automates management tasks for in-memory cache environments, such as patch
management, failure detection, and recovery. It works in conjunction with other AWS services to provide
a managed in-memory cache. For example, an application running in Amazon EC2 can securely access an
Amazon ElastiCache Cluster in the same region with very slight latency.

Using the Amazon ElastiCache service, customers create a Cache Cluster, which is a collection of one or
more Cache Nodes, each running an instance of the Memcached, Redis Engine, or DAX Engine. A Cache
Node is a self-contained environment which provides a fixed-size chunk of secure, network-attached RAM.
Each Cache Node runs an instance of the Memcached, Redis Engine, or DAX Engine, and has its own DNS
name and port. Multiple types of Cache Nodes are supported, each with varying amounts of associated

memory.

Amazon EventBridge
Amazon EventBridge delivers a near real-time stream of events that describe changes in AWS resources.
Customers can configure routing rules to determine where to send collected data to build application
architectures that react in real time to the data sources. Amazon EventBridge becomes aware of
operational changes as they occur and responds to these changes by taking corrective action as necessary
by sending message to respond to the environment, activating functions, making changes and capturing

state information.

Amazon FinSpace
Amazon FinSpace is a data management and analytics service that makes it easy to store, catalog, and
prepare financial industry data at scale. Amazon FinSpace reduces the time it takes for financial services
industry (FSI) customers to find and access all types of financial data for analysis.

Amazon Forecast

Amazon Forecast uses machine learning to combine time series data with additional variables to build
forecasts. With Amazon Forecast, customers can import time series data and associated data into Amazon
Forecast from their Amazon S3 database. From there, Amazon Forecast automatically loads the data,
inspects it, and identifies the key attributes needed for forecasting. Amazon Forecast then trains and
optimizes a customer’s custom model and hosts them in a highly available environment where it can be
used to generate business forecasts.

Amazon Forecast is protected by encryption. Any content processed by Amazon Forecast is encrypted
with customer keys through Amazon Key Management Service and encrypted at rest in the AWS Region


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


48


Section III – Description of the Amazon Web Services System


where a customer is using the service. Administrators can also control access to Amazon Forecast through
an AWS Identity and Access Management (IAM) permissions policy ensuring that sensitive information is
kept secure and confidential.

Amazon Fraud Detector

Amazon Fraud Detector helps detect suspicious online activities such as the creation of fake accounts and
online payment fraud. Amazon Fraud Detector uses machine learning (ML) and 20 years of fraud detection
expertise from AWS and Amazon.com to automatically identify fraudulent activity to catch more fraud,
faster. With Amazon Fraud Detector, customers can create a fraud detection ML model with just a few

clicks and use it to evaluate online activities in milliseconds.

Amazon FSx

Amazon FSx provides third-party file systems. Amazon FSx provides the customers with the native
compatibility of third-party file systems with feature sets for workloads such as Windows-based storage,
high-performance computing (HPC), machine learning, and electronic design automation (EDA). The
customers don’t have to worry about managing file servers and storage, as Amazon FSx automates the
time-consuming administration tasks such as hardware provisioning, software configuration, patching,
and backups. Amazon FSx integrates the file systems with cloud-native AWS services, making them even

more useful for a broader set of workloads.

Amazon GuardDuty
Amazon GuardDuty is a threat detection service that continuously monitors for malicious activity and
unauthorized behavior to protect the customers’ AWS accounts and workloads. With the cloud, the
collection and aggregation of account and network activities is simplified, but it can be time consuming
for security teams to continuously analyze event log data for potential threats. With GuardDuty, the
customers now have an intelligent and cost-effective option for continuous threat detection in the AWS

Cloud.

Amazon Inspector
Amazon Inspector is an automated vulnerability management service that continually scans AWS
workloads for software vulnerabilities and unintended network exposure. Amazon Inspector removes the
operational overhead associated with deploying and configuring a vulnerability management solution by
allowing customers to deploy Amazon Inspector across all accounts with a single step.

Amazon Inspector Classic
Amazon Inspector Classic is an automated security assessment service for customers seeking to improve
the security and compliance of applications deployed on AWS. Amazon Inspector Classic automatically
assesses applications for vulnerabilities or deviations from leading practices. After performing an
assessment, Amazon Inspector Classic produces a detailed list of security findings prioritized by level of
severity.

Amazon Kendra

Amazon Kendra is an intelligent search service powered by machine learning. Kendra reimagines
enterprise search for customer websites and applications so employees and customers can easily find
content, even when it's scattered across multiple locations and content repositories.


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


49


Section III – Description of the Amazon Web Services System


Amazon Keyspaces (for Apache Cassandra)
Amazon Keyspaces (for Apache Cassandra) is a scalable, highly available Apache Cassandra–compatible
database service. With Amazon Keyspaces, customers can run Cassandra workloads on AWS using the
same Cassandra application code and developer tools that customers use today. Amazon Keyspaces is
serverless and gives customers the performance, elasticity, and enterprise features customers need to
operate business-critical Cassandra workloads at scale.

Amazon Kinesis Data Streams

Amazon Kinesis Data Streams is a massively scalable and durable real-time data streaming service. Kinesis
Data Streams can continuously capture gigabytes of data per second from hundreds of thousands of
sources such as website clickstreams, database event streams, financial transactions, social media feeds,
IT logs and location-tracking events. The collected data is available in milliseconds to enable real-time
analytics use cases such as real-time dashboards, real-time anomaly detection, dynamic pricing and more.

Amazon Kinesis Video Streams

Amazon Kinesis Video Streams makes it easy to securely stream video from connected devices to AWS for
analytics, machine learning (ML), playback, and other processing. Kinesis Video Streams automatically
provisions and elastically scales the infrastructure needed to ingest streaming video data from millions of
devices. It also durably stores, encrypts, and indexes video data in the streams, and allows the customers
to access their data through easy-to-use APIs. Kinesis Video Streams enables the customers to playback
video for live and on-demand viewing, and quickly build applications that take advantage of computer
vision and video analytics.

Amazon Lex

Amazon Lex is a service for building conversational interfaces into any application using voice and text.
Amazon Lex provides the advanced deep learning functionalities of automatic speech recognition (ASR)
for converting speech to text, and natural language understanding (NLU) to recognize the intent of the
text, to enable customers to build applications with highly engaging user experiences and lifelike
conversational interactions. Amazon Lex scales automatically, so customers do not need to worry about
managing infrastructure.

Amazon Location Service

Amazon Location Service makes it easy for developers to add location functionality to applications without

compromising data security and user privacy. With Amazon Location Service, customers can build

applications that provide maps and points of interest, convert street addresses into geographic

coordinates, calculate routes, track resources, and trigger actions based on location. Amazon Location

Service uses high-quality geospatial data to provide maps, places, routes, tracking, and geofencing.


Amazon Macie

Amazon Macie is a data security and data privacy service that uses machine learning and pattern matching
to help customers discover, monitor, and protect their sensitive data in AWS.

Macie automates the discovery of sensitive data, such as personally identifiable information (PII) and
financial data, to provide customers with a better understanding of the data that organization stores in
Amazon Simple Storage Service (Amazon S3). Macie also provides customers with an inventory of the S3
buckets, and it automatically evaluates and monitors those buckets for security and access control. Within
minutes, Macie can identify and report overly permissive or unencrypted buckets for the organization.


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


50


Section III – Description of the Amazon Web Services System


If Macie detects sensitive data or potential issues with the security or privacy of customer content, it
creates detailed findings for customers to review and remediate as necessary. Customers can review and
analyze these findings directly in Macie, or monitor and process them by using other services, applications,
and systems.

Amazon Managed Grafana
Amazon Managed Grafana is a service for open-source Grafana, providing interactive data visualization
for monitoring and operational data. Using Amazon Managed Grafana, customers can visualize, analyze,
and alarm on their metrics, logs, and traces collected from multiple data sources in their observability
system, including AWS, third-party ISVs, and other resources across their IT portfolio. Amazon Managed
Grafana offloads the operational management of Grafana by automatically scaling compute and database
infrastructure as usage demands increase, with automated version updates and security
patching. Amazon Managed Grafana natively integrates with AWS services so customers can securely add,
query, visualize, and analyze their AWS data across multiple accounts and regions with a few clicks in the
AWS Console. Amazon Managed Grafana integrates with AWS IAM Identity Center and supports Security
Assertion Markup Language (SAML) 2.0, so customers can set up user access to specific dashboards and
data sources for only certain users in their corporate directory.

Amazon Managed Service for Apache Flink
Amazon Managed Service for Apache Flink is an easy way for customers to analyze streaming data, gain
actionable insights, and respond to business and customer needs in real time. Amazon Managed Service
for Apache Flink reduces the complexity of building, managing, and integrating streaming applications
with other AWS services. SQL users can easily query streaming data or build entire streaming applications
using templates and an interactive SQL editor. Java developers can quickly build sophisticated streaming
applications using open-source Java libraries and AWS integrations to transform and analyze data in real
time.

Amazon Managed Service for Prometheus

Amazon Managed Service for Prometheus is a Prometheus-compatible monitoring and alerting service
that facilitates monitoring of containerized applications and infrastructure at scale. The Cloud Native
Computing Foundation’s Prometheus project is an open-source monitoring and alerting solution
optimized for container environments. With Amazon Managed Service for Prometheus, customers can
use the open-source Prometheus query language (PromQL) to monitor and alert on the performance of
containerized workloads, without having to scale and operate the underlying infrastructure. Amazon
Managed Service for Prometheus automatically scales the ingestion, storage, alerting, and querying of
operational metrics as workloads grow or shrink, and it is integrated with AWS security services to enable

fast and secure access to data.

Amazon Managed Streaming for Apache Kafka
Amazon Managed Streaming for Apache Kafka is a service that makes it easy for customers to build and
run applications that use Apache Kafka to process streaming data. Apache Kafka is an open-source
platform for building real-time streaming data pipelines and applications. With Amazon MSK, customers
can use Apache Kafka APIs to populate data lakes, stream changes to and from databases, and power
machine learning and analytics applications.


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


51


Section III – Description of the Amazon Web Services System


Amazon Managed Workflows for Apache Airflow (Amazon MWAA)
Amazon Managed Workflows for Apache Airflow is a service for Apache Airflow that lets customers use
their current, familiar Apache Airflow platform to orchestrate their workflows. Customers gain improved
scalability, availability, and security without the operational burden of managing underlying
infrastructure. Amazon Managed Workflows for Apache Airflow orchestrates customer workflows using
Directed Acyclic Graphs (DAGs) written in Python. Customers provide Amazon Managed Workflows for
Apache Airflow an Amazon Simple Storage Service (S3) bucket where customer’s DAGs, plugins, and
Python requirements reside. Then customers can run and monitor their DAGs from the AWS Management
Console, a command line interface (CLI), a software development kit (SDK), or the Apache Airflow user
interface (UI).

Amazon MemoryDB (formerly known as Amazon MemoryDB for Redis)
Amazon MemoryDB is a Redis-compatible, durable, in-memory database service. It is purpose-built for
modern applications with microservices architectures.

Amazon MemoryDB is compatible with Redis, an open-source data store, enabling customers to quickly
build applications using the same flexible Redis data structures, APIs, and commands that they already
use today. With Amazon MemoryDB, all of the customer’s data is stored in memory, which enables the
customer to achieve microsecond read and single-digit millisecond write latency and high throughput.
Amazon MemoryDB also stores data durably across multiple AZs using a distributed transactional log to
enable fast failover, database recovery, and node restarts. Delivering both in-memory performance and
Multi-AZ durability, Amazon MemoryDB can be used as a high-performance primary database for
microservices applications eliminating the need to separately manage both a cache and durable database.

Amazon MQ

Amazon MQ is a managed message broker service for Apache ActiveMQ and RabbitMQ that sets up and
operates message brokers in the cloud. Message brokers allow different software systems – often using
different programming languages, and on different platforms – to communicate and exchange
information. Messaging is the communications backbone that connects and integrates the components
of distributed applications, such as order processing, inventory management, and order fulfillment for ecommerce. Amazon MQ manages the administration and maintenance of two open-source message
brokers, ActiveMQ and RabbitMQ.

Amazon Neptune
Amazon Neptune is a fast and reliable graph database service that makes it easy to build and run
applications that work with highly connected datasets. The core of Amazon Neptune is a purpose-built,
high-performance graph database engine optimized for storing billions of relationships and querying the
graph with milliseconds latency. Amazon Neptune supports popular graph models, Property Graph, and
W3C's RDF, and their respective query languages Apache, TinkerPop Gremlin, and SPARQL, allowing
customers to easily build queries that efficiently navigate highly connected datasets. Neptune powers
graph use cases such as recommendation engines, fraud detection, knowledge graphs, drug discovery,
and network security.

Amazon OpenSearch Service
Amazon OpenSearch Service is a service that makes it easy for the customer to deploy, secure, and
operate OpenSearch cost effectively at scale. Amazon OpenSearch Service lets the customers pay only for


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


52


Section III – Description of the Amazon Web Services System


what they use – there are no upfront costs or usage requirements. With Amazon OpenSearch Service, the
customers get the ELK stack they need, without the operational overhead.

Amazon Personalize

Amazon Personalize is a machine learning service that makes it easy for developers to create
individualized recommendations for customers using their applications. Amazon Personalize makes it easy
for developers to build applications capable of delivering a wide array of personalization experiences,
including specific product recommendations, personalized product re-ranking and customized direct
marketing. Amazon Personalize goes beyond rigid static rule- based recommendation systems and trains,
tunes, and deploys custom machine learning models to deliver highly customized recommendations to
customers across industries such as retail, media and entertainment.

Amazon Pinpoint and End User Messaging (formerly Amazon Pinpoint)
Amazon Pinpoint and End User Messaging helps customers engage with their customers by sending email,
SMS, and mobile push messages. The customers can use Amazon Pinpoint and End User Messaging
to send targeted messages (such as promotional alerts and customer retention campaigns), as well as
direct messages (such as order confirmations and password reset messages) to their customers.

Amazon Polly
Amazon Polly is a service that turns text into lifelike speech, allowing customers to create applications
that talk, and build entirely new categories of speech-enabled products. Amazon Polly is a Text-toSpeech service that uses advanced deep learning technologies to synthesize speech that sounds like a

human voice.

Amazon Q Business (Effective August 15, 2024)

Amazon Q Business is a service that deploys a generative AI business expert for your enterprise data. It
comes with a built-in user interface, where users ask complex questions in natural language, create or
compare documents, generate document summaries, and interact with their third- party applications.

Amazon Q Developer (Effective August 15, 2024)
Amazon Q Developer is a generative artificial intelligence (AI) powered conversational assistant that can
help customers understand, build, extend, and operate AWS applications. Customers can ask questions
about AWS architecture, AWS resources, best practices, documentation, support, and more. When used
in an integrated development environment (IDE), Amazon Q provides software development assistance.
Amazon Q can chat about code, provide inline code completions, generate net new code, scan your code
for security vulnerabilities, and make code upgrades and improvements, such as language updates,
debugging, and optimizations.

Amazon Quantum Ledger Database (QLDB)
Amazon Quantum Ledger Database (QLDB) is a ledger database that provides a transparent, immutable
and cryptographically verifiable transaction log owned by a central trusted authority. Amazon QLDB can
be used to track each and every application data change and maintains a complete and verifiable history
of changes over time.

Amazon QuickSight
Amazon QuickSight is a fast, cloud-powered business analytics service that makes it easy to build
visualizations, perform ad-hoc analysis, and quickly get business insights from customers’ data. Using this


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


53


Section III – Description of the Amazon Web Services System


cloud-based service customers can connect to their data, perform advanced analysis, and create
visualizations and dashboards that can be accessed from any browser or mobile device.

Amazon Redshift

Amazon Redshift is a data warehouse service to analyze data using a customer’s existing Business
Intelligence (BI) tools. Amazon Redshift also includes Redshift Spectrum, allowing customers to directly
run SQL queries against Exabytes of unstructured data in Amazon S3.

Amazon Rekognition
The easy-to-use Rekognition API allows customers to automatically identify objects, people, text, scenes,
and activities, as well as detect any inappropriate content. Developers can quickly build a searchable
content library to optimize media workflows, enrich recommendation engines by extracting text in
images, or integrate secondary authentication into existing applications to enhance end-user security.
With a wide variety of use cases, Amazon Rekognition enables the customers to easily add the benefits of
computer vision to the business.

Amazon Relational Database Service (RDS)
Amazon Relational Database Service (RDS) enables customers to set up, operate, and scale a relational
database in the cloud. Amazon RDS manages backups, software patching, automatic failure detection,
and recovery. It provides cost-efficient and resizable capacity while automating time-consuming
administration tasks such as hardware provisioning, database setup, patching and backups.

Amazon Route 53

Amazon Route 53 provides managed Domain Name System (DNS) web service. Amazon Route 53 connects
user requests to infrastructure running both inside and outside of AWS. Customers can use Amazon Route
53 to configure DNS health checks to route traffic to healthy endpoints or to independently monitor the
health of their application and its endpoints. Amazon Route 53 enables customers to manage traffic
globally through a variety of routing types, including Latency Based Routing, Geo DNS, and Weighted
Round Robin, all of these routing types can be combined with DNS Failover. Amazon Route 53 also offers
Domain Name Registration; customers can purchase and manage domain names such as example.com
and Amazon Route 53 will automatically configure DNS settings for their domains. Amazon Route 53 sends
automated requests over the internet to a resource, such as a web server, to verify that it is reachable,
available, and functional. Customers also can choose to receive notifications when a resource becomes
unavailable and choose to route internet traffic away from unhealthy resources.

Amazon S3 Glacier

Amazon S3 Glacier is an archival storage solution for data that is infrequently accessed for which retrieval

times of several hours are suitable. Data in Amazon S3 Glacier is stored as an archive. Archives in Amazon

S3 Glacier can be created or deleted, but archives cannot be modified. Amazon S3 Glacier archives are
organized in vaults. All vaults created have a default permission policy that only permits access by the
account creator or users that have been explicitly granted permission. Amazon S3 Glacier enables
customers to set access policies on their vaults for users within their AWS Account. User policies can
express access criteria for Amazon S3 Glacier on a per vault basis. Customers can enforce Write Once Read
Many (WORM) semantics for users through user policies that forbid archive deletion.


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


54


Section III – Description of the Amazon Web Services System


Amazon SageMaker AI (formerly Amazon SageMaker) (excludes Studio Lab, Public Workforce and
Vendor Workforce for all features)
Amazon SageMaker AI is a platform that enables developers and data scientists to quickly and easily build,
train, and deploy machine learning models at any scale. Amazon SageMaker AI removes the barriers that
typically “slow down” developers who want to use machine learning.

Amazon SageMaker AI removes the complexity that holds back developer success with the process of

building, training, and deploying machine learning models at scale. Amazon SageMaker AI includes

modules that can be used together or independently to build, train, and deploy a customer’s machine

learning models.

Amazon Security Lake (Effective August 15, 2024)
Amazon Security Lake automatically centralizes security data from AWS environments, SaaS providers, on
premises, and cloud sources into a purpose-built data lake stored in a customer account. With Security
Lake, customers can get a more complete understanding of security data across their entire organization.
They can also improve the protection of workloads, applications, and data.

Amazon Simple Email Service (SES)
Amazon Simple Email Service (SES) is a cost-effective, flexible and scalable email service that enables
developers to send mail from within any application. Customers can configure Amazon SES to support
several email use cases including transactional, marketing, or mass email communications. Amazon SES'
flexible IP deployment and email authentication options help drive higher deliverability and protect
sender reputation, while sending analytics to measure impact of each email. With Amazon SES, customers
can send email securely, globally and at scale.

Amazon Simple Notification Service (SNS)
Amazon Simple Notification Service (SNS) is a web service to set up, operate, and send notifications. It
provides developers the capability to publish messages from an application and deliver them to
subscribers or other applications. Amazon SNS follows the “publish-subscribe” (pub-sub) messaging
paradigm, with notifications being delivered to clients using a “push” mechanism. Using SNS requires
defining a "Topic", setting policies on access and delivery of the Topic, subscribing consumers and
designating delivery endpoints, and publishing messages to a Topic. Administrators define a Topic as an
access point for publishing messages and allowing customers to subscribe to notifications. Security
policies are applied to Topics to determine who can publish, who can subscribe, and to designate protocols
supported.

Amazon Simple Queue Service (SQS)
Amazon Simple Queue Service (SQS) is a message queuing service that offers a distributed hosted queue
for storing messages as they travel between computers. By using Amazon SQS, developers can move data
between distributed components of their applications that perform different tasks, without losing
messages or requiring each component to be always available. Amazon SQS allows customers to build an
automated workflow, working in close conjunction with Amazon EC2 and the other AWS infrastructure

web services.

Amazon SQS’ main components consist of a frontend request-router fleet, a backend data-storage fleet,
a metadata cache fleet, and a dynamic workload management fleet. User queues are mapped to one or


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


55


Section III – Description of the Amazon Web Services System


more backend clusters. Requests to read, write, or delete messages come into the frontends. The
frontends contact the metadata cache to find out which backend cluster hosts that queue and then
connect to nodes in that cluster to service the request.

For authorization, Amazon SQS has its own resource-based permissions system that uses policies written
in the same language used for AWS IAM policies. User permissions for any Amazon SQS resource can be
given either through the Amazon SQS policy system or the AWS IAM policy system, which is authorized
by AWS Identity and Access Management Service. Such policies with a queue are used to specify which
AWS Accounts have access to the queue as well as the type of access and conditions.

Amazon Simple Storage Service (S3)
Amazon Simple Storage Service (S3) provides a web services interface that can be used to store and
retrieve data from anywhere on the web. To provide customers with the flexibility to determine how,
when, and to whom they wish to expose the information they store in AWS, Amazon S3 APIs provide both
bucket and object-level access controls, with defaults that only permit authenticated access by the bucket
and/or object creator. Unless a customer grants anonymous access, the first step before a user can access
Amazon S3 is to be authenticated with a request signed using the user’s secret access key.

An authenticated user can read an object only if the user has been granted read permissions in an Access
Control List (ACL) at the object level. An authenticated user can list the keys and create or overwrite
objects in a bucket only if the user has been granted read and write permissions in an ACL at the bucket
level. Bucket and object-level ACLs are independent; an object does not inherit ACLs from its bucket.
Permissions to read or modify the bucket or object ACLs are themselves controlled by ACLs that default
to creator-only access. Therefore, the customer maintains full control over who has access to its data.
Customers can grant access to their Amazon S3 data to other AWS users by AWS Account ID or email, or
DevPay Product ID. Customers can also grant access to their Amazon S3 data to all AWS users or to
everyone (enabling anonymous access).

Network devices supporting Amazon S3 are configured to only allow access to specific ports on other
Amazon S3 server systems **(Control AWSCA-3.7).** External access to data stored in Amazon S3 is logged
and the logs are retained for at least 90 days, including relevant access request information, such as the
data accessor IP address, object, and operation **(Control AWSCA-3.8).**

Amazon Simple Workflow Service (SWF)
Amazon Simple Workflow Service (SWF) is an orchestration service for building scalable distributed
applications. Often an application consists of several different tasks to be performed in a particular
sequence driven by a set of dynamic conditions. Amazon SWF enables developers to architect and
implement these tasks, run them in the cloud or on-premises and coordinate their flow. Amazon SWF
manages the execution flow such that tasks are load balanced across the workers, inter-task dependencies
are respected, concurrency is handled appropriately, and child workflows are executed.

Amazon SWF enables applications to be built by orchestrating tasks coordinated by a decider process.
Tasks represent logical units of work and are performed by application components that can take any
form, including executable code, scripts, web service calls, and human actions.

Developers implement workers to perform tasks. They run their workers either on cloud infrastructure,
such as Amazon EC2, or off-cloud. Tasks can be long-running, may fail, may timeout and may complete


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


56


Section III – Description of the Amazon Web Services System


with varying throughputs and latencies. Amazon SWF stores tasks for workers, assigns them when workers
are ready, tracks their progress, and keeps their latest state, including details on their completion. To
orchestrate tasks, developers write programs that get the latest state of tasks from Amazon SWF and use
it to initiate subsequent tasks in an ongoing manner. Amazon SWF maintains an application’s execution
state durably so that the application can be resilient to failures in individual application components.

Amazon SWF provides auditability by giving customers visibility into the execution of each step in the
application. The Management Console and APIs let customers monitor all running executions of the
application. The customer can zoom in on any execution to see the status of each task and its input and
output data. To facilitate troubleshooting and historical analysis, Amazon SWF retains the history of
executions for any number of days that the customer can specify, up to a maximum of 90 days.

The actual processing of tasks happens on compute resources owned by the end customer. Customers
are responsible for securing these compute resources, for example if a customer uses Amazon EC2 for
workers then they can restrict access to their instances in Amazon EC2 to specific AWS IAM users. In
addition, customers are responsible for encrypting sensitive data before it is passed to their workflows
and decrypting it in their workers.

Amazon SimpleDB
Amazon SimpleDB is a non-relational data store that allows customers to store and query data items via
web services requests. Amazon SimpleDB then creates and manages multiple geographically distributed
replicas of data automatically to enable high availability and data durability.

Data in Amazon SimpleDB is stored in domains, which are similar to database tables except that functions
cannot be performed across multiple domains. Amazon SimpleDB APIs provide domain-level controls that
only permit authenticated access by the domain creator.

Data stored in Amazon SimpleDB is redundantly stored in multiple physical locations as part of normal
operation of those services. Amazon SimpleDB provides object durability by protecting data across
multiple AZs on the initial write and then actively doing further replication in the event of device
unavailability or detected bit-rot.

Amazon Textract

Amazon Textract automatically extracts text and data from scanned documents. With Textract customers
can quickly automate document workflows, enabling customers to process large volumes of document
pages in a short period of time. Once the information is captured, customers can take action on it within
their business applications to initiate next steps for a loan application or medical claims processing.
Additionally, customers can create search indexes, build automated approval workflows, and better
maintain compliance with document archival rules by flagging data that may require redaction.

Amazon Timestream

Amazon Timestream is a fast, scalable, and serverless time series database service for IoT and operational
applications that makes it easy to store and analyze trillions of events per day up to 1,000 times faster
and at as little as 1/10th the cost of relational databases. Amazon Timestream saves customers time and
cost in managing the lifecycle of time series data by keeping recent data in memory and moving historical
data to a cost optimized storage tier based upon user defined policies. Amazon Timestream's purposebuilt query engine lets customers access and analyze recent and historical data together, without needing


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


57


Section III – Description of the Amazon Web Services System


to specify explicitly in the query whether the data resides in the in-memory or cost-optimized tier. Amazon
Timestream has built-in time series analytics functions, helping customers identify trends and patterns in

data in real-time.

Amazon Transcribe

Amazon Transcribe makes it easy for customers to add speech-to-text capability to their applications.
Audio data is virtually impossible for computers to search and analyze. Therefore, recorded speech needs
to be converted to text before it can be used in applications.

Amazon Transcribe uses a deep learning process called automatic speech recognition (ASR) to convert
speech to text quickly. Amazon Transcribe can be used to transcribe customer service calls, to automate
closed captioning and subtitling, and to generate metadata for media assets to create a fully searchable

archive.

Amazon Transcribe automatically adds punctuation and formatting so that the output closely matches the
quality of manual transcription at a fraction of the time and expense.

Amazon Translate

Amazon Translate is a neural machine translation service that delivers fast, high-quality, and affordable
language translation. Neural machine translation is a form of language translation automation that uses
deep learning models to deliver more accurate and more natural sounding translation than traditional
statistical and rule- based translation algorithms. Amazon Translate allows customers to localize content
such as websites and applications - for international users, and to easily translate large volumes of text
efficiently.

Amazon Verified Permissions (Effective February 15, 2025)
Amazon Verified Permissions is a fully managed authorization service that uses the provably correct Cedar
policy language, so customers can build more secure applications. With Verified Permissions, developers
can build applications faster by externalizing authorization and centralizing policy management. They can
also align authorization within the application with Zero Trust principles. Security and audit teams can
better analyze and audit who has access to what within applications.

Amazon Virtual Private Cloud (VPC)
Amazon Virtual Private Cloud (VPC) enables customers to provision a logically isolated section of the AWS
cloud where AWS resources can be launched in a virtual network defined by the customer. Customers can
connect their existing infrastructure to the network isolated Amazon EC2 instances within their Amazon
VPC, including extending their existing management capabilities, such as security services, firewalls and
intrusion detection systems, to include their instances via a Virtual Private Network (VPN) connection. The
VPN service provides end-to-end network isolation by using an IP address range of a customer’s choice,
and routing all of their network traffic between their Amazon VPC and another network designated by the
customer via an encrypted Internet Protocol security (IPsec) VPN.

Customers can optionally connect their VPC to the Internet by adding an Internet Gateway (IGW) or a NAT
Gateway. An IGW allows bi-directional access to and from the internet for some instances in the VPC
based on the routes a customer defines, which specify which IP address traffic should be routable from
the internet, Security Groups, and Network ACLs (NACLS) which limit which instances can accept or send
this traffic. Customers can also optionally configure a NAT Gateway which allows egress-only traffic


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


58


Section III – Description of the Amazon Web Services System


initiated from a VPC instance to reach the internet, but not allow traffic initiated from the internet to
reach VPC instances. This is accomplished by mapping the private IP addresses to a public address on the
way out, and then map the public IP address to the private address on the return trip.

The objective of this architecture is to isolate AWS resources and data in one Amazon VPC from another
Amazon VPC, and to help prevent data transferred from outside the Amazon network except where the
customer has specifically configured internet connectivity options or via an IPsec VPN connection to their

off-cloud network.

Further details are provided below:


  - **Virtual Private Cloud (VPC):** An Amazon VPC is an isolated portion of the AWS cloud within which
customers can deploy Amazon EC2 instances into subnets that segment the VPC’s IP address
range (as designated by the customer) and isolate Amazon EC2 instances in one subnet from

another. Amazon EC2 instances within an Amazon VPC are accessible to customers via Internet

Gateway (IGW), Virtual Gateway (VGW), Transit Gateway (TGW) or VPC Peerings established to
the Amazon VPC **(Control AWSCA-3.13** and **AWSCA-3.15).**


  - **IPsec VPN:** An IPsec VPN connection connects a customer’s Amazon VPC to another network

designated by the customer. IPsec is a protocol suite for securing Internet Protocol (IP)
communications by authenticating and encrypting each IP packet of a data stream. An AWS siteto-site VPN connection consists of two independent IPsec VPN tunnels for redundancy and
availability. Amazon VPC customers can create an IPsec VPN connection to their Amazon VPC by
first establishing an Internet Key Exchange (IKE) security association between their Amazon VPC
VPN gateway and another network gateway using a pre-shared key as the authenticator. Upon
establishment, IKE negotiates an ephemeral key to secure future IKE messages. An IKE security
association cannot be established unless there is complete agreement among the parameters.
Next, using the IKE ephemeral key, two keys in total are established between the VPN gateway
and customer gateway to form an IPsec security association. Traffic between gateways is
encrypted and decrypted using this security association. IKE automatically rotates the ephemeral
keys used to encrypt traffic within the IPsec security association on a regular basis to ensure
confidentiality of communications **(Control AWSCA-3.14** and **AWSCA-4.3)** .

Amazon WorkDocs

Amazon WorkDocs is a secure content creation, storage and collaboration service. Users can share files,
provide rich feedback, and access their files on WorkDocs from any device. WorkDocs encrypts data in
transit and at rest, and offers powerful management controls, active directory integration, and near realtime visibility into file and user actions. The WorkDocs SDK allows users to use the same AWS tools they
are already familiar with to integrate WorkDocs with AWS products and services, their existing solutions,
third-party applications, or build their own.

Amazon WorkMail

Amazon WorkMail is a managed business email and calendaring service with support for existing desktop
and mobile email clients. It allows access to email, contacts, and calendars using Microsoft Outlook, a
browser, or native iOS and Android email applications. Amazon WorkMail can be integrated with a
customer’s existing corporate directory and the customer controls both the keys that encrypt the data
and the location (AWS Region) under which the data is stored.


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


59


Section III – Description of the Amazon Web Services System


Customers can create an organization in Amazon WorkMail, select the Active Directory they wish to
integrate with, and choose their encryption key to apply to all customer content. After setup and
validation of their mail domain, users from the Active Directory are selected or added, enabled for Amazon
WorkMail, and given an email address identity inside the customer owned mail domain.

Amazon WorkSpaces
Amazon WorkSpaces is a managed desktop computing service in the cloud. Amazon WorkSpaces enables
customers to deliver a high-quality desktop experience to end-users as well as help meet compliance and
security policy requirements. When using Amazon WorkSpaces, an organization’s data is neither sent to
nor stored on end-user devices. The PCoIP and WSP protocols used by Amazon WorkSpaces utilize
interactive video streaming to provide a desktop experience to the user while the data remains in the
AWS cloud or in the organization’s off-cloud environment.

When Amazon WorkSpaces is integrated with a corporate Active Directory, each WorkSpace joins the
Active Directory domain, and can be managed like any other desktop in the organization. This means that
customers can use Active Directory Group Policies to manage their Amazon WorkSpaces and can specify
configuration options that control the desktop, including those that restrict users’ abilities to use local
storage on their devices. Amazon WorkSpaces also integrates with customers’ existing RADIUS server to
enable multi-factor authentication (MFA).

Amazon WorkSpaces Secure Browser (formerly known as Amazon WorkSpaces Web)
Amazon WorkSpaces Secure Browser is an on-demand, managed service designed to facilitate secure
browser access to internal websites and software-as-a-service (SaaS) applications. Customers can access
the service from existing web browsers without infrastructure management, specialized client software,
or virtual private network (VPN) solutions.

Amazon WorkSpaces Thin Client (Effective August 15, 2024)
Amazon WorkSpaces Thin Client reduces end-user computing costs and simplifies device logistics by
shipping directly from Amazon fulfillment centers to end users or company locations. End users can set
up a device in minutes, with no IT assistance. It also helps improve security by preventing users from
storing data or loading applications on the local device and includes a simple device management service.
WorkSpaces Thin Client provides a console to centrally monitor, manage, and maintain devices and their
connectivity to AWS virtual desktop services.

AWS Amplify

AWS Amplify is a set of tools and services that can be used together or on their own, to help front-end
web and mobile developers build scalable full stack applications, powered by AWS. With Amplify,
customers can configure app backend and connect applications in minutes, deploy static web apps in a
few clicks and easily manage app content outside of AWS console. Amplify supports popular web
frameworks including JavaScript, React, Angular, Vue, Next.js, and mobile platforms including Android,
iOS, React Native, Ionic, and Flutter.

AWS App Mesh
AWS App Mesh is a service mesh that provides application-level networking which allows customer
services to communicate with each other across multiple types of compute infrastructure. App Mesh gives
customers end-to-end visibility and high availability for their applications. AWS App Mesh makes it easy


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


60


Section III – Description of the Amazon Web Services System


to run services by providing consistent visibility and network traffic controls, which helps to deliver secure
services. App Mesh removes the need to update application code to change how monitoring data is
collected or traffic is routed between services. App Mesh configures each service to export monitoring
data and implements consistent communications control logic across applications.

AWS App Runner
AWS App Runner is a service that makes it easy for developers to quickly deploy containerized web
applications and APIs, at scale and with no prior infrastructure experience required. The service provides
a simplified infrastructure-less abstraction for multi-concurrent web applications and API-based services.
With App Runner, infrastructure components like build, load balancers, certificates and application
replicas are managed by AWS. Customers simply provide their source-code (or a pre-built container
image) and get a service endpoint URL in return against which requests can be made.

AWS AppFabric
AWS AppFabric is a no-code service that connects multiple software as a service (SaaS) applications for
better security, management, and productivity. AppFabric aggregates and normalizes SaaS data (e.g., user
event logs, user access) across SaaS applications without the need to write custom data integrations.

AWS Application Migration Service
AWS Application Migration Service is the primary service that AWS recommends for lift-and-shift
applications to AWS. The service minimizes time-intensive, error-prone manual processes by
automatically converting customers’ source servers from physical, virtual, or cloud infrastructure to run
natively on AWS. Customers are able to use the same automated process to migrate a wide range of
applications to AWS without making changes to applications, their architecture, or the migrated servers.

AWS AppSync
AWS AppSync is a service that allows customers to easily develop and manage GraphQL APIs. Once
deployed, AWS AppSync automatically scales the API execution engine up and down to meet API request
volumes. AWS AppSync offers GraphQL setup, administration, and maintenance, with high availability

serverless infrastructure built in.

AWS Artifact

AWS Artifact is a self-service audit artifact retrieval portal that provides customers with on-demand access
to AWS’ compliance documentation and AWS agreements. Customers can use AWS Artifact Reports to
download AWS security and compliance documents, such as AWS ISO certifications, Payment Card
Industry (PCI), and System and Organization Control (SOC) reports. Customers can use AWS Artifact
Agreements to review, accept, and track the status of AWS agreements.

AWS Audit Manager
AWS Audit Manager helps customers continuously audit AWS usage to simplify how customers manage
risk and compliance with regulations and industry standards. AWS Audit Manager makes it easier to
evaluate whether policies, procedures, and activities—also known as controls—are operating as intended.
The service offers prebuilt frameworks with controls that are mapped to well-known industry standards
and regulations, full customization of frameworks and controls, and automated collection and
organization of evidence as designed by each control requirement.


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


61


Section III – Description of the Amazon Web Services System


AWS B2B Data Interchange (Effective February 15, 2025)
AWS B2B Data Interchange automates the transformation of business-critical EDI transactions at scale,
with elasticity and cost efficiency. B2B Data Interchange’s generative AI-assisted mapping capability
reduces the time, complexity, and cost associated with bi-directional EDI implementations, so customers
can focus on gaining valuable insight to drive meaningful business impact.

AWS Backup
AWS Backup is a backup service that makes it easy to centralize and automate the back up of data across
AWS services in the cloud as well as on premises using the AWS Storage Gateway. Using AWS Backup, the
customers can centrally configure backup policies and monitor backup activity for AWS resources, such as
Amazon EBS volumes, Amazon RDS databases, Amazon DynamoDB tables, Amazon EFS file systems, and
AWS Storage Gateway volumes. AWS Backup automates and consolidates backup tasks previously
performed service-by-service, removing the need to create custom scripts and manual processes.

AWS Batch

AWS Batch enables developers, scientists, and engineers to run batch computing jobs on AWS. AWS Batch
dynamically provisions the optimal quantity and type of compute resources (e.g., CPU or memory
optimized instances) based on the volume and specific resource requirements of the batch jobs
submitted. AWS Batch plans, schedules, and executes customers’ batch computing workloads across the
[full range of AWS compute services and features, such as Amazon EC2](https://aws.amazon.com/ec2/) [and Spot Instances.](https://aws.amazon.com/ec2/spot/)

AWS Certificate Manager (ACM)
AWS Certificate Manager (ACM) is a service that lets the customer provision, manage, and deploy public
and private Secure Sockets Layer/Transport Layer Security (SSL/TLS) certificates for use with AWS services
and their internal connected resources. SSL/TLS certificates are used to secure network communications
and establish the identity of websites over the Internet as well as resources on private networks. AWS
Certificate Manager removes the manual process of purchasing, uploading, and renewing SSL/TLS

certificates.

AWS Chatbot (Deprecated January 1, 2025)
AWS Chatbot is an AWS service that enables DevOps and software development teams to use Slack or
Amazon Chime chat rooms to monitor and respond to operational events in their AWS Cloud. AWS
Chatbot processes AWS service notifications from Amazon Simple Notification Service (Amazon SNS), and
forwards them to Slack or Amazon Chime chat rooms so teams can analyze and act on them. Teams can
respond to AWS service events from a chat room where the entire team can collaborate, regardless of

location.

AWS Clean Rooms

AWS Clean Rooms helps customers and their partners more easily and securely collaborate and analyze
their collective datasets—without sharing or copying one another’s underlying data. With AWS Clean
Rooms, customers can create a secure data clean room in minutes and collaborate with any other
company on the AWS Cloud to generate unique insights about advertising campaigns, investment
decisions, and research and development. With AWS Clean Rooms, customers can analyze data with up
to four other parties in a single collaboration. Customers can securely generate insights from multiple
companies without having to write code. Customers can create a clean room, invite companies they want
to collaborate with, and select which participants can run analyses within the collaboration.


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


62


Section III – Description of the Amazon Web Services System


AWS Cloud Map
AWS Cloud Map is a cloud resource discovery service which allows customers to define custom names for
their application resources. Cloud Map maintains the location of these changing resources to increase
application availability.

Customers can register any application resource, such as databases, queues, microservices, and other
cloud resources, with custom names. Cloud Map then constantly checks the health of resources to make
sure the location is up-to-date. The application can then query the registry for the location of the
resources needed based on the application version and deployment environment.

AWS Cloud9

AWS Cloud9 is an integrated development environment, or IDE. The AWS Cloud9 IDE offers a rich codeediting experience with support for several programming languages and runtime debuggers, and a builtin terminal. It contains a collection of tools that customers use to code, build, run, test, and debug
software, and helps customers release software to the cloud. Customers access the AWS Cloud9 IDE
through a web browser. Customers can configure the IDE to their preferences. Customers can switch color
themes, bind shortcut keys, enable programming language-specific syntax coloring and code formatting,

and more.

AWS CloudFormation

AWS CloudFormation is a service to simplify provisioning of AWS resources such as Auto Scaling groups,
ELBs, Amazon EC2, Amazon VPC, Amazon Route 53, and others. Customers author templates of the
infrastructure and applications they want to run on AWS, and the AWS CloudFormation service
automatically provisions the required AWS resources and their relationships as defined in these
templates.

AWS CloudHSM

AWS CloudHSM is a service that allows customers to use dedicated HSMs within the AWS cloud. AWS

CloudHSM is designed for applications where the use of HSMs for encryption and key storage is
mandatory.

AWS acquires these production HSM devices securely using the tamper evident authenticable (TEA) bags
from the vendors. These TEA bag serial numbers and production HSM serial numbers are verified against
data provided out-of-band by the manufacturer and logged by approved individuals in tracking systems
**(Control AWSCA-4.15)** .

AWS CloudHSM allows customers to store and use encryption keys within HSMs in AWS data centers.
With AWS CloudHSM, customers maintain full ownership, control, and access to keys and sensitive data
while Amazon manages the HSMs in close proximity to customer applications and data. All HSM media is
securely decommissioned and physically destroyed, verified by two personnel, prior to leaving AWS
control **(Control AWSCA-5.13)** .

AWS CloudShell

AWS CloudShell is a browser-based shell used to securely manage, explore, and interact with your AWS
resources. CloudShell is pre-authenticated with customer console credentials. Common development and
operations tools are pre-installed, so no local installation or configuration is required. With CloudShell,
customers can run scripts with the AWS Command Line Interface (AWS CLI), experiment with AWS service


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


63


Section III – Description of the Amazon Web Services System


APIs using the AWS SDKs, or use a range of other tools to be productive. Customers can use CloudShell
right from their browser.

AWS CloudTrail

AWS CloudTrail is a web service that records AWS activity for customers and delivers log files to a specified
Amazon S3 bucket. The recorded information includes the identity of the API caller, the time of the API
call, the source IP address of the API caller, the request parameters, and the response elements returned
by the AWS service.

AWS CloudTrail provides a history of AWS API calls for customer accounts, including API calls made via the
AWS Management Console, AWS SDKs, command line tools, and higher-level AWS services (such as AWS
CloudFormation). The AWS API call history produced by AWS CloudTrail enables security analysis, resource
change tracking, and compliance auditing.

AWS CodeBuild

AWS CodeBuild is a build service that compiles source code, runs tests, and produces software packages
that are ready to deploy. CodeBuild scales continuously and processes multiple builds concurrently, so
that customers’ builds are not left waiting in a queue. Customers can use prepackaged build environments

or can create custom build environments that use their own build tools. AWS CodeBuild eliminates the

need to set up, patch, update, and manage customers’ build servers and software.

AWS CodeCommit

AWS CodeCommit is a source control service that hosts secure Git-based repositories. It allows teams to
collaborate on code in a secure and highly scalable ecosystem. CodeCommit eliminates the need for
customers to operate their own source control system or worry about scaling their infrastructure.
CodeCommit can be used to securely store anything from source code to binaries, and it works seamlessly
with the existing Git tools.

AWS CodeDeploy
AWS CodeDeploy is a deployment service that automates software deployments to a variety of compute
services such as Amazon EC2, AWS Fargate, AWS Lambda, and the customer’s on-premises servers. AWS
CodeDeploy allows customers to rapidly release new features, helps avoid downtime during application
deployment, and handles the complexity of updating the applications.

AWS CodePipeline
AWS CodePipeline is a continuous delivery service that helps customers automate release pipelines for
fast and reliable application and infrastructure updates. CodePipeline automates the build, test, and
deploy phases of customers release process every time there is a code change, based on the release model
defined by the customer. This enables customers to rapidly and reliably deliver features and updates.
Customers can easily integrate AWS CodePipeline with third-party services such as GitHub or with their
own custom plugin.

AWS Config
AWS Config enables customers to assess, audit, and evaluate the configurations of their AWS resources.
AWS Config continuously monitors and records AWS resource configurations and allows customers to
automate the evaluation of recorded configurations against desired configurations. With AWS Config,
customers can review changes in configurations and relationships between AWS resources, dive into


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


64


Section III – Description of the Amazon Web Services System


detailed resource configuration histories, and determine overall compliance against the configurations
specified within the customers’ internal guidelines. This enables customers to simplify compliance
auditing, security analysis, change management, and operational troubleshooting.

AWS Control Tower

AWS Control Tower provides the easiest way to set up and govern a new, secure, multi-account AWS
environment based on AWS’ best practices established through AWS’ experience working with thousands
of enterprises as they move to the cloud. With AWS Control Tower, builders can provision new AWS
accounts that conform to customer policies. If customers are building a new AWS environment, starting
out on the journey to AWS, starting a new cloud initiative, or are completely new to AWS, Control Tower
will help customers get started quickly with governance and AWS’ best practices built-in.

AWS Data Exchange
AWS Data Exchange makes it easy to find, subscribe to, and use third-party data in the cloud. Qualified
data providers include category-leading brands. Once subscribed to a data product, customers can use
the AWS Data Exchange API to load data directly into Amazon S3 and then analyze it with a wide variety
of AWS analytics and machine learning services. For data providers, AWS Data Exchange makes it easy to
reach the millions of AWS customers migrating to the cloud by removing the need to build and maintain
infrastructure for data storage, delivery, billing, and entitling.

AWS Database Migration Service (DMS)
AWS Database Migration Service (DMS) is a cloud service that enables customers to migrate relational
databases, data warehouses, NoSQL databases, and other types of data stores. AWS DMS can be used to
migrate data into the AWS Cloud, between on-premises instances (through AWS Cloud setup), or between
combinations of cloud and on-premises setups. The service supports homogenous migrations within one
database platform, as well as heterogeneous migrations between different database platforms. AWS
Database Migration Service can also be used for continuous data replication with high availability.

AWS DataSync
AWS DataSync is an online data transfer service that simplifies, automates and accelerates moving data
between on-premises storage and AWS Storage services, as well as between AWS Storage services.
DataSync can copy data between Network File System (NFS), Server Message Block (SMB) file servers, selfmanaged object storage, AWS Snowcone, Amazon Simple Storage Service (Amazon S3) buckets, Amazon
EFS file systems and Amazon FSx for Windows File Server file systems. DataSync automatically handles
many of the tasks related to data transfers that can slow down migrations or burden customers’ IT
operations, including running customers own instances, handling encryption, managing scripts, network
optimization, and data integrity validation.

AWS Direct Connect

AWS Direct Connect enables customers to establish a dedicated network connection between their

network and one of the AWS Direct Connect locations. Using AWS Direct Connect, customers can establish
private connectivity between AWS and their data center, office, or colocation environment.

AWS Directory Service (excludes Simple AD)
AWS Directory Service for Microsoft Active Directory, also known as AWS Managed Microsoft Active
Directory (AD), enables customers' directory-aware workloads and AWS resources to use managed Active
Directory in the AWS Cloud. AWS Managed Microsoft AD stores directory content in encrypted Amazon


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


65


Section III – Description of the Amazon Web Services System


Elastic Block Store volumes using encryption keys. Data in transit to and from Active Directory clients is
encrypted when it travels through Lightweight Directory Access Protocol (LDAP) over customers' Amazon
Virtual Private Cloud (VPC) network. If an Active Directory client resides in an off-cloud network, the traffic
travels to customers' VPC by a virtual private network link or an AWS Direct Connect link.

AWS Elastic Beanstalk

AWS Elastic Beanstalk is an application container launch program for customers to launch and scale their
applications on top of AWS. Customers can use AWS Elastic Beanstalk to create new environments using
Elastic Beanstalk curated programs and their applications, deploy application versions, update application
configurations, rebuild environments, update AWS configurations, monitor environment health and
availability, and build on top of the scalable infrastructure provided by underlying services such as Auto
Scaling, Elastic Load Balancing, Amazon EC2, Amazon VPC, Amazon Route 53, and others.

AWS Elastic Disaster Recovery
AWS Elastic Disaster Recovery minimizes downtime and data loss with the recovery of on-premises and
cloud-based applications using affordable storage, minimal compute, and point-in-time recovery.
Customers can set up AWS Elastic Disaster Recovery on their source servers to initiate secure data
replication. Customer content is replicated to a staging area subnet in their AWS account, in the AWS
Region they select. The staging area design reduces costs by using affordable storage and minimal
compute resources to maintain ongoing replication. Customers can perform non-disruptive tests to
confirm that implementation is complete. During normal operation, customers can maintain readiness by
monitoring replication and periodically performing non-disruptive recovery and failback drills. If
customers need to recover applications, they can launch recovery instances on AWS within minutes, using
the most up-to-date server state or a previous point in time.

AWS Elemental MediaConnect

AWS Elemental MediaConnect is a high-quality transport service for live video. MediaConnect enables

customers to build mission-critical live video workflows in a fraction of the time and cost of satellite or

fiber services. Customers can use MediaConnect to ingest live video from a remote event site (like a
stadium), share video with a partner (like a cable TV distributor), or replicate a video stream for processing
(like an over-the-top service). MediaConnect combines reliable video transport, highly secure stream
sharing, and real-time network traffic and video monitoring that allow customers to focus on their
content, not their transport infrastructure.

AWS Elemental MediaConvert

AWS Elemental MediaConvert is a file-based video transcoding service with broadcast-grade features. It
allows customers to create video-on-demand (VOD) content for broadcast and multiscreen delivery at
scale. The service combines advanced video and audio capabilities with a simple web services interface.
With AWS Elemental MediaConvert, customers can focus on delivering media experiences without having
to worry about the complexity of building and operating video processing infrastructure.

AWS Elemental MediaLive

AWS Elemental MediaLive is a live video processing service. Customers can create high-quality video
streams for delivery to broadcast televisions and internet-connected multiscreen devices, like connected
TVs, tablets, smart phones, and set-top boxes. The service works by encoding live video streams in realtime, taking a larger-sized live video source and compressing it into smaller versions for distribution to


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


66


Section III – Description of the Amazon Web Services System


viewers. AWS Elemental MediaLive enables customers to focus on creating live video experiences for
viewers without the complexity of building and operating video processing infrastructure.

AWS Entity Resolution
AWS Entity Resolution is a service that helps customers match, link, and enhance their related records
stored across multiple applications, channels, and data stores. AWS Entity Resolution offers matching
techniques, such as rule-based, machine learning (ML) model-powered, and data service provider
matching to help them more accurately link related sets of customer information, product codes, or

business data codes.

AWS Fault Injection Service
AWS Fault Injection Service is a fully managed service for running fault injection experiments to improve
an application’s performance, observability, and resiliency. FIS simplifies the process of setting up and
running controlled fault injection experiments across a range of AWS services, so teams can build
confidence in their application behavior.

AWS Firewall Manager
AWS Firewall Manager is a security management service that makes it easier to centrally configure and
manage AWS WAF rules across customer accounts and applications. Using Firewall Manager, customers
can roll out AWS WAF rules for their Application Load Balancers and Amazon CloudFront distributions
across accounts in AWS Organizations. As new applications are created, Firewall Manager also allows
customers to bring new applications and resources into compliance with a common set of security rules
from day one.

AWS Global Accelerator

AWS Global Accelerator is a networking service that improves the availability and performance of the
applications that customers offer to their global users. AWS Global Accelerator also makes it easier to
manage customers’ global applications by providing static IP addresses that act as a fixed entry point to
customer applications hosted on AWS which eliminates the complexity of managing specific IP addresses
for different AWS Regions and AZs.

AWS Glue

AWS Glue is an extract, transform, and load (ETL) service that makes it easy for customers to prepare and
load their data for analytics. The customers can create and run an ETL job with a few clicks in the AWS
Management Console.

AWS Glue DataBrew

AWS Glue DataBrew is a visual data preparation tool that makes it easy for data analysts and data
scientists to clean and normalize data to prepare it for analytics and machine learning. Customers can
choose from pre-built transformations to automate data preparation tasks, all without the need to write
any code.

AWS Health Dashboard

AWS Health Dashboard provides alerts and remediation guidance when AWS is experiencing events that
may impact customers. While the AWS Health Dashboard displays the general status of AWS services,
AWS Health Dashboard gives customers a personalized view into the performance and availability of the
AWS services underlying customer’s AWS resources.


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


67


Section III – Description of the Amazon Web Services System


The dashboard displays relevant and timely information to help customers manage events in progress and
provides proactive notification to help customers plan for scheduled activities. With AWS Health
Dashboard, alerts are triggered by changes in the health of AWS resources, giving event visibility, and
guidance to help quickly diagnose and resolve issues.

AWS HealthImaging
AWS HealthImaging is a service that helps healthcare and life science organizations and their software
partners to store, analyze, and share medical imaging data at petabyte scale. With HealthImaging,
customers can reduce the total cost of ownership (TCO) of their medical imaging applications up to 40%
by running their medical imaging applications from a single copy of patient imaging data in the cloud. With
sub-second image retrieval latencies for active and archive data, customers can realize the cost savings of
the cloud without sacrificing performance at the point-of-care. HealthImaging removes the burden of
managing infrastructure for customer imaging workflows so that they can focus on delivering quality
patient care.

AWS HealthLake

AWS HealthLake is a service offering healthcare and life sciences companies a complete view of individual
or patient population health data for query and analytics at scale. Using the HealthLake APIs, health
organizations can easily copy health data, such as imaging medical reports or patient notes, from onpremises systems to a secure data lake in the cloud. HealthLake uses machine learning (ML) models to
automatically understand and extract meaningful medical information from the raw data, such as
medications, procedures, and diagnoses. HealthLake organizes and indexes information and stores it in
the Fast Healthcare Interoperability Resources (FHIR) industry standard format to provide a complete view
of each patient's medical history.

AWS HealthOmics

AWS HealthOmics helps Healthcare and Life Sciences organizations process, store, and analyze genomics
and other omics data at scale. The service supports a wide range of use cases, including DNA and RNA
sequencing (genomics and transcriptomics), protein structure prediction (proteomics), and more. By
simplifying infrastructure management for customers and removing the undifferentiated heavy lifting,
HealthOmics allows customers to generate deeper insights from their omics data, improve healthcare
outcomes, and advance scientific discoveries.

HealthOmics is comprised of three service components. Omics Storage efficiently ingests raw genomic
data into the Cloud, and it uses domain-specific compression to offer attractive storage prices to
customers. It also offers customers the ability to seamlessly access their data from various compute
environments. Omics Workflows runs bioinformatics workflows at scale in a fully-managed compute
environment. It supports three common bioinformatics domain-specific workflow languages. Omics
Analytics stores genomic variant and annotation data and allows customers to efficiently query and
analyze at scale.

AWS IAM Identity Center
AWS IAM Identity Center is a cloud-based service that simplifies managing SSO access to AWS accounts
and business applications. Customers can control SSO access and user permissions across all AWS
accounts in AWS Organizations. Customers can also administer access to popular business applications
and custom applications that support Security Assertion Markup Language (SAML) 2.0. In addition, AWS


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


68


Section III – Description of the Amazon Web Services System


IAM Identity Center offers a user portal where users can find all their assigned AWS accounts, business
applications, and custom applications in one place.

AWS Identity and Access Management (IAM)
AWS Identity and Access Management is a web service that helps customers securely control access to

AWS resources for their users. Customers use IAM to control who can use their AWS resources

(authentication) and what resources they can use and in what ways (authorization). Customers can grant
other people permission to administer and use resources in their AWS account without having to share
their password or access key. Customers can grant different permissions to different people for different
resources. Customers can use IAM features to. securely give applications that run on EC2 instances the
credentials that they need in order to access other AWS resources, like S3 buckets and RDS or DynamoDB

databases.

AWS IoT Core

AWS IoT Core is a managed cloud service that lets connected devices easily and securely interact with
cloud applications and other devices. AWS IoT Core provides secure communication and data processing
across different kinds of connected devices and locations so that customers can easily build IoT
[applications such as industrial solutions and connected home solutions.](https://aws.amazon.com/iot/solutions/industrial-iot/)

AWS IoT Device Defender

AWS IoT Device Defender is a security service that allows customers to audit the configuration of their
devices, monitor connected devices to detect abnormal behavior, and mitigate security risks. It gives
customers the ability to enforce consistent security policies across their AWS IoT device fleet and respond
quickly when devices are compromised. AWS IoT Device Defender provides tools to identify security issues
and deviations from best practices. AWS IoT Device Defender can audit device fleets to ensure they adhere
to security best practices and detect abnormal behavior on devices.

AWS IoT Device Management
AWS IoT Device Management provides customers with the ability to securely onboard, organize, and
remotely manage IoT devices at scale. With AWS IoT Device Management, customers can register their
connected devices individually or in bulk and manage permissions so that devices remain secure.

Customers can also organize their devices, monitor and troubleshoot device functionality, query the state
of any IoT device in the fleet, and send firmware updates over-the-air (OTA). AWS IoT Device Management
is agnostic to device type and OS, so customers can manage devices from constrained microcontrollers to
connected cars all with the same service. AWS IoT Device Management allows customers to scale their
fleets and reduce the cost and effort of managing large and diverse IoT device deployments.

AWS IoT Events

AWS IoT Events is a service that detects events across thousands of IoT sensors sending different
telemetry data, such as temperature from a freezer, humidity from respiratory equipment, and belt speed
on a motor. Customers can select the relevant data sources to ingest, define the logic for each event using
simple ‘if-then-else’ statements, and select the alert or custom action to trigger when an event occurs.
IoT Events continuously monitors data from multiple IoT sensors and applications, and it integrates with
other services, such as AWS IoT Core, to enable early detection and unique insights into events. IoT Events
automatically triggers alerts and actions in response to events based on the logic defined to resolve issues
quickly, reduce maintenance costs, and increase operational efficiency.


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


69


Section III – Description of the Amazon Web Services System


AWS IoT Greengrass
AWS IoT Greengrass seamlessly extends AWS to edge devices so they can act locally on the data they
generate, while still using the cloud for management, analytics, and durable storage. With AWS IoT
Greengrass, connected devices can run AWS Lambda functions, execute predictions based on machine
learning models, keep device data in sync, and communicate with other devices securely – even when not

connected to the Internet.

AWS IoT SiteWise

AWS IoT SiteWise is a service that enables industrial enterprises to collect, store, organize, and visualize
thousands of sensor data streams across multiple industrial facilities. AWS IoT SiteWise includes software
that runs on a gateway device that sits onsite in a facility, continuously collects the data from a historian
or a specialized industrial server and sends it to the AWS Cloud. With the service, customers can skip
months of developing undifferentiated data collection and cataloging solutions and focus on using their
data to detect and fix equipment issues, spot inefficiencies, and improve production output.

AWS IoT TwinMaker

AWS IoT TwinMaker makes it easier for developers to create digital twins of real-world systems such as
buildings, factories, industrial equipment, and production lines. AWS IoT TwinMaker provides the tools
customers need to build digital twins to help them optimize building operations, increase production
output, and improve equipment performance. With the ability to use existing data from multiple sources,
create virtual representations of any physical environment, and combine existing 3D models with realworld data, customers can now harness digital twins to create a holistic view of their operations faster

and with less effort.

AWS Key Management Service (KMS)
AWS Key Management Service (KMS) allows users to create and manage cryptographic keys. One class of
keys, KMS keys, are designed to never be exposed in plaintext outside the service. KMS keys can be used
to encrypt data directly submitted to the service. KMS keys can also be used to protect other types of
keys, data keys which are created by the service and returned to the user’s application for local use. AWS
KMS only creates and returns data keys to users; the service does not store or manage data keys.

AWS KMS is integrated with several AWS services so that users can request that resources in those
services are encrypted with unique data keys provisioned by KMS that are protected by a KMS key the
user chooses at the time the resource is created **(Control AWSCA-4.6).** See in-scope services integrated
[with KMS at https://aws.amazon.com/kms/. Integrated services use the data keys from AWS KMS. Data](https://aws.amazon.com/kms/)
keys provisioned by AWS KMS are encrypted with a 256-bit key unique to the customer’s account under
a defined mode of AES – Advanced Encryption Standard **(Control AWSCA-4.7)** .

When a customer requests AWS KMS to create a KMS key, the service creates a key ID for the KMS key
and key material, referred to as a backing key, which is tied to the key ID of the KMS key. The 256-bit
backing key can only be used for encrypt or decrypt operations by the service **(Control AWSCA-4.10).** KMS
will generate an associated key ID if a customer chooses to import their own key. If the customer chooses
to enable key rotation for a KMS key with a backing key that the service generated, AWS KMS will create
a new version of the backing key for each rotation event, but the key ID remains the same **(Control**
**AWSCA-4.11).** All future encrypt operations under the key ID will use the newest backing key, while all
previous versions of backing keys are retained to decrypt ciphertexts created under the previous version


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


70


Section III – Description of the Amazon Web Services System


of the key. Backing keys and customer-imported keys are encrypted under AWS-controlled keys when
created/imported and they are only ever stored on disk in encrypted form.

All requests to AWS KMS APIs are logged and available in the AWS CloudTrail of the requester and the
owner of the key. The logged requests provide information about who made the request, under which
KMS key, and describes information about the AWS resource that was protected through the use of the
KMS key. These log events are visible to the customer after turning on AWS CloudTrail in their account
**(Control AWSCA-4.8).**

AWS KMS creates and manages multiple distributed replicas of KMS keys and key metadata automatically
to enable high availability and data durability. KMS keys themselves are regional objects; KMS keys can
only be used in the AWS region in which they were created. KMS keys are only stored on persistent disk
in encrypted form and in two separate storage systems to ensure durability. When a KMS key is needed
to fulfill an authorized customer request, it is retrieved from storage, decrypted on one of many AWS KMS
hardened security modules (HSMs) in the region, then used only in memory to execute the cryptographic
operation (e.g., encrypt or decrypt). Future requests to use the KMS key each require the decryption of
the KMS key in memory for another one-time use.

AWS KMS endpoints are only accessible via TLS using the following cipher suites that support forward
secrecy **(Control AWSCA-4.9)** :


  - TLS_AES_128_GCM_SHA256

  - TLS_AES_256_GCM_SHA384

  - TLS_CHACHA20_POLY1305_SHA256

  - ECDHE-RSA-AES256-GCM-SHA384

  - ECDHE-RSA-AES128-GCM-SHA256

  - ECDHE-RSA-AES256-SHA384

  - ECDHE-RSA-AES256-SHA

  - ECDHE-RSA-AES128-SHA256

  - DHE-RSA-AES256-SHA256

  - DHE-RSA-AES128-SHA256

  - DHE-RSA-AES256-SHA

  - DHE-RSA-AES128-SHA

  - PQ-TLS-1-2-2023-11-29

By design, no one can gain access to KMS key material. KMS keys are only ever present on hardened
security modules for the amount of time needed to perform cryptographic operations under them. AWS
employees have no tools to retrieve KMS keys from these hardened security modules. In addition, multiparty access controls are enforced for operations on these hardened security modules that involve
changing the software configuration or introducing new hardened security modules into the service.
These multi-party access controls minimize the possibility of an unauthorized change to the hardened
security modules, exposing key material outside the service, or allowing unauthorized use of customer
keys **(Control AWSCA-4.5).** Additionally, key material used for disaster recovery processes by KMS are
physically secured such that no AWS employee can gain access **(Control AWSCA-4.12).** Access attempts
to recovery key materials are reviewed by authorized operators on a periodic basis **(Control AWSCA-4.13).**


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


71


Section III – Description of the Amazon Web Services System


Roles and responsibilities for those cryptographic custodians with access to systems that store or use key
material are formally documented and acknowledged **(Control AWSCA-1.6).**

AWS Lake Formation

AWS Lake Formation is an integrated data lake service that makes it easy for customers to ingest, clean,
catalog, transform, and secure their data and make it available for analysis and ML. AWS Lake Formation
gives customers a central console where they can discover data sources, set up transformation jobs to
move data to an Amazon Simple Storage Service (S3) data lake, remove duplicates and match records,
catalog data for access by analytic tools, configure data access and security policies, and audit and control
access from AWS analytic and ML services. Lake Formation automatically manages access to the registered
data in Amazon S3 through services including AWS Glue, Amazon Athena, Amazon Redshift, Amazon
QuickSight, and Amazon EMR to ensure compliance with customer defined policies. With AWS Lake
Formation, customers can configure and manage their data lake without manually integrating multiple
underlying AWS services.

AWS Lambda

AWS Lambda lets customers run code without provisioning or managing servers on their own. AWS
Lambda uses a compute fleet of Amazon Elastic Compute Cloud (Amazon EC2) instances across multiple
AZs in a region, which provides the high availability, security, performance, and scalability of the AWS

infrastructure.

AWS License Manager
AWS License Manager makes it easier to manage licenses in AWS and on-premises servers from software
vendors. AWS License Manager allows customer’s administrators to create customized licensing rules that
emulate the terms of their licensing agreements, and then enforces these rules when an instance of EC2
gets launched. Customer administrators can use these rules to limit licensing violations, such as using
more licenses than an agreement stipulates or reassigning licenses to different servers on a short-term
basis. The rules in AWS License Manager also enable customers to limit a licensing breach by stopping the
instance from launching or by notifying the customer administrators about the infringement. Customer
administrators gain control and visibility of all their licenses with the AWS License Manager dashboard
and reduce the risk of non-compliance, misreporting, and additional costs due to licensing overages.

AWS License Manager integrates with AWS services to simplify the management of licenses across
multiple AWS accounts, IT catalogs, and on-premises, through a single AWS account.

AWS Mainframe Modernization

AWS Mainframe Modernization is an elastic mainframe service and set of development tools for migrating
and modernizing mainframe and legacy workloads. Using Mainframe Modernization, system integrators
can help discover their mainframe and legacy workloads, assess and analyze migration readiness, and plan
migration and modernization projects. Once planning is complete, customers can use the Mainframe
Modernization built-in development tools to replatform or refactor their mainframe and legacy
workloads, test workload performance and functionality, and migrate their data to AWS.


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


72


Section III – Description of the Amazon Web Services System


AWS Managed Services
AWS Managed Services provides ongoing management of a customer’s AWS infrastructure. AWS
Managed Services automates common activities such as change requests, monitoring, patch
management, security, and backup services, and provides full-lifecycle services to provision, run, and
support a customer’s infrastructure.

AWS Network Firewall

AWS Network Firewall is a stateful, managed, network firewall and intrusion detection and prevention
service for customer virtual private cloud (VPC). With Network Firewall, customers can filter traffic at the
perimeter of customer VPC. This includes filtering traffic going to and coming from an internet gateway,
NAT gateway, or over VPN or AWS Direct Connect.

AWS OpsWorks (includes Chef Automate, Puppet Enterprise)
AWS OpsWorks for Chef Automate is a configuration management service that hosts Chef Automate, a
suite of automation tools from Chef for configuration management, compliance and security, and
continuous deployment. OpsWorks also maintains customers’ Chef server by automatically patching,
updating, and backing up customer servers. OpsWorks eliminates the need for customers to operate their
own configuration management systems or worry about maintaining its infrastructure. OpsWorks gives
customers access to all of the Chef Automate features, such as configuration and compliance
management, which customers manage through the Chef console or command line tools like Knife. It also
works seamlessly with customers’ existing Chef cookbooks.

AWS OpsWorks for Puppet Enterprise is a configuration management service that hosts Puppet
Enterprise, a set of automation tools from Puppet for infrastructure and application management.
OpsWorks also maintains customers’ Puppet master server by automatically patching, updating, and
backing up customers’ servers. OpsWorks eliminates the need for customers to operate their own
configuration management systems or worry about maintaining its infrastructure. OpsWorks gives
customers’ access to all of the Puppet Enterprise features, which customers manage through the Puppet
console. It also works seamlessly with customers’ existing Puppet code.

AWS OpsWorks Stacks
AWS OpsWorks Stacks is an application and server management service. OpsWorks Stacks lets customers
manage applications and servers on AWS and on-premises. With OpsWorks Stacks, customers can model
their application as a stack containing different layers, such as load balancing, database, and application
server. They can deploy and configure Amazon EC2 instances in each layer or connect other resources
such as Amazon RDS databases. OpsWorks Stacks also lets customers set automatic scaling for their
servers based on preset schedules or in response to changing traffic levels, and it uses lifecycle hooks to
orchestrate changes as their environment scales.

AWS Organizations
AWS Organizations helps customers centrally govern their environment as customers grow and scale their
workloads on AWS. Whether customers are a growing startup or a large enterprise, Organizations helps
customers to centrally manage billing; control access, compliance, and security; and share resources

across customer AWS accounts.

Using AWS Organizations, customers can automate account creation, create groups of accounts to reflect
their business needs, and apply policies for these groups for governance. Customers can also simplify


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


73


Section III – Description of the Amazon Web Services System


billing by setting up a single payment method for all of their AWS accounts. Through integrations with
other AWS services, customers can use Organizations to define central configurations and resource
sharing across accounts in their organization.

AWS Outposts
AWS Outposts is a service that extends AWS infrastructure, AWS services, APIs and tools to any data
center, co-location space, or an on-premises facility for a consistent hybrid experience. AWS Outposts is
ideal for workloads that require low latency access to on-premises systems, local data processing or local
data storage. Outposts offer the same AWS hardware infrastructure, services, APIs and tools to build and
run applications on premises and in the cloud. AWS compute, storage, database and other services run
locally on Outposts and customers can access the full range of AWS services available in the Region to
build, manage and scale on-premises applications. Service Link is established between Outposts and the
AWS region by use of a secured VPN connection over the public internet or AWS Direct Connect **(Control**
**AWSCA-3.17)** .

AWS Outposts are configured with a Nitro Security Key (NSK) which is designed to encrypt customer
content and give customers the ability to mechanically remove content from the device. Customer
content is cryptographically shredded if a customer removes the NSK from an Outposts device **(Control**
**AWSCA-7.9)** .

Additional information about Security in AWS Outposts, including the shared responsibility model, can be
[found in the AWS Outposts User Guide.](https://docs.aws.amazon.com/outposts/latest/userguide/security.html)

AWS Payment Cryptography
AWS Payment Cryptography is a managed service that can be used to replace the payments-specific
cryptography and key management functions that are usually provided by on-premises payment
hardware security modules (HSMs). This elastic, pay-as-you-go AWS API service allows credit, debit, and
payment processing applications to move to the cloud without the need for dedicated payment HSMs.

AWS Private Certificate Authority
AWS Private Certificate Authority (CA) is a managed private CA service enables customers to easily and
securely manage the lifecycle of their private certificates. Private CA allows developers to be more agile
by providing them APIs to create and deploy private certificates programmatically. Customers also have
the flexibility to create private certificates for applications that require custom certificate lifetimes or
resource names. With Private CA, customers can create and manage private certificates for their
connected resources in one place with a secure, pay as you go, managed private CA service.

AWS Resilience Hub

AWS Resilience Hub helps customers improve the resiliency of their applications and reduce applicationrelated outages by uncovering resiliency weaknesses through continuous resiliency assessment and
validation. AWS Resilience Hub can also provide Standard Operating Procedures (SOPs) to help recover
applications on AWS when experiencing unplanned disruptions caused by software, deployment, or
operational problems. The service is designed for cloud-native applications that use highly available, fault
tolerant AWS services as building blocks.


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


74


Section III – Description of the Amazon Web Services System


AWS Resource Access Manager (RAM)

AWS Resource Access Manager helps customers securely share their resources across AWS accounts,
within their organization or organizational units (OUs) in AWS Organizations, and with IAM roles and IAM
users for supported resource types. Customers are able to use AWS Resource Access Manager to share
transit gateways, subnets, AWS License Manager license configurations, Amazon Route 53 Resolver rules,
and more resource types.

AWS Resource Explorer (Effective February 15, 2025)
AWS Resource Explorer quickly and easily searches and discovers AWS resources across AWS Regions and
accounts. Customers can start their search in Unified Search in the AWS Management Console, the AWS
Resource Explorer console, the AWS Command Line Interface (AWS CLI), or the SDK - and filter using tags,
services, and other metadata.

AWS Resource Groups
AWS Resource Groups is a service that helps customers organize AWS resources into logical groupings.
These groups can represent an application, a software component, or an environment. Resource groups
can include more than fifty additional resource types, bringing the overall number of supported resource
types to seventy-seven. Some of these new resource types include Amazon DynamoDB tables, AWS
Lambda functions, AWS CloudTrail trails, and many more. Customers can now create resource groups that
accurately reflect their applications, and take action against those groups, rather than against individual

resources.

AWS RoboMaker

AWS RoboMaker is a service that makes it easy to develop, test, and deploy intelligent robotics
applications at scale. RoboMaker extends the most widely used open-source robotics software
framework, Robot Operating System (ROS), with connectivity to cloud services. This includes AWS
machine learning services, monitoring services, and analytics services that enable a robot to stream data,
navigate, communicate, comprehend, and learn. RoboMaker provides a robotics development
environment for application development, a robotics simulation service to accelerate application testing,
and a robotics fleet management service for remote application deployment, update, and management.

AWS Secrets Manager
AWS Secrets Manager helps customers protect secrets needed to access their applications, services, and

IT resources. The service enables customers to easily rotate, manage, and retrieve database credentials,

API keys, and other secrets throughout their lifecycle. Users and applications retrieve secrets with a call

to Secrets Manager APIs, eliminating the need to hardcode sensitive information in plain text. Secrets

Manager offers secret rotation with built-in integration for Amazon RDS, Amazon Redshift, and Amazon

DocumentDB. The service is also extensible to other types of secrets, including API keys and OAuth tokens.

In addition, Secrets Manager allows customers to control access to secrets using fine-grained permissions

and audit secret rotation centrally for resources in the AWS Cloud, third-party services, and on-premises.

AWS Security Hub

AWS Security Hub gives customers a comprehensive view of their high-priority security alerts and
compliance status across AWS accounts. There are a range of powerful security tools at customers’
disposal, from firewalls and endpoint protection to vulnerability and compliance scanners. With Security
Hub, customers can now have a single place that aggregates, organizes, and prioritizes their security


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


75


Section III – Description of the Amazon Web Services System


alerts, or findings, from multiple AWS services, such as Amazon GuardDuty, Amazon Inspector Classic, and
Amazon Macie, as well as from AWS Partner solutions. Findings are visually summarized on integrated
dashboards with actionable graphs and tables.

AWS Serverless Application Repository
The AWS Serverless Application Repository is a managed repository for serverless applications. It enables
teams, organizations, and individual developers to store and share reusable applications, and easily
assemble and deploy serverless architectures in powerful new ways. Using the Serverless Application
Repository, customers do not need to clone, build, package, or publish source code to AWS before
deploying it. Instead, customers can use pre-built applications from the Serverless Application Repository
in their serverless architectures, helping customers reduce duplicated work, ensure organizational best
practices, and get to market faster. Integration with AWS Identity and Access Management (IAM) provides
resource-level control of each application, enabling customers to publicly share applications with
everyone or privately share them with specific AWS accounts.

AWS Service Catalog
AWS Service Catalog allows customers to create and manage catalogs of IT services that are approved for
use on AWS. These IT services can include everything from virtual machine images, servers, software, and
databases to complete multi-tier application architectures. AWS Service Catalog allows customers to
centrally manage commonly deployed IT services, and helps customers achieve consistent governance
and meet their compliance requirements, while enabling users to quickly deploy only the approved IT
services they need.

AWS Shield

AWS Shield is a managed Distributed Denial of Service (DDoS) protection service that safeguards web
applications running on AWS. AWS Shield provides always-on detection and automatic inline mitigations
that minimize application downtime and latency, so there is no need to engage AWS Support to benefit
from DDoS protection.

AWS Signer
AWS Signer is a managed code-signing service to ensure the trust and integrity of customer code.
Customers validate code against a digital signature to confirm that the code is unaltered and from a
trusted publisher. With AWS Signer, customer security administrators have a single place to define their
signing environment, including what AWS Identity and Access Management (IAM) role can sign code and
in what regions. AWS Signer manages the code-signing certificate public and private keys and enables
central management of the code-signing lifecycle.

AWS Snowball

Snowball is a petabyte-scale data transport solution that uses secure appliances to [transfer large amounts](https://aws.amazon.com/cloud-data-migration/)
[of data](https://aws.amazon.com/cloud-data-migration/) into and out of the [AWS cloud. Using Snowball addresses common challenges with large-scale data](https://aws.amazon.com/what-is-cloud-storage/)
transfers including high network costs, long transfer times, and security concerns. Transferring data with
Snowball is simple and secure.

AWS Snowball Edge (Deprecated July 1, 2024)
AWS Snowball Edge is a 100TB data transfer device with on-board storage and compute capabilities.
Customers can use Snowball Edge to move large amounts of data into and out of AWS, as a temporary
storage tier for large local datasets, or to support local workloads in remote or offline locations. Snowball


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


76


Section III – Description of the Amazon Web Services System


Edge connects to customers’ existing applications and infrastructure using standard storage interfaces,
streamlining the data transfer process and minimizing setup and integration. Snowball Edge can cluster
together to form a local storage tier and process customers’ data on-premises, helping ensure their
applications continue to run even when they are not able to access the cloud.

AWS Step Functions
AWS Step Functions is a web service that enables customers to coordinate the components of distributed
applications and microservices using visual workflows. Customers can build applications from individual
components that each perform a discrete function, or task, allowing them to scale and change applications
quickly. Step Functions provides a reliable way to coordinate components and step through the functions
of a customer’s application. Step Functions provides a graphical console to visualize the components of a
customer’s application as a series of steps. It automatically triggers and tracks each step, and retries when
there are errors, so the customer’s application executes in order and as expected, every time. Step
Functions logs the state of each step, so when things do go wrong, customers can diagnose and debug
problems quickly.

AWS Storage Gateway
The AWS Storage Gateway service connects customers’ off-cloud software appliances with cloud-based
storage. The service enables organizations to store data in AWS’ highly durable cloud storage services:

Amazon S3 and Amazon Glacier.

AWS Storage Gateway backs up data off-site to Amazon S3 in the form of Amazon EBS snapshots. AWS
Storage Gateway transfers data to AWS and stores this data in either Amazon S3 or Amazon Glacier,
depending on the use case and type of gateway used. There are three types of gateways: Tape, File, and
Volume Gateways. The Tape Gateway allows customers to store more frequently accessed data in Amazon
S3 and less frequently accessed data in Amazon Glacier.

The File Gateway allows customers to copy data to S3 and have those files appear as individual objects in
S3. Volume gateways store data directly in Amazon S3 and allow customers to snapshot their data so that
they can access previous versions of their data. These snapshots are captured as Amazon EBS Snapshots,
which are also stored in Amazon S3. Both Amazon S3 and Amazon Glacier redundantly store these
snapshots on multiple devices across multiple facilities, detecting and repairing any lost redundancy. The
Amazon EBS snapshot provides a point-in-time backup that can be restored off-cloud or on a gateway
running in Amazon EC2 or used to instantiate new Amazon EBS volumes. Data is stored within a single
region that customers specify.

AWS Systems Manager

AWS Systems Manager gives customers the visibility and control to their infrastructure on AWS. AWS
Systems Manager provides customers a unified user interface so that customers can view their
operational data from multiple AWS services, and it allows customers to automate operational tasks

across the AWS resources.

With AWS Systems manager, customers can group resources, like Amazon EC2 instances, Amazon S3
buckets, or Amazon RDS instances, by application, view operational data for monitoring and
troubleshooting, and take action on groups of resources.


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


77


Section III – Description of the Amazon Web Services System


AWS Transfer Family
AWS Transfer Family enables the transfer of files directly into and out of Amazon S3. With the support for
Secure File Transfer Protocol (SFTP)—also known as Secure Shell (SSH) File Transfer Protocol, the File
Transfer Protocol over SSL (FTPS) and the File Transfer Protocol (FTP), the AWS Transfer Family helps the
customers seamlessly migrate their file transfer workflows to AWS by integrating with existing
authentication systems and providing DNS routing with Amazon Route 53.

AWS User Notifications

AWS User Notifications enables users to centrally configure and view notifications from AWS services,
such as AWS Health events, Amazon CloudWatch alarms, or EC2 Instance state changes, in a consistent,
human-friendly format. Users can view notifications across accounts, regions, and services in a Console
Notifications Center, and configure delivery channels, like email, chat, and push notifications to the AWS
Console mobile app, where they can receive these notifications. Notifications provide URLs to direct users
to resources on the Management Console, to enable further action and remediation.

AWS Verified Access (Effective August 15, 2024)
AWS Verified Access is a service that provides the ability to secure access to applications without requiring
the use of a virtual private network (VPN). Verified Access evaluates each application request and helps
ensure that users can access each application only when they meet the specified security requirements.

AWS WAF

AWS WAF is a web application firewall that helps protect customer web applications from common web
exploits that could affect application availability, compromise security, or consume excessive resources.

Customers can use AWS WAF to create custom rules that block common attack patterns, such as SQL
injection or cross-site scripting, and rules that are designed for their specific application. New rules can be
deployed within minutes, letting customers respond quickly to changing traffic patterns. Also, AWS WAF
includes a full-featured API that customers can use to automate the creation, deployment, and
maintenance of web security rules.

AWS Wickr

AWS Wickr is an end-to-end encrypted service that helps organizations collaborate securely through oneto-one and group messaging, voice and video calling, file sharing, screen sharing, and more. AWS Wickr
encrypts messages, calls, and files with a 256-bit end-to-end encryption protocol. Only the intended
recipients and the customer organization can decrypt these communications, reducing the risk of
adversary-in-the-middle attacks.

AWS X-Ray
AWS X-Ray helps developers analyze and debug production, distributed applications, such as those built
using a microservices architecture. With X-Ray, customers or developers can understand how their
application and its underlying services are performing to identify and troubleshoot the root cause of
performance issues and errors. X-Ray provides an end-to-end view of requests as they travel through the
customers’ application and shows a map of the application’s underlying components. Customers or
developers can use X-Ray to analyze both applications in development and in production.

EC2 Image Builder
EC2 Image Builder makes it easier to automate the creation, management, and deployment of


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


78


Section III – Description of the Amazon Web Services System


customized, secure, and up-to-date “golden” server images that are pre-installed and pre-configured with
software and settings to meet specific IT standards.

Elastic Load Balancing (ELB)
Elastic Load Balancing (ELB) provides customers with a load balancer that automatically distributes
incoming application traffic across multiple Amazon EC2 instances in the cloud. It allows customers to
achieve greater levels of fault tolerance for their applications, seamlessly providing the required amount
of load balancing capacity needed to distribute application traffic.

FreeRTOS

FreeRTOS is an operating system for microcontrollers that makes small, low-power edge devices easy to
program, deploy, secure, connect, and manage. FreeRTOS extends the FreeRTOS kernel, a popular opensource operating system for microcontrollers, with software libraries that make it easy to securely connect
the small, low-power devices to AWS cloud services like AWS IoT Core or to more powerful edge devices
running AWS IoT Greengrass.

VM Import/Export
VM Import/Export is a service that enables customers to import virtual machine images from their existing

environment to Amazon EC2 instances and export them back to their on premises environment. This

offering allows customers to leverage their existing investments in the virtual machines that customers

have built to meet their IT security, configuration management, and compliance requirements by bringing

those virtual machines into Amazon EC2 as ready-to-use instances. Customers can also export imported

instances back to their off-cloud virtualization infrastructure, allowing them to deploy workloads across

their IT infrastructure.

**D.4 Secure Data Handling**

AWS provides many methods for customers to securely handle their data. There are additional methods
detailed in the Complementary User Entity Controls (CUECs) at the end of this section. AWS enables
customers to open a secure, encrypted channel to AWS servers using HTTPS (TLS/SSL).

Amazon S3 provides a mechanism that enables users to utilize MD5 checksums to validate that data sent
to AWS is bitwise identical to what is received, and that data sent by Amazon S3 is identical to what is
received by the user. When customers choose to provide their own keys for encryption and decryption of
Amazon S3 objects (S3 SSE-C), Amazon S3 does not store the encryption key provided by the customer.
Amazon S3 generates and stores a one-way salted HMAC of the customer encryption key and that salted
HMAC value is not logged **(Control AWSCA-4.4).**

Upon initial communication with an AWS-provided Windows AMI, AWS enables secure communication
by configuring Terminal Services on the instance by generating a unique self-signed X.509 server
certificate and delivering the certificate’s thumbprint to the user over a trusted channel **(Control AWSCA-**
**4.2).**

AWS further enables secure communication with Linux AMIs by configuring SSH on the instance,
generating a unique host-key and delivering the key’s fingerprint to the user over a trusted channel
**(Control AWSCA-4.1).**


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


79


Section III – Description of the Amazon Web Services System


Connections between customer applications and Amazon RDS MySQL instances can be encrypted using
TLS/SSL. Amazon RDS generates a TLS/SSL certificate for each database instance, which can be used to
establish an encrypted connection using the default MySQL client. Once an encrypted connection is
established, data transferred between the database instance and a customer’s application will be
encrypted during transfer. If customers require data to be encrypted while “at rest” in the database, the
customer application must manage the encryption and decryption of data. Additionally, customers can
set up controls to have their database instances only accept encrypted connections for specific user

accounts.

**D.5 Physical Security and Environmental Protection**

Amazon has significant experience in designing, constructing, and operating large-scale data centers. This
experience has been applied to the AWS system and infrastructure. Refer to the “Amazon Web Services
System Overview” section above for list of in-scope data centers.

Physical Security
AWS provides physical access to its data centers for approved employees and contractors who have a
legitimate business need for such privileges. Access to data centers must be approved by an authorized
individual **(Control AWSCA-5.1).** All visitors are required to present identification and are signed in and
escorted by authorized staff.

When an employee or contractor no longer requires data center access, their access is promptly revoked,
even if they continue to be an employee or contractor of Amazon or AWS. In addition, access is
automatically revoked when an employee or contractor’s record is terminated in Amazon’s HR system
**(Control AWSCA-5.2).** Cardholder access to data centers is reviewed quarterly. Cardholders marked for
removal have their access automatically revoked as part of the review **(Control AWSCA-5.3).**

Physical access is controlled both at the perimeter and at building ingress points by professional security
staff utilizing video surveillance, intrusion detection systems, and badge and pin electronic means.
Authorized staff utilize multi-factor authentication mechanisms to access data center floors **(Control**
**AWSCA-5.4**, **AWSCA-5.5**, and **AWSCA-5.6)** .

In addition to the physical security controls, physical access to data centers in the GovCloud (US) region is
restricted to employees or contractors who have been validated as a U.S. person (green card holder or
citizen as defined by the U.S. Department of State).
Amazon owns and operates many of its data centers, while others are housed in colocation spaces that
are offered by various reputable companies under contract with Amazon. The physical access and security
controls described above are also deployed by AWS at colocation spaces.

AWS Local Zones are a type of AWS infrastructure deployment managed and supported by AWS that
places AWS compute, storage, database and other select services closer to large population, industry, IT
centers or customers where no AWS Region currently exists today. With AWS Local Zones, customers can
run latency-sensitive portions of applications local to end-users and resources in a specific geography,
delivering single-digit millisecond latency for specific use cases. Dedicated Local Zones are deployed onpremises, delivered in accordance with a customer specific contract, and dedicated to that customer. The
physical security of these Dedicated Local Zones meets the established requirements set by AWS.


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


80


Section III – Description of the Amazon Web Services System


AWS offers Wavelength infrastructure in partnership with telecom providers, which is optimized for
mobile edge computing applications. Wavelength Zones are AWS infrastructure deployments that embed
AWS compute and storage services within communications service providers’ (CSP or telecom providers)
data centers at the edge of the 5G network, so application traffic from 5G devices can reach application
servers running in Wavelength Zones without leaving the telecommunications network. This avoids the
latency that would result from application traffic having to traverse multiple hops across the Internet to
reach their destination, enabling customers to take full advantage of the latency and bandwidth benefits
offered by modern 5G networks.

Contracts with third-party colocation providers include provisions to support the protection of AWS assets
and communication of incidents or events that impact Amazon assets and/or customers to AWS **(Control**
**AWSCA-5.11).** In addition, AWS provides monitoring of adherence with security and operational
standards by performing periodic reviews of colocation service providers **(Control AWSCA-5.12).** The
frequency of colocation reviews is based on a tiering that is dependent on the contracts and level of
engagement with the colocation service provider.

AWS spaces within colocation facilities are installed with AWS-operated closed circuit television (CCTV)
cameras, intrusion detection systems, and access control devices that alert AWS personnel of access and
incidents. Physical access to AWS spaces within colocation facilities is controlled by AWS and follows
standard AWS access management processes.

Redundancy
Data centers are designed to anticipate and tolerate failure while maintaining service levels. Each AWS
Region is comprised of multiple data centers. All data centers are online and serving traffic; no data center
is “cold.” In case of failure, automated processes move traffic away from the affected area. Core
applications are deployed to an N+1 standard, so that in the event of a data center failure, there is
sufficient capacity to enable traffic to be load-balanced to the remaining sites.

Fire Detection and Suppression
Automatic fire detection and suppression equipment has been installed to reduce risk. The fire detection
system utilizes smoke detection sensors in Amazon-owned data center environments (e.g., multi-point
aspirating smoke detection (MASD), point source detection), mechanical and electrical infrastructure
spaces, chiller rooms, and generator equipment rooms. These areas are protected by either wet-pipe,
double-interlocked pre-action, or gaseous sprinkler systems **(Control AWSCA-5.7).**

Power

The data center electrical power systems supporting AWS are designed to be fully redundant and
maintainable without impact to operations, 24 hours a day, and Uninterruptible Power Supply (UPS) units
provide back-up power in the event of an electrical failure for critical and essential loads in Amazon-owned
data centers and third-party colocation sites where Amazon maintains the UPS units. Amazon-owned data
centers use generators to provide back-up power for the facility **(Control AWSCA-5.9** and **AWSCA-5.10)** .

Climate and Temperature
Climate control is required to maintain a controlled operating temperature for servers and other
hardware, preventing overheating and reducing the possibility of service outages. Amazon-owned data
centers are conditioned to maintain environmental conditions at specified levels. Personnel and systems


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


81


Section III – Description of the Amazon Web Services System


monitor and control temperature and humidity at appropriate levels. This is provided at N+1 and utilizes
free cooling as primary source of cooling where it is available based on local environmental conditions
**(Control AWSCA-5.8)** .

Environment Management
In Amazon-owned data centers, AWS monitors electrical, mechanical, and life support systems and
equipment so that any issues are immediately identified. This is carried out via daily rounds and readings,
in tandem with an overview of our data centers provided via AWS’ Building Management System (BMS)
and Electrical Monitoring System (EMS). Preventative maintenance is performed to maintain the
continued operability of equipment utilizing the Enterprise Asset Management (EAM) tool and trouble
ticketing and change management system. The primary objective of this process is to provide a holistic
insight into Mechanical, Electrical, Plumbing (MEP) Assets owned by AWS infrastructure teams. This
includes providing a centralized repository for equipment, optimizing planned and unplanned
maintenance and managing data center critical spare parts.

Management of Media
When a storage device has reached the end of its useful life, AWS procedures include a decommissioning
process that is designed to prevent unauthorized access to assets. AWS uses techniques detailed in NIST
800-88 (“Guidelines for Media Sanitization”) as part of the decommissioning process. All production media
is securely decommissioned in accordance with industry-standard practices **(Control AWSCA-5.13).**
Production media is not removed from AWS control until it has been securely decommissioned.

**D.6 Change Management**

Software

AWS applies a systematic approach to managing changes so that changes to customer impacting services
are reviewed, tested, approved, and well communicated. Change management procedures/policies are
based on Amazon change management guidelines and tailored to the specifics of each AWS service
**(Control AWSCA-6.1).** These processes are documented and communicated to the necessary personnel
by service team management.

The goal of AWS’ change management process is to prevent unintended service disruptions and maintain
the integrity of service to the customer. Change details are documented in one of Amazon’s change
management or deployment tools **(Control AWSCA-6.2)** .

Prior to deployment to production environments, changes are:

  - Developed in a development environment that is segregated from the production environment
**(Control AWSCA-6.4)** .


  - Reviewed by peers for technical aspects and appropriateness **(Control AWSCA-6.5)** .


  - Tested to confirm the changes will behave as expected when applied and not adversely impact
performance **(Control AWSCA-6.3)** .


  - Approved by authorized team members to provide appropriate oversight and understanding of
business impact **(Control AWSCA-6.5)** .


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


82


Section III – Description of the Amazon Web Services System


Changes are typically pushed into production in a phased deployment starting with the lowest impact
sites. Deployments are closely monitored so impact can be evaluated. Service owners have a number of
configurable metrics that measure the health of the service’s upstream dependencies. These metrics are
closely monitored with thresholds and alarming in place (e.g., latency, availability, fatal errors, CPU
utilization, etc.). Customer information, including personal information, and customer content are not
used in test and development environments **(Control AWSCA-6.7).** Rollback procedures are documented
so that team members can revert back to the previous state if needed.

When possible, changes are scheduled during regular change windows. Emergency changes to production
systems that require deviations from standard change management procedures are associated with an
incident and are logged and approved as appropriate.

AWS performs deployment validations and change reviews to detect unauthorized changes to its
environment and tracks identified issues to resolution. AWS management reviews and tracks deployment
violations for services enrolled in the Deployment Monitoring program as part of the AWS Security
business review. For those services not enrolled in the Deployment Monitoring program, a secondary
monthly review of deployments is conducted within 60 days of the month in which they were made. If
any unauthorized changes are detected or deviates from the standard review and approval process, they
are tracked to resolution **(Control AWSCA-6.6).**

Infrastructure

AWS internally developed configuration management software is installed when new hardware is
provisioned. These tools are run on all UNIX hosts to validate that they are configured, and software is
installed in a standard manner based on host classes and updated regularly.

Only approved users with verified business needs are authorized through a permissions service may log
in to the central configuration management servers. Host configuration settings are monitored to validate
compliance with AWS security standards and automatically pushed to the host fleet **(Control AWSCA-9.4)** .

Emergency, non-routine and other configuration changes to existing AWS infrastructure are authorized,
logged, tested, approved and documented in accordance with industry norms for similar systems. Updates
to AWS infrastructure are performed in such a manner to minimize impact to the customer and their
service use. AWS communicates with customers, either via email, or through the AWS Health Dashboard
[(https://status.aws.amazon.com/) when service use may be adversely affected.](https://status.aws.amazon.com/)

**D.7 Data Integrity, Availability, Redundancy and Data Retention**

AWS seeks to maintain data integrity through all phases including transmission, storage, and processing.
Amazon S3 utilizes checksums internally to confirm the continued integrity of data in transit within the
system and at rest. Amazon S3 provides a facility for customers to send checksums along with data
transmitted to the service. The latest AWS SDKs, CLI, and the S3 console calculate these checksums
automatically. The service validates the checksum upon receipt of the data to determine that no
corruption occurred in transit. S3 currently supports the CRC64NVME, CRC32, CRC32C, SHA1, and SHA256
algorithms for integrity validation. The MD5 algorithm is also supported for customers utilizing older SDKs
that provide their own checksum for integrity of data in transit. Regardless of whether a checksum is sent
with an object to Amazon S3, the service utilizes checksums internally to confirm the continued integrity
of data in transit within the system and at rest. When disk corruption or device failure is detected, the


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


83


Section III – Description of the Amazon Web Services System


system automatically attempts to restore normal levels of object storage redundancy **(Control AWSCA-**
**7.1, AWSCA-7.2**, and **AWSCA-7.3).**

AWS services and systems hosting customer content are designed to retain customer content until the
customer removes it or the customer agreement ends **(Control AWSCA-7.8)** . Once the contractual
obligation to retain content ends, or upon a customer-initiated action to remove or delete content, AWS
services have processes and procedures to detect a deletion and make the content inaccessible. AWS
utilizes Amazon Simple Storage Service (S3), Amazon Elastic Compute Cloud (EC2), Amazon Elastic Block
Store (EBS), and Amazon DynamoDB, as the primary services for customer content storage, which
individually or in combination are also utilized by many of the other AWS services listed in the System
Overview for storage of customer content. Amazon S3 Glacier, Amazon Relational Database Service (RDS)
Aurora, SimpleDB, Amazon Simple Queue Service (SQS), Amazon Cloud Directory, Amazon Pinpoint and
End User Messaging, AWS Secrets Manager, Amazon Elastic File System (EFS), and Amazon CloudFront
utilize local storage to store customer content but are not utilized for content storage functionalities by
other services, similar to the primary AWS content storage services. When customers request data to be
deleted, automated processes are initiated to remove the data and render the content unreadable
**(Control AWSCA-7.7).**

Availability
The AWS Resiliency Program encompasses the processes and procedures by which AWS identifies,
responds to, and recovers from a major availability event or incident within the AWS services
environment. This program builds upon the traditional approach of addressing contingency management
which incorporates elements of business continuity and disaster recovery plans and expands this to
consider critical elements of proactive risk mitigation strategies, such as engineering physically separate
Availability Zones (AZs) and continuous infrastructure capacity planning.

AWS contingency plans and incident response playbooks are maintained and updated to reflect emerging
risks and lessons learned from past incidents. Service team response plans are tested and updated
through the due course of business, and the AWS Resiliency Plan is tested, reviewed, and approved by
senior leadership annually **(Control AWSCA-10.3)** .

AWS has identified critical system components required to maintain the availability of the system and
recover service in the event of outage. Critical system components (example: code bases) are backed up
across multiple, isolated locations known as Availability Zones. Each Availability Zone runs on its own
physically distinct, independent infrastructure, and is engineered to be highly reliable. Common points of
failure, like generators and cooling equipment, are not shared across Availability Zones. Additionally,
Availability Zones are physically separate, and designed such that even extremely uncommon disasters,
such as fires, tornados, or flooding should only affect a single Availability Zone. AWS replicates critical
system components across multiple Availability Zones, and authoritative backups are maintained and
monitored to ensure successful replication **(Control AWSCA-10.1** and **AWSCA-10.2)** .

Data Backup
AWS core storage services have the capability to be redundantly stored in multiple physical locations as
part of normal operations. Customers should enable backups of their data across AWS services.

Amazon S3 is designed to provide 99.999999999% durability and 99.99% availability of objects over a
given year. Objects are redundantly stored on multiple devices across multiple facilities in an Amazon S3


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


84


Section III – Description of the Amazon Web Services System


region. To help provide durability, Amazon S3 PUT and COPY operations synchronously store customer
content across multiple facilities before returning SUCCESS. Once stored, Amazon S3 helps maintain the
durability of the objects by detecting and repairing lost redundancy. Amazon S3 also regularly verifies the
integrity of data stored using checksums. If corruption is detected, it is repaired using redundant data. In
addition, Amazon S3 calculates checksums on all network traffic to detect corruption of data packets when
storing or retrieving data **(Control AWSCA-7.3**, **AWSCA-7.4**, and **AWSCA-7.5)** .

Amazon EBS replication is stored within the same AZ, not across multiple zones, but customers have the
ability to conduct regular snapshots to Amazon Simple Storage Service (S3) in order to provide long-term
data durability. For customers who have architected complex transactional databases using Amazon EBS,
backups to Amazon S3 can be performed through the database management system so that distributed
transactions and logs can be checkpointed. AWS does not perform backups of data that are maintained
on virtual disks attached to running instances on Amazon EC2.

Amazon RDS provides two different methods for backing up and restoring customer DB Instance(s):
automated backups and database snapshots (DB Snapshots). Turned on by default, the automated backup
feature of Amazon RDS enables point-in-time recovery for a DB Instance. Amazon RDS will back up
databases and transaction logs and store both for a user-specified retention period. This allows for
restoration of a DB Instance to any second during the defined retention period, up to the last five minutes.
The automatic backup retention period can be configured to up to 35 days. During the backup window,
storage input/output (I/O) may be suspended for a few seconds, while data is being backed up. This I/O
suspension is avoided with Multi-AZ DB deployments, since the backup is taken from the standby. DB
Snapshots are user-initiated backups of DB Instances. These full database backups will be stored by
Amazon RDS until customers explicitly delete them. Customers can create a new DB Instance from a DB
Snapshot as needed **(Control AWSCA-7.6)** .

The AWS team responsible for capacity management continuously monitors service usage to project
infrastructure needs for availability commitments and requirements. AWS maintains a capacity planning
model to assess infrastructure usage and demands at least monthly, and usually more frequently (e.g.,
weekly). In addition, the AWS capacity planning model supports the planning of future demands to acquire
and implement additional resources based upon current resources and forecasted requirements **(Control**
**AWSCA-10.4)** .

**D.8 Confidentiality**

AWS is committed to protecting the security and confidentiality of its customers’ content, defined as
“Your Content” at [https://aws.amazon.com/agreement/](https://aws.amazon.com/agreement/) **(Control AWSCA-11.3)** . AWS’ systems and
services are designed to enable authenticated AWS customers to access and manage their content. AWS
notifies customers of third-party access to a customer’s content on the third-party access page located at
[https://aws.amazon.com/compliance/third-party-access. AWS may remove a customer’s content when](https://aws.amazon.com/compliance/third-party-access)
compelled to do so by a legal order, or where there is evidence of fraud or abuse as described in the
Customer Agreement [(https://aws.amazon.com/agreement/)](https://aws.amazon.com/agreement/) and Acceptable Use Policy
[(https://aws.amazon.com/aup/). In executing the removal of a customer’s content due to the reasons](https://aws.amazon.com/aup/)
stated above, employees may render it inaccessible as the situation requires. For clarity, this capability to
render customer content inaccessible extends to encrypted content as well.


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


85


Section III – Description of the Amazon Web Services System


In the course of AWS system and software design, build, and test of product features, a customer’s
content is not used and remains in the production environment. A customer’s content is not required for
the AWS software development life cycle. When content is required for the development or test of a
service’s software, AWS service teams have tools to generate mock, random data.

AWS knows customers care about privacy and data security. That is why AWS gives customers ownership
and control over their content by design through tools that allow customers to determine where their
content is stored, secure their content in transit or at rest, and manage access to AWS services and
resources. AWS also implements technical and physical controls designed to prevent unauthorized access
to or disclosure of a customer’s content. As described in the Physical Security and Change Management
areas in Section III of this report, AWS employs a number of controls to safeguard data from within and

outside of the boundaries of environments which store a customer’s content. As a result of these

measures, access to a customer’s content is restricted to authorized parties.

AWS contingency plans and incident response playbooks have defined and tested tools and processes to
detect, mitigate, investigate, and assess security incidents. These plans and playbooks include guidelines
for responding to potential data breaches in accordance with contractual and regulatory requirements.
AWS security engineers follow a documented protocol when responding to potential data security
incidents. The protocol involves steps, which include validating the presence of customer content within
the AWS service (without actually viewing the data), determining the encryption status of a customer’s
content, and determining improper access to a customer’s content to the extent possible.

During the course of their response, the security engineers document relevant findings in internal tools
used to track the security issue. AWS Security Leadership is regularly apprised of all data security issue
investigations. In the event there are positive indicators that customer content was potentially accessed
by an unintended party, a security engineer engages AWS Security Leadership and the AWS Legal team to
review the findings. AWS Security Leadership and the Legal team review the findings and determine if a
notifiable data breach has occurred pursuant to contractual or regulatory obligations. If confirmed,
affected customers are notified in accordance with the applicable reporting requirement.

Vendors and third parties with restricted access, that engage in business with Amazon, are subject to
confidentiality commitments as part of their agreements with Amazon. Confidentiality commitments are
included in agreements with vendors and third parties with restricted access and are reviewed by AWS
and the third-party at time of contract creation or execution **(Control AWSCA-11.1).** AWS monitors the
performance of third parties through periodic reviews on a risk-based approach, which evaluate
performance against contractual obligations **(Control AWSCA-11.2).**

Internally, confidentiality requirements are communicated to employees through training and policies.
Employees are required to attend Amazon Security Awareness (ASA) training, which includes policies and
procedures related to protecting a customer’s content. Confidentiality requirements are included in the
Data Handling and Classification Policy. Policies are reviewed and updated at least annually.

AWS implements policies and controls to monitor access to resources that process or store customer
content. In addition, a Master Service Agreement (MSA) or Non-Disclosure Agreement (NDA) bind a
subcontractor to confidentiality in the unlikely event they are exposed to a customer’s content. The MSA
references both an NDA and a requirement to protect a customer’s content in the event they do not have
an NDA. AWS Legal maintains the most current MSA in a legal document portal. The portal serves as the


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


86


Section III – Description of the Amazon Web Services System


repository for contracts with the most current commitments, document owner, and date modified. A legal
review is also performed when the MSA is executed with a vendor.

Services and systems hosted by AWS are designed to retain and protect a customer’s content for the
duration of the customer agreement period, and in some cases, up to 30 days beyond termination. The
customer agreement, [https://aws.amazon.com/agreement/, specifies the terms and conditions. AWS](https://aws.amazon.com/agreement/)
services are designed to retain a customer’s content until the contractual obligation to retain a customer’s
content ends, or upon a customer-initiated action to remove or delete their content.

Once the contractual obligation to retain a customer’s content ends, or upon a customer-initiated action
to remove or delete their content, AWS services have processes and procedures to detect a deletion and
make the content inaccessible. After a delete event, automated actions act on deleted content to render
the content inaccessible **(Control AWSCA-7.7).**

**D.9 Privacy**

AWS classifies customer data into two categories: customer content and account information. AWS
defines customer content as software (including machine images), data, text, audio, video, or images that
a customer or any end user transfers to AWS for processing, storage, or hosting by AWS services in
connection with that customer's account, and any computational results that a customer or any end user
derives from the foregoing through their use of AWS services. For example, customer content includes
content that a customer or any end user stores in Amazon Simple Storage Service (S3). The terms of the
AWS Customer Agreement [(https://aws.amazon.com/agreement/)](https://aws.amazon.com/agreement/) and AWS Service Terms

                       [(https://aws.amazon.com/service](https://aws.amazon.com/service-terms/) terms/) apply to customer content.

Account information is information about a customer that a customer provides to AWS in connection with
the creation or administration of a customer account. For example, account information includes names,
usernames, phone numbers, email addresses, and billing information associated with a customer account.
Any information submitted by the customer that AWS needs in order to provide services to the customer
or in connection with the administration of customer accounts, is not in-scope for this report.

The AWS Privacy Notice is available from the AWS website at [https://aws.amazon.com/privacy/. The AWS](https://aws.amazon.com/privacy/)
Privacy Notice is reviewed by the AWS Legal team and is updated as required to reflect Amazon’s current
business practices and global regulatory requirements. The Privacy Notice describes how AWS collects
and uses a customer’s personal information in relation to AWS websites, applications, products, services,
events, and experiences. The Privacy Notice does not apply to customer content.

As part of the AWS account creation and activation process, AWS customers are informed of the AWS
Privacy Notice and are required to accept the Customer Agreement, including the terms and conditions
related to the collection, use, retention, disclosure, and disposal of their data. Customers are responsible
for determining what content to store within AWS, which may include personal information. Without the
acceptance of the Customer Agreement, customers cannot sign up to use the AWS services.

The AWS Customer Agreement informs customers of the AWS data security and privacy commitments
prior to activating an AWS account and is made available to customers to review at any time on the AWS
website **(Control AWSCA-12.1)** .


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


87


Section III – Description of the Amazon Web Services System


The customer determines what data is entered into AWS services and has the ability to configure the
appropriate security and privacy settings for the data, including who can access and use the data. Further,
the customer is able to choose not to provide certain data. Additionally, the customer manages
notification or consent requirements, and maintains the accuracy of the data.

Additionally, the AWS Customer Agreement notes how AWS shares, secures, and retains customer
content. AWS also informs customers of updates to the Customer Agreement by making it available on its
website and providing the last updated date. Customers should check the Customer Agreement website
frequently for any changes to the Customer Agreement **(Control AWSCA-12.2)** .

AWS does not store any customer cardholder data obtained from customers. Rather, AWS passes the
customer cardholder data and sends it immediately to the Amazon Payments Platform, the PCI-certified
platform that Amazon uses for all payment processing. This platform returns a unique identifier that AWS
stores and uses for all future processing. The Amazon Payments Platform sits completely outside of the
AWS boundary and is run by the larger Amazon entity. It is not an AWS service, but it is utilized by the
larger Amazon entity for payment processing. As such, the Amazon payment platform is not in-scope for
this report.

AWS offers customers the ability to update their communication preferences through the AWS console
or via the AWS Email Preference Center **(Control AWSCA-12.3)** . When customers update their
communication preferences using their email, their updated preferences are saved. Customers can
unsubscribe from AWS marketing emails within the AWS console. AWS Customers will still receive
important account-related notifications from AWS, such as monthly billing statements, or if there are
significant changes to a service that customers use.

AWS provides authenticated customers the ability to access, update, and confirm their data. Denial of
access will be communicated using the AWS console **(Control** **AWSCA-12.6)** . Customers can sign into to
their AWS accounts through the AWS console to view and update their data.

AWS (or Amazon) does not disclose customer information in response to government demands unless
required to do so to comply with a legally valid and binding order. AWS Legal reviews and maintains
records of all the information requests, which lists information on the types and volume of information
requested. Unless AWS is prohibited from doing so or there is clear indication of illegal conduct in
connection with the use of Amazon products or services, AWS notifies customers before disclosing
customer content so they can seek protection from disclosure. AWS shares customer content only as
described in the AWS Customer Agreement **(Control AWSCA-12.8)** .

AWS may produce non-content and/or content information in response to valid and binding law
enforcement and governmental requests, such as subpoenas, court orders, and search warrants. “Noncontent information” means customer information such as name, address, email address, billing
information, date of account creation, and service usage information. “Content information” includes the
content that a customer transfers for processing, storage, or hosting in connection with AWS services and
any computational results. AWS records customer information requests to maintain a complete, accurate,
and timely record of such requests **(Control AWSCA-12.7)** .

If required, customers are responsible for providing notice to the individuals whose data the customer
collects and uses within AWS. AWS is not responsible for providing such notice to or obtaining consent


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


88


Section III – Description of the Amazon Web Services System


from these individuals and is only responsible for communicating its privacy commitments to AWS
customers, which is provided during the account creation and activation process.

AWS has documented an incident response policy and plan which outlines an organized approach for
responding to security breaches and incidents. The AWS Security team is responsible for monitoring
systems, tracking issues, and documenting findings of security-related events. Records are maintained for
security breaches and incidents, which include status information required for supporting forensic
activities, trend analysis, and evaluation of incident details.

As part of the process, potential breaches of customer content are investigated and escalated to AWS
Security and AWS Legal. Customers can subscribe to the AWS Security Bulletins page, which provides
information regarding identified security issues. AWS notifies affected customers and regulators of
breaches and incidents as legally required in accordance with team processes **(Control** **AWSCA-12.5)** .

AWS retains and disposes of customer content in accordance with the Customer Agreement and the AWS
Data Classification and Handling Policy. When a customer terminates their account or contract with AWS,
the account is put under isolation; after which within 90 days, customers can restore their accounts and
related content. AWS services hosting customer content are designed to retain customer content until
the contractual obligation to retain a customer’s content ends or a customer-initiated action to remove
or delete the content is taken **(Control AWSCA-7.8)** . When a customer requests data to be deleted, AWS
utilizes automated processes to detect that request and make the content inaccessible. After the deletion
is complete, automated actions are taken on deleted content to render the content unreadable **(Control**
**AWSCA-7.7)** .

AWS maintains an externally posted list of third-party sub-processors that are currently engaged by AWS
to process customer data depending on the AWS region and AWS service the customer selects at

                            [https://aws.amazon.com/compliance/sub](https://aws.amazon.com/compliance/sub-processors/) processors/. Before AWS authorizes and permits any new
third-party sub-processor to access any customer content, AWS will update the website to inform
customers **(Control AWSCA-12.12)** . AWS maintains contracts with third-party sub-processors that define
how access to customer content is limited to the minimum levels necessary to provide the service
described on the page and also contain data protection, confidentiality commitments, and security
requirements **(Control AWSCA-12.9 and 12.10).** AWS performs application security reviews for each thirdparty sub-processor provider prior to integration with AWS to ascertain and mitigate security risks
**(Control AWSCA-12.4)** . A typical security review considers privacy components, such as retention period,
use, and collection of data as applicable. The review starts with a system owner initiating a review request
to the dedicated AWS Vendor Security (AVS) team, and submitting detailed information required for the

review.

During this process, the AVS team determines the granularity of review required based on the type of
customer content that will be shared, design, threat model, and impact to AWS’ risk profile. They provide
security guidance, validate security assurance material, and meet with external parties to discuss their
penetration tests, Software Development Life Cycle, change management processes, and other operating
security controls. They work with the system owner to identify, prioritize, and remediate security findings.
The AVS team collaborates with AWS Legal as needed to validate that the content of the AVS reviews are
in-line with AWS privacy policies. The AVS team provides their final approval for the third-party system
after they have adequately assessed the risks and worked with the requester to implement security
controls to mitigate identified risks. These application security reviews are not only executed for new


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


89


Section III – Description of the Amazon Web Services System


third-party sub-processors, but also renewed on an annual basis with every third-party sub-processor
**(Control AWSCA-12.10 and AWSCA-12.11)** .


**E.** **Monitoring**

**E.1 Monitoring Activities**

AWS utilizes a wide variety of automated monitoring systems to facilitate a high level of service
performance and availability. AWS defines a Security Incident as a security-related adverse event in which
there was a loss of data confidentiality, disruption of data or systems integrity, or disruption or denial of
availability. AWS monitoring tools are implemented to detect unusual or unauthorized activities and
conditions at ingress and egress communication points. These tools monitor server and network usage,
port scanning activities, application usage, and unauthorized intrusion attempts.

Systems within AWS are further designed to monitor key operational metrics, and alarms are configured
to automatically notify operations and management personnel when early warning thresholds are
crossed. An on-call schedule is used such that personnel are always available to respond to operational
issues. This includes a pager system, so that notifications are quickly and reliably communicated to
operations personnel **(Control AWSCA-8.1)** .

Documentation is maintained to aid and inform operations personnel in handling incidents or issues. A
ticketing system is used which supports communication, progress updates, necessary collaboration
between teams, and logging capabilities. Trained call leaders facilitate communication and progress
during the handling of operational issues that require collaboration. After action reviews are convened
following significant operational issue, regardless of external impact, and Correction of Errors (COE)
documents are composed such that the root cause is captured, and preventative actions may be taken for
the future. Implementation of the preventative measures identified in COEs is tracked during weekly
operations meetings.

The AWS Security Operations team employs industry-standard diagnosis procedures (such as incident
identification, registration and verification, initial incident classification and prioritizing actions) to drive
resolution during business-impacting events. Staff operators in the US, EMEA, and APAC provide 24 x 7
continuous coverage to detect incidents and to manage the impact and resolution **(Control AWSCA-8.2)** .

**E.2 Incident Notification**

AWS has documented an incident response policy and plan which outlines an organized approach for
responding to security breaches and incidents **(Control AWSCA-1.2)** . The AWS Security team is responsible
for monitoring systems, tracking issues, and documenting findings of security-related events. Records are
maintained for security breaches and incidents, which include status information required for supporting
forensic activities, trend analysis, and evaluation of incident details.

As part of the process, potential breaches of customer content are investigated and escalated to AWS
Security and AWS Legal. Affected customers and regulators are notified of breaches and incidents where
legally required. Customers can subscribe to the AWS Security Bulletins page, which provides information
regarding identified security issues.


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


90


Section III – Description of the Amazon Web Services System


**Complementary User Entity Controls**
AWS services were designed with the assumption that certain policies, procedures, and controls are
implemented by its user entities (or customers). In certain situations, the application of specific policies,
procedures, and controls by the customer is necessary to achieve the service commitments and system
requirements that are based on the applicable trust services criteria included in this report. This section
describes the additional policies, procedures, and controls customers may need to implement in order to
satisfy the service commitments and system requirements for customers’ specific use cases.

**CC1.0 – Common Criteria Related to Control Environment**

**CC2.0 – Common Criteria Related to Communication and Information**

**CC3.0 – Common Criteria Related to Risk Assessment**

**CC4.0 – Common Criteria Related to Monitoring Activities**


  - Customers should ensure appropriate logging of events is in place to support monitoring and
incident response processes. Customers should log events that include but are not limited to
administrator activity, system errors, authentication checks, and data deletions.


  - Customers should enable and configure service-specific logging features where available for all
services and implement appropriate monitoring and incident response processes.

**CC5.0 – Common Criteria Related to Control Activities**

**CC6.0 – Common Criteria Related to Logical and Physical Access Controls**

  - Customers should use asymmetric key-pairs or multi-factor authentication to access their hosts
and avoid simple password-based authentication.


  - Customers should implement access controls, such as Security-Groups, IAM roles and/or Access
control lists (ACLs), to segment and isolate like-functioning instances.


  - S3-Specific – Customers should utilize managed rules and ACLs to secure their S3 buckets by
controlling access to the S3 buckets and preventing them being accessible to the public.


  - AppStream 2.0-Specific – Customers are responsible for managing user access to streaming
instances and should maintain controls for approving and granting access, timely removing access
when an employee leaves the organization or changes job responsibilities, and periodically
reviewing appropriate access levels for existing users.


  - Customers should utilize multi-factor authentication for controlling access to their root account
credentials and should avoid using root account credentials beyond initial account configuration
of AWS Identity and Access Management (IAM), except for Services for which IAM is not available.
Customers should delete access key(s) for the root account when not in use.


  - Outpost-Specific – Customers should restrict and monitor physical access to data centers and
facilities hosting Outpost devices to personnel based on job responsibilities.


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


91


Section III – Description of the Amazon Web Services System


  - Outpost-Specific – Customers are responsible for verifying their site meets the Outpost
requirements for facility, networking, and power as published on

                                                  [https://docs.aws.amazon.com/outposts/latest/userguide/outposts](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-requirements.html) requirements.html.


  - Outpost-Specific – Customers are responsible for removal of the Nitro Security Key (NSK) to
ensure customer content is crypto shredded from the Outpost before returning it to AWS.


  - Customers are responsible for managing and reviewing users' access to their instance of AWS
services in accordance with their access management policies.


**CC7.0 – Common Criteria Related to System Operations**


  - Customers may subscribe to Premium Support offerings that include direct communication with
the customer support team and proactive alerting to any issues that may impact the customer.


  - VPC-Specific – Customers are responsible for their network security requirements and connecting
their Amazon Virtual Private Cloud to an appropriate point of their internal network.


  - EC2-Specific – Customers are responsible for configuring the Time Sync functionality and
monitoring the synchronization for accuracy across their EC2 instances, as published by AWS in

                                                                     user guide documentation - [https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/set](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/set-time.html#configure-amazon-time-service-amazon-linux)
time.html#configure-amazon-time-service-amazon-linux.


**CC8.0 – Common Criteria Related to Change Management**


  - Customers are responsible for maintaining the application of patches to customer’s Amazon
instances. Customers can leverage automated patching tools such as AWS Systems Manager
Patch Manager to help deploy operating systems and software patches automatically across large
groups of instances.


  - Customers should set up separate development and production accounts to isolate the
production system from development work.


  - App Mesh-Specific - Customers utilizing their own Envoy image should follow a documented
change management process to ensure updated configurations are documented, tested and
approved prior to deployment to customer production instances.


**CC9.0 – Common Criteria Related to Risk Mitigation**


  - Customers should maintain policies and procedures that provide training and guidance for
information security within the organization, the IT environment, and the use of AWS services.


  - Customers should assess the objectives of their AWS cloud services network and identify the risks
and corresponding controls that need to be implemented to address those risks when using AWS
services, software, and operational controls.


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


92


Section III – Description of the Amazon Web Services System


**A – Availability Criteria**


  - EC2-Specific – Customers using the EC2 service should augment the AWS instance firewalls with
a host-based firewall for redundancy and egress filtering.


  - EC2/VPC-Specific – Data stored on Amazon EC2 virtual disks should be proactively copied to
another storage option for redundancy.


  - Customers should ensure their AWS resources such as server and database instances have the

appropriate levels of redundancy and isolation. Redundancy can be achieved through utilization
of the Multi-Region and Multi-AZ deployment option where available.


  - EBS-Specific – Amazon EBS replication is stored within the same AZ, not across multiple zones,
and therefore customers should conduct regular snapshots to Amazon S3 in order to provide longterm data durability.


  - Customers should enable backups of their data across AWS services.


**C – Confidentiality Criteria**


  - Customers should utilize Amazon S3’s option to specify an MD5 checksum as part of a REST PUT
operation for the data being sent to Amazon S3. When the request arrives at Amazon S3, an MD5
checksum will be recalculated for the object data received and compared to the provided MD5
checksum. If there is a mismatch, the PUT will be failed, preventing data that was corrupted on
the wire from being written into Amazon S3. Customers should use the MD5 checksums returned
in response to REST GET requests to confirm that the data returned by the GET was not corrupted

in transit.


  - Any code customers write to call Amazon APIs should expect to receive and handle errors from
the service. Specific guidance for each service can be found within the corresponding User Guide

and API documentation.


  - AWS Snowball-Specific – Customers should not delete any local copies of their data until they
have verified that it has been copied into AWS.


  - AWS Snowball-Specific – All data is encrypted before persisting. With AWS Snowball, there are
short periods where customer content is in plain text prior to encryption and persistence. If a
customer is concerned about this short period, they should encrypt their data before sending it

to the device.


  - Customers should transmit secret keys over secure channels. Customers should avoid embedding
secret keys in web pages or other publicly accessible source code. Customers should encrypt

sensitive data at rest as well as in transit over the network.


  - Customers should appropriately configure and manage usage and implementation of available
encryption options to meet their requirements.


  - Customers should use encrypted (TLS/SSL) connections for all of their interactions with AWS.
Leading practices include the use of TLS 1.2. Customers should opt in for a key rotation schedule
that meets their needs for any KMS key they would like rotated.


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


93


Section III – Description of the Amazon Web Services System


**P – Privacy Criteria**

**P1 – Notice and Communication**

**P2 - Choice and Consent**


  - Customers should check the Customer Agreement and Privacy Notice website frequently for any
changes.


  - Customers are responsible for updating their communication preferences.


  - Customers are responsible for managing disclosure and notice requirements for data stored in
AWS services, when applicable, because AWS is not responsible for providing notice, obtaining
consent, or having knowledge of what individuals have been provided notice or consented to.

**P3 – Collection**

**P4 – Use, Retention and Disposal**


  - Customers are responsible for complying with any regulations or laws that require a rationale of
the purposes for which personal information is collected, used, retained, and disclosed.

**P5 - Access**


  - Customers are responsible for providing individuals with their personal information, that the
customer has stored in AWS services, if required to do so by law.

**P6 - Disclosure and Notification**

**P7 - Quality**


  - Customers are responsible for keeping personal information, that the customer has stored in AWS
services, accurate, complete and relevant as required by any regulations or laws.

**P8 - Monitoring and Enforcement**

The list of control considerations presented above does not represent all the controls that should be
employed by the customer. Other controls may be required. Customers should reference additional AWS

[service documentation on the AWS website.](https://aws.amazon.com/documentation/?nc2=h_ql_d)


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


94


### **