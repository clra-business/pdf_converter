SECTION IV – Description of Criteria, AWS Controls,** **Tests, and Results of Tests**

AWS Confidential

95


Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Testing Performed and Results of Entity-Level Controls**

In planning the nature, timing and extent of testing of the controls, EY considered the aspects of AWS’
control environment and tested those controls that were considered necessary.

In addition to the tests of operating effectiveness of specific controls described below, procedures
included tests of the following components of the internal control environment of AWS:


  - Management controls and organizational structure


  - Risk assessment process


  - Information and communication


  - Control activities


  - Monitoring

Tests of the control environment included the following procedures, to the extent EY considered
necessary: (a) a review of AWS’ organizational structure, including the segregation of functional
responsibilities, policy statements, processing manuals and personnel controls, (b) discussions with
management, operations, administrative and other personnel who are responsible for developing,
ensuring adherence to and applying controls, and (c) observations of personnel in the performance of
their assigned duties.

The control environment was considered in determining the nature, timing and extent of the testing of
controls and controls relevant to the achievement of the control objectives.

**Procedures for Assessing Completeness and Accuracy of Information Provided by the Entity (IPE)**

For tests of controls requiring the use of IPE (e.g., controls requiring system-generated populations for
sample-based testing), EY performed a combination of the following procedures where possible based on
the nature of the IPE to address the completeness, accuracy, and data integrity of the data or reports
used: (1) inspect the source of the IPE, (2) inspect the query, script, or parameters used to generate the
IPE, (3) tie data between the IPE and the source, and/or (4) inspect the IPE for anomalous gaps in sequence
or timing to determine the data is complete, accurate, and maintains its integrity. In addition to the above
procedures, for tests of controls requiring management’s use of IPE in the execution of the controls (e.g.,
periodic reviews of user access listings), EY inspected management’s procedures to assess the validity of
the IPE source and the completeness, accuracy, and integrity of the data or reports.

**Trust Services Criteria and Related Controls for Systems and Applications**

On the pages that follow, the description of control objectives and the controls to achieve the objectives
have been specified by, and are the responsibility of, AWS. The “Tests Performed by EY” and the “Results
of Tests” are the responsibility of the service auditor.

Note: A comparison of AWS controls that have been revised during the examination period is provided in
Section V of this report, “Other Information Provided By Amazon Web Services” for informational

purposes.


AWS Confidential


96


Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Information System Control Environment**

The following controls apply to the services listed in the System Description and their supporting data
centers, except where controls are unique to one of the services – in those cases, the controls are
indicated as “S3-Specific,” “EC2-Specific,” “VPC-Specific,” “KMS-Specific,” “RDS-Specific,” “OutpostsSpecific,” or otherwise noted as being specific to a certain service or set of services.


**AWS Controls Mapped to the Security, Availability, Confidentiality, and Privacy Criteria**













|Criteria|Supporting AWS<br>Control Activity<br>(AWSCA)|i<br>R<br>Criteria Description|
|---|---|---|
|**CC1.0 – Common Criteria Related to Control Environment** <br>|**CC1.0 – Common Criteria Related to Control Environment** <br>|**CC1.0 – Common Criteria Related to Control Environment** <br>|
|**CC1.1**<br>|AWSCA-1.1; <br>AWSCA-1.2; <br>AWSCA-9.2; <br>AWSCA-9.3; <br>AWSCA-9.7; <br>AWSCA-9.9;<br>AWSCA-11.1; <br>AWSCA-11.2 <br>|COSO Principle 1: The entity demonstrates a commitment to integrity and<br>ethical values.<br>**4AgnI**|
|**CC1.2**<br>|AWSCA-1.7; <br>AWSCA-1.8; <br>AWSCA-9.8<br>|COSO Principle 2: The board of directors demonstrates independence from<br>management and exercises oversight of the development and performance<br>of internal control.<br>**GU**|
|**CC1.3**<br>|AWSCA-1.1; <br>AWSCA-1.2 <br>|COSO Principle 3: Management establishes, with board oversight,<br>structures, reporting lines, and appropriate authorities and responsibilities<br>in the pursuit of objectives.<br>**Fiv**|
|**CC1.4**<br>|AWSCA-1.2; <br>AWSCA-1.4; <br>AWSCA-1.7; <br>AWSCA-1.8; <br>AWSCA-9.2; <br>AWSCA-9.3;<br>AWSCA-9.9;<br>AWSCA-11.1; <br>AWSCA-11.2 <br>**ken-w**|COSO Principle 4: The entity demonstrates a commitment to attract,<br>develop, and retain competent individuals in alignment with objectives.<br>**i**|


AWS Confidential


97


Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**AWS Controls Mapped to the Security, Availability, Confidentiality, and Privacy Criteria**















|Criteria|Supporting AWS<br>Control Activity<br>(AWSCA)|x<br>k<br>Criteria Description|
|---|---|---|
|**CC1.5**<br>|AWSCA-1.1; <br>AWSCA-1.2; <br>AWSCA-1.3; <br>AWSCA-9.3; <br>AWSCA-9.7 <br>|COSO Principle 5: The entity holds individuals accountable for their internal<br>control responsibilities in the pursuit of objectives. <br>**Ri2J**|
|**CC2.0 – Common Criteria Related to Communication and Information** <br>|**CC2.0 – Common Criteria Related to Communication and Information** <br>|**CC2.0 – Common Criteria Related to Communication and Information** <br>|
|**CC2.1**<br>|AWSCA-1.2;<br>AWSCA-1.5; <br>AWSCA-1.9; <br>AWSCA-1.10;<br>AWSCA-3.6; <br>AWSCA-8.1; <br>AWSCA-8.2; <br>AWSCA-9.8<br>|COSO Principle 13: The entity obtains or generates and uses relevant,<br>quality information to support the functioning of internal control.<br>**4AgnIk**|
|**CC2.2**<br>|AWSCA-1.2;<br>AWSCA-1.4;<br>AWSCA-1.6;<br>AWSCA-1.9;<br>AWSCA-9.1; <br>AWSCA-9.5; <br>AWSCA-9.6;<br>AWSCA-10.3;<br>AWSCA-11.1; <br>AWSCA-11.3 <br>|COSO Principle 14: The entity internally communicates information,<br>including objectives and responsibilities for internal control, necessary to<br>support the functioning of internal control.<br>**i2FivGU**|
|**CC2.3**<br>**m-**|AWSCA-1.4;<br>AWSCA-1.6; <br>AWSCA-9.1; <br>AWSCA-9.5; <br>AWSCA-11.1; <br>AWSCA-11.2; <br>AWSCA-11.3; <br>AWSCA-12.1;<br>AWSCA-12.2; <br>AWSCA-12.3;<br>AWSCA-12.4; <br>AWSCA-12.5<br> <br>**token-**|COSO Principle 15: The entity communicates with external parties<br>regarding matters affecting the functioning of internal control.<br>|


AWS Confidential


98


Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**AWS Controls Mapped to the Security, Availability, Confidentiality, and Privacy Criteria**





















|Criteria|Supporting AWS<br>Control Activity<br>(AWSCA)|x<br>k<br>Criteria Description|
|---|---|---|
|**CC3.0 – Common Criteria Related to Risk Assessment**<br>|**CC3.0 – Common Criteria Related to Risk Assessment**<br>|**CC3.0 – Common Criteria Related to Risk Assessment**<br>|
|**CC3.1**<br>|AWSCA-1.5; <br>AWSCA-1.9; <br>AWSCA-1.10;<br>AWSCA-9.8<br>|COSO Principle 6: The entity specifies objectives with sufficient clarity to<br>enable the identification and assessment of risks relating to objectives.<br>**LRi2**|
|**CC3.2**<br>|AWSCA-1.5; <br>AWSCA-1.9; <br>AWSCA-1.10; <br>AWSCA-3.4; <br>AWSCA-5.12; <br>AWSCA-10.3<br> <br>|COSO Principle 7: The entity identifies risks to the achievement of its<br>objectives across the entity and analyzes risks as a basis for determining<br>how the risks should be managed.<br>**AgnIk**|
|**CC3.3**<br>|AWSCA-1.5; <br>AWSCA-1.10;<br>AWSCA-3.4; <br>AWSCA-5.12; <br>AWSCA-10.3<br>|COSO Principle 8: The entity considers the potential for fraud in assessing<br>risks to the achievement of objectives.<br>**vGU4**|
|**CC3.4**<br>|AWSCA-1.5; <br>AWSCA-1.10;<br>AWSCA-3.4; <br>AWSCA-5.12; <br>AWSCA-10.3<br>|COSO Principle 9: The entity identifies and assesses changes that could<br>significantly impact the system of internal control.<br>**i2Fi**|
|**CC4.0 – Common Criteria Related to Monitoring Activities**<br>**-**|**CC4.0 – Common Criteria Related to Monitoring Activities**<br>**-**|**CC4.0 – Common Criteria Related to Monitoring Activities**<br>**-**|
|**CC4.1**<br>|AWSCA-1.10; <br>AWSCA-3.4; <br>AWSCA-5.12; <br>AWSCA-9.8; <br>AWSCA-11.2 <br>**ken**|COSO Principle 16: The entity selects, develops, and performs ongoing<br>and/or separate evaluations to ascertain whether the components of<br>internal control are present and functioning.<br>|
|**CC4.2**<br>**m-**|AWSCA-1.5; <br>AWSCA-1.10;<br>AWSCA-9.8<br>|COSO Principle 17: The entity evaluates and communicates internal control<br>deficiencies in a timely manner to those parties responsible for taking<br>corrective action, including senior management and the board of directors,<br>as appropriate.<br>|
|**CC5.0 – Common Criteria Related to Control Activities**<br>|**CC5.0 – Common Criteria Related to Control Activities**<br>|**CC5.0 – Common Criteria Related to Control Activities**<br>|


AWS Confidential


99


Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**AWS Controls Mapped to the Security, Availability, Confidentiality, and Privacy Criteria**















|Criteria|Supporting AWS<br>Control Activity<br>(AWSCA)|x<br>k<br>Criteria Description|
|---|---|---|
|**CC5.1**<br>|AWSCA-1.2; <br>AWSCA-1.3; <br>AWSCA-1.5;<br>AWSCA-1.10 <br>|COSO Principle 10: The entity selects and develops control activities that<br>contribute to the mitigation of risks to the achievement of objectives to<br>acceptable levels.<br>**Ri2J**|
|**CC5.2**<br>|AWSCA-1.2; <br>AWSCA-1.3; <br>AWSCA-1.5; <br>AWSCA-1.10<br>|COSO Principle 11: The entity also selects and develops general control<br>activities over technology to support the achievement of objectives.<br>**IkL**|
|**CC5.3**<br>|AWSCA-1.1; <br>AWSCA-1.2; <br>AWSCA-1.3; <br>AWSCA-1.5; <br>AWSCA-1.10;<br>AWSCA-10.3 <br>|COSO Principle 12: The entity deploys control activities through policies that<br>establish what is expected and in procedures that put policies into action.<br>**4Agn**|
|**CC6.0 - Common Criteria Related to Logical and Physical Access Controls**<br>|**CC6.0 - Common Criteria Related to Logical and Physical Access Controls**<br>|**CC6.0 - Common Criteria Related to Logical and Physical Access Controls**<br>|
|**CC6.1**<br>**rm-**|AWSCA-1.2; <br>AWSCA-2.1; <br>AWSCA-2.2; <br>AWSCA-2.3; <br>AWSCA-2.4; <br>AWSCA-2.5; <br>AWSCA-2.6; <br>AWSCA-3.1; <br>AWSCA-3.2; <br>AWSCA-3.3; <br>AWSCA-3.5; <br>AWSCA-3.6; <br>AWSCA-3.7; <br>AWSCA-3.8; <br>AWSCA-3.9;<br>AWSCA-3.10; <br>AWSCA-3.11; <br>AWSCA-3.12; <br>AWSCA-3.13; <br>AWSCA-3.14; <br>AWSCA-3.15; <br>AWSCA-3.17;<br>AWSCA-3.19;<br>**token-w**|The entity implements logical access security software, infrastructure, and<br>architectures over protected information assets to protect them from<br>security events to meet the entity's objectives.<br>**i2FivG**|


AWS Confidential


100


Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**AWS Controls Mapped to the Security, Availability, Confidentiality, and Privacy Criteria**



|Criteria|Supporting AWS<br>Control Activity<br>(AWSCA)|x<br>k<br>Criteria Description|
|---|---|---|
||AWSCA-4.4; <br>AWSCA-4.5; <br>AWSCA-4.6; <br>AWSCA-4.7; <br>AWSCA-4.8; <br>AWSCA-4.9; <br>AWSCA-4.10; <br>AWSCA-4.11; <br>AWSCA-4.12; <br>AWSCA-4.13; <br>AWSCA-4.14; <br>AWSCA-4.15; <br>AWSCA-6.1; <br>AWSCA-8.1; <br>AWSCA-8.2; <br>AWSCA-9.4 <br>|**4AgnIkLRi2J**|
|**CC6.2**<br>|AWSCA-2.1; <br>AWSCA-2.2; <br>AWSCA-2.3; <br>AWSCA-2.4 <br>|Prior to issuing system credentials and granting system access, the entity<br>registers and authorizes new internal and external users whose access is<br>administered by the entity. For those users whose access is administered<br>by the entity, user system credentials are removed when user access is no<br>longer authorized.<br>**ivGU**|
|**CC6.3**<br>|AWSCA-2.1; <br>AWSCA-2.2; <br>AWSCA-2.3; <br>AWSCA-2.4; <br>AWSCA-2.5; <br>AWSCA-2.6<br>|The entity authorizes, modifies, or removes access to data, software,<br>functions, and other protected information assets based on roles,<br>responsibilities, or the system design and changes, giving consideration to<br>the concepts of least privilege and segregation of duties, to meet the<br>entity’s objectives.<br>**i2F**|
|**CC6.4**<br>**-**|AWSCA-3.16;<br>AWSCA-4.12;<br>AWSCA-4.13; <br>AWSCA-4.15; <br>AWSCA-5.1; <br>AWSCA-5.2; <br>AWSCA-5.3;<br>AWSCA-5.4; <br>AWSCA-5.5 <br>**token**|The entity restricts physical access to facilities and protected information<br>assets (for example, data center facilities, back-up media storage, and<br>other sensitive locations) to authorized personnel to meet the entity’s<br>objectives.<br>|


AWS Confidential


101








Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**AWS Controls Mapped to the Security, Availability, Confidentiality, and Privacy Criteria**



|Criteria|Supporting AWS<br>Control Activity<br>(AWSCA)|x<br>k<br>Criteria Description|
|---|---|---|
|**CC6.5**<br>|AWSCA-5.13; <br>AWSCA-7.7; <br>AWSCA-7.8; <br>AWSCA-7.9<br>|The entity discontinues logical and physical protections over physical assets<br>only after the ability to read or recover data and software from those<br>assets has been diminished and is no longer required to meet the entity’s<br>objectives.<br>**Ri2J**|
|**CC6.6**<br>|AWSCA-2.6; <br>AWSCA-3.1; <br>AWSCA-3.2; <br>AWSCA-3.3; <br>AWSCA-3.7; <br>AWSCA-3.8; <br>AWSCA-3.9; <br>AWSCA-4.14;<br>AWSCA-8.1; <br>AWSCA-8.2<br>|The entity implements logical access security measures to protect against<br>threats from sources outside its system boundaries.<br>**4AgnIkL**|
|**CC6.7**<br>**m-**|AWSCA-1.2; <br>AWSCA-1.4;<br>AWSCA-1.6; <br>AWSCA-2.2; <br>AWSCA-2.3; <br>AWSCA-3.16; <br>AWSCA-3.17; <br>AWSCA-3.18; <br>AWSCA-3.19;<br>AWSCA-4.1; <br>AWSCA-4.2; <br>AWSCA-4.3; <br>AWSCA-4.4; <br>AWSCA-4.6; <br>AWSCA-4.7; <br>AWSCA-4.9; <br>AWSCA-4.11; <br>AWSCA-4.14; <br>AWSCA-4.15; <br>AWSCA-5.1; <br>AWSCA-5.2; <br>AWSCA-5.3; <br>AWSCA-5.13; <br>AWSCA-7.1 <br>**token-w**|The entity restricts the transmission, movement, and removal of<br>information to authorized internal and external users and processes, and<br>protects it during transmission, movement, or removal to meet the entity’s<br>objectives.<br>**i2FivGU**|


AWS Confidential


102








Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**AWS Controls Mapped to the Security, Availability, Confidentiality, and Privacy Criteria**















|Criteria|Supporting AWS<br>Control Activity<br>(AWSCA)|x<br>k<br>Criteria Description|
|---|---|---|
|**CC6.8**<br>|AWSCA-2.2; <br>AWSCA-2.3; <br>AWSCA-3.4; <br>AWSCA-3.18; <br>AWSCA-6.1; <br>AWSCA-6.2; <br>AWSCA-6.3; <br>AWSCA-6.4; <br>AWSCA-6.5; <br>AWSCA-6.6; <br>AWSCA-8.1; <br>AWSCA-8.2; <br>AWSCA-9.4<br>|The entity implements controls to prevent or detect and act upon the<br>introduction of unauthorized or malicious software to meet the entity’s<br>objectives.<br>**AgnIkLRi2J**|
|**CC7.0 - Common Criteria Related to System Operations**<br>|**CC7.0 - Common Criteria Related to System Operations**<br>|**CC7.0 - Common Criteria Related to System Operations**<br>|
|**CC7.1**<br>|AWSCA-3.1; <br>AWSCA-3.2; <br>AWSCA-3.3; <br>AWSCA-3.4; <br>AWSCA-3.6; <br>AWSCA-6.6; <br>AWSCA-7.10; <br>AWSCA-9.4<br>|To meet its objectives, the entity uses detection and monitoring<br>procedures to identify (1) changes to configurations that result in the<br>introduction of new vulnerabilities, and (2) susceptibilities to newly<br>discovered vulnerabilities.<br>**FivGU**|
|**CC7.2**<br>|AWSCA-1.2; <br>AWSCA-3.4; <br>AWSCA-5.6; <br>AWSCA-8.1; <br>AWSCA-8.2; <br>AWSCA-9.6<br>**en-w**|The entity monitors system components and the operation of those<br>components for anomalies that are indicative of malicious acts, natural<br>disasters, and errors affecting the entity's ability to meet its objectives;<br>anomalies are analyzed to determine whether they represent security<br>events.<br>**i**|
|**CC7.3**<br>**rm-**|AWSCA-1.1; <br>AWSCA-5.6; <br>AWSCA-5.11;<br>AWSCA-5.12;<br>AWSCA-8.1; <br>AWSCA-8.2; <br>AWSCA-9.6; <br>AWSCA-10.3;<br>AWSCA-12.5<br>**tok**|The entity evaluates security events to determine whether they could or<br>have resulted in a failure of the entity to meet its objectives (security<br>incidents) and, if so, takes actions to prevent or address such failures.<br>|


AWS Confidential


103


Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**AWS Controls Mapped to the Security, Availability, Confidentiality, and Privacy Criteria**















|Criteria|Supporting AWS<br>Control Activity<br>(AWSCA)|x<br>k<br>Criteria Description|
|---|---|---|
|**CC7.4**<br>|AWSCA-1.1; <br>AWSCA-1.2; <br>AWSCA-3.4; <br>AWSCA-5.11; <br>AWSCA-5.12; <br>AWSCA-8.1; <br>AWSCA-8.2; <br>AWSCA-9.6; <br>AWSCA-9.7; <br>AWSCA-10.3;<br>AWSCA-12.5<br> <br>|The entity responds to identified security incidents by executing a defined<br>incident-response program to understand, contain, remediate, and<br>communicate security incidents, as appropriate.<br>**gnIkLRi2J**|
|**CC7.5**<br>|AWSCA-5.11; <br>AWSCA-5.12; <br>AWSCA-6.1; <br>AWSCA-8.2; <br>AWSCA-9.6; <br>AWSCA-10.3<br> <br>|The entity identifies, develops, and implements activities to recover from<br>identified security incidents.<br>**GU4A**|
|**CC8.0 - Common Criteria Related to Change Management** <br>|**CC8.0 - Common Criteria Related to Change Management** <br>|**CC8.0 - Common Criteria Related to Change Management** <br>|
|**CC8.1**<br>**-**|AWSCA-3.1; <br>AWSCA-3.2; <br>AWSCA-3.3; <br>AWSCA-3.6; <br>AWSCA-3.16; <br>AWSCA-6.1; <br>AWSCA-6.2; <br>AWSCA-6.3; <br>AWSCA-6.4; <br>AWSCA-6.5; <br>AWSCA-6.6; <br>AWSCA-6.7; <br>AWSCA-8.2; <br>AWSCA-9.4; <br>AWSCA-10.3;<br>AWSCA-12.4<br> <br>**token-w**|The entity authorizes, designs, develops or acquires, configures,<br>documents, tests, approves, and implements changes to infrastructure,<br>data, software, and procedures to meet its objectives.<br>**i2Fi**|
|**CC9.0 – Risk Mitigation** <br>|**CC9.0 – Risk Mitigation** <br>|**CC9.0 – Risk Mitigation** <br>|


AWS Confidential


104


Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**AWS Controls Mapped to the Security, Availability, Confidentiality, and Privacy Criteria**



|Criteria|Supporting AWS<br>Control Activity<br>(AWSCA)|x<br>k<br>Criteria Description|
|---|---|---|
|**CC9.1**<br>|AWSCA-1.2; <br>AWSCA-1.5; <br>AWSCA-1.10;<br>AWSCA-10.3<br>|The entity identifies, selects, and develops risk mitigation activities for risks<br>arising from potential business disruptions.<br>**Ri2J**|
|**CC9.2**<br>|AWSCA-1.5; <br>AWSCA-1.10;<br>AWSCA-5.11; <br>AWSCA-5.12; <br>AWSCA-9.7; <br>AWSCA-11.1; <br>AWSCA-11.2; <br>AWSCA-11.3;<br>AWSCA-12.4<br>|The entity assesses and manages risks associated with vendors and<br>business partners.<br>**AgnIkL**|


AWS Confidential


105








Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**AWS Controls Mapped to the Security, Availability, Confidentiality, and Privacy Criteria**













|Criteria|Supporting AWS<br>Control Activity<br>(AWSCA)|x<br>Criteria Description|
|---|---|---|
|**Additional Criteria for Availability** <br>|**Additional Criteria for Availability** <br>|**Additional Criteria for Availability** <br>|
|**A1.1**<br>|AWSCA-8.1; <br>AWSCA-10.3; <br>AWSCA-10.4<br>|The entity maintains, monitors, and evaluates current processing capacity<br>and use of system components (infrastructure, data, and software) to<br>manage capacity demand and to enable the implementation of additional<br>capacity to help meet its objectives.<br>**Ri2**|
|**A1.2**<br>|AWSCA-1.2; <br>AWSCA-1.5; <br>AWSCA-1.10;<br>AWSCA-5.7; <br>AWSCA-5.8; <br>AWSCA-5.9; <br>AWSCA-5.10; <br>AWSCA-5.11; <br>AWSCA-5.12; <br>AWSCA-7.3; <br>AWSCA-7.4; <br>AWSCA-7.5; <br>AWSCA-7.6; <br>AWSCA-8.1; <br>AWSCA-8.2; <br>AWSCA-10.1; <br>AWSCA-10.2; <br>AWSCA-10.3; <br>AWSCA-10.4<br>|The entity authorizes, designs, develops or acquires, implements, operates,<br>approves, maintains, and monitors environmental protections, software,<br>data backup processes, and recovery infrastructure to meet its objectives.<br>**i2FivGU4AgnIkL**|
|**A1.3**<br>|AWSCA-1.2; <br>AWSCA-10.2; <br>AWSCA-10.3 <br>**n-**|The entity tests recovery plan procedures supporting system recovery to<br>meet its objectives.<br>|


AWS Confidential


106


Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**AWS Controls Mapped to the Security, Availability, Confidentiality, and Privacy Criteria**

























|Criteria|Supporting AWS<br>Control Activity<br>(AWSCA)|x<br>Criteria Description|
|---|---|---|
|**Additional Criteria for Confidentiality** <br>|**Additional Criteria for Confidentiality** <br>|**Additional Criteria for Confidentiality** <br>|
|**C1.1**<br>|AWSCA-1.2; <br>AWSCA-7.2; <br>AWSCA-7.3; <br>AWSCA-7.4; <br>AWSCA-7.5; <br>AWSCA-7.6; <br>AWSCA-7.8;<br>AWSCA-10.2<br> <br>|The entity identifies and maintains confidential information to meet the<br>entity’s objectives related to confidentiality.<br>**nIkLRi2**|
|**C1.2**<br>|AWSCA-5.13; <br>AWSCA-7.7;<br>AWSCA-7.9 <br>|The entity disposes of confidential information to meet the entity’s<br>objectives related to confidentiality.<br>**Ag**|
|**Additional Criteria Related to Privacy** <br>|**Additional Criteria Related to Privacy** <br>|**Additional Criteria Related to Privacy** <br>|
|**P1.1**<br>|AWSCA-12.1; <br>AWSCA-12.2; <br>AWSCA-12.4 <br>|The entity provides notice to data subjects about its privacy practices to<br>meet the entity’s objectives related to privacy. The notice is updated and<br>communicated to data subjects in a timely manner for changes to the<br>entity’s privacy practices, including changes in the use of personal<br>information, to meet the entity’s objectives related to privacy.<br>**ivGU**|
|**P2.1**<br>|AWSCA-12.1; <br>AWSCA-12.3 <br>**en-w**|The entity communicates choices available regarding the collection, use,<br>retention, disclosure, and disposal of personal information to the data<br>subjects and the consequences, if any, of each choice. Explicit consent for<br>the collection, use, retention, disclosure, and disposal of personal<br>information is obtained from data subjects or other authorized persons, if<br>required. Such consent is obtained only for the intended purpose of the<br>information to meet the entity’s objectives related to privacy. The entity’s<br>basis for determining implicit consent for the collection, use, retention,<br>disclosure, and disposal of personal information is documented.<br>**i2F**|
|**P3.1**<br>|AWSCA-1.4; <br>AWSCA-3.6; <br>AWSCA-12.1; <br>AWSCA-12.4<br>**ok**|Personal information is collected consistent with the entity’s objectives<br>related to privacy.<br>|


AWS Confidential


107


Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**AWS Controls Mapped to the Security, Availability, Confidentiality, and Privacy Criteria**









|Criteria|Supporting AWS<br>Control Activity<br>(AWSCA)|x<br>Criteria Description|
|---|---|---|
|**P3.2**<br>|Not Applicable -<br>Customers<br>maintain<br>ownership of their<br>content, and<br>select which AWS<br>services can<br>process, store, and<br>host their content.<br>AWS does not<br>access or use<br>customer content<br>for any purpose<br>without explicit<br>customer consent.<br>Customers are<br>responsible for<br>complying with<br>any regulations or<br>laws around the<br>collection of<br>personal<br>information.<br>|For information requiring explicit consent, the entity communicates the<br>need for such consent as well as the consequences of a failure to provide<br>consent for the request for personal information and obtains the consent<br>prior to the collection of the information to meet the entity’s objectives<br>related to privacy.<br>**ivGU4AgnIkLRi2Jk**|
|**P4.1**<br>|AWSCA-1.2; <br>AWSCA-1.4; <br>AWSCA-3.6; <br>AWSCA-7.7; <br>AWSCA-11.2;<br>AWSCA-12.4 <br>**-w**|The entity limits the use of personal information to the purposes identified<br>in the entity’s objectives related to privacy.<br>**i2F**|
|**P4.2**<br>|AWSCA-1.2; <br>AWSCA-3.6; <br>AWSCA-7.7; <br>AWSCA-7.8; <br>AWSCA-7.9; <br>AWSCA-12.4 <br>**oken**|The entity retains personal information consistent with the entity’s<br>objectives related to privacy.<br>|


AWS Confidential


108


Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**AWS Controls Mapped to the Security, Availability, Confidentiality, and Privacy Criteria**















|Criteria|Supporting AWS<br>Control Activity<br>(AWSCA)|x<br>Criteria Description|
|---|---|---|
|**P4.3**<br>|AWSCA-1.2; <br>AWSCA-5.13; <br>AWSCA-7.7; <br>AWSCA-7.8; <br>AWSCA-7.9 <br>|The entity securely disposes of personal information to meet the entity’s<br>objectives related to privacy.<br>**Ri2Jk**|
|**P5.1**<br>|AWSCA-9.5; <br>AWSCA-12.1; <br>AWSCA-12.5;<br>AWSCA-12.6; <br>AWSCA-12.7; <br>|The entity grants identified and authenticated data subjects the ability to<br>access their stored personal information for review and, upon request,<br>provides physical or electronic copies of that information to data subjects<br>to meet the entity’s objectives related to privacy. If access is denied, data<br>subjects are informed of the denial and reason for such denial, as required,<br>to meet the entity’s objectives related to privacy.<br>**nIkL**|
|**P5.2**<br>|AWSCA-9.5; <br>AWSCA-12.1; <br>AWSCA-12.5;<br>AWSCA-12.6; <br>AWSCA-12.7<br> <br>|The entity corrects, amends, or appends personal information based on<br>information provided by data subjects and communicates such information<br>to third parties, as committed or required, to meet the entity’s objectives<br>related to privacy. If a request for correction is denied, data subjects are<br>informed of the denial and reason for such denial to meet the entity’s<br>objectives related to privacy.<br>**U4Ag**|
|**P6.1**<br>|AWSCA-11.2;<br>AWSCA-12.1; <br>AWSCA-12.4;<br>AWSCA-12.7;<br>AWSCA-12.9;<br>AWSCA-12.11 <br>|The entity discloses personal information to third parties with the explicit<br>consent of data subjects and such consent is obtained prior to disclosure to<br>meet the entity’s objectives related to privacy.<br>**FivG**|
|**P6.2**<br>|AWSCA-12.7 <br>|The entity creates and retains a complete, accurate, and timely record of<br>authorized disclosures of personal information to meet the entity’s<br>objectives related to privacy.<br>**i**|
|**P6.3**<br>|AWSCA-8.1; <br>AWSCA-8.2; <br>AWSCA-9.5; <br>AWSCA-10.3; <br>AWSCA-12.5 <br>**ken**|The entity creates and retains a complete, accurate, and timely record of<br>detected or reported unauthorized disclosures (including breaches) of<br>personal information to meet the entity’s objectives related to privacy.<br>|
|**P6.4**<br>**m-**|AWSCA-11.1; <br>AWSCA-11.2;<br>AWSCA-11.3; <br>AWSCA-12.4; <br>AWSCA-12.5<br> <br>|The entity obtains privacy commitments from vendors and other third<br>parties who have access to personal information to meet the entity’s<br>objectives related to privacy. The entity assesses those parties’ compliance<br>on a periodic and as-needed basis and takes corrective action, if necessary.<br>|


