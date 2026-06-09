\# Week 2: The Server Commander



\*\*DecodeLabs Cloud Computing Internship — Batch 2026\*\*  

\*\*Operator:\*\* Selorm Tetteh-Abotsi



\## What this project does



Provisions a live web server on AWS EC2 running nginx, serving a custom static page over HTTP.



\## Infrastructure



| Component | Detail |

|-----------|--------|

| Cloud | AWS |

| Region | us-east-1 (N. Virginia) |

| Instance | t2.micro (Free Tier) |

| OS | Ubuntu Server 24.04 LTS |

| Web Server | nginx |

| Public IP | 34.204.13.47 |



\## Security Group Rules



| Type | Port | Source | Reason |

|------|------|--------|--------|

| SSH | 22 | My IP only | Prevent unauthorized access |

| HTTP | 80 | 0.0.0.0/0 | Public web traffic |



\## Steps taken



1\. Launched EC2 t2.micro instance (Ubuntu 24.04) in us-east-1

2\. Configured security group — SSH locked to my IP, HTTP open

3\. SSH'd into instance using key pair

4\. Installed

