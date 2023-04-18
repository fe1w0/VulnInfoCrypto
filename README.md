Project: VulnInfoCrytpo
---
# Introduction

This project aims to collect CVEs related to cryptography software and CWEs related to cryptography using web crawlers. Users may modify the YAML files in the "sources" directory to add new software or CWEs. Specifically, "software.yml" in the "sources" directory contains cryptography software and libraries, while "cwe_info.yml" contains CWEs related to cryptography. The corresponding web crawlers are "software_info_get.py" for collecting software information and "cwe2cve_info_get.py" for collecting information on CWEs mapped to CVEs.


Usage: 
- See the script file in the program directory

Sources:
- crypto libs:
  - MIRACL Crypto SDK
  - OpenSSL
  - NTL
  - Crypto++
  - PBC Library
  - NaCl
  - libsodium
  - RELIC
  - OpenABE
  - cpabe toolkit
  - Paillier Library
  - Proxy Re-cryptography Library
  - Broadcast Encryption
  - JPBC
  - GMSSL
  - GoPBC
  - GoFE
  - CONIKS
  - Private Join and Compute
  - CryptoTools
  - ENCRYPTO_utils
  - TFHE
  - SEAL
  - palisade
  - HELIB
  - lattigo
  - bellman
  - Bulletproofs
  - libsnark
  - blockchain-crypto-mpc
  - libSTARK
  - SolCrypto
  - vrf-solidity
  - liboqs
  - rlwekex
  - Apache Commons Crypto
  - Jasypt
  - Bouncy Castle
  - Tink
  - EverCrypt
  - 天安TASSL
  - PoralSSL
  - Cryptlib
  - Keyczar
  - Botan
  - GnuPG
  - Nettle
  - mbedTLS
  - LibTomCrypt
  - wolfSSL
  - tinycrypt
- related cwes
  - CWE-261
  - CWE-310
  - CWE-321
  - CWE-324
  - CWE-325
  - CWE-326
  - CWE-327
  - CWE-328
  - CWE-329
  - CWE-330
  - CWE-331
  - CWE-334
  - CWE-335
  - CWE-338
  - CWE-347
  - CWE-635
  - CWE-699
  - CWE-916
  - CWE-1240

Output:
  - classification_data.yml
  - cwe_result.yml
  - result.yml