AWS Confidential


109


Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**AWS Controls Mapped to the Security, Availability, Confidentiality, and Privacy Criteria**



|Criteria|Supporting AWS<br>Control Activity<br>(AWSCA)|x<br>Criteria Description|
|---|---|---|
|**P6.5**<br>|AWSCA-8.1; <br>AWSCA-8.2; <br>AWSCA-11.1; <br>AWSCA-11.2;<br>AWSCA-11.3;<br>AWSCA-12.5 <br>|The entity obtains commitments from vendors and other third parties with<br>access to personal information to notify the entity in the event of actual or<br>suspected unauthorized disclosures of personal information. Such<br>notifications are reported to appropriate personnel and acted on in<br>accordance with established incident-response procedures to meet the<br>entity’s objectives related to privacy.<br>**Ri2Jk**|
|**P6.6**<br>|AWSCA-8.2;<br>AWSCA-12.5 <br>|The entity provides notification of breaches and incidents to affected data<br>subjects, regulators, and others to meet the entity’s objectives related to<br>privacy.<br>**IkL**|
|**P6.7**<br>|AWSCA-1.2;<br>AWSCA-8.2; <br>AWSCA-12.5; <br>AWSCA-12.7; <br>AWSCA-12.8; <br>AWSCA-12.10; <br>AWSCA-12.12 <br>|The entity provides data subjects with an accounting of the personal<br>information held and disclosure of the data subjects’ personal information,<br>upon the data subjects’ request, to meet the entity’s objectives related to<br>privacy.<br>**U4Agn**|
|**P7.1**<br>|AWSCA-1.2; <br>AWSCA-12.6 <br>|The entity collects and maintains accurate, up-to-date, complete, and<br>relevant personal information to meet the entity’s objectives related to<br>privacy.<br>**vG**|
|**P8.1**<br>|AWSCA-1.5; <br>AWSCA-8.2; <br>AWSCA-9.5;<br>AWSCA-9.7;<br>AWSCA-9.8;<br>AWSCA-12.1; <br>AWSCA-12.5 <br>**-w**|The entity implements a process for receiving, addressing, resolving, and<br>communicating the resolution of inquiries, complaints, and disputes from<br>data subjects and others and periodically monitors compliance to meet the<br>entity’s objectives related to privacy. Corrections and other necessary<br>actions related to identified deficiencies are made or taken in a timely<br>manner.<br>**i2Fi**|


AWS Confidential


110








Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**







|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|**AWSCA-1.1:** The<br>AWS organization<br>has defined<br>structures, reporting<br>lines with assigned<br>authority and<br>responsibilities to<br>appropriately meet<br>requirements<br>relevant to security,<br>availability,<br>confidentiality, and<br>privacy. <br>|CC1.1; <br>CC1.3; <br>CC1.5; <br>CC5.3; <br>CC7.3; <br>CC7.4 <br>|Inquired of an AWS IT Security Response<br>Director to ascertain the AWS organization<br>has defined structures, reporting lines with<br>assigned authority, and responsibilities to<br>appropriately meet business requirements,<br>including an information security function.<br>**R**|No deviations noted.<br>**i2J**|
|**AWSCA-1.1:** The<br>AWS organization<br>has defined<br>structures, reporting<br>lines with assigned<br>authority and<br>responsibilities to<br>appropriately meet<br>requirements<br>relevant to security,<br>availability,<br>confidentiality, and<br>privacy. <br>|CC1.1; <br>CC1.3; <br>CC1.5; <br>CC5.3; <br>CC7.3; <br>CC7.4 <br>|Inspected the organizational chart and the<br>Integrated Information Management System<br>Policy to ascertain the AWS organization has<br>defined structures, reporting lines with<br>assigned authority, and responsibilities to<br>appropriately meet security, availability,<br>confidentiality, and privacy requirements,<br>including an information security function.<br>**AgnIkL**|No deviations noted.<br>|
|**AWSCA-1.1:** The<br>AWS organization<br>has defined<br>structures, reporting<br>lines with assigned<br>authority and<br>responsibilities to<br>appropriately meet<br>requirements<br>relevant to security,<br>availability,<br>confidentiality, and<br>privacy. <br>|CC1.1; <br>CC1.3; <br>CC1.5; <br>CC5.3; <br>CC7.3; <br>CC7.4 <br>|Inspected the Integrated Information<br>Management System Policy to ascertain the<br>full document was approved within the last<br>year by Security Leadership and that any<br>changes were approved by appropriate<br>members of the Security team.<br>**vGU4**|No deviations noted.<br>|
|**AWSCA-1.2:** AWS<br>maintains formal<br>policies that provide<br>guidance for<br>information security<br>within the<br>organization and the<br>supporting IT<br>environment.<br>**en**|CC1.1; <br>CC1.3; <br>CC1.4; <br>CC1.5; <br>CC2.1; <br>CC2.2; <br>CC5.1; <br>CC5.2; <br>CC5.3; <br>**-wi2**|Inquired of an AWS Security Assurance<br>Program Manager to ascertain formal<br>security policies exist, including designation<br>of responsibility and accountability for<br>managing the system and controls, and<br>providing guidance for information security<br>within the organization and the supporting IT<br>environment.<br> <br>**Fi**|No deviations noted.<br>|


AWS Confidential


111




Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**



|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
||CC6.1; <br>CC6.7; <br>CC7.2; <br>CC7.4; <br>CC9.1; <br>P4.1; <br>P4.2; <br>P4.3; <br>P6.7; <br>P7.1; <br>A1.2; <br>A1.3; <br>C1.1 <br>|Inspected the information security policies<br>listed in the System Description and the<br>internal Amazon Policy tool to ascertain they<br>included organization-wide security<br>procedures as guidance for the AWS<br>environment and the supporting IT<br>environment.<br>**gnIkLR**|No deviations noted.<br>**i2J**|
|**AWSCA-1.3:** Security<br>policies are reviewed<br>and approved on an<br>annual basis by<br>Security Leadership. <br>|CC1.5; <br>CC5.1; <br>CC5.2; <br>CC5.3 <br>|Inquired of an AWS Security Assurance<br>Program Manager to ascertain the security<br>policies that were reviewed and approved at<br>least annually by Security Leadership.<br>**U4A**|No deviations noted.<br>|
|**AWSCA-1.3:** Security<br>policies are reviewed<br>and approved on an<br>annual basis by<br>Security Leadership. <br>|CC1.5; <br>CC5.1; <br>CC5.2; <br>CC5.3 <br>|Inspected the security policies listed in the<br>System Description and the internal Amazon<br>Policy tool to ascertain they are approved<br>within the last 12 months by reviewing the<br>approval date and Security Leadership<br>approval from the tool logs.<br>**FivG**|No deviations noted.<br>|
|**AWSCA-1.4:** AWS<br>maintains employee<br>training programs to<br>promote awareness<br>of AWS information<br>security<br>requirements as<br>defined in the AWS<br>Security Awareness<br>Training Policy. <br>**token**|CC1.4; <br>CC2.2; <br>CC2.3; <br>CC6.7; <br>P3.1; <br>P4.1 <br> <br>**-wi**|Inquired of a Technical Training Operations<br>Specialist to ascertain employee training<br>programs were established to promote<br>awareness of AWS information security and<br>data privacy requirements.<br> <br> <br> <br> <br>|No deviations noted.<br>|


AWS Confidential


112








Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**







|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|||For a sample of AWS employees selected<br>from the HR active employees and<br>contractors listing, inspected the training<br>transcript to ascertain the employees<br>completed the Amazon Security Awareness<br>(ASA) training course within 60 days of role<br>assignment and that the training course<br>included information security requirements<br>and data privacy requirements as defined in<br>the AWS Security Awareness Training Policy.<br>**IkLR**|No deviations noted.<br>**i2J**|
|**AWSCA-1.5:** AWS<br>maintains a formal<br>risk management<br>program to identify,<br>analyze, treat and<br>continuously<br>monitor and report<br>risks that affect<br>AWS’ business<br>objectives and<br>regulatory<br>requirements. The<br>program identifies<br>risks, documents<br>them in a risk<br>register as<br>appropriate, and<br>reports results to<br>leadership at least<br>semi-annually. <br>**oken**|CC2.1; <br>CC3.1; <br>CC3.2; <br>CC3.3; <br>CC3.4; <br>CC4.2; <br>CC5.1; <br>CC5.2; <br>CC5.3; <br>CC9.1; <br>CC9.2; <br>A1.2; <br>P8.1 <br>**-wi2**|Inquired of an AWS Senior Regulatory Risk<br>Manager to ascertain a formal risk<br>management program was maintained to<br>identify, analyze, treat, and continuously<br>monitor and report risks that affect AWS’<br>business objectives, regulatory requirements,<br>and customers. The program identifies risks,<br>documents them in a risk register as<br>appropriate, and reports results to leadership<br>at least semi-annually.<br>**vGU4Agn**|No deviations noted.<br>|
|**AWSCA-1.5:** AWS<br>maintains a formal<br>risk management<br>program to identify,<br>analyze, treat and<br>continuously<br>monitor and report<br>risks that affect<br>AWS’ business<br>objectives and<br>regulatory<br>requirements. The<br>program identifies<br>risks, documents<br>them in a risk<br>register as<br>appropriate, and<br>reports results to<br>leadership at least<br>semi-annually. <br>**oken**|CC2.1; <br>CC3.1; <br>CC3.2; <br>CC3.3; <br>CC3.4; <br>CC4.2; <br>CC5.1; <br>CC5.2; <br>CC5.3; <br>CC9.1; <br>CC9.2; <br>A1.2; <br>P8.1 <br>**-wi2**|Inspected the AWS Risk Management policy<br>to ascertain, it was designed to outline how<br>to identify, analyze, treat, and continuously<br>monitor and report risks that affect AWS’<br>business objectives, regulatory requirements<br>and customers, as well as detailed risk<br>treatment options such as acceptance,<br>avoidance, mitigation, and transfer.<br>**Fi**|No deviations noted.<br>|
|**AWSCA-1.5:** AWS<br>maintains a formal<br>risk management<br>program to identify,<br>analyze, treat and<br>continuously<br>monitor and report<br>risks that affect<br>AWS’ business<br>objectives and<br>regulatory<br>requirements. The<br>program identifies<br>risks, documents<br>them in a risk<br>register as<br>appropriate, and<br>reports results to<br>leadership at least<br>semi-annually. <br>**oken**|CC2.1; <br>CC3.1; <br>CC3.2; <br>CC3.3; <br>CC3.4; <br>CC4.2; <br>CC5.1; <br>CC5.2; <br>CC5.3; <br>CC9.1; <br>CC9.2; <br>A1.2; <br>P8.1 <br>**-wi2**|For a sample of risks selected from the risk<br>register, inspected relevant documentation<br>to ascertain the risk was identified, analyzed,<br>treated, and monitored by management.<br>|No deviations noted.<br>|


AWS Confidential


113




Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**







|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|**AWSCA-1.6:** KMS-<br>Specific – Roles and<br>responsibilities for<br>KMS cryptographic<br>custodians are<br>formally<br>documented and<br>agreed to by those<br>individuals when<br>they assume the role<br>or when<br>responsibilities<br>change. <br>|CC2.2;<br>CC2.3; <br>CC6.7 <br>|Inquired of a Cryptography Technical<br>Program Manager to ascertain roles and<br>responsibilities for KMS cryptographic<br>custodians were formally documented and<br>acknowledged by those individuals when<br>assumed or when responsibilities change.<br> <br>**LR**|No deviations noted.<br>**i2J**|
|**AWSCA-1.6:** KMS-<br>Specific – Roles and<br>responsibilities for<br>KMS cryptographic<br>custodians are<br>formally<br>documented and<br>agreed to by those<br>individuals when<br>they assume the role<br>or when<br>responsibilities<br>change. <br>|CC2.2;<br>CC2.3; <br>CC6.7 <br>|For a sample of individuals selected from the<br>KMS cryptographic custodians group with<br>access to systems that store or use key<br>material, inspected the roles and<br>responsibilities documents to ascertain user<br>responsibilities were formally documented<br>and that the individuals signed the<br>document.<br>**4AgnIk**|No deviations noted.<br>|
|**AWSCA-1.7**: The<br>Amazon Board and<br>its Committees have<br>the required number<br>of independent<br>Board members, and<br>the Board and each<br>Committee member<br>is qualified to serve<br>in such capacity.<br>Annually, Board<br>members complete<br>questionnaires to<br>establish whether<br>they are<br>independent and<br>qualified to serve on<br>each Board<br>Committee under<br>applicable rules. <br>**-token**|CC1.2; <br>CC1.4 <br>**-wi2**|Inquired of the Amazon Corporate Counsel to<br>ascertain the Board and its Committees had<br>the required number of independent Board<br>members, and each Board and Committee<br>member was qualified to serve in such<br>capacity.<br>**ivGU**|No deviations noted.<br>|
|**AWSCA-1.7**: The<br>Amazon Board and<br>its Committees have<br>the required number<br>of independent<br>Board members, and<br>the Board and each<br>Committee member<br>is qualified to serve<br>in such capacity.<br>Annually, Board<br>members complete<br>questionnaires to<br>establish whether<br>they are<br>independent and<br>qualified to serve on<br>each Board<br>Committee under<br>applicable rules. <br>**-token**|CC1.2; <br>CC1.4 <br>**-wi2**|Inspected Amazon’s Company Bylaws and<br>the Company’s Corporate Governance<br>guidelines to ascertain they defined the<br>number and roles of officers on the Board of<br>Directors and their responsibilities.<br>|No deviations noted.<br>|
|**AWSCA-1.7**: The<br>Amazon Board and<br>its Committees have<br>the required number<br>of independent<br>Board members, and<br>the Board and each<br>Committee member<br>is qualified to serve<br>in such capacity.<br>Annually, Board<br>members complete<br>questionnaires to<br>establish whether<br>they are<br>independent and<br>qualified to serve on<br>each Board<br>Committee under<br>applicable rules. <br>**-token**|CC1.2; <br>CC1.4 <br>**-wi2**|Inspected the annual Board member<br>questionnaire to ascertain the questionnaires<br>were completed by all Board members and<br>included questions to establish whether<br>members were independent and qualified to<br>serve on each part of the Board Committee<br>under the applicable bylaws and guidelines.<br>|No deviations noted.<br>|


AWS Confidential


114




Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**







|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|**AWSCA-1.8**: The<br>Board of Directors<br>conducts an annual<br>assessment of<br>individual Board<br>members and overall<br>Board performance.<br>The Nominating and<br>Corporate<br>Governance<br>Committee<br>periodically reviews<br>and assesses the<br>composition of the<br>board. The<br>Leadership<br>Development and<br>Compensation<br>Committee, with the<br>full Board present,<br>annually evaluates<br>the succession plan<br>for each member of<br>the senior<br>management team.<br>As part of the annual<br>Company and CEO<br>Performance review,<br>the Board reviews<br>the succession plan<br>for the CEO.<br>|CC1.2; <br>CC1.4 <br>**-wi2**|Inquired of the Amazon Corporate Counsel to<br>ascertain the Board of Directors conducted<br>an annual assessment of individual Board<br>members and overall Board performance,<br>the nominating and Corporate Governance<br>Committee periodically reviewed and<br>assessed the composition of the Board, and<br>the Leadership Development and<br>Compensation Committee evaluated the<br>succession plan for each member of the<br>senior management team, including the CEO.<br>**nIkLR**|No deviations noted.<br>**i2J**|
|**AWSCA-1.8**: The<br>Board of Directors<br>conducts an annual<br>assessment of<br>individual Board<br>members and overall<br>Board performance.<br>The Nominating and<br>Corporate<br>Governance<br>Committee<br>periodically reviews<br>and assesses the<br>composition of the<br>board. The<br>Leadership<br>Development and<br>Compensation<br>Committee, with the<br>full Board present,<br>annually evaluates<br>the succession plan<br>for each member of<br>the senior<br>management team.<br>As part of the annual<br>Company and CEO<br>Performance review,<br>the Board reviews<br>the succession plan<br>for the CEO.<br>|CC1.2; <br>CC1.4 <br>**-wi2**|Inspected the Nominating and Corporate<br>Governance meeting minutes to ascertain<br>the annual assessment and review of the<br>composition of the Board of Directors was<br>discussed and completed.<br>**U4Ag**|No deviations noted.<br>|
|**AWSCA-1.8**: The<br>Board of Directors<br>conducts an annual<br>assessment of<br>individual Board<br>members and overall<br>Board performance.<br>The Nominating and<br>Corporate<br>Governance<br>Committee<br>periodically reviews<br>and assesses the<br>composition of the<br>board. The<br>Leadership<br>Development and<br>Compensation<br>Committee, with the<br>full Board present,<br>annually evaluates<br>the succession plan<br>for each member of<br>the senior<br>management team.<br>As part of the annual<br>Company and CEO<br>Performance review,<br>the Board reviews<br>the succession plan<br>for the CEO.<br>|CC1.2; <br>CC1.4 <br>**-wi2**|Inspected the Board of Directors meeting<br>minutes to ascertain that the Board reviewed<br>the succession plan for the CEO and senior<br>management team as part of the annual<br>Company and CEO performance review.<br>**FivG**|No deviations noted.<br>|


AWS Confidential


115




Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**







|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|**AWSCA-1.9**: AWS<br>prepares and<br>consolidates the<br>operational planning<br>document annually.<br>The operational plan<br>includes operational<br>and performance<br>objectives, regulatory<br>and compliance<br>requirements with<br>sufficient clarity to<br>enable the<br>identification and<br>assessment of risks<br>relating to objectives.<br>|CC2.1; <br>CC2.2; <br>CC3.1; <br>CC3.2 <br> <br> <br>|Inquired of the Financial Planning and<br>Analysis Director to ascertain AWS prepared<br>and consolidated the operational planning<br>document annually including operational and<br>performance objectives as well as regulatory<br>and compliance requirements with sufficient<br>clarity to enable the identification and<br>assessment of risks relating to objectives.<br>**kLR**|No deviations noted.<br>**i2J**|
|**AWSCA-1.9**: AWS<br>prepares and<br>consolidates the<br>operational planning<br>document annually.<br>The operational plan<br>includes operational<br>and performance<br>objectives, regulatory<br>and compliance<br>requirements with<br>sufficient clarity to<br>enable the<br>identification and<br>assessment of risks<br>relating to objectives.<br>|CC2.1; <br>CC2.2; <br>CC3.1; <br>CC3.2 <br> <br> <br>|Inspected the Operational Plan related to the<br>creation of the operational planning<br>document to ascertain it included<br>operational and performance objectives as<br>well as regulatory and compliance<br>requirements that identified and assessed<br>risks relating to those objectives.<br>**4AgnI**|No deviations noted.<br>|
|**AWSCA-1.10**: AWS<br>has a process in place<br>to review<br>environmental and<br>geo-political risks<br>before launching a<br>new region. <br>|CC2.1; <br>CC3.1;<br>CC3.2; <br>CC3.3; <br>CC3.4; <br>CC4.1; <br>CC4.2; <br>CC5.1; <br>CC5.2; <br>CC5.3; <br>CC9.1; <br>CC9.2; <br>A1.2 <br>**-wi2**|Inquired of the AWS Data Center Risk<br>Management Head to ascertain<br>environmental and geo-political risks were<br>reviewed before launching new data center<br>regions.<br>**ivGU**|No deviations noted.<br>|
|**AWSCA-1.10**: AWS<br>has a process in place<br>to review<br>environmental and<br>geo-political risks<br>before launching a<br>new region. <br>|CC2.1; <br>CC3.1;<br>CC3.2; <br>CC3.3; <br>CC3.4; <br>CC4.1; <br>CC4.2; <br>CC5.1; <br>CC5.2; <br>CC5.3; <br>CC9.1; <br>CC9.2; <br>A1.2 <br>**-wi2**|For all new in-scope data center regions<br>selected from the data center inventory<br>system, inspected review documentation to<br>ascertain a review of environmental and<br>geopolitical risks was performed before the<br>new data center region was launched.<br>**F**|No deviations noted.<br>|
|**AWSCA-2.1:** User<br>access to the<br>internal Amazon<br>network is not<br>provisioned unless<br>an active record is<br>created in the HR<br>System by Human<br>Resources. Access is<br>automatically<br>**m-toke**|CC6.1; <br>CC6.2; <br>CC6.3 <br>|Inquired of an Employee Onboarding<br>Software Development Engineer to ascertain<br>user access to the internal Amazon network<br>was not activated unless an active record was<br>created in the HR System by Human<br>Resources, that access was automatically<br>provisioned with least privilege per job<br>function, and that first-time passwords were<br>set to a unique value and changed<br>immediately after first use.<br>|No deviations noted.<br>|


AWS Confidential


116




Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**







|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|provisioned with<br>least privilege per<br>job function. First<br>time passwords are<br>set to a unique value<br>and changed<br>immediately after<br>first use.<br>||Inspected the system configurations<br>responsible for provisioning access to the<br>internal Amazon network to ascertain access<br>to Windows and UNIX user accounts could<br>not be provisioned unless an active record<br>was created in the HR System by Human<br>Resources, that access was provisioned<br>automatically with least privilege per job<br>function prior to employee start dates, and<br>that first time passwords were configured to<br>create a unique value and were required to<br>be changed immediately after first use.<br>**gnIkLR**|No deviations noted.<br>**i2J**|
|provisioned with<br>least privilege per<br>job function. First<br>time passwords are<br>set to a unique value<br>and changed<br>immediately after<br>first use.<br>||For one corporate new hire and one<br>associate new hire selected from an HR<br>system generated listing of new hires,<br>inspected the employee’s HR System record<br>to ascertain the HR system activated the<br>employee’s record prior to the creation of an<br>employee’s Windows and UNIX accounts and<br>that the first-time passwords are changed<br>immediately after employee's first use of the<br>account.<br>**ivGU4A**|No deviations noted.<br>|
|**AWSCA-2.2:** IT<br>access above least<br>privileged, including<br>administrator<br>accounts, is<br>approved by<br>appropriate<br>personnel prior to<br>access provisioning.<br>**m-token**|CC6.1; <br>CC6.2; <br>CC6.3; <br>CC6.7; <br>CC6.8 <br>**-wi**|Inquired of Software Development Managers<br>to ascertain IT access above least privileged,<br>including administrator accounts, was<br>approved by appropriate personnel prior to<br>access provisioning.<br>|No deviations noted.<br>|
|**AWSCA-2.2:** IT<br>access above least<br>privileged, including<br>administrator<br>accounts, is<br>approved by<br>appropriate<br>personnel prior to<br>access provisioning.<br>**m-token**|CC6.1; <br>CC6.2; <br>CC6.3; <br>CC6.7; <br>CC6.8 <br>**-wi**|Inspected the system configurations<br>responsible for the access provisioning<br>process to ascertain IT access above least<br>privileged, including administrator accounts,<br>was required to be approved by appropriate<br>personnel prior to automatic access<br>provisioning.<br> <br> <br>|No deviations noted.<br>|


AWS Confidential


117




Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**







|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|||For one active employee, inspected the<br>process of access provisioning to ascertain<br>approval of the access was provided by<br>appropriate personnel prior to the automatic<br>provisioning of the access.<br>|No deviations noted.<br>**i2J**|
|||For one active manager who met the access<br>rules, inspected the access provisioning<br>process to ascertain the manager could not<br>add users who were not their direct reports.<br>**IkL**|No deviations noted.<br>|
|||For one active manager that did not meet the<br>access rules, inspected the access<br>provisioning process to ascertain the<br>manager could not add users.<br>**Agn**|No deviations noted.<br>|
|**AWSCA-2.3:** IT<br>access privileges are<br>reviewed on a<br>periodic basis by<br>appropriate<br>personnel.<br>**m-token**|CC6.1; <br>CC6.2; <br>CC6.3; <br>CC6.7; <br>CC6.8 <br> <br>**-wi2**|Inquired of Software Development Managers<br>to ascertain access to systems supporting the<br>infrastructure and network above least<br>privilege was reviewed and approved on a<br>quarterly basis by appropriate personnel.<br>**GU4**|No deviations noted.<br>|
|**AWSCA-2.3:** IT<br>access privileges are<br>reviewed on a<br>periodic basis by<br>appropriate<br>personnel.<br>**m-token**|CC6.1; <br>CC6.2; <br>CC6.3; <br>CC6.7; <br>CC6.8 <br> <br>**-wi2**|Inquired of Software Development Managers<br>to ascertain access to internal AWS accounts<br>above least privilege was reviewed and<br>approved on a semi-annual basis by<br>appropriate personnel.<br>**Fiv**|No deviations noted.<br>|
|**AWSCA-2.3:** IT<br>access privileges are<br>reviewed on a<br>periodic basis by<br>appropriate<br>personnel.<br>**m-token**|CC6.1; <br>CC6.2; <br>CC6.3; <br>CC6.7; <br>CC6.8 <br> <br>**-wi2**|Inspected the system configurations<br>responsible for the access review process to<br>ascertain IT infrastructure and network<br>access privileges were reviewed on a<br>quarterly basis by appropriate personnel or<br>access was automatically removed.<br>|No deviations noted.<br>|
|**AWSCA-2.3:** IT<br>access privileges are<br>reviewed on a<br>periodic basis by<br>appropriate<br>personnel.<br>**m-token**|CC6.1; <br>CC6.2; <br>CC6.3; <br>CC6.7; <br>CC6.8 <br> <br>**-wi2**|Inspected the system configurations<br>responsible for the temporary access<br>revocation process to ascertain that when the<br>temporary privileges to resources expired<br>access to the resources was automatically<br>removed.<br>|No deviations noted.<br>|


AWS Confidential


118




Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**



|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|**m-token**|**-wi2**|Inspected the system configurations<br>responsible for the internal transfer<br>revocation process to ascertain when users<br>transferred internally, access to the previous<br>resources was automatically removed.<br>|No deviations noted.<br>**i2J**|
|**m-token**|**-wi2**|Selected an active access group of IT<br>infrastructure and network access privileges<br>marked for removal as part of the user access<br>review process and inspected the access log<br>to ascertain access was automatically<br>revoked.<br>**gnIkL**|No deviations noted.<br>|
|**m-token**|**-wi2**|Observed a Software Development Manager<br>mark an active internal AWS account for<br>removal as part of the user access review<br>process and inspected the account after the<br>review to ascertain access was automatically<br>revoked.<br>**U4A**|No deviations noted.<br>|
|**m-token**|**-wi2**|Selected a user with temporary access to the<br>IT infrastructure and network access<br>privileges to ascertain that when the<br>temporary privileges to the resource expired,<br>access was automatically revoked.<br>**FivG**|No deviations noted.<br>|
|**m-token**|**-wi2**|Selected an active access group of IT<br>infrastructure and network access privileges<br>that was not reviewed during the quarter and<br>inspected the access log to ascertain access<br>privileges were automatically revoked.<br>|No deviations noted.<br>|
|**m-token**|**-wi2**|Selected an active access group and inspected<br>the access review process to ascertain IT<br>infrastructure and network access privileges<br>were reviewed quarterly by appropriate<br>personnel.<br> <br> <br>|No deviations noted.<br>|


AWS Confidential


119




Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**







