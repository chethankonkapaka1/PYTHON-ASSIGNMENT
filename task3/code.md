### Case Study 30: Student Email and Identifier Validation

### 1\. Problem Statement

To check whether a student's email address and registration number are valid using simple conditions.

### 2\. Algorithm

* Start.

* Read the student's email and registration number.

* Check whether the email contains `@` and `.`, and whether `@` appears before the last dot.

* Display whether the email is valid or invalid.

* Check whether the registration number has exactly 10 characters and contains only letters and numbers.

* Display whether the registration number is valid or invalid.

* Stop.

### 3\. Flowchart

```mermaid
flowchart TD
    A([Start]) --> B[/Enter email and registration number/]
    B --> C{Email contains @ and . and @ is before last dot?}
    C -- Yes --> D[Display Email is valid]
    C -- No --> E[Display Email is invalid]
    D --> F{Registration number has 10 alphanumeric characters?}
    E --> F
    F -- Yes --> G[Display Registration number is valid]
    F -- No --> H[Display Registration number is invalid]
    G --> I([Stop])
    H --> I
```

### 4\. Sample Input

```text
Enter student email: student@gmail.com
Enter registration number: AIML123456
```

### 5\. Sample Output

```text
Email is valid
Registration number is valid
```
