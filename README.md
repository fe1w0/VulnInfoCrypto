Project: VulnInfoCrytpo
---
# Introduction

This project aims to collect CVEs related to cryptography software and CWEs related to cryptography using web crawlers. Users may modify the YAML files in the "sources" directory to add new software or CWEs. Specifically, "software.yml" in the "sources" directory contains cryptography software and libraries, while "cwe_info.yml" contains CWEs related to cryptography. The corresponding web crawlers are "software_info_get.py" for collecting software information and "cwe2cve_info_get.py" for collecting information on CWEs mapped to CVEs.