|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|||Selected a sample of AWS accounts from a<br>system generated listing of active internal<br>AWS accounts and inspected the access<br>review process to ascertain internal AWS<br>account access privileges were reviewed<br>semi-annually by appropriate personnel.<br>**R**|No deviations noted.<br>**i2J**|
|**AWSCA-2.4:** User<br>access to Amazon<br>systems is revoked<br>within 24 hours of<br>the employee record<br>being terminated<br>(deactivated) in the<br>HR System by<br>Human Resources.<br>|CC6.1; <br>CC6.2; <br>CC6.3 <br>**i2**|Inquired of a Sr Screening and Work<br>Authorization SDM to ascertain access to<br>systems was automatically revoked within 24<br>hours of an employee record being<br>terminated (deactivated) in the HR System.<br>**gnIk**|No deviations noted.<br>|
|**AWSCA-2.4:** User<br>access to Amazon<br>systems is revoked<br>within 24 hours of<br>the employee record<br>being terminated<br>(deactivated) in the<br>HR System by<br>Human Resources.<br>|CC6.1; <br>CC6.2; <br>CC6.3 <br>**i2**|Inspected the system configurations<br>responsible for terminating access to Amazon<br>systems, to ascertain access to Windows and<br>UNIX user accounts were configured to be<br>automatically revoked within 24 hours after<br>an employee's record was terminated<br>(deactivated) in the HR System by Human<br>Resources.<br>**vGU4A**|No deviations noted.<br>|
|**AWSCA-2.4:** User<br>access to Amazon<br>systems is revoked<br>within 24 hours of<br>the employee record<br>being terminated<br>(deactivated) in the<br>HR System by<br>Human Resources.<br>|CC6.1; <br>CC6.2; <br>CC6.3 <br>**i2**|For one terminated employee, inspected the<br>employee's HR system record, to ascertain<br>access to the Amazon systems was<br>automatically revoked within 24 hours on<br>both Unix/LDAP and Windows/AD accounts.<br>**Fi**|No deviations noted.<br>|
|**AWSCA-2.5:** <br>Password settings<br>are managed in<br>compliance with<br>Amazon.com’s<br>Password Policy. <br>**m-token**|CC6.1; <br>CC6.3 <br>**-**|Inquired of a Corporate Systems Manager<br>and Corporate Response Manager to<br>ascertain password complexity, length,<br>maximum age, history, lockout and<br>credential monitoring was enforced per the<br>Amazon.com Password Policy.<br>|No deviations noted.<br>|
|**AWSCA-2.5:** <br>Password settings<br>are managed in<br>compliance with<br>Amazon.com’s<br>Password Policy. <br>**m-token**|CC6.1; <br>CC6.3 <br>**-**|Inspected the password configurations in the<br>Active Directory domain to ascertain they<br>were configured to enforce the Amazon.com<br>Password Policy, including:<br>• Passwords must be at least eight (8)<br>characters long<br>|No deviations noted.<br>|


AWS Confidential


120




Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**



|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|**-token**|**-wi2**|• Passwords must contain a combination of<br>letters, numbers, and special characters<br>• Passwords must not contain the user’s real<br>name or username<br>• Passwords must not be modifications or<br>increments of a recently used password for<br>the account<br>• Accounts are set to lockout after 6 invalid<br>attempts<br>**nIkLR**|**i2J**|
|**-token**|**-wi2**|Observed that the following password<br>configurations were enforced according to<br>the Amazon.com Password Policy after<br>attempting to set a combination of out-of-<br>policy passwords using the password tool<br>within the production environment:<br>• Passwords must be at least eight characters<br>long<br>• Passwords must contain a combination of<br>letters, numbers, and special characters<br>• Passwords must not contain the user’s real<br>name or username<br>• Passwords must not be the same as or<br>similar to a recently used password<br>• Passwords must not contain 'Amazon' or<br>any other business name<br>**FivGU4Ag**|No deviations noted.<br>|
|**-token**|**-wi2**|Inspected the credential compromise<br>monitoring configuration to ascertain that<br>tickets for incidents were created<br>automatically and logged within a ticketing<br>system per the Amazon.com Password Policy.<br>|No deviations noted.<br>|


AWS Confidential


121




Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**







|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|||Inspected an incident ticket created for<br>impacted user credentials to ascertain<br>credentials of flagged Amazon accounts were<br>identified, tracked and rotated in a timely<br>manner.<br>|No deviations noted.<br>**i2J**|
|**AWSCA-2.6:** AWS<br>requires two-factor<br>authentication over<br>an approved<br>cryptographic<br>channel for<br>authentication to the<br>internal AWS<br>network from<br>remote locations. <br>|CC6.1; <br>CC6.3; <br>CC6.6 <br>|Inquired of a Network Development Engineer<br>to ascertain two-factor authentication over<br>an approved cryptographic channel was<br>required to access the Amazon corporate<br>network from remote locations.<br>**nIkL**|No deviations noted.<br>|
|**AWSCA-2.6:** AWS<br>requires two-factor<br>authentication over<br>an approved<br>cryptographic<br>channel for<br>authentication to the<br>internal AWS<br>network from<br>remote locations. <br>|CC6.1; <br>CC6.3; <br>CC6.6 <br>|Inspected the RADIUS and SAML servers<br>authentication protocol configuration to<br>ascertain authentication to the internal AWS<br>network from remote locations required<br>two-factor authentication over an approved<br>cryptographic channel.<br>**U4Ag**|No deviations noted.<br>|
|**AWSCA-2.6:** AWS<br>requires two-factor<br>authentication over<br>an approved<br>cryptographic<br>channel for<br>authentication to the<br>internal AWS<br>network from<br>remote locations. <br>|CC6.1; <br>CC6.3; <br>CC6.6 <br>|Attempted to login to the Amazon corporate<br>network from a remote location to ascertain<br>both a physical token and password were<br>required to access the Amazon corporate<br>network over an approved cryptographic<br>channel.<br>**FivG**|No deviations noted.<br>|


AWS Confidential


122




Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality, and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**







|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|**AWSCA-3.1:** Firewall<br>devices are<br>configured to restrict<br>access to the<br>computing<br>environment and<br>enforce boundaries<br>of computing<br>clusters. <br>|CC6.1; <br>CC6.6; <br>CC7.1; <br>CC8.1 <br>|Inquired of an AWS Infrastructure Security<br>Engineer to ascertain firewall devices were<br>configured to restrict access to the<br>computing environment and enforce<br>boundaries of computing clusters.<br>|No deviations noted.<br>**i2J**|
|**AWSCA-3.1:** Firewall<br>devices are<br>configured to restrict<br>access to the<br>computing<br>environment and<br>enforce boundaries<br>of computing<br>clusters. <br>|CC6.1; <br>CC6.6; <br>CC7.1; <br>CC8.1 <br>|For a sample of in-scope firewalls selected<br>from a system generated list within the<br>firewall management tool, inspected the<br>access control lists to ascertain the devices<br>were configured to deny all access to the<br>computing environment and enforce<br>boundaries of computing clusters, unless<br>explicitly authorized.<br>**AgnIkL**|No deviations noted.<br>|
|**AWSCA-3.2:** Firewall<br>policies<br>(configuration files)<br>are automatically<br>pushed to<br>production firewall<br>devices. <br>|CC6.1; <br>CC6.6; <br>CC7.1; <br>CC8.1 <br>|Inquired of an AWS Infrastructure Security<br>Engineer to ascertain firewall policies were<br>automatically pushed to production firewall<br>devices.<br>**GU4**|No deviations noted.<br>|
|**AWSCA-3.2:** Firewall<br>policies<br>(configuration files)<br>are automatically<br>pushed to<br>production firewall<br>devices. <br>|CC6.1; <br>CC6.6; <br>CC7.1; <br>CC8.1 <br>|For a sample of in-scope firewall devices<br>selected from a system generated list within<br>the firewall management tool, inspected the<br>deployment log output to ascertain policies<br>were automatically pushed to production<br>firewall devices.<br>**Fiv**|No deviations noted.<br>|
|**AWSCA-3.3:** Firewall<br>policy updates are<br>reviewed and<br>approved. <br>**-token**|CC6.1; <br>CC6.6; <br>CC7.1; <br>CC8.1 <br>**-w**|Inquired of an AWS Infrastructure Security<br>Engineer to ascertain data center firewall<br>policy updates were reviewed and approved.<br>|No deviations noted.<br>|
|**AWSCA-3.3:** Firewall<br>policy updates are<br>reviewed and<br>approved. <br>**-token**|CC6.1; <br>CC6.6; <br>CC7.1; <br>CC8.1 <br>**-w**|For a sample of in-scope firewall policy<br>updates selected from a system generated<br>list within the firewall management tool,<br>inspected approval evidence to ascertain<br>they were reviewed and approved by<br>appropriate personnel prior to<br>implementation.<br>|No deviations noted.<br>|


AWS Confidential


123




Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality, and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**







|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|||For a sample of employees selected from a<br>system generated list of individuals eligible to<br>approve ACL requests, inspected the job title<br>and team of the employee to ascertain that<br>approval and user access rights were<br>appropriate.<br>**R**|No deviations noted.<br>**i2J**|
|**AWSCA-3.4:** AWS<br>performs external<br>vulnerability<br>assessments at least<br>quarterly, identified<br>issues are<br>investigated and<br>tracked to resolution<br>in a timely manner.<br>|CC3.2; <br>CC3.3; <br>CC3.4; <br>CC4.1; <br>CC6.8; <br>CC7.1; <br>CC7.2; <br>CC7.4 <br>**i2**|Inquired of an AWS Security Engineer to<br>ascertain quarterly external vulnerability<br>assessments were performed and that<br>identified issues were investigated and<br>tracked to resolution.<br>**gnIk**|No deviations noted.<br>|
|**AWSCA-3.4:** AWS<br>performs external<br>vulnerability<br>assessments at least<br>quarterly, identified<br>issues are<br>investigated and<br>tracked to resolution<br>in a timely manner.<br>|CC3.2; <br>CC3.3; <br>CC3.4; <br>CC4.1; <br>CC6.8; <br>CC7.1; <br>CC7.2; <br>CC7.4 <br>**i2**|Inspected the listing of production end points<br>used by the vulnerability assessment tools of<br>the quarterly external vulnerability<br>assessments performed to ascertain<br>production hosts for the in-scope services<br>(that supported public end points) were<br>included in the quarterly scans.<br>**GU4A**|No deviations noted.<br>|
|**AWSCA-3.4:** AWS<br>performs external<br>vulnerability<br>assessments at least<br>quarterly, identified<br>issues are<br>investigated and<br>tracked to resolution<br>in a timely manner.<br>|CC3.2; <br>CC3.3; <br>CC3.4; <br>CC4.1; <br>CC6.8; <br>CC7.1; <br>CC7.2; <br>CC7.4 <br>**i2**|For a sample of quarters, inspected evidence<br>of external vulnerability assessments to<br>ascertain assessments were performed,<br>results were documented, and that the<br>process existed for any identified issues to be<br>tracked, addressed, and resolved in a timely<br>manner.<br>**Fiv**|No deviations noted.<br>|
|**AWSCA-3.5:** AWS<br>enables customers<br>to select who has<br>access to AWS<br>services and<br>resources that they<br>own. AWS prevents<br>customers from<br>accessing AWS<br>resources that are<br>**-token**|CC6.1 <br>|Inquired of Software Development Managers<br>and Sr. Software Engineers to ascertain AWS<br>enabled customers to select who had access<br>to AWS services and resources that they<br>owned, that customers were prevented from<br>accessing AWS resources that were not<br>assigned to them via access permissions, and<br>that content was only returned to individuals<br>authorized to access the specific AWS service<br>or resource.<br>|No deviations noted.<br>|


AWS Confidential


124






Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality, and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**







|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|not assigned to them<br>via access<br>permissions. Content<br>is only returned to<br>individuals<br>authorized to access<br>the specified AWS<br>service or resource<br>(if resource-level<br>permissions are<br>applicable to the<br>service). <br>||Inspected the configurations in-place for the<br>AWS services that managed external access<br>to AWS services and resources (if resource-<br>level permissions were applicable to the<br>service), to ascertain services were designed<br>to return content only to individuals<br>authorized to access the specified AWS<br>service or resource, and that AWS prevented<br>customers from accessing resources that had<br>not been assigned to them via access<br>permissions.<br>**nIkLR**|No deviations noted.<br>**i2J**|
|not assigned to them<br>via access<br>permissions. Content<br>is only returned to<br>individuals<br>authorized to access<br>the specified AWS<br>service or resource<br>(if resource-level<br>permissions are<br>applicable to the<br>service). <br>||Observed a user with authorized access<br>permissions attempt to access AWS services<br>and resources, to ascertain that services<br>returned content to individuals authorized to<br>access the specified AWS service or resource.<br>**4Ag**|No deviations noted.<br>|
|not assigned to them<br>via access<br>permissions. Content<br>is only returned to<br>individuals<br>authorized to access<br>the specified AWS<br>service or resource<br>(if resource-level<br>permissions are<br>applicable to the<br>service). <br>||Observed a user without authorized access<br>permissions attempt to access AWS services<br>and resources, to ascertain that services did<br>not return content to individuals without<br>authorized access to the specified AWS<br>service or resource.<br>**ivGU**|No deviations noted.<br>|
|**AWSCA-3.6:** AWS<br>performs application<br>security reviews for<br>externally launched<br>products, services,<br>and significant<br>feature additions<br>prior to launch to<br>evaluate whether<br>security risks are<br>identified and<br>mitigated.<br>**m-token**|CC2.1; <br>CC6.1; <br>CC7.1; <br>CC8.1; <br>P3.1; <br>P4.1; <br>P4.2 <br>**-wi**|Inquired of an Application Security Technical<br>Program Manager to ascertain AWS<br>performed application security reviews for<br>launched products, services, and significant<br>feature additions prior to launch to evaluate<br>whether security risks were identified and<br>mitigated.<br>|No deviations noted.<br>|
|**AWSCA-3.6:** AWS<br>performs application<br>security reviews for<br>externally launched<br>products, services,<br>and significant<br>feature additions<br>prior to launch to<br>evaluate whether<br>security risks are<br>identified and<br>mitigated.<br>**m-token**|CC2.1; <br>CC6.1; <br>CC7.1; <br>CC8.1; <br>P3.1; <br>P4.1; <br>P4.2 <br>**-wi**|For a sample of products, services, and<br>significant feature additions selected from a<br>system generated list of trouble tickets<br>representing launches during the period,<br>inspected the Application Security team’s<br>review to ascertain the products, services,<br>and significant feature additions were<br>reviewed and approved prior to launch.<br>|No deviations noted.<br>|


AWS Confidential


125




Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality, and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**







|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|**AWSCA-3.7:** S3-<br>Specific – Network<br>devices are<br>configured by AWS<br>to only allow access<br>to specific ports on<br>other server systems<br>within Amazon S3.<br>|CC6.1; <br>CC6.6; <br>|Inquired of an S3 Software Development<br>Engineer to ascertain network devices were<br>configured to only allow access to specific<br>ports on server systems within Amazon S3.<br>|No deviations noted.<br>**2J**|
|**AWSCA-3.7:** S3-<br>Specific – Network<br>devices are<br>configured by AWS<br>to only allow access<br>to specific ports on<br>other server systems<br>within Amazon S3.<br>|CC6.1; <br>CC6.6; <br>|For a sample of S3 network devices selected<br>from a listing of S3 network devices<br>generated from the S3 code repository,<br>inspected the configuration settings to<br>ascertain the devices were configured to only<br>allow access to specified ports.<br>**nIkL**|No deviations noted.<br>|
|**AWSCA-3.8**: S3-<br>Specific – External<br>data access is logged<br>with the following<br>information: data<br>accessor IP address,<br>object and<br>operation. Logs are<br>retained for at least<br>90 days.<br>**-token**|CC6.1; <br>CC6.6; <br>**-wi2**|Inquired of an S3 Software Development<br>Engineer to ascertain external data access<br>was logged with the data accessor IP address,<br>object, and operation, and that logs were<br>retained for at least 90 days.<br>**U4Ag**|No deviations noted.<br>|
|**AWSCA-3.8**: S3-<br>Specific – External<br>data access is logged<br>with the following<br>information: data<br>accessor IP address,<br>object and<br>operation. Logs are<br>retained for at least<br>90 days.<br>**-token**|CC6.1; <br>CC6.6; <br>**-wi2**|Inspected the configuration settings pushed<br>to the S3 web servers to ascertain the servers<br>were configured to log the data accessor IP<br>address, object, and operation information.<br>**vG**|No deviations noted.<br>|
|**AWSCA-3.8**: S3-<br>Specific – External<br>data access is logged<br>with the following<br>information: data<br>accessor IP address,<br>object and<br>operation. Logs are<br>retained for at least<br>90 days.<br>**-token**|CC6.1; <br>CC6.6; <br>**-wi2**|For a sample of AWS Availability Zones (AZs) <br>selected from a listing of AZs generated from<br>the AZ code repository, inspected the<br>environment operational configurations for<br>log retention of external access to data to<br>ascertain that logs were configured to be<br>retained for 90 days.<br>**Fi**|No deviations noted.<br>|
|**AWSCA-3.8**: S3-<br>Specific – External<br>data access is logged<br>with the following<br>information: data<br>accessor IP address,<br>object and<br>operation. Logs are<br>retained for at least<br>90 days.<br>**-token**|CC6.1; <br>CC6.6; <br>**-wi2**|Observed a Software Development Engineer<br>perform an access operation on an S3 object<br>and inspected the external data access log<br>output after 90 days to ascertain the<br>following information was logged for at least<br>90 days: data accessor IP accessing the data,<br>object accessed, and operation performed.<br>|No deviations noted.<br>|


AWS Confidential


126




Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality, and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**







|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|**AWSCA-3.9:** EC2-<br>Specific – Physical<br>hosts have host-<br>based firewalls to<br>prevent<br>unauthorized access.<br>|CC6.1; <br>CC6.6 <br>**i2**|Inquired of an EC2 Security Engineer to<br>ascertain EC2 physical hosts had host-based<br>firewalls, or access was logically restricted, to<br>prevent unauthorized access.<br>|No deviations noted.<br>**2J**|
|**AWSCA-3.9:** EC2-<br>Specific – Physical<br>hosts have host-<br>based firewalls to<br>prevent<br>unauthorized access.<br>|CC6.1; <br>CC6.6 <br>**i2**|Inspected the automated configurations<br>responsible for configuring a new host to<br>ascertain that host-based firewalls were<br>automatically added during the build process<br>of new hosts.<br>**IkL**|No deviations noted.<br>|
|**AWSCA-3.9:** EC2-<br>Specific – Physical<br>hosts have host-<br>based firewalls to<br>prevent<br>unauthorized access.<br>|CC6.1; <br>CC6.6 <br>**i2**|Inspected the monitoring configurations of<br>physical hosts to ascertain that monitoring<br>was in place to notify service team members<br>in the case that a physical host did not have<br>an active firewall.<br>**Agn**|No deviations noted.<br>|
|**AWSCA-3.9:** EC2-<br>Specific – Physical<br>hosts have host-<br>based firewalls to<br>prevent<br>unauthorized access.<br>|CC6.1; <br>CC6.6 <br>**i2**|Observed an EC2 Security Engineer make an<br>API request with and without the appropriate<br>token to ascertain a host based access token<br>was required to authorize access to the host.<br>**GU4**|No deviations noted.<br>|
|**AWSCA-3.9:** EC2-<br>Specific – Physical<br>hosts have host-<br>based firewalls to<br>prevent<br>unauthorized access.<br>|CC6.1; <br>CC6.6 <br>**i2**|For a sample of EC2 physical hosts supporting<br>in-scope AWS regions selected from listings<br>of production hosts for each region,<br>inspected the host-based firewall settings to<br>ascertain host-based firewalls were in place<br>and operational to prevent unauthorized<br>access.<br>**Fiv**|No deviations noted.<br>|
|**AWSCA-3.10:** EC2-<br>Specific – Virtual<br>hosts are behind<br>software firewalls<br>which are configured<br>to prevent TCP/IP<br>spoofing, packet<br>sniffing, and restrict<br>incoming<br>connections to<br>**m-token**|CC6.1 <br>|Inquired of an EC2 Security Manager to<br>ascertain virtual hosts were behind software<br>firewalls, which prevented TCP/IP spoofing,<br>packet sniffing, and restricted incoming<br>connections to customer-specified ports.<br>|No deviations noted.<br>|
|**AWSCA-3.10:** EC2-<br>Specific – Virtual<br>hosts are behind<br>software firewalls<br>which are configured<br>to prevent TCP/IP<br>spoofing, packet<br>sniffing, and restrict<br>incoming<br>connections to<br>**m-token**|CC6.1 <br>|Observed an EC2 Security Engineer create a<br>virtual EC2 host with a firewall configured to<br>communicate with only specified IP<br>addresses and ascertained that<br>communications with the specified IP<br>address were successful.<br>|No deviations noted.<br>|


AWS Confidential


127






Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality, and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**











|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|customer-specified<br>ports.<br>||Observed an EC2 Security Engineer attempt<br>to communicate with an unspecified IP<br>address to ascertain the attempts were<br>denied.<br>|No deviations noted.<br>**2J**|
|customer-specified<br>ports.<br>||Observed an EC2 Security Engineer create a<br>virtual EC2 host and inspected the IP table<br>configurations to ascertain traffic was routed<br>to prevent TCP/IP spoofing.<br>**IkL**|No deviations noted.<br>|
|customer-specified<br>ports.<br>||Observed an EC2 Security Engineer create<br>two EC2 instances on a single physical EC2<br>host and generate network traffic on each<br>instance to ascertain neither of the instances<br>was able to packet sniff the traffic of the<br>other instance.<br>**4Agn**|No deviations noted.<br>|
|**AWSCA-3.11:** EC2-<br>Specific – AWS<br>prevents customers<br>from accessing<br>custom AMIs not<br>assigned to them by<br>a property of the<br>AMI called launch-<br>permissions. By<br>default, the launch-<br>permissions of an<br>AMI restrict its use<br>to the<br>customer/account<br>that created and<br>registered it.<br>**-token**|CC6.1 <br> <br>**-wi2**|Inquired of an EC2 Security Manager to<br>ascertain AWS prevented customers from<br>accessing custom AMIs not assigned to them<br>by default launch-permissions.<br>**vGU**|No deviations noted.<br>|
|**AWSCA-3.11:** EC2-<br>Specific – AWS<br>prevents customers<br>from accessing<br>custom AMIs not<br>assigned to them by<br>a property of the<br>AMI called launch-<br>permissions. By<br>default, the launch-<br>permissions of an<br>AMI restrict its use<br>to the<br>customer/account<br>that created and<br>registered it.<br>**-token**|CC6.1 <br> <br>**-wi2**|Inspected the AMI launch-permissions<br>configuration within the AWS console to<br>ascertain that by default the launch<br>permission of an AMI restricted its use to the<br>account that created it unless the customer<br>granted access permissions.<br>**Fi**|No deviations noted.<br>|
|**AWSCA-3.11:** EC2-<br>Specific – AWS<br>prevents customers<br>from accessing<br>custom AMIs not<br>assigned to them by<br>a property of the<br>AMI called launch-<br>permissions. By<br>default, the launch-<br>permissions of an<br>AMI restrict its use<br>to the<br>customer/account<br>that created and<br>registered it.<br>**-token**|CC6.1 <br> <br>**-wi2**|Created an AMI, attempted to access the AMI<br>without the designated launch permissions,<br>and inspected the error message within the<br>AWS management console, to ascertain<br>access was restricted.<br> <br>|No deviations noted.<br>|


AWS Confidential


128


Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality, and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**







|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|**AWSCA-3.12:** EC2-<br>Specific – AWS<br>prevents customers<br>from accessing<br>physical hosts or<br>instances not<br>assigned to them by<br>filtering through the<br>virtualization<br>software.<br>|CC6.1 <br> <br>|Inquired of an EC2 Security Manager to<br>ascertain customers were restricted from<br>accessing physical hosts or instances not<br>assigned to them by filtering through the<br>virtualization software.<br>|No deviations noted.<br>**i2J**|
|**AWSCA-3.12:** EC2-<br>Specific – AWS<br>prevents customers<br>from accessing<br>physical hosts or<br>instances not<br>assigned to them by<br>filtering through the<br>virtualization<br>software.<br>|CC6.1 <br> <br>|Observed an EC2 Security Engineer attempt<br>to IP ping the physical EC2 host from an EC2<br>instance within the host, to ascertain the<br>physical host was isolated from the<br>instances.<br>**nIkL**|No deviations noted.<br>|
|**AWSCA-3.12:** EC2-<br>Specific – AWS<br>prevents customers<br>from accessing<br>physical hosts or<br>instances not<br>assigned to them by<br>filtering through the<br>virtualization<br>software.<br>|CC6.1 <br> <br>|Observed an EC2 Security Engineer attempt<br>to access a file stored on an EC2 instance<br>from the physical EC2 host the instance was<br>located on, to ascertain the instances located<br>on physical hosts were unable to be<br>accessed.<br>**U4Ag**|No deviations noted.<br>|
|**AWSCA-3.12:** EC2-<br>Specific – AWS<br>prevents customers<br>from accessing<br>physical hosts or<br>instances not<br>assigned to them by<br>filtering through the<br>virtualization<br>software.<br>|CC6.1 <br> <br>|Observed an EC2 Security Engineer attempt<br>to access a file stored on an EC2 instance<br>from a different instance on the same<br>physical EC2 host, to ascertain the instances<br>on the same physical hosts were isolated<br>from one another.<br>**FivG**|No deviations noted.<br>|
|**AWSCA-3.13:** VPC-<br>Specific – Network<br>communications<br>within a VPC are<br>isolated from<br>network<br>communications<br>within other VPCs.<br>**-token**|CC6.1 <br>**-wi**|Inquired of an EC2 Networking Software<br>Development Engineer to ascertain network<br>communications between different VPCs<br>were isolated from one another.<br>|No deviations noted.<br>|
|**AWSCA-3.13:** VPC-<br>Specific – Network<br>communications<br>within a VPC are<br>isolated from<br>network<br>communications<br>within other VPCs.<br>**-token**|CC6.1 <br>**-wi**|Observed an EC2 Networking Software<br>Development Engineer configure the VPC<br>infrastructure for two VPCs and attempt to<br>communicate between instances across the<br>two VPCs to ascertain network<br>communication between the two VPCs was<br>isolated.<br>|No deviations noted.<br>|


AWS Confidential


129






Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality, and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**





|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|**AWSCA-3.14:** VPC-<br>Specific – Network<br>communications<br>within a VPN<br>Gateway are isolated<br>from network<br>communications<br>within other VPN<br>Gateways. <br>|CC6.1 <br> <br>|Inquired of an EC2 Networking Software<br>Development Engineer to ascertain network<br>communications between VPN gateways<br>were isolated from one another.<br>|No deviations noted.<br>**2J**|
|**AWSCA-3.14:** VPC-<br>Specific – Network<br>communications<br>within a VPN<br>Gateway are isolated<br>from network<br>communications<br>within other VPN<br>Gateways. <br>|CC6.1 <br> <br>|Observed an EC2 Networking Software<br>Development Engineer configure a VPC<br>infrastructure with two VPN Gateways and<br>attempt to communicate between instances<br>across the two VPN Gateways, to ascertain<br>network communication between VPN<br>gateways was isolated.<br>**gnIkL**|No deviations noted.<br>|
|**AWSCA-3.15:** VPC-<br>Specific – Internet<br>traffic through an<br>Internet Gateway is<br>forwarded to an<br>instance in a VPC<br>only when an<br>Internet Gateway is<br>attached to the VPC<br>and a public IP is<br>mapped to the<br>instance in the VPC. <br>|CC6.1 <br>**-wi2**|Inquired of a Sr. Software Engineer, EC2 VPC<br>to ascertain internet traffic through an<br>Internet Gateway was only forwarded to an<br>instance in a VPC when an Internet Gateway<br>was attached to the VPC, and a public IP was<br>mapped to the instance in the VPC.<br>**GU4A**|No deviations noted.<br>|
|**AWSCA-3.15:** VPC-<br>Specific – Internet<br>traffic through an<br>Internet Gateway is<br>forwarded to an<br>instance in a VPC<br>only when an<br>Internet Gateway is<br>attached to the VPC<br>and a public IP is<br>mapped to the<br>instance in the VPC. <br>|CC6.1 <br>**-wi2**|Created a VPC, attached an Internet<br>Gateway, allocated a public IP, and per<br>inspection of traffic on an instance,<br>ascertained traffic was successfully<br>forwarded.<br>**Fiv**|No deviations noted.<br>|
|**AWSCA-3.15:** VPC-<br>Specific – Internet<br>traffic through an<br>Internet Gateway is<br>forwarded to an<br>instance in a VPC<br>only when an<br>Internet Gateway is<br>attached to the VPC<br>and a public IP is<br>mapped to the<br>instance in the VPC. <br>|CC6.1 <br>**-wi2**|Removed the Internet Gateway and public IP<br>from the VPC and per inspection of the traffic<br>on the instance, ascertained traffic was<br>prevented from being forwarded.<br>|No deviations noted.<br>|


AWS Confidential


130








Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality, and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**







