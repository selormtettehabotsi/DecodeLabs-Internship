\# Week 3: The Data Warehouse



\*\*DecodeLabs Cloud Computing Internship — Batch 2026\*\*  

\*\*Operator:\*\* Selorm Tetteh-Abotsi



\## What this project does



Provisions a managed cloud database, creates a structured Interns table

with proper constraints, inserts dummy records, and verifies data persistence

via a SELECT query.



\## Intended Architecture (AWS)



| Component | Detail |

|-----------|--------|

| Database | AWS RDS MySQL 8.x |

| Instance class | db.t3.micro |

| Storage | 20 GB gp2 |

| Subnet | Private subnet (no public access) |

| Security Group | Port 3306 restricted to EC2 bastion SG only |

| Access method | SSH tunnel via EC2 bastion host |



\## Security Design



\- RDS placed in private subnet with no public IP

\- Security group allows port 3306 from EC2 bastion SG only

\- Credentials stored in environment variables, never hardcoded

\- SSH tunnel used for all local connections



\## Schema



```sql

CREATE TABLE Interns (

&#x20;   InternID  INT AUTO\_INCREMENT PRIMARY KEY,

&#x20;   FirstName VARCHAR(50)  NOT NULL,

&#x20;   LastName  VARCHAR(50)  NOT NULL,

&#x20;   Email     VARCHAR(100) UNIQUE NOT NULL

);

```



\## Sample Records



```sql

INSERT INTO Interns (FirstName, LastName, Email) VALUES

('Selorm', 'Tetteh-Abotsi', 'selorm@decodelabs.com'),

('Jane',   'Smith',         'jsmith@decodelabs.com'),

('Kofi',   'Mensah',        'kmensah@decodelabs.com'),

('Ama',    'Owusu',         'aowusu@decodelabs.com');

```



\## Verification



```sql

SELECT \* FROM Interns;

```



Returns all 4 records confirming data persistence.

