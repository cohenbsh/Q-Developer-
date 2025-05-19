<<<<<<< HEAD
java 8 path: /Library/Java/JavaVirtualMachines/jdk-1.8.jdk/Contents/Home
Project: spring-mysql-app

# java-ecommerce-website

```src
├── main
│   ├── java
│   │   └── com
│   │       └── example
│   │           ├── CrudApplication.java
│   │           ├── controller
│   │           │   └── CrudController.java
│   │           ├── dto
│   │           │   ├── CustomerDTO.java
│   │           │   ├── OrderDTO.java
│   │           │   └── ProductDTO.java
│   │           ├── model
│   │           │   ├── Customer.java
│   │           │   ├── Order.java
│   │           │   └── Product.java
│   │           ├── repository
│   │           │   ├── CustomerRepository.java
│   │           │   ├── OrderRepository.java
│   │           │   └── ProductRepository.java
│   │           └── service
│   │               ├── CustomerService.java
│   │               ├── OrderService.java
│   │               └── ProductService.java
│   └── resources
│       └── application.properties
└── pom.xml
```

## Amazon Q - Code Transformation expectations
* DTO objects should be converted to Records
* DTO classes have multiline `ToString()` methods that should be optimize with Java 17
* CrudController contains an old style `Switch` statement that should be replaced by modern pattern matching code
* CrudController uses an old `toArray(String[0])` which should be converted to `toArray()` in Java 17

=======
# javaTransformation
Amazon Q
>>>>>>> origin/main