|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|**AWSCA-3.16**: AWS<br>maintains formal<br>policies and<br>procedures that<br>provide guidance for<br>operations and<br>information security<br>within the<br>organization and the<br>supporting AWS<br>environments. The<br>mobile device policy<br>provides guidance<br>on:<br>• <br>Use of mobile<br>devices.<br>• <br>Protection of<br>devices that<br>access content<br>for which<br>Amazon is<br>responsible.<br>• <br>Remote wipe<br>capability.<br>• <br>Password-<br>guessing<br>protection<br>restrictions.<br>• <br>Remote<br>synchronization<br>requirements.<br>• <br>Security patch<br>requirements<br>• <br>Approved<br>methods for<br>accessing<br>Amazon data.<br>**m-token**|CC6.4; <br>CC6.7; <br>CC8.1 <br>**-wi2**|Inquired of an AWS Risk Management<br>Program Manager to ascertain formal<br>policies and procedures for the use of mobile<br>devices existed and included guidance for<br>operations and information security for<br>organizations that support AWS<br>environments.<br>**LR**|No deviations noted.<br>**i2J**|
|**AWSCA-3.16**: AWS<br>maintains formal<br>policies and<br>procedures that<br>provide guidance for<br>operations and<br>information security<br>within the<br>organization and the<br>supporting AWS<br>environments. The<br>mobile device policy<br>provides guidance<br>on:<br>• <br>Use of mobile<br>devices.<br>• <br>Protection of<br>devices that<br>access content<br>for which<br>Amazon is<br>responsible.<br>• <br>Remote wipe<br>capability.<br>• <br>Password-<br>guessing<br>protection<br>restrictions.<br>• <br>Remote<br>synchronization<br>requirements.<br>• <br>Security patch<br>requirements<br>• <br>Approved<br>methods for<br>accessing<br>Amazon data.<br>**m-token**|CC6.4; <br>CC6.7; <br>CC8.1 <br>**-wi2**|Inspected the AWS internal website to<br>ascertain formal policies and procedures for<br>the use of mobile devices were available to<br>AWS employees.<br>**gnIk**|<br>No deviations noted.<br>|
|**AWSCA-3.16**: AWS<br>maintains formal<br>policies and<br>procedures that<br>provide guidance for<br>operations and<br>information security<br>within the<br>organization and the<br>supporting AWS<br>environments. The<br>mobile device policy<br>provides guidance<br>on:<br>• <br>Use of mobile<br>devices.<br>• <br>Protection of<br>devices that<br>access content<br>for which<br>Amazon is<br>responsible.<br>• <br>Remote wipe<br>capability.<br>• <br>Password-<br>guessing<br>protection<br>restrictions.<br>• <br>Remote<br>synchronization<br>requirements.<br>• <br>Security patch<br>requirements<br>• <br>Approved<br>methods for<br>accessing<br>Amazon data.<br>**m-token**|CC6.4; <br>CC6.7; <br>CC8.1 <br>**-wi2**|Inspected the mobile device policy to<br>ascertain it included organization-wide<br>security procedures as guidance for the AWS<br>environment regarding:<br> <br>• <br>Use of mobile devices<br>• <br>Protection of devices that access content<br>for which Amazon is responsible<br>• <br>Remote wipe capability<br>• <br>Password-guessing protection<br>restrictions<br>• <br>Remote synchronization requirements<br>• <br>Security patch requirements<br>• <br>Approved methods for accessing Amazon<br>data<br>**FivGU4A**|No deviations noted.<br>|


AWS Confidential


131




Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality, and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**







|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|**AWSCA-3.17:**<br>Outposts-Specific –<br>Service link is<br>established between<br>Outposts and AWS<br>Region by use of a<br>secured VPN<br>connection over<br>public internet or<br>AWS Direct Connect. <br>|CC6.1; <br>CC6.7 <br> <br>|Inquired of an AWS Senior Software<br>Development Manager to ascertain a Service<br>link was established between Outposts and<br>AWS Region by use of a secured VPN<br>connection over public internet or AWS<br>Direct Connect.<br>**R**|No deviations noted.<br>**i2J**|
|**AWSCA-3.17:**<br>Outposts-Specific –<br>Service link is<br>established between<br>Outposts and AWS<br>Region by use of a<br>secured VPN<br>connection over<br>public internet or<br>AWS Direct Connect. <br>|CC6.1; <br>CC6.7 <br> <br>|Inspected the Outpost configurations to<br>ascertain a Service link was established<br>between Outposts and AWS Region by use of<br>a secured VPN connection over the public<br>internet or AWS Direct Connect.<br>**gnIk**|No deviations noted.<br>|
|**AWSCA-3.17:**<br>Outposts-Specific –<br>Service link is<br>established between<br>Outposts and AWS<br>Region by use of a<br>secured VPN<br>connection over<br>public internet or<br>AWS Direct Connect. <br>|CC6.1; <br>CC6.7 <br> <br>|Inspected dashboards of an active Outpost to<br>ascertain the health of the secure VPN<br>connection between Outpost and AWS<br>region was tracked and monitored.<br>**4A**|No deviations noted.<br>|
|**AWSCA-3.17:**<br>Outposts-Specific –<br>Service link is<br>established between<br>Outposts and AWS<br>Region by use of a<br>secured VPN<br>connection over<br>public internet or<br>AWS Direct Connect. <br>|CC6.1; <br>CC6.7 <br> <br>|Inspected the monitoring configurations of<br>an active Outpost to ascertain alarming<br>around the secure VPN connection was<br>configured to notify service team members in<br>the case of network issues.<br>**ivGU**|No deviations noted.<br>|
|**AWSCA-3.18**: Anti-<br>virus software is<br>installed, updated<br>and running on<br>workstations. <br>**m-token**|CC6.7; <br>CC6.8 <br>**-wi**|Inquired of an AWS Security Platform<br>Manager to ascertain anti-virus software was<br>installed, updated, and running on<br>workstations.<br>|No deviations noted.<br>|
|**AWSCA-3.18**: Anti-<br>virus software is<br>installed, updated<br>and running on<br>workstations. <br>**m-token**|CC6.7; <br>CC6.8 <br>**-wi**|Inspected the anti-virus configurations on the<br>administrator console for the imaging of<br>workstations to ascertain the anti-virus<br>software was in place to monitor for<br>malicious code, was automatically updated<br>with new release or virus definitions and<br>prevented end-users from disabling the<br>service.<br>|No deviations noted<br>|
|**AWSCA-3.18**: Anti-<br>virus software is<br>installed, updated<br>and running on<br>workstations. <br>**m-token**|CC6.7; <br>CC6.8 <br>**-wi**|Inspected a workstation that had disabled<br>anti-virus software to ascertain that the<br>workstation was in process of being isolated<br>from the network.<br>|No deviations noted<br>|


AWS Confidential


132




Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality, and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**









|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|||Inspected a workstation to ascertain anti-<br>virus software was installed, updated and<br>running in accordance with the AWS System<br>and Information Integrity Policy.<br>|No deviations noted.<br>**2J**|
|**AWSCA-3.19:**S3-<br>Specific - All new<br>objects uploaded to<br>Amazon S3 are<br>automatically<br>encrypted with<br>server-side<br>encryption.<br>|CC6.1; <br>CC6.7 <br> <br>|Inquired of a Software Development<br>Engineer to ascertain new objects uploaded<br>to Amazon S3 were automatically encrypted<br>with server-side encryption.<br>**IkL**|No deviations noted.<br>|
|**AWSCA-3.19:**S3-<br>Specific - All new<br>objects uploaded to<br>Amazon S3 are<br>automatically<br>encrypted with<br>server-side<br>encryption.<br>|CC6.1; <br>CC6.7 <br> <br>|Inspected the code configurations to<br>ascertain new objects uploaded to Amazon<br>S3 were automatically encrypted with server-<br>side encryption.<br>**Agn**|No deviations noted.<br>|
|**AWSCA-3.19:**S3-<br>Specific - All new<br>objects uploaded to<br>Amazon S3 are<br>automatically<br>encrypted with<br>server-side<br>encryption.<br>|CC6.1; <br>CC6.7 <br> <br>|Observed a Software Development Engineer<br>upload a new object to a general-purpose S3<br>bucket, and inspected the object's attributes<br>to ascertain the newly uploaded object was<br>encrypted with server-side encryption.<br>**GU4**|No deviations noted.<br>|
|**AWSCA-4.1:** EC2-<br>Specific – Upon<br>initial<br>communication with<br>an AWS-provided<br>Linux AMI, AWS<br>enables secure<br>communication by<br>SSH configuration on<br>the instance, by<br>generating a unique<br>host-key and<br>delivering the key’s<br>fingerprint to the<br>user over a trusted<br>channel.<br>**-token**|CC6.7 <br>**-wi2**|Inquired of a Technical Program Manager to<br>ascertain upon initial communication with an<br>AWS-provided Linux AMI, AWS enabled a<br>secure communication by SSH configuration<br>on the instance by generating and delivering<br>a unique host-key fingerprint to the user over<br>a trusted channel.<br>**Fiv**|No deviations noted.<br>|
|**AWSCA-4.1:** EC2-<br>Specific – Upon<br>initial<br>communication with<br>an AWS-provided<br>Linux AMI, AWS<br>enables secure<br>communication by<br>SSH configuration on<br>the instance, by<br>generating a unique<br>host-key and<br>delivering the key’s<br>fingerprint to the<br>user over a trusted<br>channel.<br>**-token**|CC6.7 <br>**-wi2**|Launched a public Linux AMI EC2 instance<br>and inspected the EC2 console to ascertain<br>the unique host-key fingerprint was<br>accessible from the system log.<br>|No deviations noted.<br>|
|**AWSCA-4.1:** EC2-<br>Specific – Upon<br>initial<br>communication with<br>an AWS-provided<br>Linux AMI, AWS<br>enables secure<br>communication by<br>SSH configuration on<br>the instance, by<br>generating a unique<br>host-key and<br>delivering the key’s<br>fingerprint to the<br>user over a trusted<br>channel.<br>**-token**|CC6.7 <br>**-wi2**|Using the launched public Linux AMI EC2<br>instance, connected to the instance via SSH<br>using the unique host-key fingerprint and<br>inspected the connection logs to ascertain<br>the unique host-key fingerprint was listed.<br>|No deviations noted.<br>|


AWS Confidential


133




Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality, and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**





|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|||Launched a second public Linux AMI EC2<br>instance and inspected the EC2 console and<br>instance connection logs to ascertain the<br>unique host-key fingerprint was different<br>from the first instance.<br>|No deviations noted.<br>**i2J**|
|||Using the second public Linux AMI EC2<br>instance, attempted to connect to the<br>instance via SSH using the first instance's<br>unique host-key fingerprint and observed the<br>attempt was rejected by the system, to<br>ascertain that the connection to a Linux AMI<br>EC2 instance could only be performed using<br>the instance's unique host-key fingerprint.<br>**AgnIkL**|No deviations noted.<br>|
|**AWSCA-4.2:** EC2-<br>Specific – Upon<br>initial<br>communication with<br>an AWS-provided<br>Windows AMI, AWS<br>enables secure<br>communication by<br>configuring Windows<br>Terminal Services on<br>the instance by<br>generating a unique<br>self-signed server<br>certificate and<br>delivering the<br>certificate’s<br>thumbprint to the<br>user over a trusted<br>channel.<br>**m-token**|CC6.7 <br>**-wi2**|Inquired of a Technical Program Manager to<br>ascertain upon initial communication with an<br>AWS-provided Windows AMI, AWS enabled a<br>secure communication by configuring<br>Windows Terminal Services on the instance<br>by generating a unique self-signed server<br>certificate and delivering the certificate’s<br>thumbprint to the user over a trusted<br>channel.<br>**ivGU4**|No deviations noted.<br>|
|**AWSCA-4.2:** EC2-<br>Specific – Upon<br>initial<br>communication with<br>an AWS-provided<br>Windows AMI, AWS<br>enables secure<br>communication by<br>configuring Windows<br>Terminal Services on<br>the instance by<br>generating a unique<br>self-signed server<br>certificate and<br>delivering the<br>certificate’s<br>thumbprint to the<br>user over a trusted<br>channel.<br>**m-token**|CC6.7 <br>**-wi2**|Launched a public Windows AMI EC2<br>instance and inspected the EC2 console and<br>the system log to ascertain the self-signed<br>server certificate was accessible.<br>|No deviations noted.<br>|
|**AWSCA-4.2:** EC2-<br>Specific – Upon<br>initial<br>communication with<br>an AWS-provided<br>Windows AMI, AWS<br>enables secure<br>communication by<br>configuring Windows<br>Terminal Services on<br>the instance by<br>generating a unique<br>self-signed server<br>certificate and<br>delivering the<br>certificate’s<br>thumbprint to the<br>user over a trusted<br>channel.<br>**m-token**|CC6.7 <br>**-wi2**|Using the launched public Windows AMI EC2<br>instance, connected to the instance using the<br>unique self-signed server certificate to<br>ascertain the connection logs matched the<br>unique self-signed server certificate from the<br>instance’s EC2 console system log.<br>|No deviations noted.<br>|
|**AWSCA-4.2:** EC2-<br>Specific – Upon<br>initial<br>communication with<br>an AWS-provided<br>Windows AMI, AWS<br>enables secure<br>communication by<br>configuring Windows<br>Terminal Services on<br>the instance by<br>generating a unique<br>self-signed server<br>certificate and<br>delivering the<br>certificate’s<br>thumbprint to the<br>user over a trusted<br>channel.<br>**m-token**|CC6.7 <br>**-wi2**|Launched a second public Windows AMI EC2<br>instance and inspected the EC2 console and<br>instance connection logs to ascertain the<br>unique self-signed server certificate was<br>different than for the first instance.<br>|No deviations noted.<br>|


AWS Confidential


134




Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality, and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**











|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|||Using the second public Windows AMI EC2<br>instance, attempted to connect to the<br>instance using the first instance's unique self-<br>signed server certificate and observed the<br>attempt was rejected by the system, to<br>ascertain that connection to a Windows AMI<br>EC2 instance can only be performed using<br>the instance's unique self-signed server<br>certificate.<br>**IkLR**|No deviations noted.<br>**i2J**|
|**AWSCA-4.3:** VPC-<br>Specific – Amazon<br>enables secure VPN<br>communication to a<br>VPN Gateway by<br>providing a shared<br>secret key that is<br>used to establish<br>IPSec Associations.<br>|CC6.7 <br>|Inquired of a VPC Manager of Software<br>Development to ascertain Amazon enabled<br>secure VPN communication to a VPN<br>Gateway through a secret key that<br>established IPSec Associations.<br>**Agn**|No deviations noted.<br>|
|**AWSCA-4.3:** VPC-<br>Specific – Amazon<br>enables secure VPN<br>communication to a<br>VPN Gateway by<br>providing a shared<br>secret key that is<br>used to establish<br>IPSec Associations.<br>|CC6.7 <br>|Observed a VPC Manager of Software<br>Development use the shared secret key to<br>establish IPSec Associations to ascertain the<br>connection was successful.<br>**GU4**|No deviations noted.<br>|
|**AWSCA-4.3:** VPC-<br>Specific – Amazon<br>enables secure VPN<br>communication to a<br>VPN Gateway by<br>providing a shared<br>secret key that is<br>used to establish<br>IPSec Associations.<br>|CC6.7 <br>|Observed the VPC Manager of Software<br>Development alter the shared secret key to<br>establish IPSec Security Associations to<br>ascertain the connection was unsuccessful.<br>**Fiv**|No deviations noted.<br>|
|**AWSCA-4.4:** S3-<br>Specific – S3<br>generates and stores<br>a one-way salted<br>HMAC of the<br>customer encryption<br>key. This salted<br>HMAC value is not<br>logged. <br>**-token**|CC6.1; <br>CC6.7 <br>**-wi**|Inquired of an S3 Software Development<br>Engineer to ascertain S3 generated and<br>stored a one-way salted HMAC of the<br>customer encryption key, and that the salted<br>HMAC value was not logged.<br>|No deviations noted.<br>|
|**AWSCA-4.4:** S3-<br>Specific – S3<br>generates and stores<br>a one-way salted<br>HMAC of the<br>customer encryption<br>key. This salted<br>HMAC value is not<br>logged. <br>**-token**|CC6.1; <br>CC6.7 <br>**-wi**|Observed an S3 Software Development<br>Engineer upload an encrypted object to S3<br>and inspected the metadata for the stored<br>object to ascertain the encryption<br>information included a one-way salted HMAC<br>of the customer encryption key.<br>|No deviations noted.<br>|


AWS Confidential


135


Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality, and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**





|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|||Observed an S3 Software Development<br>Engineer upload an encrypted object to S3<br>and searched the S3 host logs for the one-<br>way salted HMAC value to ascertain it was<br>not logged.<br>|No deviations noted.<br>**i2J**|
|||Observed an S3 Software Development<br>Engineer attempt to decrypt an object in S3<br>with an incorrect encryption key to ascertain<br>the decrypt function failed and the object<br>was unreadable.<br>**nIkL**|No deviations noted.<br>|
|**AWSCA-4.5:** KMS-<br>Specific – KMS keys<br>used for<br>cryptographic<br>operations in KMS<br>are logically secured<br>so that no AWS<br>employee can gain<br>access to the key<br>material. <br>**token**|CC6.1 <br>**-wi2**|Inquired of an AWS Cryptography Software<br>Development Engineer to ascertain no AWS<br>employee could gain logical access to the<br>hardened security modules where customer<br>keys were used for cryptographic operations.<br>**U4Ag**|No deviations noted.<br>|
|**AWSCA-4.5:** KMS-<br>Specific – KMS keys<br>used for<br>cryptographic<br>operations in KMS<br>are logically secured<br>so that no AWS<br>employee can gain<br>access to the key<br>material. <br>**token**|CC6.1 <br>**-wi2**|Inspected the configurations for gaining<br>logical access to the hardened security<br>module to ascertain KMS keys used for<br>cryptographic operations in KMS were<br>logically secured so that no AWS employee<br>could gain access to the key material.<br>**FivG**|No deviations noted.<br>|
|**AWSCA-4.5:** KMS-<br>Specific – KMS keys<br>used for<br>cryptographic<br>operations in KMS<br>are logically secured<br>so that no AWS<br>employee can gain<br>access to the key<br>material. <br>**token**|CC6.1 <br>**-wi2**|Inspected the KMS key material access<br>configurations to ascertain no single AWS<br>employee could modify rulesets, host or<br>operator membership to the domain of the<br>hardened security appliance.<br>|No deviations noted.<br>|
|**AWSCA-4.5:** KMS-<br>Specific – KMS keys<br>used for<br>cryptographic<br>operations in KMS<br>are logically secured<br>so that no AWS<br>employee can gain<br>access to the key<br>material. <br>**token**|CC6.1 <br>**-wi2**|Observed an AWS Cryptography Software<br>Development Engineer attempt to gain<br>logical access to the hardened security<br>module where customer keys were used in<br>memory to ascertain this was not possible.<br>|No deviations noted.<br>|


AWS Confidential


136




Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality, and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**







|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|||Observed an AWS Cryptography Software<br>Development Engineer attempt to remove a<br>host or operator without meeting the<br>quorum rules to ascertain the actions<br>resulted in a quorum rule error.<br>|No deviations noted.<br>**i2J**|
|**AWSCA-4.6:** KMS-<br>Specific – AWS<br>Services that<br>integrate with AWS<br>KMS for key<br>management use a<br>256-bit data key<br>locally to protect<br>customer content.<br>|CC6.1; <br>CC6.7 <br>|Inquired of an AWS Cryptography Technical<br>Program Manager to ascertain AWS Services<br>which integrate with AWS KMS for key<br>management used a 256-bit AES data key<br>locally to protect customer content.<br>**nIkL**|No deviations noted.<br>|
|**AWSCA-4.6:** KMS-<br>Specific – AWS<br>Services that<br>integrate with AWS<br>KMS for key<br>management use a<br>256-bit data key<br>locally to protect<br>customer content.<br>|CC6.1; <br>CC6.7 <br>|Inspected the API call configurations of the<br>services which integrated with KMS for<br>services that stored customer content to<br>ascertain each service was configured to<br>send 256-bit AES key requests to KMS.<br>**4Ag**|No deviations noted.<br>|
|**AWSCA-4.7:** KMS-<br>Specific – The key<br>provided by KMS to<br>integrated services is<br>a 256-bit key and is<br>encrypted with a<br>256-bit AES key<br>unique to the<br>customer’s AWS<br>account.<br>**m-token**|CC6.1; <br>CC6.7 <br>**-wi2**|Inquired of an AWS Cryptography Technical<br>Program Manager to ascertain keys provided<br>by KMS to integrated services were 256-bit<br>AES keys and were themselves encrypted by<br>256-bit AES keys unique to each customer’s<br>AWS account.<br>**ivGU**|No deviations noted.<br>|
|**AWSCA-4.7:** KMS-<br>Specific – The key<br>provided by KMS to<br>integrated services is<br>a 256-bit key and is<br>encrypted with a<br>256-bit AES key<br>unique to the<br>customer’s AWS<br>account.<br>**m-token**|CC6.1; <br>CC6.7 <br>**-wi2**|Inspected the KMS key creation configuration<br>to ascertain KMS keys created by KMS<br>utilized the AES-256 cryptographic algorithm.<br>|No deviations noted.<br>|
|**AWSCA-4.7:** KMS-<br>Specific – The key<br>provided by KMS to<br>integrated services is<br>a 256-bit key and is<br>encrypted with a<br>256-bit AES key<br>unique to the<br>customer’s AWS<br>account.<br>**m-token**|CC6.1; <br>CC6.7 <br>**-wi2**|Inspected the KMS encryption activity<br>configuration to ascertain 256-bit AES keys<br>were returned for 256-bit AES key requests<br>coming from the integrated KMS services to<br>encrypt customer data.<br>|No deviations noted.<br>|
|**AWSCA-4.7:** KMS-<br>Specific – The key<br>provided by KMS to<br>integrated services is<br>a 256-bit key and is<br>encrypted with a<br>256-bit AES key<br>unique to the<br>customer’s AWS<br>account.<br>**m-token**|CC6.1; <br>CC6.7 <br>**-wi2**|Observed an AWS Cryptography Software<br>Development Engineer create a resource<br>with content enabled for encryption using<br>KMS to ascertain a KMS key was used to<br>encrypt a 256-bit AES data encryption key<br>(which was used to encrypt the content) as<br>requested from the service.<br>|No deviations noted.<br>|


AWS Confidential


137




Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality, and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**





|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|||Observed an AWS Cryptography Software<br>Development Engineer create a resource<br>with content enabled for encryption using<br>KMS and then attempt to access the data<br>without decrypting to ascertain it was<br>unreadable.<br>**R**|No deviations noted.<br>**i2J**|
|||Observed an AWS Cryptography Software<br>Development Engineer create a resource<br>with content enabled for encryption using<br>KMS and then attempt to decrypt the data<br>using the required 256-bit AES data<br>encryption key to ascertain the data was<br>successfully decrypted.<br>**AgnIk**|No deviations noted.<br>|
|||Uploaded test data using a KMS-integrated<br>service encrypted with a data encryption key,<br>encrypted by a KMS key relating to an AWS<br>account and attempted to perform the same<br>activity, using another AWS account, calling<br>upon the same KMS key to observe an<br>upload failure occurred due to an<br>authorization failure caused by a mismatch<br>between the owner of the KMS key and the<br>AWS account.<br>**FivGU4**|No deviations noted.<br>|
|**AWSCA-4.8**: KMS-<br>Specific – Requests<br>in KMS are logged in<br>AWS CloudTrail.<br>**oken**|CC6.1 <br>**-wi**|Inquired of an AWS Cryptography Technical<br>Program Manager to ascertain API calls made<br>by the AWS services that integrate with KMS<br>were captured when the logging feature was<br>enabled.<br>|No deviations noted.<br>|
|**AWSCA-4.8**: KMS-<br>Specific – Requests<br>in KMS are logged in<br>AWS CloudTrail.<br>**oken**|CC6.1 <br>**-wi**|Inspected the configuration for KMS logging<br>to ascertain requests in KMS were designed<br>to be logged in AWS CloudTrail.<br>|No deviations noted.<br>|


AWS Confidential


138




Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality, and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**







|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|||Enabled CloudTrail logging on a service that<br>integrated with KMS, uploaded data using a<br>KMS key for encryption, and downloaded the<br>same file for decryption and inspected the<br>logs in AWS CloudTrail to ascertain activity<br>from both encryption and decryption API<br>calls was logged.<br>**LR**|No deviations noted.<br>**i2J**|
|**AWSCA-4.9:** KMS-<br>Specific – KMS<br>endpoints can only<br>be accessed by<br>customers using TLS<br>with cipher suites<br>that support forward<br>secrecy.<br>|CC6.1; <br>CC6.7 <br>**wi2**|Inquired of an AWS Cryptography Technical<br>Program Manager to ascertain KMS<br>endpoints could only be accessed using TLS<br>with cipher suites to support forward<br>secrecy.<br>**gnIk**|No deviations noted.<br>|
|**AWSCA-4.9:** KMS-<br>Specific – KMS<br>endpoints can only<br>be accessed by<br>customers using TLS<br>with cipher suites<br>that support forward<br>secrecy.<br>|CC6.1; <br>CC6.7 <br>**wi2**|Inspected the configuration for KMS TLS<br>communication to ascertain the cipher suites<br>listed supported forward secrecy.<br>**4A**|No deviations noted.<br>|
|**AWSCA-4.9:** KMS-<br>Specific – KMS<br>endpoints can only<br>be accessed by<br>customers using TLS<br>with cipher suites<br>that support forward<br>secrecy.<br>|CC6.1; <br>CC6.7 <br>**wi2**|Observed an AWS Security Assurance<br>Manager attempt to connect to a public KMS<br>service endpoint using an unsupported<br>cipher suite to ascertain the endpoints could<br>not be accessed.<br>**ivGU**|No deviations noted.<br>|
|**AWSCA-4.9:** KMS-<br>Specific – KMS<br>endpoints can only<br>be accessed by<br>customers using TLS<br>with cipher suites<br>that support forward<br>secrecy.<br>|CC6.1; <br>CC6.7 <br>**wi2**|Observed an AWS Security Assurance<br>Manager attempt to connect to a public KMS<br>service endpoint using a supported cipher<br>suite supporting forward secrecy to ascertain<br>the endpoint connection was successful.<br>|No deviations noted.<br>|
|**AWSCA-4.10:** KMS-<br>Specific – Keys used<br>in AWS KMS are only<br>used for a single<br>purpose as defined<br>by the key usage<br>parameter for each<br>key. <br>**m-toke**|CC6.1 <br>|Inquired of an AWS Cryptography Technical<br>Program Manager to ascertain keys used in<br>AWS KMS were only used for a single<br>purpose as defined by the key usage<br>parameter for each key.<br>|No deviations noted.<br>|
|**AWSCA-4.10:** KMS-<br>Specific – Keys used<br>in AWS KMS are only<br>used for a single<br>purpose as defined<br>by the key usage<br>parameter for each<br>key. <br>**m-toke**|CC6.1 <br>|Inspected the source code responsible for<br>AWS KMS key usage, to ascertain the key<br>usage parameter was configured at the key<br>level and that key operations required the<br>use of keys designated by the system for that<br>operation.<br>|No deviations noted.<br>|


AWS Confidential


139






Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality, and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**







|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|||Created an AWS KMS key and attempted to<br>perform a key operation in alignment with<br>the key usage parameter to ascertain the<br>operation was performed in accordance with<br>the set parameter.<br>|No deviations noted.<br>**i2J**|
|||Created an AWS KMS key and attempted to<br>perform a key operation not in alignment<br>with the key usage parameter to ascertain<br>the operation resulted in a key usage error.<br>**IkL**|No deviations noted.<br>|
|**AWSCA-4.11:** KMS-<br>Specific – KMS keys<br>created by KMS are<br>rotated on a defined<br>frequency if enabled<br>by the customer. <br>**n**|CC6.1; <br>CC6.7 <br>**-wi2**|Inquired of an AWS Cryptography Technical<br>Program Manager to ascertain the KMS<br>service included functionality for KMS keys to<br>be rotated on a defined frequency, if enabled<br>by the customer.<br>**4Agn**|No deviations noted.<br>|
|**AWSCA-4.11:** KMS-<br>Specific – KMS keys<br>created by KMS are<br>rotated on a defined<br>frequency if enabled<br>by the customer. <br>**n**|CC6.1; <br>CC6.7 <br>**-wi2**|Inspected the source code responsible for<br>KMS key rotation to ascertain a new backing<br>key would be created in accordance with the<br>customer defined frequency, if enabled.<br>**vGU**|No deviations noted.<br>|
|**AWSCA-4.11:** KMS-<br>Specific – KMS keys<br>created by KMS are<br>rotated on a defined<br>frequency if enabled<br>by the customer. <br>**n**|CC6.1; <br>CC6.7 <br>**-wi2**|Inspected the on-demand key rotation event<br>log for an AWS internal key to ascertain the<br>key was rotated immediately, and that the<br>rotation event was logged.<br>**Fi**|No deviations noted.<br>|
|**AWSCA-4.11:** KMS-<br>Specific – KMS keys<br>created by KMS are<br>rotated on a defined<br>frequency if enabled<br>by the customer. <br>**n**|CC6.1; <br>CC6.7 <br>**-wi2**|Inspected a scheduled key rotation event log<br>for an AWS internal key to ascertain the<br>backing key was rotated in accordance with<br>the defined frequency, and the rotation<br>event was logged.<br>|No deviations noted.<br>|
|**AWSCA-4.12:** KMS-<br>Specific – Recovery<br>key materials used<br>for disaster recovery<br>processes by KMS<br>are physically<br>**-tok**|CC6.1; <br>CC6.4 <br>|Inquired of an AWS Cryptography Technical<br>Program Manager to ascertain recovery key<br>materials used for disaster recovery<br>processes by KMS were physically secured<br>offline so that no single AWS employee could<br>gain access to the key material.<br>|No deviations noted.<br>|


AWS Confidential


140




Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality, and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**







