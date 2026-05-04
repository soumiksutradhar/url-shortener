# DevOps Pipeline Forge 🚀

A production-grade CI/CD pipeline demonstrating the full software delivery lifecycle — from code push to automated deployment on Kubernetes, with IAC and live monitoring.

Built as a hands-on DevOps portfolio project using a simple 3-tier expense tracker application as the vehiclek, built using PostgreSQL, Flask and simple HTML/JS.

---

Infrastructure is provisioned with **Terraform** and configured with **Ansible**.

---

## Application

A simple **3-tier expense tracker**:
- **Frontend** — static HTML/JS served via Nginx; lets users add and view expenses
- **API** — Python/Flask REST backend; handles CRUD operations
- **Database** — PostgreSQL; persists expense records

The application itself is quite simple as the focus of this project is entirely on the DevOps infrastructure around it.

---

## Infrastructure

### Terraform
Provisions AWS infrastructure from code:
- EC2 instance (or EKS cluster)
- Security groups, key pairs, networking
- Outputs the public IP for downstream use

```bash
cd infra
terraform init
terraform plan
terraform apply
```

### Ansible
Configures the provisioned server automatically:
- Installs Docker, kubectl, and dependencies
- Idempotent —> safe to re-run

```bash
ansible-playbook -i inventory.ini playbook.yaml
```

### One-command provisioning
```bash
bash infra/provision.sh
# Terraform creates EC2 → IP fed into Ansible inventory → Ansible configures the server
```

---

## Local Development

```bash
docker-compose up --build
```
