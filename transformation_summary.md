Code Transformation Summary by Amazon Q

 Lines of code in your application: 554

 Transformation duration: 8 min(s)

 Planned dependencies replaced: 7 of 9

 Additional dependencies added: 1

 Planned deprecated code instances replaced: 0 of 0

 Files changed: 7

 Build status in Java 17: SUCCEEDED

Table of Contents
Build log summary
Planned dependencies replaced
Additional dependencies added
Deprecated code replaced
All files changed
Next steps
Build log summaryScroll to top
Amazon Q successfully built the upgraded code in Java 17. Here is a relevant snippet from the build log. To view the full build log, open buildCommandOutput.log

The Maven build compiled 14 source files and 1 test file, ran 6 tests with no failures, created a JAR file, and repackaged it into a executable JAR. The build was successful overall.
Planned dependencies replacedScroll to top
Amazon Q updated the following dependencies that it identified in the transformation plan

Dependency	Action	Previous version in Java 8	Current version in Java 17
com.mysql:mysql-connector-j	Added	-	-
javax.persistence:javax.persistence-api	Added	-	2.2
junit:junit	Removed	4.11	-
mysql:mysql-connector-java	Removed	5.0.5	-
org.junit.jupiter:junit-jupiter	Added	-	-
org.mockito:mockito-junit-jupiter	Added	-	-
org.springframework.boot:spring-boot-starter-parent	Updated	1.4.7.RELEASE	3.2.7
Additional dependencies addedScroll to top
Amazon Q updated the following additional dependencies during the upgrade

Dependency	Action	Previous version in Java 8	Current version in Java 17
org.mockito:mockito-core	Updated	2.28.2	-
Deprecated code replacedScroll to top
Amazon Q replaced the following instances of deprecated code. An instance with 0 files changed indicates Amazon Q wasn't able to replace the deprecated code.

Deprecated code	Files changed
All files changedScroll to top
File	Action
pom.xml	Updated
src/main/java/com/example/controller/CrudController.java	Updated
src/main/java/com/example/model/Customer.java	Updated
src/main/java/com/example/model/Order.java	Updated
src/main/java/com/example/model/Product.java	Updated
src/main/java/com/example/service/ProductService.java	Updated
src/test/java/com/example/project/CrudControllerTest.java	Updated
Next stepsScroll to top
Please review and accept the code changes using the diff viewer.If you are using a Private Repository, please ensure that updated dependencies are available.

In order to successfully verify these changes on your machine, you will need to change your project to Java 17. We verified the changes using Amazon Corretto Java 17 build environment.