|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|secured offline so<br>that no single AWS<br>employee can gain<br>access to the key<br>material.<br>||For all employees with physical access to the<br>recovery key material resources used for<br>disaster recovery processes by KMS,<br>inspected their job titles and reporting<br>structure within the employee directory tool,<br>to ascertain access privileges were<br>appropriate based on their roles and<br>responsibilities.<br>**kLR**|No deviations noted.<br>**i2J**|
|secured offline so<br>that no single AWS<br>employee can gain<br>access to the key<br>material.<br>||Inspected a physical access log of access<br>attempts to recovery key materials to<br>ascertain no single AWS employee could gain<br>access by themselves.<br>**gnI**|No deviations noted.<br>|
|**AWSCA-4.13:** KMS-<br>Specific – Access<br>attempts to recovery<br>key materials are<br>reviewed by<br>authorized operators<br>on a cadence<br>defined in team<br>documentation. <br>|CC6.1; <br>CC6.4 <br>|Inquired of an AWS Cryptography Technical<br>Program Manager to ascertain access<br>attempts to recovery key materials were<br>reviewed by authorized operators on a<br>cadence defined in team documentation.<br>**U4A**|No deviations noted.<br>|
|**AWSCA-4.13:** KMS-<br>Specific – Access<br>attempts to recovery<br>key materials are<br>reviewed by<br>authorized operators<br>on a cadence<br>defined in team<br>documentation. <br>|CC6.1; <br>CC6.4 <br>|Inspected the reviews of access attempts or<br>requests to recovery key materials to<br>ascertain reviews were performed and<br>documented by authorized operators on a<br>cadence defined in team documentation.<br>**FivG**|No deviations noted.<br>|
|**AWSCA-4.14:**KMS-<br>Specific – Each<br>production firmware<br>version release for<br>the AWS Key<br>Management Service<br>HSM (Hardware<br>**en**|CC6.1; <br>CC6.6; <br>CC6.7 <br>**-wi**|Inquired of an AWS Cryptography Technical<br>Program Manager to ascertain the<br>production firmware version of the AWS Key<br>Management Service HSM was certified with<br>NIST under the FIPS 140-2 level 3 standard or<br>is in the process of being certified under the<br>FIPS 140-3 level 3 standard.<br>|No deviations noted.<br>|


AWS Confidential


141




Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality, and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**







|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|Security Module)<br>either holds or is in<br>the process of<br>actively pursuing<br>FIPS-3 level 3<br>certification from<br>the National<br>Institute of<br>Standards and<br>Technology’s (NIST)<br>Cryptographic<br>Module Validation<br>Program (CMVP). <br>||For all in scope regions, inspected the<br>firmware version running on production AWS<br>Key Management Service HSM devices to<br>ascertain the production firmware version of<br>the AWS Key Management Service HSMs was<br>certified by NIST Cryptographic Module<br>Validation Program Certificate under the FIPS<br>140-2 level 3 standard or updated firmware<br>was in the process of being certified under<br>the FIPS 140-3 level 3 standard.<br>**gnIkLR**|No deviations noted.<br>**i2J**|
|**AWSCA-4.15**: <br>CloudHSM-Specific -<br>Production HSM<br>devices are received<br>in tamper evident<br>authenticable bags.<br>Tamper evident<br>authenticable bag<br>serial numbers and<br>production HSM<br>serial numbers are<br>verified against data<br>provided out-of-<br>band by the<br>manufacturer and<br>logged into tracking<br>systems by approved<br>individuals. <br>**m-token**|CC6.1; <br>CC6.4; <br>CC6.7 <br>**-wi2**|Inquired of a CloudHSM Technical Program<br>Manager to ascertain Production HSM<br>devices were received in tamper evident<br>authenticable bags and tamper evident<br>authenticable bag serial numbers and<br>production HSM serial numbers were<br>verified against data provided out-of-band<br>by the manufacturer and logged by<br>individuals approved for access to tracking<br>systems based on roles and responsibilities<br>in adherence with AWS security and<br>operational standards. <br>**FivGU4A**|No deviations noted.<br>|
|**AWSCA-4.15**: <br>CloudHSM-Specific -<br>Production HSM<br>devices are received<br>in tamper evident<br>authenticable bags.<br>Tamper evident<br>authenticable bag<br>serial numbers and<br>production HSM<br>serial numbers are<br>verified against data<br>provided out-of-<br>band by the<br>manufacturer and<br>logged into tracking<br>systems by approved<br>individuals. <br>**m-token**|CC6.1; <br>CC6.4; <br>CC6.7 <br>**-wi2**|Inspected the configuration of the<br>automated verifications performed prior to<br>moving an HSM device to production to<br>ascertain HSM serial numbers were verified<br>against data provided out-of-band before<br>entering production.<br>|No deviations noted.<br>|
|**AWSCA-4.15**: <br>CloudHSM-Specific -<br>Production HSM<br>devices are received<br>in tamper evident<br>authenticable bags.<br>Tamper evident<br>authenticable bag<br>serial numbers and<br>production HSM<br>serial numbers are<br>verified against data<br>provided out-of-<br>band by the<br>manufacturer and<br>logged into tracking<br>systems by approved<br>individuals. <br>**m-token**|CC6.1; <br>CC6.4; <br>CC6.7 <br>**-wi2**|For one HSM device that failed validation,<br>inspected the validations log to ascertain that<br>the HSM device was automatically prohibited<br>from entering production when the HSM<br>serial number could not be verified against<br>data provided out-of-band by the<br>manufacturer.<br>|No deviations noted.<br>|


AWS Confidential


142




Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality, and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**









|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|||For one production HSM device, inspected<br>the validations log to ascertain the HSM<br>device’s serial number was verified against<br>data provided out-of-band before it entered<br>into production.<br>|No deviations noted.<br>**i2J**|
|**AWSCA-5.1:** Physical<br>access to data<br>centers is approved<br>by an authorized<br>individual.<br>|CC6.4; <br>CC6.7 <br> <br>|Inquired of an AWS DC Security Senior Global<br>Program Manager to ascertain physical<br>access to data centers was approved by an<br>authorized individual.<br>**IkL**|No deviations noted.<br>|
|**AWSCA-5.1:** Physical<br>access to data<br>centers is approved<br>by an authorized<br>individual.<br>|CC6.4; <br>CC6.7 <br> <br>|Inspected the configuration for executing the<br>physical access approval and provisioning<br>within the data center access management<br>system to ascertain physical access to data<br>centers was designed to be granted after an<br>approval by an authorized individual.<br>**4Agn**|No deviations noted.<br>|
|**AWSCA-5.1:** Physical<br>access to data<br>centers is approved<br>by an authorized<br>individual.<br>|CC6.4; <br>CC6.7 <br> <br>|For one user provisioned data center access<br>during the period, inspected the data center<br>physical access provisioning records to<br>ascertain physical access was granted after it<br>was approved by an authorized individual.<br>**ivGU**|No deviations noted.<br>|
|**AWSCA-5.2:** Physical<br>access is revoked<br>within 24 hours of<br>the employee or<br>vendor record being<br>deactivated.<br>**m-token**|CC6.4; <br>CC6.7 <br> <br>**-wi**|Inquired of an AWS DC Security Senior Global<br>Program Manager to ascertain physical<br>access was automatically revoked within 24<br>hours of the employee or vendor record<br>being deactivated.<br>|No deviations noted.<br>|
|**AWSCA-5.2:** Physical<br>access is revoked<br>within 24 hours of<br>the employee or<br>vendor record being<br>deactivated.<br>**m-token**|CC6.4; <br>CC6.7 <br> <br>**-wi**|Inspected the system configurations within<br>the data center access management system<br>to ascertain physical access was<br>automatically revoked within 24 hours of the<br>employee, contractor or vendor record being<br>deactivated in the HR system.<br>|No deviations noted.<br>|
|**AWSCA-5.2:** Physical<br>access is revoked<br>within 24 hours of<br>the employee or<br>vendor record being<br>deactivated.<br>**m-token**|CC6.4; <br>CC6.7 <br> <br>**-wi**|For one terminated employee, inspected the<br>HR System record to ascertain physical access<br>was systematically revoked within 24 hours<br>of the employee record being deactivated in<br>the HR system by the access provisioning<br>system.<br>|No deviations noted.<br>|


AWS Confidential


143


Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality, and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**







|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|**AWSCA-5.3:** Physical<br>access to data<br>centers is reviewed<br>on a quarterly basis<br>by appropriate<br>personnel.<br>|CC6.4; <br>CC6.7 <br> <br>|Inquired of an AWS DC Security Global<br>Program Manager to ascertain physical<br>access to data centers was reviewed on a<br>quarterly basis by appropriate personnel.<br>|No deviations noted.<br>**2J**|
|**AWSCA-5.3:** Physical<br>access to data<br>centers is reviewed<br>on a quarterly basis<br>by appropriate<br>personnel.<br>|CC6.4; <br>CC6.7 <br> <br>|Inspected most recent quarterly physical<br>access review to ascertain that reviews of<br>physical access were completed at least once<br>per quarter.<br>**IkL**|No deviations noted.<br>|
|**AWSCA-5.3:** Physical<br>access to data<br>centers is reviewed<br>on a quarterly basis<br>by appropriate<br>personnel.<br>|CC6.4; <br>CC6.7 <br> <br>|For one user marked for removal during the<br>most recent quarterly physical access review,<br>inspected the CloudWatch logs for<br>revocation activities to ascertain the user's<br>access was appropriately removed from the<br>data center access management system.<br>**4Agn**|No deviations noted.<br>|
|**AWSCA-5.3:** Physical<br>access to data<br>centers is reviewed<br>on a quarterly basis<br>by appropriate<br>personnel.<br>|CC6.4; <br>CC6.7 <br> <br>|For a sample of users who had data center<br>access selected from a listing of in-scope<br>data center access levels within the period,<br>inspected the access reviews to ascertain the<br>reviews were performed quarterly and that<br>access was approved by appropriate<br>personnel. <br>**FivGU**|No deviations noted.<br>|
|**AWSCA-5.4:** CCTV<br>are used to monitor<br>server locations in<br>data centers. Images<br>are retained for 90<br>days, unless limited<br>by legal or<br>contractual<br>obligations.<br>**m-token**|CC6.4 <br>**-w**|Inquired of an AWS Security Industry<br>Specialist to ascertain physical access points<br>to server locations were monitored by a<br>closed circuit television camera (CCTV) and<br>that images were retained for 90 days unless<br>limited by legal or contractual obligations.<br>|No deviations noted.<br>|
|**AWSCA-5.4:** CCTV<br>are used to monitor<br>server locations in<br>data centers. Images<br>are retained for 90<br>days, unless limited<br>by legal or<br>contractual<br>obligations.<br>**m-token**|CC6.4 <br>**-w**|For a sample of data centers selected from<br>the asset management tool, observed the<br>CCTV footage or inspected screenshots of<br>video recordings around server location<br>access points, to ascertain physical access<br>points to server locations were recorded. <br>|No deviations noted.<br>|


AWS Confidential


144






Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality, and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**











|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|||For a sample of data centers selected from<br>the asset management tool, inspected the<br>network video recorder configuration to<br>ascertain CCTV images to server locations<br>were retained for at least 90 days, unless<br>limited by legal or contractual obligations.<br>**R**|No deviations noted.<br>**i2J**|
|**AWSCA-5.5:** Access<br>to server locations is<br>managed by<br>electronic access<br>control devices.<br>|CC6.4 <br>|Inquired of an AWS DC Security Senior<br>Program Manager to ascertain physical<br>access points to server locations were<br>managed by electronic access control<br>devices.<br>**gnIk**|No deviations noted.<br>|
|**AWSCA-5.5:** Access<br>to server locations is<br>managed by<br>electronic access<br>control devices.<br>|CC6.4 <br>|For a sample of data centers selected from<br>the asset management tool, observed<br>electronic access control devices at physical<br>access points to server locations or inspected<br>the physical security access control<br>configurations to ascertain electronic access<br>control devices were installed at physical<br>access points to server locations and that<br>they required authorized Amazon badges<br>with corresponding PINs to enter server<br>locations.<br>**ivGU4A**|No deviations noted.<br>|
|**AWSCA-5.6:** <br>Electronic intrusion<br>detection systems<br>are installed within<br>data server locations<br>to monitor, detect,<br>and automatically<br>alert appropriate<br>personnel of security<br>incidents.<br>**oken**|CC7.2; <br>CC7.3 <br>**-wi**|Inquired of an AWS Security Industry<br>Specialist to ascertain electronic intrusion<br>detection systems were installed and capable<br>of detecting breaches into data center server<br>locations.<br> <br> <br> <br> <br>|No deviations noted.<br>|


AWS Confidential


145


Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality, and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**





|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|||For a sample of data centers selected from<br>the asset management tool, observed on-<br>premise electronic intrusion detection<br>systems or inspected the physical security<br>access control configurations to ascertain<br>electronic intrusion detection systems were<br>installed, that they were capable of detecting<br>intrusion attempts, and that they<br>automatically alerted security personnel of<br>detected events for investigation and<br>resolution.<br>**nIkLR**|No deviations noted.<br>**i2J**|
|**AWSCA-5.7:** <br>Amazon-owned data<br>centers are<br>protected by fire<br>detection and<br>suppression systems.<br>|A1.2 <br>**i2**|Inquired of Data Center Operations<br>Managers to ascertain Amazon-owned data<br>centers were protected by fire detection and<br>fire suppression systems.<br>**4Ag**|No deviations noted.<br>|
|**AWSCA-5.7:** <br>Amazon-owned data<br>centers are<br>protected by fire<br>detection and<br>suppression systems.<br>|A1.2 <br>**i2**|For a sample of Amazon-owned data centers<br>selected from the asset management tool,<br>observed on-premise fire detection systems<br>to ascertain they were located throughout<br>the data centers.<br>**vGU**|No deviations noted.<br>|
|**AWSCA-5.7:** <br>Amazon-owned data<br>centers are<br>protected by fire<br>detection and<br>suppression systems.<br>|A1.2 <br>**i2**|For a sample of Amazon-owned data centers,<br>observed on-premise fire suppression<br>devices to ascertain they were located<br>throughout the data centers.<br>**F**|No deviations noted.<br>|
|**AWSCA-5.8:** <br>Amazon-owned data<br>centers are air<br>conditioned to<br>maintain appropriate<br>environmental<br>conditions.<br>Personnel and<br>systems monitor and<br>control air<br>temperature and<br>humidity at<br>appropriate levels.<br>**m-token**|A1.2 <br>**-**|Inquired of Data Center Operations<br>Managers to ascertain Amazon-owned data<br>centers were air conditioned to maintain<br>appropriate environmental conditions and<br>that the units were monitored by personnel<br>and systems to control air temperature and<br>humidity at appropriate levels.<br>|No deviations noted.<br>|
|**AWSCA-5.8:** <br>Amazon-owned data<br>centers are air<br>conditioned to<br>maintain appropriate<br>environmental<br>conditions.<br>Personnel and<br>systems monitor and<br>control air<br>temperature and<br>humidity at<br>appropriate levels.<br>**m-token**|A1.2 <br>**-**|For a sample of Amazon-owned data centers<br>selected from the asset management tool,<br>observed on-premise air-conditioning<br>systems to ascertain they monitored and<br>controlled temperature and humidity at<br>appropriate levels.<br>|No deviations noted.<br>|


AWS Confidential


146




Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality, and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**





|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|**AWSCA-5.9:** <br>Uninterruptible<br>Power Supply (UPS)<br>units provide backup<br>power in the event<br>of an electrical<br>failure in Amazon-<br>owned data centers<br>and third-party<br>colocation sites<br>where Amazon<br>maintains the UPS<br>units.<br>|A1.2 <br>**i2**|Inquired of Data Center Operations<br>Managers and Hardware Engineering<br>Services Software Development Engineer to<br>ascertain UPS units provided backup power<br>in the event of an electrical failure in<br>Amazon-owned data centers and in<br>colocation sites where Amazon maintains the<br>UPS units.<br>**kLR**|No deviations noted.<br>**i2J**|
|**AWSCA-5.9:** <br>Uninterruptible<br>Power Supply (UPS)<br>units provide backup<br>power in the event<br>of an electrical<br>failure in Amazon-<br>owned data centers<br>and third-party<br>colocation sites<br>where Amazon<br>maintains the UPS<br>units.<br>|A1.2 <br>**i2**|Inspected the system configuration<br>responsible for the automatic onboarding<br>and continuous monitoring of the health of<br>Amazon maintained backup battery units<br>(BBU) to ascertain that BBUs were being<br>monitored and would send an alert in the<br>event of an electrical failure.<br>**4AgnI**|No deviations noted.<br>|
|**AWSCA-5.9:** <br>Uninterruptible<br>Power Supply (UPS)<br>units provide backup<br>power in the event<br>of an electrical<br>failure in Amazon-<br>owned data centers<br>and third-party<br>colocation sites<br>where Amazon<br>maintains the UPS<br>units.<br>|A1.2 <br>**i2**|For a sample third-party colocation site,<br>inspected evidence that BBUs were being<br>monitored and would send an alert in the<br>event of an electrical failure.<br>**vGU**|No deviations noted.<br>|
|**AWSCA-5.9:** <br>Uninterruptible<br>Power Supply (UPS)<br>units provide backup<br>power in the event<br>of an electrical<br>failure in Amazon-<br>owned data centers<br>and third-party<br>colocation sites<br>where Amazon<br>maintains the UPS<br>units.<br>|A1.2 <br>**i2**|For a sample of Amazon-owned data centers<br>selected from the asset management tool,<br>observed on-premise UPS equipment to<br>ascertain UPS units were configured to<br>provide backup power in the event of an<br>electrical failure.<br>**Fi**|No deviations noted.<br>|
|**AWSCA-5.10:** <br>Amazon-owned data<br>centers have<br>generators to<br>provide backup<br>power in case of<br>electrical failure.<br>**m-token**|A1.2 <br>|Inquired of Data Center Operations<br>Managers to ascertain Amazon-owned data<br>centers had generators to provide backup<br>power in case of utility power failure.<br>|No deviations noted.<br>|
|**AWSCA-5.10:** <br>Amazon-owned data<br>centers have<br>generators to<br>provide backup<br>power in case of<br>electrical failure.<br>**m-token**|A1.2 <br>|For a sample of Amazon-owned data centers<br>selected from the asset management tool,<br>observed on-premise generator equipment<br>to ascertain generators were configured to<br>provide backup power in case of electrical<br>failure.<br>|No deviations noted.<br>|


AWS Confidential


147




Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality, and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**







|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|**AWSCA-5.11:** <br>Contracts are in<br>place with third-<br>party colocation<br>service providers<br>which include<br>provisions to provide<br>fire suppression<br>systems, air<br>conditioning to<br>maintain appropriate<br>atmospheric<br>conditions,<br>Uninterruptible<br>Power Supply (UPS)<br>units (unless<br>maintained by<br>Amazon), and<br>redundant power<br>supplies. Contracts<br>also include<br>provisions requiring<br>communication of<br>incidents or events<br>that impact Amazon<br>assets and/or<br>customers to AWS.<br>|CC7.3; <br>CC7.4; <br>CC7.5; <br>CC9.2; <br>A1.2 <br>**i2**|Inquired of AWS Legal Corporate Counsel to<br>ascertain contracts were in place at the<br>colocation service providers which included<br>provisions for fire suppression systems, air<br>conditioning, UPS units, and redundant<br>power supplies as well as provisions requiring<br>communication of incidents or events that<br>impacted Amazon assets or customers to<br>AWS.<br>**IkLR**|No deviations noted.<br>**i2J**|
|**AWSCA-5.11:** <br>Contracts are in<br>place with third-<br>party colocation<br>service providers<br>which include<br>provisions to provide<br>fire suppression<br>systems, air<br>conditioning to<br>maintain appropriate<br>atmospheric<br>conditions,<br>Uninterruptible<br>Power Supply (UPS)<br>units (unless<br>maintained by<br>Amazon), and<br>redundant power<br>supplies. Contracts<br>also include<br>provisions requiring<br>communication of<br>incidents or events<br>that impact Amazon<br>assets and/or<br>customers to AWS.<br>|CC7.3; <br>CC7.4; <br>CC7.5; <br>CC9.2; <br>A1.2 <br>**i2**|For a sample of data centers managed by<br>colocation service providers selected from<br>the asset management tool, inspected the<br>current contractual agreements between<br>service providers and AWS to ascertain they<br>included provisions for fire suppression<br>systems, air conditioning, UPS units, and<br>redundant power supplies as well as<br>provisions requiring colocation service<br>providers to notify Amazon immediately of<br>discovery of any unauthorized use or<br>disclosure of confidential information or any<br>other breach.<br>**FivGU4Agn**|No deviations noted.<br>|
|**AWSCA-5.12:** AWS<br>performs periodic<br>reviews of colocation<br>service providers to<br>validate adherence<br>with AWS security<br>and operational<br>standards.<br>**m-token**|CC3.2; <br>CC3.3; <br>CC3.4; <br>CC4.1; <br>CC7.3; <br>CC7.4; <br>CC7.5; <br>CC9.2; <br>A1.2 <br>**-**|Inquired of a Sr. Security Engineer, AWS<br>Infrastructure Security to ascertain periodic<br>reviews were performed for colocation<br>vendor relationships to validate adherence<br>with AWS security and operational standards.<br>|No deviations noted.<br>|
|**AWSCA-5.12:** AWS<br>performs periodic<br>reviews of colocation<br>service providers to<br>validate adherence<br>with AWS security<br>and operational<br>standards.<br>**m-token**|CC3.2; <br>CC3.3; <br>CC3.4; <br>CC4.1; <br>CC7.3; <br>CC7.4; <br>CC7.5; <br>CC9.2; <br>A1.2 <br>**-**|For a sample of data centers managed by<br>colocation service providers selected from<br>the asset management tool, inspected the<br>corresponding vendor reviews to ascertain<br>they were performed in accordance with the<br>colocation business review schedule and<br>included an evaluation of adherence to AWS<br>security and operational standards.<br>|No deviations noted.<br>|


AWS Confidential


148




Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality, and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**







|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|**AWSCA-5.13**: All<br>AWS production<br>media is securely<br>decommissioned and<br>physically destroyed,<br>verified by two<br>personnel, prior to<br>leaving AWS control.<br>|CC6.5; <br>CC6.7; <br>C1.2; <br>P4.3 <br>**-wi2**|Inquired of an AWS Infrastructure Security Sr.<br>Technical Program Manager and Data Center<br>Operations Managers to ascertain AWS<br>production media was securely<br>decommissioned and physically destroyed<br>prior to leaving AWS control.<br>**R**|No deviations noted.<br>**i2J**|
|**AWSCA-5.13**: All<br>AWS production<br>media is securely<br>decommissioned and<br>physically destroyed,<br>verified by two<br>personnel, prior to<br>leaving AWS control.<br>|CC6.5; <br>CC6.7; <br>C1.2; <br>P4.3 <br>**-wi2**|Inspected the AWS Media Destruction<br>Standard Operating Procedures document to<br>ascertain that it included procedures for data<br>center personnel to securely decommission<br>production media prior to leaving AWS<br>control.<br>**gnIk**|No deviations noted.<br>|
|**AWSCA-5.13**: All<br>AWS production<br>media is securely<br>decommissioned and<br>physically destroyed,<br>verified by two<br>personnel, prior to<br>leaving AWS control.<br>|CC6.5; <br>CC6.7; <br>C1.2; <br>P4.3 <br>**-wi2**|For a sample of data centers selected from<br>the asset management tool, observed on-<br>premise security practices to ascertain<br>production media was restricted to the AWS<br>control, unless securely decommissioned and<br>physically destroyed.<br>**GU4A**|No deviations noted.<br>|
|**AWSCA-5.13**: All<br>AWS production<br>media is securely<br>decommissioned and<br>physically destroyed,<br>verified by two<br>personnel, prior to<br>leaving AWS control.<br>|CC6.5; <br>CC6.7; <br>C1.2; <br>P4.3 <br>**-wi2**|For a sample of data centers selected from<br>the asset management tool, observed on-<br>premise equipment and media or inspected<br>media destruction logs for secure<br>decommissioning and physical destruction to<br>ascertain production media was securely<br>decommissioned, physically destroyed, and<br>verified by two personnel prior to leaving<br>AWS control. <br>**Fiv**|No deviations noted.<br>|
|**AWSCA-6.1:** AWS<br>applies a systematic<br>approach to<br>managing change to<br>ensure changes to<br>customer-impacting<br>aspects of a service<br>are reviewed, tested<br>**-toke**|CC6.1; <br>CC6.8; <br>CC7.5; <br>CC8.1 <br>|Inquired of Software Development Managers<br>to ascertain customer-impacting changes of<br>service to the production environment were<br>reviewed, tested, approved, and followed<br>relevant change management guidelines and<br>that service-specific change management<br>processes were maintained, followed, and<br>communicated to the service teams.<br>|No deviations noted.<br>|


AWS Confidential


149




Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality, and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**







|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|and approved.<br>Change management<br>policies/procedures<br>are based on<br>Amazon guidelines<br>and tailored to the<br>specifics of each<br>AWS service.<br>||For one sampled service, inspected the<br>relevant change management guidelines to<br>ascertain they communicated specific<br>guidance on change management processes,<br>including initiation, testing and approval, and<br>that service team-specific steps were<br>documented and maintained by the teams.<br>**LR**|No deviations noted.<br>**i2J**|
|**AWSCA-6.2:** Change<br>details are<br>documented within<br>one of Amazon’s<br>change management<br>or deployment tools.<br>|CC6.8; <br>CC8.1 <br>|Inquired of Software Development Managers<br>to ascertain changes were documented<br>within one of Amazon's change management<br>or deployment tools.<br>**gnIk**|No deviations noted.<br>|
|**AWSCA-6.2:** Change<br>details are<br>documented within<br>one of Amazon’s<br>change management<br>or deployment tools.<br>|CC6.8; <br>CC8.1 <br>|For a sample of changes selected from a<br>system-generated listing of changes<br>deployed to production, inspected Amazon’s<br>change management or deployment tools to<br>ascertain the change details were<br>documented and communicated to service<br>team management.<br>**GU4A**|No deviations noted.<br>|
|**AWSCA-6.3:** Changes<br>are tested according<br>to service team<br>change management<br>policies/procedures<br>prior to migration to<br>production.<br>**ken**|CC6.8; <br>CC8.1 <br>**-wi2**|Inquired of Software Development Managers<br>to ascertain changes were tested according<br>to service team change management<br>standards prior to migration to production.<br>**Fiv**|No deviations noted.<br>|
|**AWSCA-6.3:** Changes<br>are tested according<br>to service team<br>change management<br>policies/procedures<br>prior to migration to<br>production.<br>**ken**|CC6.8; <br>CC8.1 <br>**-wi2**|For a sample of changes selected from a<br>system-generated listing of changes migrated<br>to production, inspected the change<br>management policy to ascertain changes<br>were tested according to service team<br>change management standards and testing<br>occurred in a development environment<br>prior to migration to production.<br>|No deviations noted.<br>|
|**AWSCA-6.4**: AWS<br>maintains separate<br>production and<br>development<br>environments.<br>**m-to**|CC6.8; <br>CC8.1 <br>|Inquired of Software Development Managers<br>to ascertain AWS maintained separate<br>production and development environments.<br> <br> <br>|No deviations noted.<br>|


AWS Confidential


150




Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality, and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**







|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|||For a sample of changes selected from a<br>system-generated listing of changes<br>deployed to production, inspected the<br>related deployment pipelines to ascertain the<br>production and development environments<br>were separate.<br>**R**|No deviations noted.<br>**i2J**|
|**AWSCA-6.5:** Changes<br>are reviewed for<br>business impact and<br>approved by<br>authorized<br>personnel prior to<br>migration to<br>production according<br>to service team<br>change management<br>policies/procedures.<br>**ken**|CC6.8; <br>CC8.1 <br>**-wi2**|Inquired of Software Development Managers<br>to ascertain changes were reviewed for<br>business impact and approved by authorized<br>personnel prior to migration to production<br>according to service team change<br>management standards.<br>**gnIk**|No deviations noted.<br>|
|**AWSCA-6.5:** Changes<br>are reviewed for<br>business impact and<br>approved by<br>authorized<br>personnel prior to<br>migration to<br>production according<br>to service team<br>change management<br>policies/procedures.<br>**ken**|CC6.8; <br>CC8.1 <br>**-wi2**|For a sample of changes selected from a<br>system-generated listing of changes migrated<br>to production, inspected the relevant change<br>management or deployment tools to<br>ascertain changes were reviewed and<br>approved by authorized personnel prior to<br>migration to production according to service<br>team change management standards.<br>**vGU4A**|No deviations noted.<br>|
|**AWSCA-6.5:** Changes<br>are reviewed for<br>business impact and<br>approved by<br>authorized<br>personnel prior to<br>migration to<br>production according<br>to service team<br>change management<br>policies/procedures.<br>**ken**|CC6.8; <br>CC8.1 <br>**-wi2**|Inspected the configurations in-place for<br>publishing AWS managed IAM policies to<br>ascertain that policies were designed to<br>require approvals prior to being moved to<br>production.<br>**F**|No deviations noted.<br>|
|**AWSCA-6.5:** Changes<br>are reviewed for<br>business impact and<br>approved by<br>authorized<br>personnel prior to<br>migration to<br>production according<br>to service team<br>change management<br>policies/procedures.<br>**ken**|CC6.8; <br>CC8.1 <br>**-wi2**|Inspected an AWS managed IAM policy to<br>ascertain that the policy managed by AWS<br>was approved prior to being moved to<br>production.<br>|No deviations noted.<br>|


AWS Confidential


151




Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality, and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**







|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|**AWSCA-6.6:** AWS<br>performs<br>deployment<br>validations and<br>change reviews to<br>detect unauthorized<br>changes to its<br>environment and<br>tracks identified<br>issues to resolution.<br>**m-token**|CC6.8; <br>CC7.1; <br>CC8.1 <br>**-wi2**|Inquired of Software Development Managers<br>to ascertain AWS performed deployment<br>validations and change reviews to detect<br>changes that did not follow the change<br>management process and that appropriate<br>actions were taken to track identified issues<br>to resolution.<br> <br>**kLR**|No deviations noted.<br>**i2J**|
|**AWSCA-6.6:** AWS<br>performs<br>deployment<br>validations and<br>change reviews to<br>detect unauthorized<br>changes to its<br>environment and<br>tracks identified<br>issues to resolution.<br>**m-token**|CC6.8; <br>CC7.1; <br>CC8.1 <br>**-wi2**|For a sample of changes migrated to<br>production, inspected the associated<br>validation output to ascertain AWS<br>performed deployment validations and<br>change reviews to detect unauthorized<br>changes and that follow-up actions were<br>taken as necessary to remediate any issues<br>identified.<br>**U4AgnI**|No deviations noted.<br>|
|**AWSCA-6.6:** AWS<br>performs<br>deployment<br>validations and<br>change reviews to<br>detect unauthorized<br>changes to its<br>environment and<br>tracks identified<br>issues to resolution.<br>**m-token**|CC6.8; <br>CC7.1; <br>CC8.1 <br>**-wi2**|For a sample of quarters, inspected the<br>quarterly security business reviews and the<br>contents of the deployment violations<br>dashboard to ascertain unauthorized changes<br>were reviewed by AWS management.<br>**ivG**|No deviations noted.<br> <br>|
|**AWSCA-6.6:** AWS<br>performs<br>deployment<br>validations and<br>change reviews to<br>detect unauthorized<br>changes to its<br>environment and<br>tracks identified<br>issues to resolution.<br>**m-token**|CC6.8; <br>CC7.1; <br>CC8.1 <br>**-wi2**|For a sample of months for all services not<br>enrolled in automated deployment<br>monitoring, inspected manual deployment<br>monitoring to ascertain that the related AWS<br>service team generated a listing of all<br>changes deployed to production during the<br>month, assessed the changes for<br>appropriateness, and follow-up actions were<br>taken as necessary to remediate any issues<br>identified.<br>|No deviations noted.<br>|
|**AWSCA-6.6:** AWS<br>performs<br>deployment<br>validations and<br>change reviews to<br>detect unauthorized<br>changes to its<br>environment and<br>tracks identified<br>issues to resolution.<br>**m-token**|CC6.8; <br>CC7.1; <br>CC8.1 <br>**-wi2**|For a sample of months and services,<br>inspected the contents of the deployment<br>violation dashboard to ascertain<br>unauthorized changes were tracked to<br>resolution by AWS management. <br>|No deviations noted.<br>|


AWS Confidential


152




Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality, and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**







|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|||For a sample of GRC IDs, inspected the<br>quarterly GRC baseline review to ascertain<br>that GRC IDs were reviewed to ensure that<br>all compliance-impacting change processes<br>were registered in the automated change<br>management monitoring tool.<br>**LR**|No deviations noted.<br>**i2J**|
|**AWSCA-6.7**: <br>Customer<br>information,<br>including personal<br>information, and<br>customer content<br>are not used in test<br>and development<br>environments.<br>|CC8.1 <br>|Inquired of software development managers,<br>to ascertain production data, including<br>customer content and AWS employee data,<br>were not used in test or development<br>environments.<br>**gnIk**|No deviations noted.<br>|
|**AWSCA-6.7**: <br>Customer<br>information,<br>including personal<br>information, and<br>customer content<br>are not used in test<br>and development<br>environments.<br>|CC8.1 <br>|Inspected the contents of the Secure<br>Software Development Policy intended for<br>software development engineers and<br>software development managers throughout<br>AWS to ascertain it provided instructions to<br>not use production data in test or<br>development environments.<br>**GU4A**|No deviations noted.<br>|
|**AWSCA-7.1**: S3-<br>Specific – S3<br>compares checksums<br>to validate the<br>integrity of data in<br>transit. If the<br>customer provided<br>or automatically<br>calculated checksum<br>does not match the<br>S3’s server-side<br>checksum validation,<br>the upload will fail,<br>preventing<br>corrupted data from<br>being written to S3.<br>**m-token**|CC6.7 <br>**-wi2**|Inquired of an S3 Software Development<br>Manager to ascertain S3 compared<br>checksums to validate the integrity of data in<br>transit. If the customer provided or<br>automatically calculated checksum did not<br>match the S3’s server-side checksum<br>validation, the upload would fail, preventing<br>corrupted data from being written to S3.<br>**Fiv**|No deviations noted.<br>|
|**AWSCA-7.1**: S3-<br>Specific – S3<br>compares checksums<br>to validate the<br>integrity of data in<br>transit. If the<br>customer provided<br>or automatically<br>calculated checksum<br>does not match the<br>S3’s server-side<br>checksum validation,<br>the upload will fail,<br>preventing<br>corrupted data from<br>being written to S3.<br>**m-token**|CC6.7 <br>**-wi2**|Inspected the checksum configurations to<br>ascertain S3 was configured to continually<br>compare the user provided or automatically<br>calculated checksums with the S3’s server-<br>side checksums to validate the integrity of<br>data in transit.<br>|No deviations noted.<br>|
|**AWSCA-7.1**: S3-<br>Specific – S3<br>compares checksums<br>to validate the<br>integrity of data in<br>transit. If the<br>customer provided<br>or automatically<br>calculated checksum<br>does not match the<br>S3’s server-side<br>checksum validation,<br>the upload will fail,<br>preventing<br>corrupted data from<br>being written to S3.<br>**m-token**|CC6.7 <br>**-wi2**|Observed an S3 Software Development<br>Engineer upload a file with an invalid<br>checksum, to ascertain the transfer was<br>aborted and an error message was displayed.<br>|No deviations noted.<br>|


AWS Confidential


153


Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality, and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**





|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|||Observed an S3 Software Development<br>Engineer upload a file with a valid checksum<br>that matched the S3 calculated checksum to<br>ascertain the transfer was completed<br>successfully.<br>|No deviations noted.<br>**i2J**|
|**AWSCA-7.2:** S3-<br>Specific – S3<br>performs continuous<br>integrity checks of<br>the data at rest.<br>Objects are<br>continuously<br>validated against<br>their checksums to<br>prevent object<br>corruption.<br>**-token**|C1.1 <br>**-wi2**|Inquired of an S3 Software Development<br>Engineer to ascertain S3 performed<br>continuous integrity checks of the data at<br>rest and that objects were automatically<br>validated against their checksums to prevent<br>object corruption.<br>**gnIkL**|No deviations noted.<br>|
|**AWSCA-7.2:** S3-<br>Specific – S3<br>performs continuous<br>integrity checks of<br>the data at rest.<br>Objects are<br>continuously<br>validated against<br>their checksums to<br>prevent object<br>corruption.<br>**-token**|C1.1 <br>**-wi2**|Inspected the integrity checks configurations<br>to determine S3 was configured to<br>continually perform integrity checks of the<br>data at rest and validated against their<br>checksums.<br>**U4A**|No deviations noted.<br>|
|**AWSCA-7.2:** S3-<br>Specific – S3<br>performs continuous<br>integrity checks of<br>the data at rest.<br>Objects are<br>continuously<br>validated against<br>their checksums to<br>prevent object<br>corruption.<br>**-token**|C1.1 <br>**-wi2**|Observed an S3 Software Development<br>Engineer locate an object whose checksum<br>was not validated against its object locator,<br>to ascertain the object was automatically<br>detected by the S3 service to prevent object<br>corruption.<br>**FivG**|No deviations noted<br>|
|**AWSCA-7.2:** S3-<br>Specific – S3<br>performs continuous<br>integrity checks of<br>the data at rest.<br>Objects are<br>continuously<br>validated against<br>their checksums to<br>prevent object<br>corruption.<br>**-token**|C1.1 <br>**-wi2**|Inspected system log files for an object at<br>rest to ascertain checksums were utilized to<br>assess the continuous integrity checks of<br>data.<br>|No deviations noted.<br>|
|**AWSCA-7.2:** S3-<br>Specific – S3<br>performs continuous<br>integrity checks of<br>the data at rest.<br>Objects are<br>continuously<br>validated against<br>their checksums to<br>prevent object<br>corruption.<br>**-token**|C1.1 <br>**-wi2**|Inspected the S3 logs to ascertain S3 was<br>designed to automatically attempt to restore<br>normal levels of object storage redundancy<br>when disk corruption or device failure was<br>detected.<br>|No deviations noted.<br>|


AWS Confidential


154




Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality, and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**







|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|**AWSCA-7.3:** S3-<br>Specific – When disk<br>corruption or device<br>failure is detected,<br>the system<br>automatically<br>attempts to restore<br>normal levels of<br>object storage<br>redundancy.<br>|A1.2; <br>C1.1 <br>|Inquired of an S3 Software Development<br>Engineer to ascertain when disk corruption<br>or device failure was detected, the system<br>automatically attempted to restore normal<br>levels of object storage redundancy. <br>|No deviations noted.<br>**i2J**|
|**AWSCA-7.3:** S3-<br>Specific – When disk<br>corruption or device<br>failure is detected,<br>the system<br>automatically<br>attempts to restore<br>normal levels of<br>object storage<br>redundancy.<br>|A1.2; <br>C1.1 <br>|Inspected the system repair configurations<br>to ascertain S3 was configured to<br>automatically attempt to restore object<br>storage redundancy when disk corruption or<br>device failure was detected.<br>**gnIkL**|No deviations noted<br>|
|**AWSCA-7.3:** S3-<br>Specific – When disk<br>corruption or device<br>failure is detected,<br>the system<br>automatically<br>attempts to restore<br>normal levels of<br>object storage<br>redundancy.<br>|A1.2; <br>C1.1 <br>|Inspected the S3 logs to ascertain S3 was<br>designed to automatically attempt to restore<br>normal levels of object storage redundancy<br>when disk corruption or device failure was<br>detected.<br>**U4A**|No deviations noted<br>|
|**AWSCA-7.3:** S3-<br>Specific – When disk<br>corruption or device<br>failure is detected,<br>the system<br>automatically<br>attempts to restore<br>normal levels of<br>object storage<br>redundancy.<br>|A1.2; <br>C1.1 <br>|Observed an S3 Software Development<br>Engineer locate an object that was corrupted<br>or suffered device failure to ascertain the<br>object was rewritten to a known location,<br>which restored normal levels of object<br>storage redundancy.<br>**FivG**|No deviations noted.<br>|
|**AWSCA-7.4:** S3-<br>Specific – Objects are<br>stored redundantly<br>across multiple fault-<br>isolated facilities.<br>**m-token**|A1.2; <br>C1.1 <br>**-w**|Inquired of an S3 Software Development<br>Engineer to ascertain objects were stored<br>redundantly across multiple fault-isolated<br>facilities.<br>|No deviations noted.<br>|
|**AWSCA-7.4:** S3-<br>Specific – Objects are<br>stored redundantly<br>across multiple fault-<br>isolated facilities.<br>**m-token**|A1.2; <br>C1.1 <br>**-w**|Inspected the object sharding configurations<br>to ascertain objects were stored redundantly<br>across multiple fault-isolated facilities.<br>|No deviations noted.<br>|
|**AWSCA-7.4:** S3-<br>Specific – Objects are<br>stored redundantly<br>across multiple fault-<br>isolated facilities.<br>**m-token**|A1.2; <br>C1.1 <br>**-w**|Uploaded an object and observed an S3<br>Software Development Engineer access the<br>object location configuration to ascertain the<br>object was stored redundantly across<br>multiple fault-isolated facilities.<br>|No deviations noted.<br>|


AWS Confidential


155




Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality, and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**







|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|**AWSCA-7.5:** S3-<br>Specific – The design<br>of systems is<br>sufficiently<br>redundant to sustain<br>the loss of a data<br>center facility<br>without interruption<br>to the service.<br>|A1.2; <br>C1.1 <br>|Inquired of an S3 Software Development<br>Engineer to ascertain systems were designed<br>to sustain the loss of a data center facility<br>without interruption to the service.<br>|No deviations noted.<br>**2J**|
|**AWSCA-7.5:** S3-<br>Specific – The design<br>of systems is<br>sufficiently<br>redundant to sustain<br>the loss of a data<br>center facility<br>without interruption<br>to the service.<br>|A1.2; <br>C1.1 <br>|Inspected the system configuration utilized<br>by S3 on stored objects to ascertain critical<br>services were designed to sustain the loss of<br>a facility without interruption to the service.<br>**IkL**|No deviations noted.<br>|
|**AWSCA-7.6:** RDS-<br>Specific – If enabled<br>by the customer,<br>RDS backs up<br>customer databases,<br>stores backups for<br>user-defined<br>retention periods,<br>and supports point-<br>in-time recovery.<br>**-token**|A1.2; <br>C1.1 <br>**-wi2**|Inquired of an RDS Software Development<br>Manager to ascertain, if enabled by the<br>customer, RDS backed up customer<br>databases, stored backups for user-defined<br>retention periods, and supported point-in-<br>time recovery.<br>**4Agn**|No deviations noted.<br>|
|**AWSCA-7.6:** RDS-<br>Specific – If enabled<br>by the customer,<br>RDS backs up<br>customer databases,<br>stores backups for<br>user-defined<br>retention periods,<br>and supports point-<br>in-time recovery.<br>**-token**|A1.2; <br>C1.1 <br>**-wi2**|Inspected the RDS backup configurations to<br>ascertain, if enabled by the customer, RDS<br>backed up customer database and stored<br>backups for user-defined retention periods.<br>**ivGU**|No deviations noted.<br>|
|**AWSCA-7.6:** RDS-<br>Specific – If enabled<br>by the customer,<br>RDS backs up<br>customer databases,<br>stores backups for<br>user-defined<br>retention periods,<br>and supports point-<br>in-time recovery.<br>**-token**|A1.2; <br>C1.1 <br>**-wi2**|Created an RDS database, enabled backups<br>and backed up the database to ascertain RDS<br>backed up customer databases via scheduled<br>backups according to a user-defined<br>retention period.<br>|No deviations noted.<br> <br>|
|**AWSCA-7.6:** RDS-<br>Specific – If enabled<br>by the customer,<br>RDS backs up<br>customer databases,<br>stores backups for<br>user-defined<br>retention periods,<br>and supports point-<br>in-time recovery.<br>**-token**|A1.2; <br>C1.1 <br>**-wi2**|Created an RDS database, captured a point in<br>time database snapshot and restored the<br>RDS database using the captured snapshot,<br>to ascertain RDS databases were capable of a<br>point-in-time recovery using database<br>snapshots.<br>|No deviations noted<br>|
|**AWSCA-7.6:** RDS-<br>Specific – If enabled<br>by the customer,<br>RDS backs up<br>customer databases,<br>stores backups for<br>user-defined<br>retention periods,<br>and supports point-<br>in-time recovery.<br>**-token**|A1.2; <br>C1.1 <br>**-wi2**|Restored an RDS database using a database<br>backup, to ascertain RDS databases were<br>capable of a point-in-time recovery.<br>|No deviations noted.<br>|


AWS Confidential


156




Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality, and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**







|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|**AWSCA-7.7**: AWS<br>provides customers<br>the ability to delete<br>their content. Once<br>successfully removed<br>the data is rendered<br>unreadable.<br>**ken**|CC6.5; <br>C1.2; <br>P4.1; <br>P4.2; <br>P4.3 <br>**-wi2**|Inquired of an EC2 Principal Engineer to<br>ascertain AWS provided customers the ability<br>to delete their content and render it<br>unreadable.<br>|No deviations noted.<br>**2J**|
|**AWSCA-7.7**: AWS<br>provides customers<br>the ability to delete<br>their content. Once<br>successfully removed<br>the data is rendered<br>unreadable.<br>**ken**|CC6.5; <br>C1.2; <br>P4.1; <br>P4.2; <br>P4.3 <br>**-wi2**|Observed an EC2 Security Engineer create a<br>virtual host, upload content, delete the<br>underlying storage volume, then create a<br>different instance within the same virtual<br>memory slot and query for the original<br>content to ascertain that the underlying<br>storage volume and in memory data was<br>removed.<br>**gnIkL**|No deviations noted.<br>|
|**AWSCA-7.7**: AWS<br>provides customers<br>the ability to delete<br>their content. Once<br>successfully removed<br>the data is rendered<br>unreadable.<br>**ken**|CC6.5; <br>C1.2; <br>P4.1; <br>P4.2; <br>P4.3 <br>**-wi2**|For the services that provide content storage<br>as described in the System Description,<br>inspected the configurations designed to<br>automatically delete content from buckets,<br>volumes, instances, or other means of<br>content storage, to ascertain it was designed<br>to delete and render the data unreadable.<br>**vGU4A**|No deviations noted.<br>|
|**AWSCA-7.7**: AWS<br>provides customers<br>the ability to delete<br>their content. Once<br>successfully removed<br>the data is rendered<br>unreadable.<br>**ken**|CC6.5; <br>C1.2; <br>P4.1; <br>P4.2; <br>P4.3 <br>**-wi2**|For the services that provide content storage<br>as described in the System Description,<br>independently created an AWS cloud account<br>registered to an independent email address<br>and created sample content into buckets,<br>volumes, instances, or other means of<br>content storage, and compared the time<br>stamp of creation with the current date and<br>time. Observed Software Development<br>Managers query for the objects to ascertain<br>the objects existed and were in an active<br>state.<br>**Fi**|No deviations noted.<br>|


AWS Confidential


157




Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality, and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**







|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
||**i2**|For the core storage services that provide<br>content storage as described in the System<br>Description, created an AWS cloud account<br>registered to an independent email address<br>and created sample content into buckets,<br>volumes, instances, or other means of<br>content storage, and compared the time<br>stamp of creation with the current date and<br>time. Observed Software Development<br>Managers query the backend to ascertain the<br>objects existed and were in an active state.<br>**nIkLR**|No deviations noted.<br>**i2J**|
||**i2**|For the services that provide content storage<br>as described in the System Description,<br>deleted the content and/or the underlying<br>buckets, volumes, instances, or other means<br>of content storage, and inspected if the data<br>identifiers were removed or the data itself<br>was zeroed out after being deleted to<br>ascertain it was rendered unreadable.<br>**GU4Ag**|No deviations noted.<br>|
||**i2**|For the core storage services that provide<br>content storage as described in the System<br>Description, observed Software Development<br>Managers query for the objects metadata for<br>the deleted objects to ascertain that an error<br>was returned stating the object could not be<br>found.<br>**Fiv**|No deviations noted.<br>|
|**AWSCA-7.8**: AWS<br>retains customer<br>content per<br>customer<br>agreements.<br>**-token**|CC6.5; <br>C1.1; <br>P4.2 <br>|Inquired of an IAM Software Dev II to<br>ascertain AWS retained customer content<br>per the customer agreements.<br>|No deviations noted.<br>|
|**AWSCA-7.8**: AWS<br>retains customer<br>content per<br>customer<br>agreements.<br>**-token**|CC6.5; <br>C1.1; <br>P4.2 <br>|Inspected the most recent copy of the AWS<br>Customer Agreement to ascertain it was<br>communicated externally to customers and<br>contained an effective date, which was the<br>most recent version of the agreement.<br>|No deviations noted.<br>|


AWS Confidential


158




Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality, and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**







|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|||Inspected the AWS Customer Agreement to<br>ascertain the contractual language in section<br>7.3b stated that AWS will not delete<br>customer information for up to 30 days in the<br>event of AWS account termination, and that<br>the language explicitly stated the customer<br>agreed to the responsibilities regarding<br>confidential information disposal.<br>**kLR**|No deviations noted.<br>**i2J**|
|||Inspected the customer account content<br>retention configuration to ascertain a<br>centralized account service was designed to<br>send notifications to services to delete<br>customer content 90 days after account<br>closure.<br>**AgnI**|No deviations noted.<br>|
|||For a sample AES integrated service, selected<br>a service that stores customer content<br>integrated with the centralized account<br>service, created a unit of content storage,<br>closed the AWS account and inspected the<br>content throughout the 90- day lifecycle to<br>ascertain customer content was retained until<br>deleted 90 days after customer account<br>closure.<br>**FivGU4**|No deviations noted.<br>|
|**AWSCA-7.9:**<br>Outpost-Specific –<br>Nitro Security Key is<br>configured in<br>Outpost to encrypt<br>customer content<br>and allow a<br>customer to have a<br>mechanical means to<br>perform crypto<br>shredding of the<br>content. <br>**-token**|CC6.5; <br>C1.2; <br>P4.2; <br>P4.3 <br>**-wi**|Inquired of an AWS Senior Security Engineer<br>to ascertain the Nitro Security Key was<br>configured in Outpost to encrypt customer<br>content and allowed a customer to have a<br>mechanical means to perform crypto<br>shredding of the content.<br>|No deviations noted.<br>|
|**AWSCA-7.9:**<br>Outpost-Specific –<br>Nitro Security Key is<br>configured in<br>Outpost to encrypt<br>customer content<br>and allow a<br>customer to have a<br>mechanical means to<br>perform crypto<br>shredding of the<br>content. <br>**-token**|CC6.5; <br>C1.2; <br>P4.2; <br>P4.3 <br>**-wi**|Inspected the Outpost configurations to<br>ascertain the Outpost was configured to<br>encrypt customer content with the Nitro<br>Security Key.<br> <br>|No deviations noted.<br>|


AWS Confidential


159




Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality, and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**







|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|||Inspected the Standard Operating<br>Procedures for Outpost Retrieval document<br>to ascertain the Nitro Security Key was<br>mechanically destroyed at the time of<br>retrieval.<br>|No deviations noted.<br>**i2J**|
|||Inspected logs of an Outpost with a valid<br>Nitro Security Key to ascertain that it<br>successfully encrypted the content on the<br>Outpost with a valid Nitro Security Key. <br>**IkL**|No deviations noted.<br>|
|||Inspected logs of an Outpost without a valid<br>Nitro Security Key to ascertain that it was not<br>able to unencrypt the content on the<br>Outpost without the valid Nitro Security Key.<br>**Agn**|No deviations noted.<br>|
|**AWSCA-7.10**: EC2-<br>Specific - Amazon<br>EC2 enables clock<br>synchronization<br>based on Network<br>Time Protocol in EC2<br>Linux instances, to<br>achieve accuracy<br>within 1 millisecond<br>of Coordinated<br>Universal Time.<br>**-token**|CC7.1 <br>**-wi2**|Inquired of an EC2 Software Development<br>Manager to ascertain Amazon EC2 enabled<br>clock synchronization based on Network<br>Time Protocol in EC2 instances, to achieve<br>accuracy within 1 millisecond of Coordinated<br>Universal Time for non-supported instances<br>and within 100 microseconds of Coordinated<br>Universal Time for supported instances.<br>**ivGU4**|No deviations noted.<br>|
|**AWSCA-7.10**: EC2-<br>Specific - Amazon<br>EC2 enables clock<br>synchronization<br>based on Network<br>Time Protocol in EC2<br>Linux instances, to<br>achieve accuracy<br>within 1 millisecond<br>of Coordinated<br>Universal Time.<br>**-token**|CC7.1 <br>**-wi2**|Inspected the clock synchronization<br>configurations to ascertain the different<br>infrastructure layers were linked to ensure<br>clock synchronization.<br>|No deviations noted.<br>|
|**AWSCA-7.10**: EC2-<br>Specific - Amazon<br>EC2 enables clock<br>synchronization<br>based on Network<br>Time Protocol in EC2<br>Linux instances, to<br>achieve accuracy<br>within 1 millisecond<br>of Coordinated<br>Universal Time.<br>**-token**|CC7.1 <br>**-wi2**|Observed an EC2 Software Development<br>Engineer create an EC2 instance and enable<br>clock synchronization to ascertain that clock<br>synchronization achieved an accuracy within<br>1 millisecond of Coordinated Universal Time<br>for one non-supported instance and within<br>100 microseconds of Coordinated Universal<br>Time for one supported instance.<br>|No deviations noted.<br>|


AWS Confidential


160


Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality, and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**









|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|||For a supported instance, inspected the AWS<br>managed Grandmaster clock devices to<br>ascertain that the Grandmaster devices were<br>active, and that monitoring was enabled to<br>ensure that an accuracy within 100<br>microseconds of Coordinated Universal Time.<br>**R**|No deviations noted<br>**i2J**|
|||For a sample of AWS Availability Zones (AZs)<br>selected from a listing of AZs generated from<br>the AZ code repository, inspected the AWS<br>managed Grandmaster clock devices to<br>ascertain that the Grandmaster devices were<br>active, and that monitoring was enabled to<br>ensure that an accuracy within 1 millisecond<br>of Coordinated Universal Time was achieved.<br>**AgnIk**|No deviations noted.<br>|
|**AWSCA-8.1:** <br>Monitoring and<br>alarming are<br>configured by<br>Service Owners to<br>identify and notify<br>operational and<br>management<br>personnel of<br>incidents when early<br>warning thresholds<br>are crossed on key<br>operational metrics.<br>**-token**|CC2.1; <br>CC6.1; <br>CC6.6; <br>CC6.8; <br>CC7.2; <br>CC7.3;<br>CC7.4; <br>A1.1; <br>A1.2; <br>P6.3; <br>P6.5 <br>**-wi2**|Inquired of an AWS IT Security Response<br>Director and a Senior Security Engineer to<br>ascertain the production environment was<br>monitored and that alarming was configured<br>by Service Owners to notify operational and<br>management personnel when early warning<br>thresholds were crossed on key operational<br>metrics.<br>**ivGU4**|No deviations noted.<br>|
|**AWSCA-8.1:** <br>Monitoring and<br>alarming are<br>configured by<br>Service Owners to<br>identify and notify<br>operational and<br>management<br>personnel of<br>incidents when early<br>warning thresholds<br>are crossed on key<br>operational metrics.<br>**-token**|CC2.1; <br>CC6.1; <br>CC6.6; <br>CC6.8; <br>CC7.2; <br>CC7.3;<br>CC7.4; <br>A1.1; <br>A1.2; <br>P6.3; <br>P6.5 <br>**-wi2**|For a sample of key operational metrics<br>selected from a listing of critical alarms,<br>inspected the applicable configurations to<br>ascertain related monitoring and alarming<br>were in place to notify appropriate personnel<br>when a threshold was reached or exceeded.<br>|No deviations noted.<br>|
|**AWSCA-8.1:** <br>Monitoring and<br>alarming are<br>configured by<br>Service Owners to<br>identify and notify<br>operational and<br>management<br>personnel of<br>incidents when early<br>warning thresholds<br>are crossed on key<br>operational metrics.<br>**-token**|CC2.1; <br>CC6.1; <br>CC6.6; <br>CC6.8; <br>CC7.2; <br>CC7.3;<br>CC7.4; <br>A1.1; <br>A1.2; <br>P6.3; <br>P6.5 <br>**-wi2**|Inspected the network monitoring tool<br>configurations that automatically generate<br>tickets for Network Monitoring incidents to<br>ascertain incidents were logged within a<br>ticketing system, assigned severity rating and<br>tracked to resolution.<br>|No deviations noted.<br>|


AWS Confidential


161


Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality, and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**



|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|**AWSCA-8.2:** <br>Incidents are logged<br>within a ticketing<br>system, assigned a<br>severity rating and<br>tracked to<br>resolution.<br>|CC2.1; <br>CC6.1; <br>CC6.6; <br>CC6.8; <br>CC7.2; <br>CC7.3; <br>CC7.4; <br>CC7.5; <br>CC8.1; <br>A1.2; <br>P6.3; <br>P6.5; <br>P6.6; <br>P6.7; <br>P8.1<br>|Inquired of an AWS IT Security Response<br>Director to ascertain security incidents were<br>logged in a ticketing system, assigned a<br>severity level, and tracked through<br>resolution.<br>|No deviations noted.<br>**i2J**|
|**AWSCA-8.2:** <br>Incidents are logged<br>within a ticketing<br>system, assigned a<br>severity rating and<br>tracked to<br>resolution.<br>|CC2.1; <br>CC6.1; <br>CC6.6; <br>CC6.8; <br>CC7.2; <br>CC7.3; <br>CC7.4; <br>CC7.5; <br>CC8.1; <br>A1.2; <br>P6.3; <br>P6.5; <br>P6.6; <br>P6.7; <br>P8.1<br>|For a sample of incidents selected from a<br>system generated listing of security alerts,<br>inspected associated entries in the ticketing<br>system to ascertain incidents were assigned a<br>severity level and tracked through to<br>resolution.<br>**AgnIkL**|No deviations noted.<br>|
|**AWSCA-9.1:** AWS<br>maintains internal<br>informational<br>websites describing<br>the AWS<br>environment, its<br>boundaries, user<br>responsibilities and<br>services.<br>|CC2.2; <br>CC2.3 <br>**i2**|Inquired of the AWS Security Assurance<br>Technical Program Manager to ascertain<br>AWS maintained internal informational<br>websites describing the AWS environment,<br>its boundaries, user responsibilities, and the<br>services.<br>**ivGU4**|No deviations noted.<br>|
|**AWSCA-9.1:** AWS<br>maintains internal<br>informational<br>websites describing<br>the AWS<br>environment, its<br>boundaries, user<br>responsibilities and<br>services.<br>|CC2.2; <br>CC2.3 <br>**i2**|Inspected AWS internal informational<br>websites for each in-scope AWS service to<br>ascertain they described the AWS<br>environment, its boundaries, user<br>responsibilities, and the services.<br>**F**|No deviations noted.<br>|
|**AWSCA-9.2:** AWS<br>conducts pre-<br>employment<br>screening of<br>candidates<br>commensurate with<br>the employee’s<br>position and level, in<br>accordance with<br>local law and the<br>AWS Personnel<br>Security Policy.<br>**m-token**|CC1.1; <br>CC1.4 <br>|Inquired of the HR Specialist to ascertain<br>AWS conducted pre-employment screening<br>of full-time candidates prior to the<br>employees’ start dates in accordance with<br>local laws.<br> <br> <br> <br> <br> <br>|No deviations noted.<br>|


AWS Confidential


162








Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality, and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**







|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|||For a sample of AWS full-time new hires<br>selected from a listing of active employees,<br>inspected pre-employment screening records<br>to ascertain pre-employment screening was<br>performed prior to each employee’s start<br>date.<br>**R**|No deviations noted.<br>**i2J**|
|**AWSCA-9.3:** AWS<br>performs annual<br>formal evaluation of<br>resourcing and<br>staffing including<br>assessment of<br>employee<br>qualification<br>alignment with<br>entity objectives.<br>Employees receive<br>feedback on their<br>strengths and<br>growth ideas<br>annually.<br>|CC1.1; <br>CC1.4; <br>CC1.5 <br>|Inquired of the Principal, HR Business Partner<br>to ascertain a process was in place to<br>perform a formal evaluation of resourcing<br>and staffing annually, including an<br>assessment of employee qualification<br>alignment with entity objectives and that<br>employees received feedback on their<br>strengths and growth ideas.<br>**AgnIk**|No deviations noted.<br>|
|**AWSCA-9.3:** AWS<br>performs annual<br>formal evaluation of<br>resourcing and<br>staffing including<br>assessment of<br>employee<br>qualification<br>alignment with<br>entity objectives.<br>Employees receive<br>feedback on their<br>strengths and<br>growth ideas<br>annually.<br>|CC1.1; <br>CC1.4; <br>CC1.5 <br>|For a sample of AWS employees selected<br>from an HR system-generated listing,<br>inspected performance evaluation records to<br>ascertain each employee was formally<br>evaluated against entity objectives during the<br>most recent annual formal evaluation of<br>resourcing and staffing.<br>**ivGU4**|No deviations noted.<br>|
|**AWSCA-9.4:** AWS<br>host configuration<br>settings are<br>monitored to<br>validate compliance<br>with AWS security<br>standards and to<br>verify that settings<br>are automatically<br>deployed to the host<br>fleet.<br>**-token**|CC6.1; <br>CC6.8; <br>CC7.1; <br>CC8.1 <br>**-wi**|Inquired of a System Engineering Manager<br>and Software Development Manager to<br>ascertain AWS host configuration settings<br>were monitored to validate compliance with<br>AWS security standards and that settings<br>were automatically deployed to the fleet.<br>|No deviations noted.<br>|
|**AWSCA-9.4:** AWS<br>host configuration<br>settings are<br>monitored to<br>validate compliance<br>with AWS security<br>standards and to<br>verify that settings<br>are automatically<br>deployed to the host<br>fleet.<br>**-token**|CC6.1; <br>CC6.8; <br>CC7.1; <br>CC8.1 <br>**-wi**|Inspected the monitoring configurations to<br>ascertain production hosts were configured<br>to monitor compliance with AWS security<br>standards and to automatically request and<br>install host configuration setting updates<br>deployed to the fleet.<br>|No deviations noted.<br>|


AWS Confidential


163




Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality, and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**







|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|||Inspected the provisioning configurations to<br>ascertain hosts could not be deployed into<br>production environment without the<br>successful installation of configuration<br>management tools.<br>|No deviations noted.<br>**i2J**|
|||For a sample of production hosts selected<br>from listings of production hosts for each in-<br>scope AWS region, inspected the automated<br>deployment logs to ascertain production<br>hosts automatically requested and installed<br>host configuration setting updates deployed<br>to the fleet.<br>**gnIkL**|No deviations noted.<br>|
|||Inspected the ticket details for one incident<br>ticket created for a failed deployment<br>attempt for each host deployment<br>mechanism to ascertain the unsuccessful<br>installation of host configuration settings was<br>identified, tracked and resolved in a timely<br>manner.<br>**vGU4A**|No deviations noted.<br>|
|**AWSCA-9.5:** AWS<br>provides publicly<br>available<br>mechanisms for<br>customers to contact<br>AWS to report<br>security events and<br>publishes<br>information<br>including a system<br>description and<br>security and<br>compliance<br>information<br>addressing AWS<br>commitments and<br>responsibilities.<br>**m-token**|CC2.2; <br>CC2.3; <br>P5.1; <br>P5.2; <br>P6.3; <br>P8.1 <br>**-wi2**|Inquired of an AWS Security Compliance<br>Program Manager to ascertain AWS provided<br>publicly available mechanisms for customers<br>to contact AWS to report security events and<br>published information including a system<br>description and security and compliance<br>information addressing AWS commitments<br>and responsibilities.<br>**Fi**|No deviations noted.<br>|
|**AWSCA-9.5:** AWS<br>provides publicly<br>available<br>mechanisms for<br>customers to contact<br>AWS to report<br>security events and<br>publishes<br>information<br>including a system<br>description and<br>security and<br>compliance<br>information<br>addressing AWS<br>commitments and<br>responsibilities.<br>**m-token**|CC2.2; <br>CC2.3; <br>P5.1; <br>P5.2; <br>P6.3; <br>P8.1 <br>**-wi2**|Inspected AWS informational websites to<br>ascertain they provided publicly available<br>mechanisms for customers to contact AWS to<br>report security events.<br>|No deviations noted.<br>|
|**AWSCA-9.5:** AWS<br>provides publicly<br>available<br>mechanisms for<br>customers to contact<br>AWS to report<br>security events and<br>publishes<br>information<br>including a system<br>description and<br>security and<br>compliance<br>information<br>addressing AWS<br>commitments and<br>responsibilities.<br>**m-token**|CC2.2; <br>CC2.3; <br>P5.1; <br>P5.2; <br>P6.3; <br>P8.1 <br>**-wi2**|Inspected the AWS whitepapers and public<br>websites to ascertain they provided<br>information including a system description<br>and security and compliance information<br>addressing AWS commitments and<br>responsibilities.<br>|No deviations noted.<br>|


AWS Confidential


164




Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality, and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**







|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|||Inspected a ticket resulting from a customer<br>inquiry, to ascertain a process is in place to<br>address, track and resolve customer inquiries<br>in a timely manner.<br>|No deviations noted.<br>**2J**|
|||For a sample of customer submitted<br>compliance inquiries selected from the AWS<br>Contact Us Compliance Support portal,<br>inspected supporting documentation to<br>ascertain that each inquiry was followed up<br>on timely through email or phone call by a<br>marketing representative.<br>**gnIkL**|No deviations noted<br>|
|**AWSCA-9.6**: The<br>Company provides a<br>hotline for<br>employees to<br>anonymously report<br>on possible<br>violations of<br>conduct. <br>|CC2.2; <br>CC7.2; <br>CC7.3; <br>CC7.4; <br>CC7.5 <br>**wi2**|Inquired of a Vice President of Litigation Legal<br>to ascertain the company provided a hotline<br>for employees to anonymously report on<br>possible violations of conduct.<br>**U4A**|No deviations noted.<br>|
|**AWSCA-9.6**: The<br>Company provides a<br>hotline for<br>employees to<br>anonymously report<br>on possible<br>violations of<br>conduct. <br>|CC2.2; <br>CC7.2; <br>CC7.3; <br>CC7.4; <br>CC7.5 <br>**wi2**|Inspected the Owner’s Manual and Guide to<br>Employment policy to ascertain employees<br>were provided access to the ethics hotline in<br>all geographies during orientation.<br>**ivG**|No deviations noted.<br>|
|**AWSCA-9.6**: The<br>Company provides a<br>hotline for<br>employees to<br>anonymously report<br>on possible<br>violations of<br>conduct. <br>|CC2.2; <br>CC7.2; <br>CC7.3; <br>CC7.4; <br>CC7.5 <br>**wi2**|Called the fraud hotline number to ascertain<br>it was available for employees to<br>anonymously report on possible violations of<br>conduct.<br>|No deviations noted.<br>|


AWS Confidential


165




Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality, and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**







|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|**AWSCA-9.7**: Material<br>violations of the<br>Company's Code of<br>Business Conduct<br>and Ethics and<br>similar policies are<br>appropriately<br>handled in terms of<br>communication and<br>possible disciplinary<br>action or<br>termination.<br>Violations involving<br>third parties or<br>contractors are<br>reported to their<br>respective<br>employers which will<br>carry out any<br>possible disciplinary<br>action, removal of<br>assignment with<br>Amazon, or<br>termination.<br>|CC1.1; <br>CC1.5; <br>CC9.2; <br>P8.1 <br>**wi2**|Inquired of a Principal of Corporate<br>Employee Relations to ascertain material<br>violations of the Company’s Code of Business<br>Conduct and Ethics and similar policies were<br>appropriately handled in terms of<br>communications and possible disciplinary<br>action or termination, and violations<br>involving third parties or contractors were<br>reported to their respective employers which<br>were responsible for any possible disciplinary<br>action, removal of assignment with Amazon,<br>or termination.<br>**gnIkLR**|No deviations noted.<br>**i2J**|
|**AWSCA-9.7**: Material<br>violations of the<br>Company's Code of<br>Business Conduct<br>and Ethics and<br>similar policies are<br>appropriately<br>handled in terms of<br>communication and<br>possible disciplinary<br>action or<br>termination.<br>Violations involving<br>third parties or<br>contractors are<br>reported to their<br>respective<br>employers which will<br>carry out any<br>possible disciplinary<br>action, removal of<br>assignment with<br>Amazon, or<br>termination.<br>|CC1.1; <br>CC1.5; <br>CC9.2; <br>P8.1 <br>**wi2**|Inspected the Code of Business Conduct and<br>Ethics policy to ascertain that employee<br>expectations were published on the intranet<br>for employees to review and consequences<br>for certain violations were documented<br>within the policy.<br>**U4A**|No deviations noted.<br>|
|**AWSCA-9.7**: Material<br>violations of the<br>Company's Code of<br>Business Conduct<br>and Ethics and<br>similar policies are<br>appropriately<br>handled in terms of<br>communication and<br>possible disciplinary<br>action or<br>termination.<br>Violations involving<br>third parties or<br>contractors are<br>reported to their<br>respective<br>employers which will<br>carry out any<br>possible disciplinary<br>action, removal of<br>assignment with<br>Amazon, or<br>termination.<br>|CC1.1; <br>CC1.5; <br>CC9.2; <br>P8.1 <br>**wi2**|Inspected the Human Resources team<br>investigation process wiki and Enterprise<br>Case Management system to ascertain they<br>detailed standard operating procedures for<br>the handling of a potential material violation<br>of the Company’s Code of Business Conduct<br>Ethics for both employees and vendors,<br>including the handling of communication and<br>possible disciplinary action.<br>**FivG**|No deviations noted.<br>|
|**AWSCA-9.8**: AWS<br>has established a<br>formal audit<br>program that<br>includes continual,<br>independent internal<br>and external<br>assessments to<br>**-toke**|CC1.2; <br>CC2.1; <br>CC3.1; <br>CC4.1; <br>CC4.2; <br>P8.1 <br>|Inquired of a Business Risk Management<br>Director to ascertain AWS had established a<br>formal audit program that included<br>continual, independent internal and external<br>assessments to validate the implementation<br>and operating effectiveness of the AWS<br>control environment.<br> <br>|No deviations noted.<br>|


AWS Confidential


166




Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality, and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**







|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|validate the<br>implementation and<br>operating<br>effectiveness of the<br>AWS control<br>environment.<br>||Inspected the audit framework and list of<br>interviewees to ascertain AWS functional<br>areas including AWS Security and AWS<br>Service teams were covered within the<br>Internal Audit Risk assessment creation.<br>|No deviations noted.<br>**i2J**|
|validate the<br>implementation and<br>operating<br>effectiveness of the<br>AWS control<br>environment.<br>||Inspected the yearly audit plan created by<br>Internal Audit and submitted to the Audit<br>Committee to ascertain Internal Audit<br>formalized and outlined their specific audit<br>plan as a response of the risk assessment<br>conducted, and that the audit plan contained<br>the AWS organization.<br>**gnIkL**|No deviations noted.<br>|
|**AWSCA-9.9**: AWS<br>has a process to<br>assess whether AWS<br>employees who have<br>access to resources<br>that store or process<br>customer data via<br>permission groups<br>are subject to a post-<br>hire background<br>check as applicable<br>with local law and<br>the AWS Personnel<br>Security Policy.<br>**-token**|CC1.1; <br>CC1.4; <br>**-wi2**|Inquired of a Security Program Manager to<br>ascertain employees with access to resources<br>that store or process customer data via<br>permission groups received a background<br>check, as applicable with local law, no less<br>than once per calendar year.<br>**GU4A**|No deviations noted.<br>|
|**AWSCA-9.9**: AWS<br>has a process to<br>assess whether AWS<br>employees who have<br>access to resources<br>that store or process<br>customer data via<br>permission groups<br>are subject to a post-<br>hire background<br>check as applicable<br>with local law and<br>the AWS Personnel<br>Security Policy.<br>**-token**|CC1.1; <br>CC1.4; <br>**-wi2**|For a sample of AWS employees selected<br>from a system generated listing of accounts<br>with access to resources that stored or<br>processed customer data, inspected their<br>background check status to ascertain<br>background checks were completed once per<br>calendar year or access to resources that<br>stored or processed customer data was<br>removed as appropriate.<br>**Fiv**|No deviations noted.<br>|
|**AWSCA-9.9**: AWS<br>has a process to<br>assess whether AWS<br>employees who have<br>access to resources<br>that store or process<br>customer data via<br>permission groups<br>are subject to a post-<br>hire background<br>check as applicable<br>with local law and<br>the AWS Personnel<br>Security Policy.<br>**-token**|CC1.1; <br>CC1.4; <br>**-wi2**|For a sample of AWS employees selected<br>from a system generated listing of accounts<br>that had opted out of a background check,<br>inspected their group membership audit<br>history to ascertain that access to permission<br>groups granting access to resources that<br>stored or processed customer data had been<br>removed.<br> <br>|No deviations noted.<br>|


AWS Confidential


167




Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality, and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**











|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|**AWSCA-10.1:** Critical<br>AWS system<br>components are<br>replicated across<br>multiple Availability<br>Zones and backups<br>are maintained.<br>|A1.2 <br>|Inquired of Software Development Manager<br>and AWS Code Services Sr. Software<br>Development Engineer to ascertain critical<br>AWS system components were replicated<br>across multiple Availability Zones and that<br>backups were maintained.<br>**R**|No deviations noted.<br>**i2J**|
|**AWSCA-10.1:** Critical<br>AWS system<br>components are<br>replicated across<br>multiple Availability<br>Zones and backups<br>are maintained.<br>|A1.2 <br>|Inspected the replication configurations to<br>ascertain critical AWS system components<br>were configured to be replicated across<br>multiple Availability Zones.<br>**nIkL**|No deviations noted.<br>|
|**AWSCA-10.1:** Critical<br>AWS system<br>components are<br>replicated across<br>multiple Availability<br>Zones and backups<br>are maintained.<br>|A1.2 <br>|Inspected the backup configurations to<br>ascertain critical AWS system components<br>were backed up as changes were deployed or<br>in accordance with periodically-configured<br>jobs throughout the day.<br>**4Ag**|No deviations noted.<br>|
|**AWSCA-10.1:** Critical<br>AWS system<br>components are<br>replicated across<br>multiple Availability<br>Zones and backups<br>are maintained.<br>|A1.2 <br>|For a package of system component files,<br>inspected the production environment<br>replication and backup logs for the related<br>AWS service to ascertain data was replicated<br>and backed up across multiple Availability<br>Zones.<br>**ivGU**|No deviations noted.<br>|
|**AWSCA-10.2**: <br>Backups of critical<br>AWS system<br>components are<br>monitored for<br>successful<br>replication across<br>multiple Availability<br>Zones. <br>**m-token**|A1.2; <br>A1.3; <br>C1.1 <br>**-wi**|Inquired of an AWS Code Services Sr.<br>Software Development Engineer to ascertain<br>critical AWS system components were<br>monitored for replication across multiple<br>Availability Zones.<br>|No deviations noted.<br>|
|**AWSCA-10.2**: <br>Backups of critical<br>AWS system<br>components are<br>monitored for<br>successful<br>replication across<br>multiple Availability<br>Zones. <br>**m-token**|A1.2; <br>A1.3; <br>C1.1 <br>**-wi**|Inspected the backup monitoring<br>configuration to ascertain that error incident<br>tickets were automatically generated in the<br>event of backup failures.<br>|No deviations noted.<br>|
|**AWSCA-10.2**: <br>Backups of critical<br>AWS system<br>components are<br>monitored for<br>successful<br>replication across<br>multiple Availability<br>Zones. <br>**m-token**|A1.2; <br>A1.3; <br>C1.1 <br>**-wi**|For a critical alarm, inspected monitoring<br>dashboards and alarming configurations to<br>ascertain an alarming mechanism existed to<br>notify appropriate personnel of replication<br>and backup successes and failures and when<br>files were insufficiently replicated across<br>multiple Availability Zones.<br>|No deviations noted.<br>|


AWS Confidential


168


Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality, and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**







|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|||Inspected notifications of when a backup did<br>not complete and when files were<br>insufficiently represented across multiple<br>Availability Zones to ascertain the service<br>team initiated the remediation process and<br>tracked the issues to resolution.<br>**R**|No deviations noted.<br>**i2J**|
|**AWSCA-10.3:** AWS<br>contingency planning<br>and incident<br>response playbooks<br>are maintained and<br>updated to reflect<br>emerging continuity<br>risks and lessons<br>learned from past<br>incidents. The AWS<br>contingency plan is<br>tested on at least an<br>annual basis. <br>**token**|CC2.2; <br>CC3.2; <br>CC3.3; <br>CC3.4; <br>CC5.3; <br>CC7.3; <br>CC7.4; <br>CC7.5; <br>CC8.1; <br>CC9.1; <br>A1.1; <br>A1.2; <br>A1.3; <br>P6.3 <br>**-wi2**|Inquired of an AWS Security Business<br>Continuity Manager to ascertain AWS<br>maintained an overall contingency planning<br>procedure that reflected emerging continuity<br>risks and incorporated lessons learned from<br>past incidents, and that the AWS contingency<br>plan was tested on at least an annual basis.<br>**AgnIkL**|No deviations noted.<br>|
|**AWSCA-10.3:** AWS<br>contingency planning<br>and incident<br>response playbooks<br>are maintained and<br>updated to reflect<br>emerging continuity<br>risks and lessons<br>learned from past<br>incidents. The AWS<br>contingency plan is<br>tested on at least an<br>annual basis. <br>**token**|CC2.2; <br>CC3.2; <br>CC3.3; <br>CC3.4; <br>CC5.3; <br>CC7.3; <br>CC7.4; <br>CC7.5; <br>CC8.1; <br>CC9.1; <br>A1.1; <br>A1.2; <br>A1.3; <br>P6.3 <br>**-wi2**|Inquired of AWS Security Business Continuity<br>Manager to ascertain AWS contingency<br>planning and incident response playbooks<br>specific to each service team were<br>maintained and updated to reflect emerging<br>continuity risks and lessons learned from<br>past incidents.<br>**vGU4**|No deviations noted.<br>|
|**AWSCA-10.3:** AWS<br>contingency planning<br>and incident<br>response playbooks<br>are maintained and<br>updated to reflect<br>emerging continuity<br>risks and lessons<br>learned from past<br>incidents. The AWS<br>contingency plan is<br>tested on at least an<br>annual basis. <br>**token**|CC2.2; <br>CC3.2; <br>CC3.3; <br>CC3.4; <br>CC5.3; <br>CC7.3; <br>CC7.4; <br>CC7.5; <br>CC8.1; <br>CC9.1; <br>A1.1; <br>A1.2; <br>A1.3; <br>P6.3 <br>**-wi2**|Inspected the AWS contingency plan<br>documentation to ascertain it was reviewed<br>and approved at least annually, and that<br>playbooks for each service existed, were<br>maintained, and updated to reflect emerging<br>continuity risks and lessons learned from<br>past incidents.<br>**Fi**|No deviations noted.<br>|
|**AWSCA-10.3:** AWS<br>contingency planning<br>and incident<br>response playbooks<br>are maintained and<br>updated to reflect<br>emerging continuity<br>risks and lessons<br>learned from past<br>incidents. The AWS<br>contingency plan is<br>tested on at least an<br>annual basis. <br>**token**|CC2.2; <br>CC3.2; <br>CC3.3; <br>CC3.4; <br>CC5.3; <br>CC7.3; <br>CC7.4; <br>CC7.5; <br>CC8.1; <br>CC9.1; <br>A1.1; <br>A1.2; <br>A1.3; <br>P6.3 <br>**-wi2**|For a recent AWS contingency plan test,<br>inspected the ticket, to ascertain the<br>contingency plan was tested within the past<br>year, and that drills conducted to imitate<br>incidents were resolved and service<br>availability was restored.<br>|No deviations noted.<br>|


AWS Confidential


169




Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality, and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**







|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|**AWSCA-10.4:** AWS<br>maintains a capacity<br>planning model to<br>assess infrastructure<br>usage and demands<br>at least monthly, and<br>usually more<br>frequently (e.g.,<br>weekly). In addition,<br>the AWS capacity<br>planning model<br>supports the<br>planning of future<br>demands to acquire<br>and implement<br>additional resources<br>based upon current<br>resources and<br>forecasted<br>requirements.<br>|A1.1; <br>A1.2 <br>|Inquired of a Senior Tech Infrastructure<br>Program Manager, to ascertain AWS<br>maintained a centralized capacity planning<br>model that assessed infrastructure usage,<br>forecasted demand, and additional resources<br>required to meet the availability<br>requirements.<br>**LR**|No deviations noted.<br>**i2J**|
|**AWSCA-10.4:** AWS<br>maintains a capacity<br>planning model to<br>assess infrastructure<br>usage and demands<br>at least monthly, and<br>usually more<br>frequently (e.g.,<br>weekly). In addition,<br>the AWS capacity<br>planning model<br>supports the<br>planning of future<br>demands to acquire<br>and implement<br>additional resources<br>based upon current<br>resources and<br>forecasted<br>requirements.<br>|A1.1; <br>A1.2 <br>|For a sample of Regions and Edge locations,<br>inspected the capacity planning model to<br>ascertain capacity was assessed per the<br>defined cadence, and the model contained<br>forecasting for future demands and resource<br>availability.<br>**GU4AgnIk**|No deviations noted.<br>|
|**AWSCA-11.1**: <br>Vendors and third<br>parties with<br>restricted access,<br>that engage in<br>business with<br>Amazon are subject<br>to confidentiality<br>commitments as part<br>of their agreements<br>with Amazon.<br>Confidentiality<br>commitments<br>included in<br>**oken**|CC1.1; <br>CC1.4; <br>CC2.2; <br>CC2.3; <br>CC9.2; <br>P6.4; <br>P6.5 <br>**-wi2**|Inquired of AWS Legal Corporate Counsel to<br>ascertain vendors or third parties with<br>restricted access, that engage in business<br>with AWS, were subject to confidentiality<br>agreements as part of their agreements with<br>AWS and that these agreements were<br>reviewed by AWS and the third party at the<br>time of contract creation or execution.<br>**Fiv**|No deviations noted.<br>|
|**AWSCA-11.1**: <br>Vendors and third<br>parties with<br>restricted access,<br>that engage in<br>business with<br>Amazon are subject<br>to confidentiality<br>commitments as part<br>of their agreements<br>with Amazon.<br>Confidentiality<br>commitments<br>included in<br>**oken**|CC1.1; <br>CC1.4; <br>CC2.2; <br>CC2.3; <br>CC9.2; <br>P6.4; <br>P6.5 <br>**-wi2**|For a sample of external vendors and third<br>parties with restricted access who engage in<br>business with AWS, inspected vendor<br>agreements to ascertain the agreements<br>contained confidentiality commitments.<br>|No deviations noted.<br>|


AWS Confidential


170




Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality, and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**







|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|agreements with<br>vendors and third<br>parties with<br>restricted access are<br>reviewed by AWS<br>and the third party<br>at time of contract<br>creation or<br>execution.<br>||For a sample of external vendors and third<br>parties with restricted access who engage in<br>business with AWS, inspected vendor<br>agreements to ascertain the agreements<br>were signed and approved by the vendor and<br>AWS.<br>**kLR**|No deviations noted.<br>**i2J**|
|**AWSCA-11.2**: AWS<br>has a program in<br>place for evaluating<br>vendor performance<br>and compliance with<br>contractual<br>obligations. <br>|CC1.1; <br>CC1.4; <br>CC2.3; <br>CC4.1; <br>CC9.2; <br>P4.1; <br>P6.1; <br>P6.4; <br>P6.5 <br>**-wi2**|Inquired of the Data Center Global Services<br>team to ascertain AWS has a program in<br>place for evaluating vendor performance and<br>compliance with contractual obligations.<br>**AgnI**|No deviations noted.<br>|
|**AWSCA-11.2**: AWS<br>has a program in<br>place for evaluating<br>vendor performance<br>and compliance with<br>contractual<br>obligations. <br>|CC1.1; <br>CC1.4; <br>CC2.3; <br>CC4.1; <br>CC9.2; <br>P4.1; <br>P6.1; <br>P6.4; <br>P6.5 <br>**-wi2**|Inspected the AWS evaluation program<br>calendars for vendor performance and<br>compliance with contractual obligations to<br>ascertain reviews for vendors with restricted<br>access were scheduled on a frequency<br>subject to the overall risk of doing business<br>with each vendor.<br>**vGU4**|No deviations noted.<br>|
|**AWSCA-11.2**: AWS<br>has a program in<br>place for evaluating<br>vendor performance<br>and compliance with<br>contractual<br>obligations. <br>|CC1.1; <br>CC1.4; <br>CC2.3; <br>CC4.1; <br>CC9.2; <br>P4.1; <br>P6.1; <br>P6.4; <br>P6.5 <br>**-wi2**|For a sample of vendors selected from a<br>listing of third-party vendors, inspected<br>vendor evaluations of performance and<br>compliance with contractual obligations to<br>ascertain reviews were performed in<br>accordance with policy and served as means<br>for evaluations of vendor performance with<br>contractual obligations, based on risk.<br>**Fi**|No deviations noted.<br>|
|**AWSCA-11.3**: AWS<br>communicates<br>confidentiality<br>requirements in<br>agreements when<br>they are renewed<br>with vendors and<br>third parties with<br>restricted access.<br>**m-toke**|CC2.2; <br>CC2.3; <br>CC9.2; <br>P6.4; <br>P6.5 <br>|Inquired of an AWS Security Assurance<br>Technical Program Manager to ascertain<br>AWS communicated confidentiality<br>requirements in agreements when they were<br>renewed with vendors and third parties with<br>restricted access and that changes to<br>standard confidentiality commitments to<br>customers were communicated on the AWS<br>website via the AWS customer agreement.<br>|No deviations noted.<br>|


AWS Confidential


171




Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality, and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**







|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|Changes to standard<br>confidentiality<br>commitments to<br>customers are<br>communicated on<br>the AWS website via<br>the AWS customer<br>agreement. <br>||Inspected the public-facing AWS Customer<br>Agreement located on the AWS website to<br>ascertain changes to standard confidentiality<br>commitments were communicated via the<br>AWS Customer Agreement and made publicly<br>available via an embedded change log.<br>**LR**|No deviations noted.<br>**i2J**|
|**AWSCA-12.1:** AWS<br>informs customers of<br>the AWS Data<br>security and privacy<br>commitments within<br>the AWS Customer<br>Agreement prior to<br>activating an AWS<br>account and makes it<br>available to<br>customers to review<br>at any time on the<br>AWS website. <br>**oken**|P1.1; <br>P2.1; <br>P3.1; <br>P5.1; <br>P5.2; <br>P6.1; <br>P8.1 <br>**-wi2**|Inquired of AWS Corporate Counsel to<br>ascertain AWS informed customers of the<br>AWS Data security and privacy commitments<br>within the AWS Customer Agreement prior to<br>activating an AWS account and made it<br>available to customers to review any time on<br>the AWS website.<br>**4AgnIk**|No deviations noted.<br>|
|**AWSCA-12.1:** AWS<br>informs customers of<br>the AWS Data<br>security and privacy<br>commitments within<br>the AWS Customer<br>Agreement prior to<br>activating an AWS<br>account and makes it<br>available to<br>customers to review<br>at any time on the<br>AWS website. <br>**oken**|P1.1; <br>P2.1; <br>P3.1; <br>P5.1; <br>P5.2; <br>P6.1; <br>P8.1 <br>**-wi2**|Attempted to create an AWS account<br>without acknowledging the AWS Customer<br>Agreement and observed the system<br>prevented proceeding any further with<br>opening the account.<br>**vGU**|No deviations noted.<br>|
|**AWSCA-12.1:** AWS<br>informs customers of<br>the AWS Data<br>security and privacy<br>commitments within<br>the AWS Customer<br>Agreement prior to<br>activating an AWS<br>account and makes it<br>available to<br>customers to review<br>at any time on the<br>AWS website. <br>**oken**|P1.1; <br>P2.1; <br>P3.1; <br>P5.1; <br>P5.2; <br>P6.1; <br>P8.1 <br>**-wi2**|Acknowledged the AWS Customer<br>Agreement and successfully created an AWS<br>account to ascertain that acknowledgement<br>of the AWS Customer Agreement was<br>required prior to opening an AWS account.<br>**Fi**|No deviations noted.<br>|
|**AWSCA-12.1:** AWS<br>informs customers of<br>the AWS Data<br>security and privacy<br>commitments within<br>the AWS Customer<br>Agreement prior to<br>activating an AWS<br>account and makes it<br>available to<br>customers to review<br>at any time on the<br>AWS website. <br>**oken**|P1.1; <br>P2.1; <br>P3.1; <br>P5.1; <br>P5.2; <br>P6.1; <br>P8.1 <br>**-wi2**|Inspected the AWS Customer Agreement on<br>the AWS website to ascertain that the AWS<br>Customer Agreement is publicly available for<br>customers to review and informed customers<br>of AWS data security and privacy<br>commitments.<br>|No deviations noted.<br>|


AWS Confidential


172




Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality, and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**















|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|**AWSCA-12.2:** AWS<br>informs customers of<br>changes made to the<br>AWS Customer<br>Agreement via the<br>AWS public website. <br>|CC2.3; <br>P1.1 <br>|Inquired of AWS Corporate Counsel to<br>ascertain AWS informed customers of<br>changes made to the AWS Customer<br>Agreement via the AWS public website.<br> <br> <br>**LR**|No deviations noted.<br>**i2J**|
|**AWSCA-12.2:** AWS<br>informs customers of<br>changes made to the<br>AWS Customer<br>Agreement via the<br>AWS public website. <br>|CC2.3; <br>P1.1 <br>|Inspected the AWS Customer Agreement via<br>the AWS website to ascertain that the last<br>update date was displayed to customers.<br>**nIk**|No deviations noted.<br>|
|**AWSCA-12.2:** AWS<br>informs customers of<br>changes made to the<br>AWS Customer<br>Agreement via the<br>AWS public website. <br>|CC2.3; <br>P1.1 <br>|Inspected the AWS Customer Agreement to<br>ascertain that it contained a commitment<br>from management to make available to<br>customers any changes made to the AWS<br>Customer Agreement.<br>**4Ag**|No deviations noted.<br>|
|**AWSCA-12.3:** AWS<br>offers customers the<br>capability to update<br>communication<br>preferences via the<br>AWS console. <br>**n**|P2.1 <br>**-wi2**|Inquired of a Senior Digital Marketing Leader<br>to ascertain that Amazon offered customers<br>the capability to update their communication<br>preferences via the AWS console.<br>**vGU**|No deviations noted.<br>|
|**AWSCA-12.3:** AWS<br>offers customers the<br>capability to update<br>communication<br>preferences via the<br>AWS console. <br>**n**|P2.1 <br>**-wi2**|Observed a Senior Digital Marketing Leader<br>update communication preferences for an<br>AWS account via the AWS console; inspected<br>the update in the back-end repository, and<br>inspected the communication preferences<br>update confirmation notification to ascertain<br>that Amazon offered customers the<br>capability to update communication<br>preferences via the AWS console.<br>**F**|No deviations noted.<br>|
|**AWSCA-12.4:** AWS<br>performs application<br>security reviews for<br>Third-Party systems<br>that collect customer<br>content in<br>**-tok**|CC2.3; <br>P1.1; <br>P3.1; <br>P4.1; <br>P4.2; <br>P6.1; <br>|Inquired of an AWS Security Manager to<br>ascertain that AWS performed application<br>security reviews for third-party systems that<br>collect customer content in accordance with<br>team processes, to ascertain security risks<br>were identified and mitigated.<br>|No deviations noted.<br>|


AWS Confidential


173


Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality, and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**











|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|accordance with<br>team processes, to<br>ascertain security<br>risks are identified<br>and mitigated. <br>|P6.4 <br>|Inspected team documentation of external<br>party onboarding for providers of third-party<br>systems that collected customer content to<br>ascertain that external parties were assessed<br>for the collection of customer content and<br>referred for additional security reviews.<br>**R**|No deviations noted.<br>**i2J**|
|accordance with<br>team processes, to<br>ascertain security<br>risks are identified<br>and mitigated. <br>|P6.4 <br>|Selected a sample of security reviews for<br>third-party systems that collected customer<br>content which went live during the<br>examination period to ascertain that the<br>system was assessed prior to launch to<br>evaluate whether security risks were<br>identified and mitigated.<br>**AgnIk**|No deviations noted.<br>|
|**AWSCA-12.5**: AWS<br>notifies affected<br>data subjects and<br>regulators of<br>breaches and<br>incidents as legally<br>required in<br>accordance with<br>team processes.<br>**oken**|P5.1; <br>P5.2; <br>P6.3; <br>P6.4; <br>P6.6; <br>P6.7; <br>P8.1; <br>CC2.3; <br>CC7.4 <br> <br>**-wi2**|Inquired of Corporate Counsel to ascertain<br>that AWS notified affected data subjects and<br>regulators of breaches and incidents as<br>legally required in accordance with team<br>processes.<br>**GU4**|No deviations noted.<br>|
|**AWSCA-12.5**: AWS<br>notifies affected<br>data subjects and<br>regulators of<br>breaches and<br>incidents as legally<br>required in<br>accordance with<br>team processes.<br>**oken**|P5.1; <br>P5.2; <br>P6.3; <br>P6.4; <br>P6.6; <br>P6.7; <br>P8.1; <br>CC2.3; <br>CC7.4 <br> <br>**-wi2**|Inspected the AWS Internal Privacy Policy to<br>ascertain that AWS notified affected data<br>subjects and regulators of breaches and<br>incidents as legally required in accordance<br>with team processes.<br>**Fiv**|No deviations noted.<br>|
|**AWSCA-12.5**: AWS<br>notifies affected<br>data subjects and<br>regulators of<br>breaches and<br>incidents as legally<br>required in<br>accordance with<br>team processes.<br>**oken**|P5.1; <br>P5.2; <br>P6.3; <br>P6.4; <br>P6.6; <br>P6.7; <br>P8.1; <br>CC2.3; <br>CC7.4 <br> <br>**-wi2**|Inspected the AWS internal Wiki Page to<br>ascertain that AWS Security Operations<br>should be engaged for security incidents<br>above Sev 2.<br>|No deviations noted.<br>|
|**AWSCA-12.5**: AWS<br>notifies affected<br>data subjects and<br>regulators of<br>breaches and<br>incidents as legally<br>required in<br>accordance with<br>team processes.<br>**oken**|P5.1; <br>P5.2; <br>P6.3; <br>P6.4; <br>P6.6; <br>P6.7; <br>P8.1; <br>CC2.3; <br>CC7.4 <br> <br>**-wi2**|Inspected the Personal Health Dashboard of<br>AWS account to ascertain that privacy events<br>affecting AWS resources were listed.<br>|No deviations noted.<br>|


AWS Confidential


174


Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality, and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**



|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|||Inspected incident response details for a<br>sample of security alert incident tickets to<br>ascertain if evaluations were conducted to<br>determine if disclosures were required to be<br>made to affected data subjects and<br>regulators of breaches, and if required<br>disclosures were appropriately made<br>according to incident response<br>documentation.<br>**IkLR**|No deviations noted<br>**i2J**|
|**AWSCA-12.6:** AWS<br>provides<br>authenticated<br>customers the ability<br>to access, update,<br>and confirm their<br>data. Denial of<br>access will be<br>communicated using<br>the AWS console. <br>|P5.1; <br>P5.2; <br>P7.1 <br>**i2**|Inquired of Corporate Counsel to ascertain<br>that AWS provided authenticated customers<br>the ability to access, update, and confirm<br>their data. Additionally, inquired of<br>Corporate Counsel to ascertain what<br>conditions would trigger a denial of access<br>and that a denial of access will be<br>communicated using the AWS console.<br>**U4Agn**|No deviations noted.<br>|
|**AWSCA-12.6:** AWS<br>provides<br>authenticated<br>customers the ability<br>to access, update,<br>and confirm their<br>data. Denial of<br>access will be<br>communicated using<br>the AWS console. <br>|P5.1; <br>P5.2; <br>P7.1 <br>**i2**|Inspected the AWS Customer Agreement to<br>ascertain that AWS committed to notifying<br>customers prior to denial of access.<br>**vG**|No deviations noted.<br>|
|**AWSCA-12.6:** AWS<br>provides<br>authenticated<br>customers the ability<br>to access, update,<br>and confirm their<br>data. Denial of<br>access will be<br>communicated using<br>the AWS console. <br>|P5.1; <br>P5.2; <br>P7.1 <br>**i2**|Updated personal account information in the<br>AWS Console to ascertain that AWS provided<br>authenticated customers the ability to<br>access, update, and confirm their data.<br>**F**|No deviations noted.<br>|
|**AWSCA-12.7:**AWS<br>records customer<br>information requests<br>to maintain a<br>complete, accurate,<br>and timely record of<br>such requests. <br>**m-token**|P5.1; <br>P5.2; <br>P6.1; <br>P6.2; <br>P6.7; <br>**-**|Inquired of AWS Corporate Counsel to<br>ascertain that AWS recorded customer<br>information requests to maintain a complete,<br>accurate, and timely record of such requests.<br>|No deviations noted.<br>|
|**AWSCA-12.7:**AWS<br>records customer<br>information requests<br>to maintain a<br>complete, accurate,<br>and timely record of<br>such requests. <br>**m-token**|P5.1; <br>P5.2; <br>P6.1; <br>P6.2; <br>P6.7; <br>**-**|Inspected the configurations for the<br>recording of customer information requests<br>through the Amazon Law Enforcement<br>Request Tracker system to ascertain that<br>AWS recorded customer information<br>requests to maintain a complete, accurate,<br>and timely record of such requests.<br>|No deviations noted.<br>|


AWS Confidential


175








Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality, and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**











|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|||Observed the repository of AWS customer<br>information requests to ascertain that AWS<br>recorded customer information requests.<br>|No deviations noted.<br>**2J**|
|**AWSCA-12.8:**Unless<br>prohibited from<br>doing so or there is a<br>clear indication of<br>illegal conduct in<br>connection with the<br>use of AWS products<br>or services, AWS<br>makes a reasonable<br>attempt to notify<br>customers before<br>disclosing Customer<br>Content in response<br>to valid/binding law<br>enforcement<br>requests. <br>|<br>P6.7 <br>|Inquired of AWS Corporate Counsel to<br>ascertain that AWS made a reasonable<br>attempt to notify customers before disclosing<br>Customer Content in response to<br>valid/binding law enforcement requests<br>unless legally prohibited from doing so.<br>**nIkLR**|No deviations noted.<br>|
|**AWSCA-12.8:**Unless<br>prohibited from<br>doing so or there is a<br>clear indication of<br>illegal conduct in<br>connection with the<br>use of AWS products<br>or services, AWS<br>makes a reasonable<br>attempt to notify<br>customers before<br>disclosing Customer<br>Content in response<br>to valid/binding law<br>enforcement<br>requests. <br>|<br>P6.7 <br>|Inspected the Amazon Law Enforcement<br>Guidelines public policy to ascertain that<br>AWS did not disclose customer information<br>in response to government demands unless<br>AWS was legally required by a binding order.<br>In such cases, AWS notified customers before<br>disclosure, unless legally prohibited from<br>doing so.<br>**GU4Ag**|No deviations noted.<br>|
|**AWSCA-12.8:**Unless<br>prohibited from<br>doing so or there is a<br>clear indication of<br>illegal conduct in<br>connection with the<br>use of AWS products<br>or services, AWS<br>makes a reasonable<br>attempt to notify<br>customers before<br>disclosing Customer<br>Content in response<br>to valid/binding law<br>enforcement<br>requests. <br>|<br>P6.7 <br>|For a Customer Content disclosure in<br>response to a binding law enforcement<br>request, inspected an email notification sent<br>from AWS Legal to an AWS customer to<br>ascertain that AWS notified the customer<br>before disclosure of customer content.<br>**Fiv**|No deviations noted.<br>|
|**AWSCA-12.9:**AWS<br>maintains contracts<br>with third party sub-<br>processors that<br>contain data<br>protection,<br>confidentiality<br>commitments, and<br>security<br>requirements. <br>**-token**|P6.1 <br> <br>**-w**|Inquired of AWS Senior Corporate Counsel to<br>ascertain that AWS maintained contracts<br>with third party sub-processors that contain<br>data protection, confidentiality<br>commitments, and security requirements.<br>|No deviations noted.<br>|
|**AWSCA-12.9:**AWS<br>maintains contracts<br>with third party sub-<br>processors that<br>contain data<br>protection,<br>confidentiality<br>commitments, and<br>security<br>requirements. <br>**-token**|P6.1 <br> <br>**-w**|For a sample of third party sub-processors<br>selected from the AWS sub-processor public<br>website, inspected the contracts to ascertain<br>that they contained data protection,<br>confidentiality commitments, and security<br>requirements.<br>|No deviations noted.<br>|


AWS Confidential


176


Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality, and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**











|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|**AWSCA-12.10:** A<br>formal review of<br>third-party sub-<br>processors is<br>performed prior to<br>AWS allowing any<br>processing by third-<br>party sub-processors<br>to determine that<br>appropriate<br>restrictions are in<br>place to limit the<br>third-party sub-<br>processors’<br>processing of<br>customer content<br>only to the customer<br>content that is<br>necessary to provide<br>or maintain the AWS<br>services selected by<br>the customer. <br>|P6.7 <br>|Inquired of AWS Senior Corporate Counsel to<br>ascertain that a formal review of third-party<br>sub-processors was performed prior to AWS<br>allowing any processing by third-party sub-<br>processors.<br>|No deviations noted.<br>**i2J**|
|**AWSCA-12.10:** A<br>formal review of<br>third-party sub-<br>processors is<br>performed prior to<br>AWS allowing any<br>processing by third-<br>party sub-processors<br>to determine that<br>appropriate<br>restrictions are in<br>place to limit the<br>third-party sub-<br>processors’<br>processing of<br>customer content<br>only to the customer<br>content that is<br>necessary to provide<br>or maintain the AWS<br>services selected by<br>the customer. <br>|P6.7 <br>|For a sample of third party sub-processors<br>selected from the AWS sub-processor public<br>website, inspected the application security<br>review performed by the Application Vendor<br>Security (AVS) team to ascertain that<br>restrictions to limit the processing of<br>customer content by third-party sub-<br>processors only to the customer content that<br>was necessary to provide or maintain the<br>AWS services selected by the customer were<br>reviewed prior to AWS allowing any<br>processing by the third-party sub-processor.<br>**ivGU4AgnIkL**|No deviations noted.<br>|
|**AWSCA-12.11:**AWS<br>conducts annual<br>reassessments of<br>third-party sub-<br>processors, or after<br>major incidents or<br>significant changes. <br>**-token**|P6.1 <br> <br>**-wi2**|Inquired of AWS Senior Corporate Counsel to<br>ascertain that AWS had a process in place to<br>conduct annual reassessments of third-party<br>sub-processors, or after major incidents or<br>significant changes.<br>**F**|No deviations noted.<br>|
|**AWSCA-12.11:**AWS<br>conducts annual<br>reassessments of<br>third-party sub-<br>processors, or after<br>major incidents or<br>significant changes. <br>**-token**|P6.1 <br> <br>**-wi2**|For a sample of third party sub-processors<br>selected from the AWS sub-processor public<br>website, inspected the application security<br>review performed by the Application Vendor<br>Security (AVS) team to ascertain that<br>reassessments of third-party sub-processors<br>were performed annually or following major<br>incidents or significant changes.<br>|No deviations noted.<br>|


AWS Confidential


177


Section IV – Description of Criteria, AWS Controls, Tests, and Results of Tests


**Security, Availability, Confidentiality, and Privacy Criteria Mapped to AWS Controls & Service Auditor’s**
**Testing Performed and Results**





|Controls Specified by<br>AWS|Criteria|Tests Performed by EY|x<br>k<br>Results of Tests|
|---|---|---|---|
|**AWSCA-12.12:**The<br>launch process for<br>new third-party sub-<br>processors requires<br>addition to the<br>externally posted list<br>of third-party sub-<br>processors that are<br>currently engaged by<br>AWS to process<br>customer data<br>depending on the<br>AWS region and AWS<br>service the customer<br>selects. <br>|P6.7 <br>|Inquired of AWS Senior Corporate Counsel to<br>ascertain the launch process for new third-<br>party sub-processors required addition to the<br>publicly available list of third-party sub-<br>processors engaged by AWS.<br> <br>**LR**|No deviations noted.<br>**i2J**|
|**AWSCA-12.12:**The<br>launch process for<br>new third-party sub-<br>processors requires<br>addition to the<br>externally posted list<br>of third-party sub-<br>processors that are<br>currently engaged by<br>AWS to process<br>customer data<br>depending on the<br>AWS region and AWS<br>service the customer<br>selects. <br>|P6.7 <br>|Inspected the AWS Products Legal sub-<br>processor page to ascertain that AWS notified<br>customers when it engaged a third-party to<br>process customer data.<br>**nIk**|No deviations noted.<br>|
|**AWSCA-12.12:**The<br>launch process for<br>new third-party sub-<br>processors requires<br>addition to the<br>externally posted list<br>of third-party sub-<br>processors that are<br>currently engaged by<br>AWS to process<br>customer data<br>depending on the<br>AWS region and AWS<br>service the customer<br>selects. <br>|P6.7 <br>|Inspected the launch playbook to ascertain<br>that it included requirements on notifying the<br>appropriate team and adding third-party sub-<br>processors to the externally posted list of<br>sub-processors for the public disclosure of<br>the use of new third-party sub-processors<br>prior to AWS allowing any processing by<br>third-party sub-processors.<br>**GU4Ag**|No deviations noted.<br>|


AWS Confidential


178




### **SECTION V – Other Information Provided By Amazon Web Services**

Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


179


|Section V – Other   For the current Spring SOC report (4/1/2024 – 3/3 enhancements to the existing controls and related in report. These changes were driven by our commitm align our documented controls with our evolving feedback received from our customers. The Sections  Modifications to existing controls Minor wording changes were made to the following existing processes.|r Information Provided By Amazon Web Services 31/2025) AWS has added new controls and made nformation presented compared to the previous SOC ment to continuous improvement, a desire to better g operational processes, AICPA SOC guidance and s below provide an overview of the changes:  control descriptions to more accurately reflect the LRi2Jkxwds|
|---|---|
|**OLD – Fall 2024 **<br>|**NEW – Spring 2025 **<br>|
|**AWSCA-1.7:** The Board and its Committees have<br>the required number of independent Board<br>members and each Board and Committee<br>member is qualified to serve in such capacity.<br>Annually, Board members complete<br>questionnaires to establish whether they are<br>independent and qualified to serve on each<br>Board Committee under applicable rules.<br>|**AWSCA-1.7:**The Amazon Board and its<br>Committees have the required number of<br>independent Board members, and the Board and<br>each Committee member is qualified to serve in<br>such capacity. Annually, Board members<br>complete questionnaires to establish whether<br>they are independent and qualified to serve on<br>each Board Committee under applicable rules.<br>**AgnIk**|
|**AWSCA-3.5:** AWS enables customers to select<br>who has access to AWS services and resources (if<br>resource-level permissions are applicable to the<br>service) that they own. AWS prevents customers<br>from accessing AWS resources that are not<br>assigned to them via access permissions. Content<br>is only returned to individuals authorized to<br>access the specified AWS service or resource (if<br>resource-level permissions are applicable to the<br>service). <br>**FivG**|**AWSCA-3.5:**AWS enables customers to select<br>who has access to AWS services and resources<br>that they own. AWS prevents customers from<br>accessing AWS resources that are not assigned to<br>them via access permissions. Content is only<br>returned to individuals authorized to access the<br>specified AWS service or resource (if resource-<br>level permissions are applicable to the service). <br>**U4**|
|**AWSCA-3.17:** Outpost-Specific – Service link is<br>established between Outpost and AWS Region by<br>use of a secured VPN connection over public<br>internet or AWS Direct Connect. <br>**wi2**|**AWSCA-3.17:**Outposts-Specific – Service link is<br>established between Outposts and AWS Region<br>by use of a secured VPN connection over public<br>internet or AWS Direct Connect. <br>|
|**AWSCA-4.14:**Each production firmware version<br>for the AWS Key Management Service HSM<br>(Hardware Security Module) has been certified<br>with NIST under the FIPS 140-2 level 3 standard<br>or is in the process of being certified under FIPS<br>140-3 level 3. <br>**oken-**|**AWSCA-4.14:**Each production firmware version<br>release for the AWS Key Management Service<br>HSM (Hardware Security Module) either holds or<br>is in the process of actively pursuing FIPS 140-3<br>level 3 certification from the National Institute of<br>Standards and Technology's (NIST) Cryptographic<br>Module Validation Program (CMVP). <br>|
|**AWSCA-6.1:** AWS applies a systematic approach<br>to managing change to ensure changes to<br>customer-impacting aspects of a service are<br>reviewed, tested and approved. Change<br>**m-t**|**AWSCA-6.1:**AWS applies a systematic approach<br>to managing change to ensure changes to<br>customer-impacting aspects of a service are<br>reviewed, tested and approved. Change<br>management policies/procedures are based on<br>|



Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


180


|Section V – Other|r Information Provided By Amazon Web Services wds|
|---|---|
|**OLD – Fall 2024 **<br>|**NEW – Spring 2025 **<br>|
|management standards are based on Amazon<br>guidelines and tailored for each AWS service. <br>|Amazon guidelines and tailored to the specifics of<br>each AWS service. <br>|
|**AWSCA-6.3:**Changes are tested according to<br>service team change management standards<br>prior to migration to production. <br>|**AWSCA-6.3:**Changes are tested according to<br>service team change management<br>policies/procedures prior to migration to<br>production. <br>**Jkx**|
|**AWSCA-6.5:**Changes are reviewed for business<br>impact and approved by authorized personnel<br>prior to migration to production according to<br>service team change management standards. <br>|**AWSCA-6.5:**Changes are reviewed for business<br>impact and approved by authorized personnel<br>prior to migration to production according to<br>service team change management<br>policies/procedures. <br>**LRi2**|
|**AWSCA-7.1:** S3-Specific – S3 compares user<br>provided checksums to validate the integrity of<br>data in transit. If the customer provided MD5<br>checksum does not match the MD5 checksum<br>calculated by S3 on the data received, the REST<br>PUT will fail, preventing data that was corrupted<br>on the wire from being written into S3. <br>|**AWSCA-7.1:**S3-Specific — S3 compares<br>checksums to validate the integrity of data in<br>transit. If the customer provided or automatically<br>calculated checksum does not match S3's server-<br>side checksum validation, the upload will fail,<br>preventing corrupted data from being written to<br>S3. <br>**gnIk**|
|**AWSCA-9.4:** AWS host configuration settings are<br>monitored to validate compliance with AWS<br>security standards and automatically pushed to<br>the host fleet. <br>|**AWSCA-9.4:**AWS host configuration settings are<br>monitored to validate compliance with AWS<br>security standards and to verify that settings are<br>automatically deployed to the host fleet. <br>**4A**|
|**AWSCA-9.9:** AWS has a process to assess<br>whether AWS employees who have access to<br>resources that store or process customer data via<br>permission groups are subject to a post-hire<br>background check as applicable with local law.<br>AWS employees who have access to resources<br>that store or process customer data will have a<br>background check in accordance to the AWS<br>Personnel Security Policy. <br>**i2FivG**|**AWSCA-9.9:**AWS has a process to assess<br>whether AWS employees who have access to<br>resources that store or process customer data via<br>permission groups are subject to a post-hire<br>background check as applicable with local law<br>and the AWS Personnel Security Policy. <br>|



**Addition of new controls**

A new control was added to the AWS SOC report scope to expand our control framework capabilities,
reflecting our commitment to continuous security improvement.

|k<br>New Controls|Mapped to Criteria|
|---|---|
|**AWSCA-3.19**: S3-Specific - All new objects<br>uploaded to Amazon S3 are automatically<br>encrypted with server-side encryption. <br>**-to**|CC6.1, CC6.7<br>|



Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


181


### **APPENDIX – Glossary of Terms**

Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


182


Appendix – Glossary of Terms


**Appendix – Glossary of Terms**

**AMI:** An Amazon Machine Image (AMI) is an encrypted machine image stored in Amazon S3. It contains
all the information necessary to boot instances of a customer’s software.


**API:** Application Programming Interface (API) is an interface in computer science that defines the ways by
which an application program may request services from libraries and/or operating systems.


**Authentication:** Authentication is the process of determining whether someone or something is, in fact,

who or what it is declared to be.


**Availability Zone:** Amazon EC2 locations are composed of regions and Availability Zones. Availability
Zones are distinct locations that are engineered to be insulated from failures in other Availability Zones
and provide inexpensive, low latency network connectivity to other Availability Zones in the same region.


**Bucket:** A container for objects stored in Amazon S3. Every object is contained within a bucket. More
information can be found in [https://docs.aws.amazon.com/AmazonS3/latest/dev/Introduction.html](https://docs.aws.amazon.com/AmazonS3/latest/dev/Introduction.html#BasicsBucket)

[#BasicsBucket](https://docs.aws.amazon.com/AmazonS3/latest/dev/Introduction.html#BasicsBucket)


**AWS Content:** “AWS Content” means Content we or any of our affiliates make available in connection
with the Services or on the AWS Site to allow access to and use of the Services, including APIs; WSDLs;
Documentation; sample code; software libraries; command line tools; roofs of concept; templates; and
other related technology (including any of the foregoing that are provided by our personnel). AWS
Content does not include the Services or Third-Party Content.


**Customer Content** [: Defined as “Your Content” in https://aws.amazon.com/agreement/](https://aws.amazon.com/agreement/)


**HMAC** : In cryptography, a keyed-Hash Message Authentication Code (HMAC or KHMAC), is a type of
message authentication code (MAC) calculated using a specific algorithm involving a cryptographic hash
function in combination with a secret key. As with any MAC, it may be used to simultaneously verify both
the data integrity and the authenticity of a message. Any iterative cryptographic hash function, such as
MD5 or SHA-1, may be used in the calculation of an HMAC; the resulting MAC algorithm is termed HMACMD5 or HMAC-SHA1, accordingly. The cryptographic strength of the HMAC depends upon the
cryptographic strength of the underlying hash function, on the size and quality of the key and the size of
the hash output length in bits.


**Personal Information:** Personal information that AWS collects in the course of providing
AWS’ offerings include:


  - **Information You Give Us:** We collect any information you provide in relation to AWS Offerings.
[Click here](https://aws.amazon.com/privacy/#Information_You_Give_Us) to see examples of information you give us.


  - **Automatic Information:** We automatically collect certain types of information when you interact
[with AWS Offerings. Click here](https://aws.amazon.com/privacy/#Automatic_Information) to see examples of information we collect automatically.


  - **Information from Other Sources:** We might collect information about you from other sources,
[including service providers, partners, and publicly available sources. Click here to see examples](https://aws.amazon.com/privacy/#Information_from_Other_Sources)

of information we collect from other sources.


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


183


Appendix – Glossary of Terms


**Hypervisor:** A hypervisor, also called Virtual Machine Monitor (VMM), is computer software/hardware
virtualization software that allows multiple operating systems to run on a host computer concurrently.


**IP Address:** An Internet Protocol (IP) address is a numerical label that is assigned to devices participating
in a computer network utilizing the Internet Protocol for communication between its nodes.


**IP Spoofing:** Creation of Internet Protocol (IP) packets with a forged source IP address, called spoofing,
with the purpose of concealing the identity of the sender or impersonating another computing system.


**MD5 checksums:** In cryptography, MD5 (Message-Digest algorithm 5) is a widely used cryptographic hash
function with a 128-bit hash value. As an Internet standard (RFC 1321), MD5 has been employed in a wide
variety of security applications and is also commonly used to check the integrity of files.


**Object:** The fundamental entities stored in Amazon S3. Objects consist of object data and metadata. The
data portion is opaque to Amazon S3. The metadata is a set of name-value pairs that describe the object.

These include some default metadata such as the date last modified and standard HTTP metadata such

as Content-Type. The developer can also specify custom metadata at the time the Object is stored.


**Port Scanning:** A port scan is a series of messages sent by someone attempting to break into a computer
to learn which computer network services, each associated with a “well-known” port number, the
computer provides.


**Privacy Policy:** “Privacy Policy” means the privacy policy located at [https://aws.amazon.com/privacy/](https://aws.amazon.com/privacy/)
(and any successor or related locations designated by us), as it may be updated by AWS from time to time.


**User entity:** The entities that use the services of a service organization during some or all of the review
period.


**Service:** Software or computing ability provided across a network (e.g., Amazon EC2, Amazon S3).


**Service Organization:** An organization or segment of an organization that provides services to user entities
that are likely to be relevant to those user entities’ internal control over financial reporting.


**Signature Version 4** : Signature Version 4 is the process to add authentication information to AWS
requests. For security, most requests to AWS must be signed with an access key, which consists of an
access key ID and secret access key.


**Subservice Organization:** A service organization used by another service organization to perform some of
the services provided to user entities that are likely to be relevant to those user entities’ internal control
over financial reporting.


**Virtual Instance:** Once an AMI has been launched, the resulting running system is referred to as a virtual
instance. All instances based on the same AMI start out identical and any information on them is lost when

the instances are terminated or fail.


**X.509:** In cryptography, X.509 is an ITU-T standard for a Public Key Infrastructure (PKI) for Single Sign-On
(SSO) and Privilege Management Infrastructure (PMI). X.509 specifies, among other things, standard
formats for public key certificates, certificate revocation lists, attribute certificates and a certification path
validation algorithm.


Proprietary and Confidential Information - Trade Secret

©2025 Amazon.com, Inc. or its affiliates


184